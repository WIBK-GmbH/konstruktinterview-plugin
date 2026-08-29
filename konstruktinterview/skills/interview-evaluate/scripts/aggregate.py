#!/usr/bin/env python3
"""Berechnet die drei Aggregationsebenen der Konstruktinterview-Auswertung.

Ebene 1  Personen je Kategorie                 Verbreitungsmaß „X von N“
Ebene 2  Äußerungen je Bewertung je Kategorie  Sheet Auszählung
Ebene 3  Personen je Bewertung je Kategorie    Zählzeilen im Ergebnisdokument

Ebene 2 und Ebene 3 sehen identisch aus und bedeuten Verschiedenes. Für
Folienzahlen gilt immer Ebene 3.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _kern as K  # noqa: E402


HILFE = """
Liest entweder die JSON-Codiertabelle oder eine geschriebene Arbeitsmappe und
gibt die Aggregate als Markdown, als JSON oder als fertige Zählzeilen aus.

EBENEN
  personen-kategorie       distinkte Kennungen je Unterkategorie
  aeusserungen-bewertung   Codiereinheiten je Bewertung je Unterkategorie
  personen-bewertung       distinkte Kennungen je Bewertung je Unterkategorie
  alle                     alle drei nacheinander (Default)

FORMATE
  md       Markdown-Tabellen für die Prozessnotiz
  json     maschinenlesbar, Eingabe für die Folienerzeugung
  zeilen   fertige Zählzeilen „X von N Personen (a +, b -, c o, d >)“
           mit Prüfung der Regel max(a, b, c, d) <= X <= N

WARUM DIE ZÄHLZEILE NICHT AUS DEM AUSZÄHLUNGSBLATT KOMMT
  Das Auszählungsblatt enthält Äußerungszahlen. Die Folie braucht
  Personenzahlen. Die vier Bewertungszahlen sind keine Partition: eine Person
  kann in derselben Kategorie positiv und negativ codiert sein, deshalb ist
  a + b + c + d regelmäßig größer als X. Das ist korrekt und wird nicht
  repariert.

GRUPPIERUNG
  --group-by perspektive schlüsselt Ebene 1 und Ebene 3 zusätzlich nach
  Perspektivgruppe auf. Bei Gruppen mit weniger als drei Personen unterbleibt
  die Gruppenangabe im Ergebnisdokument wegen Re-Identifikationsrisiko; das
  Skript weist solche Gruppen aus, entfernt sie aber nicht.
  Die Gruppen stammen aus der JSON oder aus der Registry im Sheet Info.

BEISPIELE
  python3 aggregate.py --input codierung.json --level alle --format md
  python3 aggregate.py --input codierung.json \\
      --level personen-bewertung --format zeilen
  python3 aggregate.py --workbook "Codierung_P01-P14_260315_v3.xlsx" \\
      --level alle --format json
  python3 aggregate.py --input codierung.json --level personen-kategorie \\
      --group-by perspektive --format md

AUSGABE
  Markdown, JSON oder Zählzeilen auf stdout. Exit-Code 1, wenn eine Zählzeile
  die Regel max(a, b, c, d) <= X <= N verletzt, 2 bei Bedienfehlern.
"""


def daten_laden(args) -> dict:
    """Liefert Zeilen, Kategorien, N und Gruppen aus JSON oder Arbeitsmappe."""
    if args.input:
        rohdaten = K.lade_codierung(args.input)
        zeilen = K.zeilen_aus_json(rohdaten)
        katsys = [k for k in rohdaten["kategoriensystem"] if k["ebene"] == "unter"]
        kategorien = [(K.norm_kat(k["nummer"]), k["bezeichnung"]) for k in katsys]
        gruppen = {g["name"]: list(g["kennungen"])
                   for g in rohdaten["perspektivgruppen"]}
        n_personen = rohdaten["meta"]["n_personen"]
        quelle = args.input
    else:
        mappe = K.lade_arbeitsmappe(args.workbook)
        zeilen = mappe["zeilen"]
        kategorien = [(k["nummer"], k["bezeichnung"]) for k in mappe["katsys"]
                      if k["ebene"] == "unter"]
        gruppen = mappe["registry"]
        n_personen = mappe["n_personen"]
        if not n_personen:
            raise K.KernFehler(
                "Die Stichprobengröße N ließ sich weder aus der "
                "Perspektivgruppen-Registry noch aus dem Auszählungskopf lesen.")
        quelle = args.workbook
    kategorien.sort(key=lambda paar: K.kat_sortkey(paar[0]))
    return {"zeilen": zeilen, "kategorien": kategorien, "n": n_personen,
            "gruppen": gruppen, "quelle": quelle}


def baue_ergebnis(kontext: dict) -> dict:
    """Berechnet alle drei Ebenen samt Zählzeilen und Plausibilitätsprüfung."""
    zeilen = kontext["zeilen"]
    nummern = [nummer for nummer, _ in kontext["kategorien"]]
    bezeichnungen = dict(kontext["kategorien"])
    n_personen = kontext["n"]

    ebene1 = K.personen_je_kategorie(zeilen, nummern)
    ebene2 = K.aeusserungen_je_bewertung(zeilen, nummern)
    ebene3 = K.personen_je_bewertung(zeilen, nummern)

    zeilentexte = {}
    verstoesse = []
    verletzte = []
    for nummer in nummern:
        werte = ebene3[nummer]
        zeilentexte[nummer] = K.zaehlzeile(werte, n_personen)
        if not K.zaehlzeile_plausibel(werte, n_personen):
            verletzte.append(nummer)
            verstoesse.append(
                f"{nummer}: {zeilentexte[nummer]} verletzt max(a, b, c, d) "
                f"<= X <= N (N = {n_personen}).")

    gruppen = {}
    for name, kennungen in (kontext["gruppen"] or {}).items():
        teilzeilen = [z for z in zeilen if z["kennung"] in kennungen]
        gruppen[name] = {
            "kennungen": sorted(kennungen),
            "groesse": len(kennungen),
            "re_identifikationsrisiko": len(kennungen) < 3,
            "personen_je_kategorie": K.personen_je_kategorie(teilzeilen, nummern),
            "personen_je_bewertung": K.personen_je_bewertung(teilzeilen, nummern),
        }

    return {
        "quelle": kontext["quelle"],
        "n_personen": n_personen,
        "einheiten": len(zeilen),
        "personen_gesamt": len({z["kennung"] for z in zeilen}),
        "bezeichnungen": bezeichnungen,
        "kategorien": nummern,
        "personen_je_kategorie": ebene1,
        "aeusserungen_je_bewertung": ebene2,
        "personen_je_bewertung": ebene3,
        "zaehlzeilen": zeilentexte,
        "plausibilitaet_verletzt": verstoesse,
        "plausibilitaet_verletzt_kategorien": verletzte,
        "perspektivgruppen": gruppen,
    }


def ausgabe_markdown(ergebnis: dict, level: str, mit_gruppen: bool) -> str:
    teile = []
    n_personen = ergebnis["n_personen"]
    bezeichnung = ergebnis["bezeichnungen"]

    if level in ("personen-kategorie", "alle"):
        teile.append("## Ebene 1: Personen je Kategorie\n")
        teile.append("| Kategorie | Bezeichnung | Personen |")
        teile.append("|---|---|---|")
        for nummer in ergebnis["kategorien"]:
            teile.append(f"| {nummer} | {bezeichnung.get(nummer, '')} | "
                         f"{ergebnis['personen_je_kategorie'][nummer]} von {n_personen} |")
        teile.append(f"| Gesamt | Alle Kategorien (aggregiert) | "
                     f"{ergebnis['personen_gesamt']} von {n_personen} |")
        teile.append("")

    if level in ("aeusserungen-bewertung", "alle"):
        teile.append("## Ebene 2: Äußerungen je Bewertung je Kategorie\n")
        teile.append("| Kategorie | Bezeichnung | + | - | o | > | Gesamt |")
        teile.append("|---|---|---:|---:|---:|---:|---:|")
        summen = {b: 0 for b in K.BEWERTUNGEN}
        gesamt = 0
        for nummer in ergebnis["kategorien"]:
            werte = ergebnis["aeusserungen_je_bewertung"][nummer]
            for b in K.BEWERTUNGEN:
                summen[b] += werte[b]
            gesamt += werte["gesamt"]
            teile.append(f"| {nummer} | {bezeichnung.get(nummer, '')} | {werte['+']} "
                         f"| {werte['-']} | {werte['o']} | {werte['>']} "
                         f"| {werte['gesamt']} |")
        teile.append(f"| Gesamt | Alle Kategorien (aggregiert) | {summen['+']} "
                     f"| {summen['-']} | {summen['o']} | {summen['>']} | {gesamt} |")
        teile.append("")

    if level in ("personen-bewertung", "alle"):
        teile.append("## Ebene 3: Personen je Bewertung je Kategorie\n")
        teile.append("Diese Zahlen gehören in die Zählzeilen des Ergebnisdokuments.\n")
        teile.append("| Kategorie | Bezeichnung | X | a + | b - | c o | d > | Zählzeile |")
        teile.append("|---|---|---:|---:|---:|---:|---:|---|")
        for nummer in ergebnis["kategorien"]:
            werte = ergebnis["personen_je_bewertung"][nummer]
            teile.append(f"| {nummer} | {bezeichnung.get(nummer, '')} "
                         f"| {werte['personen']} | {werte['+']} | {werte['-']} "
                         f"| {werte['o']} | {werte['>']} "
                         f"| {ergebnis['zaehlzeilen'][nummer]} |")
        teile.append("")

    if mit_gruppen and ergebnis["perspektivgruppen"]:
        teile.append("## Aufschlüsselung nach Perspektivgruppe\n")
        for name, block in ergebnis["perspektivgruppen"].items():
            hinweis = (" Achtung: weniger als drei Personen, Gruppenangabe im "
                       "Ergebnisdokument unterlassen."
                       if block["re_identifikationsrisiko"] else "")
            teile.append(f"### {name} ({block['groesse']} Interviews)"
                         f"{hinweis}\n")
            teile.append("| Kategorie | Personen der Gruppe | + | - | o | > |")
            teile.append("|---|---:|---:|---:|---:|---:|")
            for nummer in ergebnis["kategorien"]:
                werte = block["personen_je_bewertung"][nummer]
                teile.append(f"| {nummer} | {werte['personen']} von {block['groesse']} "
                             f"| {werte['+']} | {werte['-']} | {werte['o']} "
                             f"| {werte['>']} |")
            teile.append("")

    if ergebnis["plausibilitaet_verletzt"]:
        teile.append("## Verletzte Prüfregel max(a, b, c, d) <= X <= N\n")
        for text in ergebnis["plausibilitaet_verletzt"]:
            teile.append(f"- {text}")
        teile.append("")
    return "\n".join(teile)


def ausgabe_zeilen(ergebnis: dict) -> str:
    teile = []
    verletzte = set(ergebnis["plausibilitaet_verletzt_kategorien"])
    for nummer in ergebnis["kategorien"]:
        marke = "FEHLER" if nummer in verletzte else "OK    "
        teile.append(f"{marke} {nummer} {ergebnis['bezeichnungen'].get(nummer, '')}")
        teile.append(f"      {ergebnis['zaehlzeilen'][nummer]}")
    return "\n".join(teile)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="aggregate.py",
        description="Berechnet die drei Aggregationsebenen der Auswertung.",
        epilog=HILFE,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    quelle = parser.add_mutually_exclusive_group(required=True)
    quelle.add_argument("--input", help="JSON-Codiertabelle")
    quelle.add_argument("--workbook", help="geschriebene Arbeitsmappe .xlsx")
    parser.add_argument("--level", default="alle",
                        choices=("personen-kategorie", "aeusserungen-bewertung",
                                 "personen-bewertung", "alle"),
                        help="welche Aggregationsebene ausgegeben wird (Default: alle)")
    parser.add_argument("--group-by", choices=("perspektive",), default=None,
                        help="zusätzliche Aufschlüsselung nach Perspektivgruppe")
    parser.add_argument("--format", default="md", choices=("md", "json", "zeilen"),
                        help="Ausgabeformat (Default: md)")
    args = parser.parse_args(argv)

    try:
        kontext = daten_laden(args)
    except K.KernFehler as fehler:
        sys.stderr.write(f"FEHLER: {fehler}\n")
        return 2

    ergebnis = baue_ergebnis(kontext)
    mit_gruppen = args.group_by == "perspektive"

    if args.format == "json":
        if not mit_gruppen:
            ergebnis = dict(ergebnis)
            ergebnis["perspektivgruppen"] = {}
        print(json.dumps(ergebnis, ensure_ascii=False, indent=2))
    elif args.format == "zeilen":
        print(ausgabe_zeilen(ergebnis))
        for text in ergebnis["plausibilitaet_verletzt"]:
            sys.stderr.write(f"FEHLER: {text}\n")
    else:
        print(ausgabe_markdown(ergebnis, args.level, mit_gruppen))

    return 1 if ergebnis["plausibilitaet_verletzt"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
