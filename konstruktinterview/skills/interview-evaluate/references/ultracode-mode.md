# Ultracode-Auswertungsmodus (Multi-Agent)

> Diese Anleitung gilt nur, wenn in **Schritt 1b** der Modus *Ultracode* oder
> *Ultracode + Doppelcodierung* gewählt wurde (bzw. der Skill mit dem Stichwort
> `ultracode` gestartet wurde). Andernfalls gilt der sequenzielle Standardpfad
> der `SKILL.md`.

Du bist hier **Orchestrator**, nicht Codierer. Du steuerst Sub-Agenten über das
Workflow-Tool (`agent` / `parallel` / `pipeline`) und sicherst die Methodik.
Schritt 1 (Datensichtung) und Schritt 4 (Auswertung + Bericht) bleiben unverändert
wie im Standardpfad — der ultracode-Modus verzweigt nur das WIE von Schritt 2–3,
nicht das Ergebnis. **Am Ende steht derselbe Auswertungsbericht wie im Standardpfad.**

## Leitprinzipien (nicht verhandelbar)
- **Parallelisieren nur, was unabhängig ist** (Codieren je Transkript).
  **Serialisieren, was geteilt ist**: Kategoriensystem, Dedup, Zählung, Bericht.
- **Das Kategoriensystem kommt aus EINER Hand** (ein Synthese-Schritt). Sonst
  driften Kategorien auseinander. Schritt 3 wird NICHT parallelisiert.
- **Die Codiertabelle ist Single Source of Truth.** Prosa und Zahlen im Bericht
  werden gegen sie geprüft, nie umgekehrt.
- Jeder Sub-Agent befolgt dieselben Regeln wie der Standardpfad: ein Kerngedanke
  pro Codiereinheit, glätten OHNE eigene Begriffe (Wortlaut der Interviewpartner),
  Kontext in [eckigen Klammern], anonymisiert (nur IV-Nr + Perspektivgruppe).

## Tabellen-Erweiterung (Voraussetzung für alle Prüfungen)
Jede Codiereinheit führt zusätzlich zur geglätteten `Äußerung` drei Felder:
`zitat_roh` (unveränderter Originalspan, copy-paste), `char_start`, `char_end`
(Zeichen-Offsets im Transkript). Ohne diese Felder sind die deterministischen
Gates nicht umsetzbar.

## Phasen

**P0 — Datensichtung (du selbst, kein Fan-out).**
Untersuchungsziel, Stichprobeninfo, Zuordnung Transkript→Perspektivgruppe. Lege
die Namens-Denylist aus den Stichprobeninfos an (echte Namen/Orte/Funktionen)
für das Anonymisierungs-Gate.

**P1 — Offene Codierung (`pipeline`, kein Barrier).**
`pipeline(transkripte, codiere, glaette_pruefe)`. Jedes Transkript ist
unabhängig → `pipeline`, nicht `parallel`: ein langsames Transkript blockiert die
anderen nicht. Bei *Ultracode + Doppelcodierung*: je Transkript K=2 Codierer-Jobs,
sonst K=1. Spalte `kategorie_vorschlag` ist hier induktiv/vorläufig.
Schema je Codier-Agent:
```json
{ "codiereinheiten": [{ "iv_nr": "str", "perspektive": "str",
  "zitat_roh": "str", "char_start": "int", "char_end": "int",
  "geglaettet": "str", "bewertung": "positiv|negativ|neutral",
  "kategorie_vorschlag": "str" }] }
```

**P2 — Kategoriensystem-Synthese (`parallel`-Barrier, EIN Synthese-Agent).**
`parallel([() => agent(synthese, ...)])[0]`. Der Barrier garantiert, dass ALLE
P1-Codierungen vorliegen. Der Synthese-Agent dedupliziert synonyme Vorschläge zu
EINEM induktiven System (Definition, Ankerbeispiel im Wortlaut, Codierregeln je
Kategorie). **Keine Stärken/Schwächen als Hauptkategorien** — thematische
Kategorien, Bewertung als Attribut innerhalb. Kategorien, die nur ein Codierer
sah, NICHT verwerfen, sondern als Einzelnennung-Kandidat markieren. Jeder
Kategorienname muss an die Sprache der Interviewpartner anschließen.
Schema:
```json
{ "kategorien": [{ "name": "str", "definition": "str",
  "ankerbeispiel": "str (zitat + IV-Nr)", "codierregel": "str" }] }
```

**P3+P4 — Re-Codierung + adversariale Verifikation (`pipeline`, kein Barrier).**
Alle Codiereinheiten gegen das FINALE System neu zuordnen und prüfen. Bei vielen
Einheiten zu Chunks bündeln (`chunk_size ≈ ceil(anzahl / 12)`), Items = Chunks.
`pipeline(chunks, rekodiere, verifiziere)`:
- *rekodiere*: ordnet jede Einheit dem konsolidierten System zu.
- *verifiziere* (adversarial, Auftrag „widerlege"): prüft je Einheit gegen
  `zitat_roh` und Transkript: Steht das Zitat dort? Wurde nur getilgt (Füllwörter,
  Wiederholungen) oder ein inhaltstragender Begriff SUBSTITUIERT? Status ∈
  {VERIFIED, SMOOTHING_OK, DRIFT, NOT_FOUND}.
Schema je Urteil:
```json
{ "iv_nr": "str", "kategorie_final": "str", "zuordnung_korrekt": "bool",
  "status": "VERIFIED|SMOOTHING_OK|DRIFT|NOT_FOUND", "begruendung": "str" }
```
**Gates (blockierend):** `NOT_FOUND` → Einheit raus aus Tabelle + protokollieren.
`DRIFT` → zurück an Codierer, Originalbegriff wiederherstellen.

**Mayring-Revision:** P2→P3 einmal wiederholen (max. 2 Durchgänge). Stößt die
Re-Codierung auf Material, das nicht passt, das SYSTEM nachschärfen (zurück in P2),
nicht ins bestehende System pressen. Dann terminieren.

**Dedup (deterministisch, du selbst).** Zwei Einheiten = Duplikat, wenn ihre
`zitat_roh`-Spans im selben Transkript überlappen (Offsets vergleichen, nicht
semantisch raten) UND dieselbe Kategorie tragen → auf eine Zeile mergen.
Überlappung bei VERSCHIEDENEN Kategorien ist erlaubte Mehrfachcodierung.

**P5 — Auszählung (deterministisch, du selbst — KEIN Agent).**
Häufigkeiten aus der dedupten Tabelle per Aggregation, nicht durch Lesen rechnen
(ein Zähl-Agent verzählt sich). **Zähleinheit: distinct IV-Nr (Personen), nicht
Codiereinheiten** — sonst inflationiert eine gesprächige Person die Zahl.
**Rohwerte, nie Prozent.** Nenner X = befragte Personen je Perspektivgruppe, pro
Gruppe ausgewiesen. Einzelnennungen explizit kennzeichnen. Bei Doppelcodierung:
Codierer-Dissens je Stelle als Befund ausweisen, nicht wegmitteln.

**P6 — Berichtssynthese (EIN Autor-Agent).**
Baut den Standard-Bericht aus Kategoriensystem (P2) + Auszählung (P5) +
verifizierten Zitaten. Im Bericht zitiert er `zitat_roh` (Originalwortlaut), nicht
die geglättete Fassung. Zusatzabschnitt **„Codierübereinstimmung und Diskrepanzen"**
(Rohwerte, qualitativ beschrieben — kein Kappa, keine Scheingenauigkeit bei
kleinem N).

**Anonymisierungs-Gate (blockierend, letzter Schritt vor Ausgabe).**
EIN Redaction-Durchgang über den FERTIGEN Bericht inkl. Anhang (nicht verteilt in
den Codier-Agenten). Adversarialer Auftrag: finde alles Re-Identifizierende
(Eigennamen, Funktionen mit Einzelbesetzung, Orte, Projektnamen). Backstop: Grep
des finalen Berichts gegen die Namens-Denylist aus P0 muss NULL Treffer liefern.
Der Anhang mit allen `zitat_roh` ist der größte Leck-Kandidat.

## Konsistenz-Endcheck (du selbst, vor Abgabe)
Jede im Bericht genannte Zahl „Y von X" gegen die Tabelle prüfen: tatsächlich
Y distinct IV-Nr in der Kategorie? Abweichung → Tabellenwert gewinnt.

## Diskrepanzauflösung (kein Mehrheitsvotum)
Abweichungen sind Befund, nicht Störung. Auslegungsfehler am Material korrigieren;
unscharfe Codierregel → System nachschärfen; echte Mehrdeutigkeit einer Stelle →
beide Lesarten in den Bericht, Stelle als ambig markieren. Tragfähige
Einzelnennungen bleiben drin. Strittiges transparent in die Limitationen.

## Fallback
Steht das Workflow-Tool nicht zur Verfügung oder ist N sehr klein, sauber auf den
sequenziellen Standardpfad zurückfallen. Die Prüf-Gates (Zitatabgleich,
deterministische Zählung, Anonymisierung) gelten auch dort — ultracode ist
schneller, nicht qualitativ niedriger.
