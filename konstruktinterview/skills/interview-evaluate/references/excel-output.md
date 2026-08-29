# Arbeitsmappe

Spezifikation des primären Artefakts. Die Arbeitsmappe ist die Datenwahrheit:
Alles, was im Ergebnisdokument steht, wird aus ihr abgeleitet. Beispiele stammen
aus dem Übungsfall *Firma M.* (Möbelhersteller, Verlagerung der Fertigung an
einen zweiten Standort, 14 Interviews).

## Inhalt

1. [Workbook-Ebene](#1-workbook-ebene)
2. [Sheet `Aussagen`](#2-sheet-aussagen)
3. [Sheet `Kategoriensystem`](#3-sheet-kategoriensystem)
4. [Sheet `Auszählung`](#4-sheet-auszählung)
5. [Sheet `Info`](#5-sheet-info)
6. [Die drei Aggregationsebenen](#6-die-drei-aggregationsebenen)
7. [Kategoriennummern normalisieren](#7-kategoriennummern-normalisieren)
8. [Validierung nach dem Schreiben](#8-validierung-nach-dem-schreiben)
9. [Skripte](#9-skripte)

---

## 1. Workbook-Ebene

**Vier Sheets in exakt dieser Reihenfolge**, aktives Sheet beim Öffnen ist
`Aussagen`:

| # | Sheet | Inhalt |
|---|---|---|
| 1 | `Aussagen` | eine Zeile je Codiereinheit |
| 2 | `Kategoriensystem` | Haupt- und Unterkategorien mit Definition, Ankerbeispiel, Codierregel |
| 3 | `Auszählung` | Aggregation je Unterkategorie plus Gesamtzeile |
| 4 | `Info` | Metadaten, Perspektivgruppen-Registry, Hinweise |

**Keine Formeln.** Alle Zellen tragen statische Werte, auch in der Auszählung.
Die Aggregate werden in Python berechnet und als Zahlen geschrieben, nicht als
`=SUMME()`. Grund: Die Datei wird weitergereicht und zitiert; Formeln brechen
beim manuellen Zeilenlöschen.

**Keine Freeze Panes, kein AutoFilter, keine bedingte Formatierung, keine
Datenvalidierung, keine verbundenen Zellen, kein Tab-Farbcode.** Wünscht der User
ausdrücklich Bedienkomfort, sind `freeze_panes="A2"` und ein AutoFilter auf
`Aussagen` unschädlich; Default ist der schlanke Zustand.

**Schrift** durchgängig Arial: Kopfzeilen 11 pt fett, Datenzeilen 10 pt
(Ausnahme `Kategoriensystem`: Datenzeilen ebenfalls 11 pt).

**Farbschema (ARGB).** Die Zweifarbigkeit ist bewusst: rot markiert Datentabellen,
blau die Methodentabelle. Die Hexwerte sind austauschbar, solange der Kontrast zu
weißer Schrift trägt.

| Element | Füllung | Schrift |
|---|---|---|
| Kopfzeile `Aussagen`, `Auszählung` | `FF8B0000` | `FFFFFFFF` |
| Kopfzeile `Kategoriensystem` | `FF1F4E79` | `FFFFFFFF` |
| Hauptkategoriezeilen | `FFF2F2F2`, fett | Standard |
| Gesamtzeile `Auszählung` | `FFD9D9D9`, fett | Standard |
| `Info` | keine | Labels fett, Werte normal |

**Dateiname:** `Codierung_<ErsteKennung>-<LetzteKennung>_<JJMMTT>_v<N>.xlsx`,
zum Beispiel `Codierung_P01-P14_260315_v3.xlsx`. Die Versionsangabe im Dateinamen
und die im Sheet `Info` kommen **aus einer Quelle** und dürfen nicht auseinander
laufen.

## 2. Sheet `Aussagen`

Kopfzeile in Zeile 1, exakt diese fünf Bezeichner in dieser Reihenfolge:

| Spalte | Header | Typ | Pflicht | Breite |
|---|---|---|---|---|
| A | `Kennung` | Text | ja | 12,0 |
| B | `Kategorie` | **Text** | ja | Default |
| C | `Bewertung` | Text | ja | Default |
| D | `Kernaussage` | Text | nein | 14,0 |
| E | `Äußerung` | Text | ja | **110,0** |

Inhaltliche Konventionen für alle fünf Spalten stehen in `codierung.md`. Hier nur
das, was das Dateiformat betrifft.

**Datentyp-Falle.** `Kategorie` muss als **String** geschrieben werden. Als Float
geschrieben macht die Tabellenkalkulation daraus eine Zahl, und `2.10` kollabiert
zu `2.1`. In openpyxl: Wert als `str` übergeben und zusätzlich
`cell.number_format = "@"` setzen.

Dieselbe Falle steht schon eine Stufe früher offen, auf der **Eingabeseite**:
`"kategorie": 2.10` in der JSON-Codiertabelle wird beim Einlesen zu `"2.1"`, die
Einheit wandert lautlos in die falsche Kategorie und beide Auszählungen sind
falsch. `_kern.py` erzwingt deshalb den Datentyp `str` für
`aussagen[].kategorie` und `kategoriensystem[].nummer` und bricht bei einer Zahl
mit Exit-Code 2 ab.

**Vollständigkeit ist erzwungen.** In A, B, C und E darf keine Zelle leer sein.
D ist die einzige optionale Spalte.

**Formatierung.** Kopfzeile: Arial 11 fett, weiß auf `FF8B0000`, vertikal
zentriert, `wrap_text=True`, horizontal zentriert für A bis D, **linksbündig für
E**. Datenzeilen: Arial 10, keine Füllung, keine Rahmen, vertikale Ausrichtung
`top`, horizontal zentriert für A bis D ohne Umbruch, **E linksbündig mit
`wrap_text=True`**. Die Formatierung ist über alle Zeilen homogen.

**Zeilenhöhen** nach Näherungsformel, damit umgebrochener Text vollständig
sichtbar ist:

```python
zeilen = max(1, math.ceil(len(aeusserung) / 132))   # ~132 Zeichen je Zeile bei Breite 110 / Arial 10
hoehe  = None if zeilen <= 1 else 12.5 * zeilen     # 25.0, 37.5, 50.0 …
```

**Sortierung** dreistufig nach Kategorie (numerisch), Kennung, Gesprächsverlauf.
Bei Nachträgen wird die vollständige Tabelle neu sortiert.

```python
daten.sort(key=lambda r: ([int(t) for t in r["kategorie"].split(".")],
                          r["kennung"], r["reihenfolge"]))
```

## 3. Sheet `Kategoriensystem`

Kopfzeile Zeile 1 mit fünf Spalten:

| Spalte | Header | Breite | Inhalt |
|---|---|---|---|
| A | `Hauptkategorie` | 16,0 | Nummer **mit** Schlusspunkt: `1.` bzw. `1.1.` |
| B | `Unterkategorie` | 45,0 | Klartextbezeichnung |
| C | `Definition` | Default | Was fällt in die Kategorie |
| D | `Ankerbeispiel` | Default | prototypisches Zitat |
| E | `Codierregel` | Default | Abgrenzung zu Nachbarkategorien |

Die Überschrift von Spalte A ist historisch irreführend: A trägt die **Nummer**
aller Zeilen, B die **Bezeichnung**. Beibehalten, damit Dateien vergleichbar
bleiben.

**Zwei Zeilentypen, verschränkt in Gliederungsreihenfolge:**

| | Hauptkategoriezeile | Unterkategoriezeile |
|---|---|---|
| A | `1.` | `1.1.` |
| B | Bezeichnung der Hauptkategorie | Bezeichnung der Unterkategorie |
| C | Definition, beginnt mit „Oberkategorie für …“ | Definition mit Facettenklammer |
| D, E | **leer** | Pflicht |
| Format | fett, Füllung `FFF2F2F2` | normal, keine Füllung |

Satzmuster und Beispiele: `kategoriensystem.md`.

**Formatierung.** Kopfzeile: Arial 11 fett, weiß auf `FF1F4E79`, **linksbündig**,
vertikal zentriert, `wrap_text=True`, dünner Rahmen an allen vier Seiten. Dieses
Sheet ist das einzige mit Rahmen. Datenzeilen: Arial 11, links und vertikal
zentriert, `wrap_text=True`.

**Zeilenhöhen** explizit setzen, Näherung
`hoehe = 14 * ceil(max_zellenlänge / 60)`, gedeckelt bei 140.

## 4. Sheet `Auszählung`

Kopfzeile Zeile 1, acht Spalten:

| Spalte | Header | Breite | Typ | Inhalt |
|---|---|---|---|---|
| A | `Kategorie` | 12,0 | Text | `x.y` ohne Schlusspunkt; letzte Zeile `Gesamt` |
| B | `Bezeichnung` | 58,0 | Text | Kategorienbezeichnung aus dem Kategoriensystem |
| C | `Personen (n von <N>)` | 20,0 | **Text** | `"<k> von <N>"` |
| D | `+` | 10,0 | Zahl | Anzahl **Äußerungen** mit `+` |
| E | `-` | Default | Zahl | Anzahl `-` |
| F | `o` | Default | Zahl | Anzahl `o` |
| G | `>` | Default | Zahl | Anzahl `>` |
| H | `Gesamt Äußerungen` | 18,0 | Zahl | Summe D bis G |

Der Kopfzeilentext von Spalte C ist **dynamisch** und trägt die Stichprobengröße,
etwa `Personen (n von 14)`.

Eine Zeile je **Unterkategorie** in aufsteigender Reihenfolge, keine
Hauptkategoriezeilen, danach eine Gesamtzeile.

**Aggregationslogik**, ausschließlich aus dem Sheet `Aussagen`:

```
Für jede Unterkategorie k:
  C = f"{len({z.Kennung for z in zeilen if z.Kategorie == k})} von {N}"
  D = count(z.Kategorie == k and z.Bewertung == "+")
  E = count(z.Kategorie == k and z.Bewertung == "-")
  F = count(z.Kategorie == k and z.Bewertung == "o")
  G = count(z.Kategorie == k and z.Bewertung == ">")
  H = count(z.Kategorie == k)

Gesamtzeile:
  A = "Gesamt"
  B = "Alle Kategorien (aggregiert)"
  C = f"{len({z.Kennung for z in zeilen})} von {N}"    # NICHT die Summe von C
  D..H = Spaltensummen über alle Kategorienzeilen
```

**Kritische Feinheiten:**

1. **Spalte C ist eine Personenzählung, keine Äußerungszählung.** Sie zählt, wie
   viele verschiedene Personen sich zur Kategorie geäußert haben. Genau diese
   Zahl braucht das Ergebnisdokument als Verbreitungsmaß.
2. **Spalte C wird in der Gesamtzeile nicht aufsummiert**, sondern über alle
   Zeilen distinct gezählt.
3. **Spalte C ist Text**, Format `"<k> von <N>"` mit kleingeschriebenem „von“.
   So bleibt der Bezugsrahmen in jeder Zelle sichtbar.
4. `H == D + E + F + G` muss zeilenweise gelten.
5. `Σ H (Kategorienzeilen) == H (Gesamtzeile) == Zeilenzahl in Aussagen`.
6. **D bis G zählen Äußerungen.** Die optisch gleich aussehende Klammer im
   Ergebnisdokument zählt Personen. Siehe Abschnitt 6.

**Formatierung.** Kopfzeile: Arial 11 fett, weiß auf `FF8B0000`, vertikal
zentriert, `wrap_text=True`, Zeilenhöhe 28,0, horizontal zentriert außer B.
Datenzeilen: Arial 10, vertikal zentriert, kein Umbruch, horizontal zentriert
außer B. Gesamtzeile: fett, Füllung `FFD9D9D9`.

## 5. Sheet `Info`

**Kein Tabellenkopf.** Zweispaltige Label-Wert-Liste ab Zeile 1: Spalte A Label
(fett, mit Doppelpunkt), Spalte B Wert. Leerzeilen trennen Blöcke.
Spaltenbreiten A = 38,0 und B = 75,0, Arial 10.

**Block 1, Metadaten (Pflichtfelder):**

| Label | Inhalt |
|---|---|
| `Projekt:` | Projektbezeichnung |
| `Gegenstand:` | Was wurde ausgewertet |
| `Stand:` | Datum, Version, Bearbeitungsstand |
| `Umfang:` | N Interviews und Anzahl Codiereinheiten |
| `Auswertungsmethode:` | Methodenbezeichnung, Kategorienzahl und -struktur |
| `Codierregeln:` | Kurzlegende des Bewertungsschemas |
| `Kernaussagen:` | Legende der `*`-Spalte samt Verwendungszweck |
| `Ankerbeispiele:` | reale Codiereinheiten oder konstruierte Prototypen |

Die Zeile `Kernaussagen:` ist Pflicht. Ohne sie ist die `*`-Spalte für Dritte
nicht interpretierbar; sie nennt Zeichen **und** Verwendungszweck. Die Zeile
`Ankerbeispiele:` ist Pflicht, sobald konstruierte Prototypen verwendet werden.

**Block 2, Perspektivgruppen-Registry.** Eine Überschriftszeile
`Perspektivgruppen (<N> Interviews gesamt):`, dann je Gruppe eine Zeile:
A = `<lfd. Nr>. <Gruppenname> (<k> Interviews):`, B = kommaseparierte
Kennungsliste.

```
Perspektivgruppen (14 Interviews gesamt):
1. Geschäftsleitung (2 Interviews):   P04, P11
2. Fertigung (6 Interviews):          P01, P03, P06, P08, P12, P14
3. Vertrieb (3 Interviews):           P02, P07, P13
4. Verwaltung (3 Interviews):         P05, P09, P10
```

Dies ist die **einzige** Stelle im Workbook mit Gruppenzuordnung. Die Listen
müssen partitionierend sein und werden gegen den Pseudonymschlüssel gegengeprüft
(`validate_deliverables.py --key`).

*Bei Auswertungen, die stark nach Gruppen differenzieren*, entsteht die
Aufschlüsselung als **abgeleitete Tabelle außerhalb der Mappe**, erzeugt mit
`aggregate.py --group-by perspektive`, und wandert in die Prozessnotiz. Das Sheet
`Aussagen` bekommt **keine** Perspektivspalte: Sie wäre eine zweite Stelle mit
Gruppenzuordnung, das Schreibskript erzeugt sie nicht und die Validierung würde
sie nicht mitprüfen.

**Block 3, Anonymisierungshinweis (Pflicht).** A =
`Wichtiger Hinweis zur Anonymisierung:`, B = Erklärung, was pseudonymisiert
wurde.

## 6. Die drei Aggregationsebenen

Das häufigste Missverständnis der ganzen Auswertung. Drei Kennzahlen stehen
nebeneinander, zwei davon sehen identisch aus:

| # | Kennzahl | Zähleinheit | Berechnung | Wo sie steht |
|---|---|---|---|---|
| 1 | **Personen je Kategorie** | distinkte Kennungen | `len({kennung : kategorie == k})` | Sheet `Auszählung` Spalte C; Verbreitungsmaß „X von N“ im Bericht |
| 2 | **Äußerungen je Bewertung je Kategorie** | Codiereinheiten | `count(kategorie == k and bewertung == b)` | Sheet `Auszählung` Spalten D bis G |
| 3 | **Personen je Bewertung je Kategorie** | distinkte Kennungen | `len({kennung : kategorie == k and bewertung == b})` | Zählzeilen im Ergebnisdokument: `X von N Personen (a +, b -, c o, d >)` |

Ebene 2 und Ebene 3 haben dieselbe Form und verschiedene Bedeutung. **Ein
vorhandenes Auszählungsblatt darf nie ungeprüft in Folien übernommen werden**,
es liefert Ebene 2, die Folie braucht Ebene 3.

**Folgeregeln für Ebene 3:**

- Die vier Bewertungszahlen sind **keine Partition**. Eine Person kann in
  derselben Kategorie positiv und negativ codiert sein, deshalb ist
  `a + b + c + d` regelmäßig **größer** als `X`. Das ist korrekt und wird nicht
  repariert.
- Es gilt stets `max(a, b, c, d) ≤ X ≤ N`. Verletzt eine Zahl das, liegt ein
  Rechenfehler vor.
- Jede Kennzahl trägt die Zähleinheit im Namen: `Personen (n von N)` gegen
  `Gesamt Äußerungen`.

**Aufschlüsselung nach Perspektivgruppe** ist optional. Sie kann als eigene
Tabelle geführt werden, reicht aber häufig als qualitative Aussage im Fließtext
des Ergebnisdokuments („getragen von der Fertigung“, „die einzige in sich
geteilte Gruppe“). Bei Gruppen mit weniger als drei Personen unterbleibt die
Gruppenangabe wegen Re-Identifikationsrisiko.

## 7. Kategoriennummern normalisieren

Zwischen den Sheets bestehen zwei Schreibweisen:

| Sheet | Schreibweise | Beispiel |
|---|---|---|
| `Aussagen` Spalte B | ohne Schlusspunkt | `1.1` |
| `Auszählung` Spalte A | ohne Schlusspunkt | `1.1` |
| `Kategoriensystem` Spalte A | **mit** Schlusspunkt | `1.1.` bzw. `1.` |

Beim Verknüpfen der Sheets deshalb **immer** normalisieren
(`kategorie.rstrip(".")`) und nie auf Stringgleichheit vertrauen.

## 8. Validierung nach dem Schreiben

`scripts/build_workbook.py` führt diese Prüfungen aus und meldet das Ergebnis.
Verstöße in den Blöcken Struktur, Felder, Konsistenz und Anonymisierung, also die
Punkte 1 bis 23, sind **blockierend** (Exit-Code 1). Die Punkte 24 bis 28 sind
Warnungen und erlauben den Abschluss. Eine Ausnahme ist deklariert: Punkt 19
wird mit `--teilbestand` zur Warnung, siehe dort.

**Struktur**

1. Genau vier Sheets in der Reihenfolge `Aussagen`, `Kategoriensystem`,
   `Auszählung`, `Info`
2. Kopfzeilen exakt wie spezifiziert
3. keine Formelzellen

**Felder `Aussagen`**

4. keine Leerwerte in A, B, C, E
5. `Bewertung` ∈ {`+`, `-`, `o`, `>`}, Länge genau 1
6. `Kernaussage` ∈ {`*`, leer}
7. `Kennung` passt auf `^P\d{2}$` und steht in der Registry
8. `Kategorie` passt auf `^\d+\.\d+$` und existiert normalisiert im Kategoriensystem
9. keine doppelten Äußerungstexte
10. eckige Klammern paarig geschlossen
11. keine Zeilenumbrüche, Tabulatoren, Gedankenstriche, Auslassungspunkte
12. keine führenden, nachlaufenden oder doppelten Leerzeichen
13. Sortierung nach **Kategorie (numerisch) und Kennung**. Die dritte Stufe,
    der Gesprächsverlauf, ist aus der geschriebenen Datei nicht prüfbar, weil
    `reihenfolge` nicht in die Mappe geschrieben wird. Sie ist garantiert, solange
    die Mappe aus der JSON-Codiertabelle entsteht; eine von Hand umsortierte
    Mappe passiert diesen Punkt.

**Konsistenz zwischen den Sheets**

14. Auszählung wird **neu berechnet** und gegen die geschriebenen Werte geprüft;
    jede Abweichung ist ein Fehler
15. `Σ H (Kategorienzeilen) == H (Gesamtzeile) == Zeilenzahl in Aussagen`
16. `H == D + E + F + G` je Zeile
17. Gesamtzeile Spalte C ist die distinkte Gesamtzahl, nicht die Spaltensumme
18. jede Unterkategorie hat genau eine Zeile in `Auszählung`, Bezeichnung wörtlich
    identisch mit dem Kategoriensystem
19. jede Kategorie hat mindestens eine Codiereinheit. **Mit `--teilbestand` ist
    dieser Punkt eine Warnung**, siehe unten.
20. `Info.Umfang` nennt dieselbe Einheitenzahl wie die Gesamtzeile; das N im
    Auszählungskopf entspricht dem N der Registry
21. Registry ist partitionierend: jede Kennung genau einmal, Summe gleich N
22. Version im Dateinamen entspricht der Version in `Info.Stand`

**Anonymisierung**

23. Abgleich der Spalten `Äußerung` und `Ankerbeispiel` gegen die Klarnamensliste
    des Pseudonymschlüssels: null Treffer

**Warnungen, kein Abbruch**

24. `*`-Quote außerhalb 15 bis 30 Prozent, oder eine Kategorie mit Quote null
25. `o`-Anteil über 40 Prozent oder `>`-Anteil unter 15 Prozent
26. Klammeranteil über 40 Prozent
27. eine Kategorie mit weniger als drei verschiedenen Kennungen
28. `*`-Anteil **je Person** über 45 Prozent, oder bei mindestens zehn Einheiten
    dieser Person unter 5 Prozent

**Warum die Quote auch personenweise geprüft wird (Punkt 28).** Die Gesamtquote
aus Punkt 24 kann im Korridor liegen, während sich der Zitatpool auf wenige
Personen konzentriert: Eine besonders pointiert sprechende Person trägt ein
Drittel der Belege, eine andere kommt im Ergebnisdokument gar nicht vor. Beides
bleibt global unsichtbar. Punkt 28 hält die **Belegbasis je Person ausgewogen**,
damit die Zitate den Befund tragen und nicht das Sprachtalent Einzelner. Die
Schwellen sind bewusst weit gesetzt: Eine Streuung der Dichte ist normal
(`codierung.md` Abschnitt 7), gemeint sind die Ausreißer.

**Teilbestand.** `build_workbook.py --teilbestand` stuft Punkt 19 zur Warnung
herab. Gemeint ist der Zwischenstand einer Erhebungswelle oder eines einzeln
ausgewerteten Interviews: Stammt das Kategoriensystem aus einer größeren
Erhebung, hat fast jedes Einzelinterview unbesetzte Kategorien, und Punkt 19
wäre strukturell unerfüllbar. Ohne das Flag müsste der Anwender das
Kategoriensystem beschneiden und wiche damit vom Berichtssystem ab. Für den
Vollabschluss läuft der Bau **ohne** das Flag; dann ist eine leere Kategorie
wieder blockierend, denn dort bedeutet sie: System überarbeiten
(`kategoriensystem.md` Abschnitt 5).

Artefaktübergreifende Prüfungen gegen Ergebnisdokument und Prosa stehen in
`gates.md` und laufen mit `scripts/validate_deliverables.py`.

## 9. Skripte

### `scripts/build_workbook.py`

Schreibt die Mappe aus einer JSON-Codiertabelle und validiert sie anschließend.

```bash
python3 scripts/build_workbook.py \
  --input  codierung.json \
  --output "Codierung_P01-P14_260315_v3.xlsx" \
  [--anchor-mode real|prototyp] \
  [--denylist VERTRAULICH_klarnamen.txt] \
  [--teilbestand]        # Zwischenstand: Prüfpunkt 19 als Warnung
  [--comfort]            # optional freeze_panes + AutoFilter auf Aussagen
```

**Präzedenz von `--anchor-mode`.** Der Modus entscheidet sich in dieser
Reihenfolge:

1. eine **ausdrücklich gesetzte** Option `--anchor-mode` gewinnt immer,
2. sonst `meta.ankerbeispiele` aus der JSON, wenn dort `real` oder `prototyp`
   steht,
3. sonst `real`.

Die Option trägt bewusst keinen argparse-Default, damit „nicht gesetzt“ von „auf
`real` gesetzt“ unterscheidbar bleibt und ein Aufruf ohne Option die Angabe in
der JSON nicht stillschweigend überstimmt. Bei einem übernommenen
Kategoriensystem stammen die Ankerbeispiele aus fremdem Material; wähle dann
`prototyp` oder setze reale Anker aus dem neuen Material
(`kategoriensystem.md` Abschnitt 9).

Eingabeformat:

```json
{
  "meta": {
    "projekt": "…", "gegenstand": "…",
    "stand": "15.03.2026 (Version 3)",
    "umfang": "14 Interviews vollständig erhoben und codiert (612 Einheiten)",
    "auswertungsmethode": "…", "codierregeln": "…",
    "kernaussagen": "…", "ankerbeispiele": "real",
    "anonymisierungshinweis": "…",
    "n_personen": 14, "version": 3
  },
  "personen": [
    { "kennung": "P01", "perspektivgruppe": "Fertigung", "quellenart": "transkript" }
  ],
  "perspektivgruppen": [
    { "name": "Fertigung", "kennungen": ["P01", "P03", "P06", "P08", "P12", "P14"] }
  ],
  "kategoriensystem": [
    { "nummer": "1",   "ebene": "haupt", "bezeichnung": "…",
      "definition": "Oberkategorie für …" },
    { "nummer": "1.1", "ebene": "unter", "bezeichnung": "…",
      "definition": "…", "ankerbeispiel": "„…“ (P03)",
      "codierregel": "Hier codieren, wenn …" }
  ],
  "aussagen": [
    { "kennung": "P03", "kategorie": "2.1", "bewertung": "-",
      "kernaussage": true, "aeusserung": "…", "reihenfolge": 17 }
  ]
}
```

`reihenfolge` ist die Position im Gesprächsverlauf und steuert die tertiäre
Sortierung. `quellenart` ∈ {`transkript`, `mitschrift`, `protokoll`, `diktat`}
und ist nicht identifizierend, gehört also in die JSON und nicht nur in den
vertraulichen Schlüssel. `kategorie` und `nummer` sind **immer Zeichenketten**,
auch wenn sie wie Zahlen aussehen.

Während der Codierung dürfen die Einträge in `aussagen` die Zusatzfelder
`zitat_roh`, `char_start` und `char_end` tragen. Die Skripte ignorieren sie; sie
sind das Prüfmittel der Zitatprüfung in Richtung Transkript und werden nicht in
die Arbeitsmappe geschrieben. Bezugsfassung der Offsets und Statussemantik:
`codierung.md` Abschnitt 10.

**Sobald `zitat_roh` mitläuft, ist die JSON-Codiertabelle ein vertrauliches
Arbeitsdokument.** Der Rohspan trägt die Klarnamen und Ortsangaben, die die
Spalte `Äußerung` bereits ersetzt hat. Dateiname mit dem Präfix `VERTRAULICH_`,
Ablage in der geschützten Projektablage, nie in ein Repository
(`codierung.md` Abschnitt 1). Das betrifft insbesondere den Aufruf
`validate_deliverables.py --key <codierung.json>`: Für die Registry-Gegenprüfung
genügt der Pseudonymschlüssel im normierten Markdown-Format.

Ein vollständiges, lauffähiges Beispiel liegt als
`references/beispiel_codierung.json` bei (erfundener Übungsfall, sechs
Interviews, 32 Codiereinheiten, vier Unterkategorien).

**Zahlen in den Metadaten werden ebenfalls generiert.** Drei Felder von `meta`
dürfen Platzhalter tragen, die beim Schreiben gefüllt werden:

| Feld | Platzhalter |
|---|---|
| `umfang` | `{n}`, `{einheiten}` |
| `auswertungsmethode` | `{kategorien}`, `{hauptkategorien}` |
| `stand` | `{version}` |

Stehen dort feste Zahlen, prüft die Validierung sie gegen die berechneten
Werte (Punkt 20 und 22). Der Platzhalterweg ist der sichere.

Ausgabe: die `.xlsx`, dazu auf stdout die berechnete Auszählung als
Markdown-Tabelle und der Validierungsbericht. Exit-Code ungleich null bei
blockierenden Verstößen.

### `scripts/aggregate.py`

Berechnet die drei Aggregationsebenen.

```bash
python3 scripts/aggregate.py \
  (--input codierung.json | --workbook "Codierung_P01-P14_260315_v3.xlsx") \
  --level personen-kategorie|aeusserungen-bewertung|personen-bewertung|alle \
  [--group-by perspektive] \
  [--format md|json|zeilen]
```

`--format zeilen` liefert je Kategorie die fertige, einsetzbare Zählzeile
`X von N Personen (a +, b -, c o, d >)` und prüft dabei `max(a,b,c,d) ≤ X ≤ N`.
`--format json` ist die Eingabe für die Folienerzeugung.

### `scripts/_kern.py`

Gemeinsames Modul der drei Skripte: Laden und Prüfen der JSON-Codiertabelle,
Normalisierung der Kategoriennummern, Sortierung, die drei Aggregationsebenen,
Rücklesen einer geschriebenen Arbeitsmappe, Text- und Zitatnormalisierung.
Wird nicht direkt aufgerufen. Dass alle drei Skripte dieselbe Rechenfunktion
benutzen, schwächt die Gates nicht: `validate_deliverables.py` rechnet aus der
**geschriebenen Datei** neu und vergleicht mit dem, was dort steht.
