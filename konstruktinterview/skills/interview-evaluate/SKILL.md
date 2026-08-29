---
name: interview-evaluate
description: >
  Wertet durchgeführte Konstruktinterviews (König/Volmer 2018) inhaltsanalytisch aus.
  Nutze diesen Skill, wenn der User Interviewtranskripte, -mitschriften oder
  -protokolle auswerten, codieren, auszählen oder zu einem Ergebnisdokument
  verdichten möchte.
argument-hint: [Pfad zu Interviewdaten oder Beschreibung des Kontexts]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash, WebSearch, AskUserQuestion, Task, Skill, Workflow
---

# Konstruktinterview-Auswertung

Du wertest Konstruktinterviews (König/Volmer 2018) nach der qualitativen
Inhaltsanalyse (Mayring) aus. Das Ergebnis ist kein Fließtextbericht, sondern ein
Artefaktpaar: eine Arbeitsmappe, die die Daten hält, und ein Ergebnisdokument,
das vollständig aus ihr abgeleitet wird.

## Artefaktmodell

| Artefakt | Rolle | Format | Adressat |
|---|---|---|---|
| **Arbeitsmappe** | Datenwahrheit: jede Codiereinheit, das Kategoriensystem, die Auszählung, die Rahmendaten | `.xlsx`, vier Sheets | intern |
| **Ergebnisdokument** | Bericht an den Auftraggeber; enthält keine Zahl und kein Zitat, das nicht in der Arbeitsmappe steht | Standard `.pptx`, Markdown nur bei sehr kleinem N | Auftraggeber |
| **Prozessnotiz** | Zwischenstand je Erhebungswelle: Artefaktliste, Datenbasis, Stichprobe je Perspektivgruppe, Bewertungsverteilung, offene Punkte, nächste Schritte | `.md`, zwei Seiten | intern |
| **Pseudonymschlüssel** | Zuordnung Klarname zu Kennung, Perspektivgruppe, Quellenart, Sonderfallhinweise | `.md` mit Präfix `VERTRAULICH_`, außerhalb der Klientenablage | streng intern |
| **JSON-Codiertabelle** | Arbeitsformat der Codierung samt `zitat_roh`; Quelle der Arbeitsmappe | `.json` mit Präfix `VERTRAULICH_`, geschützte Projektablage, nie in ein Repository | streng intern |

Drei Grundsätze tragen das Modell:

1. **Zahlen werden generiert, nie getippt.** Jede Zahl im Ergebnisdokument wird
   aus dem Sheet `Aussagen` neu berechnet.
2. **Jedes Zitat stammt wortgleich aus einer mit `*` markierten Zeile** derselben
   Arbeitsmappe.
3. **Rückfluss ist Pflicht, aber nur für den Wortlaut.** Wird am Ergebnisdokument
   der **Wortlaut** einer Äußerung geändert, also ersetzt, übersetzt oder
   anonymisiert, wandert die Änderung in die Arbeitsmappe zurück, bevor der Stand
   geschlossen wird. Eine mit `…` markierte **Kürzung** ist kein Rückflussfall:
   Die Arbeitsmappe hält immer die vollständige Äußerung, die gekürzte Fassung
   lebt nur im Ergebnisdokument.

Dateiname der Arbeitsmappe: `Codierung_<ErsteKennung>-<LetzteKennung>_<JJMMTT>_v<N>.xlsx`.
Version im Dateinamen und im Sheet `Info` kommen aus einer Quelle.

## Vorgehen

### Schritt 1: Datenbasis sichten, pseudonymisieren

Frage den User nach Untersuchungsziel und Verwendungszweck, nach der Stichprobe
(wer, welche Perspektivgruppen) und nach den Interviewdaten. Lies alle Daten
vollständig.

Kläre die **Weiche Neubeginn oder Fortschreibung**: Existiert bereits eine
Arbeitsmappe, lade sie, codiere nur die neuen Interviews und schärfe das
Kategoriensystem nach, statt es neu zu erfinden (Fortschreibungspfad in
`references/kategoriensystem.md`).

Lege den Pseudonymschlüssel an: interne Interviewnummer nach Durchführungs-
reihenfolge, davon entkoppelt eine stabile Kennung `P01`, `P02` … Pro Person
Perspektivgruppe und **Quellenart** (Transkript, Mitschrift, Gedächtnisprotokoll,
Diktat) festhalten, im normierten Tabellenformat aus `references/codierung.md`
Abschnitt 2; nur so läuft später die Registry-Gegenprüfung. Bei Fortschreibung
werden Kennungen nur ergänzt, nie neu vergeben.

**Lege im selben Schritt die Namens-Denylist an**, als Textdatei mit einem
Begriff je Zeile: die realen Namen, Orte, Einheiten- und Projektbezeichnungen aus
Schlüssel und Stichprobeninfos. Sie geht später als `--denylist` in beide
Skripte. Ohne sie entfällt der blockierende Teil des Anonymisierungs-Gates; die
Skripte melden das als „Denylist-Gate nicht geprüft“, reparieren es aber nicht.
Beide Dateien tragen das Präfix `VERTRAULICH_` und liegen außerhalb der
Klientenablage.

### Schritt 1b: Auswertungsmodus wählen

Frage **einmal** via `AskUserQuestion`. Hat der User den Skill mit dem Stichwort
`ultracode` gestartet, überspringe die Frage.

Empfehlung einblenden: N ≤ 3 oder eine Perspektivgruppe → Standard. N ≥ 9 und
mehrere Perspektivgruppen → Ultracode.

| Option | Beschreibung |
|--------|--------------|
| **Standard (sequenziell)** | Ein Agent durchläuft Codierung, Kategoriensystem und Auswertung nacheinander. Schnell, token-sparsam, Schritt für Schritt nachvollziehbar. Empfohlen bis etwa 8 Interviews. |
| **Ultracode (Multi-Agent)** | Mehrere Sub-Agenten codieren parallel, ein Orchestrator führt zu EINEM Kategoriensystem zusammen und prüft Zitate, Dedup und Anonymisierung gegen. Empfohlen ab etwa 9 Interviews. |
| **Ultracode + Doppelcodierung** | Wie Ultracode, zusätzlich codiert ein zweiter Agent jedes Transkript unabhängig nach; Abweichungen werden als Codiersignal ausgewiesen. Höchste Absicherung, höchster Aufwand. |

Default: Standard. Bei Ultracode folge `references/ultracode-mode.md`; sie
verzweigt das WIE der Schritte 2 bis 3 und weist für die Schritte 4 bis 6
Rollen zu. Die Regeln und die Gates bleiben dieselben, und am Ende stehen
dieselben Artefakte. Steht das Workflow-Tool nicht zur Verfügung, fällt der Modus
sauber auf den Standardpfad zurück.

### Schritt 2: Codieren

Gehe jedes Interview systematisch durch und erzeuge Zeilen dieser Form:

| Kennung | Kategorie | Bewertung | Kernaussage | Äußerung |
|---|---|---|---|---|
| P03 | 2.1 | - | `*` | Wir erfahren Neuigkeiten meistens zuerst in der Kantine. |

- **Eine Codiereinheit trägt einen Kerngedanken.** Zwei Gedanken in einer Passage
  ergeben zwei Zeilen; ein Gedanke bleibt eine Zeile, auch wenn er drei Sätze
  braucht.
- **Relevanzschwelle.** Im Zweifel codieren gilt für inhaltstragende,
  deutungsrelevante Aussagen. Reine Verfahrens-, Chronik- und
  Faktendarstellungen ohne Bezug zu Untersuchungsziel und Verwendungszweck
  bleiben draußen.
- **Glätten ohne eigene Begriffe.** Füllwörter und Abbrüche raus, Wortlaut,
  Register und Ich-Perspektive der befragten Person bleiben.
- **Bewerten vierwertig**: `+` positiv, `-` negativ, `o` neutral,
  `>` Veränderungswunsch. Vorrang: `>` schlägt `-`; `-` und `+` schlagen `o`.
- **Belege markieren**, nicht Kernaussagen formulieren: `*` in der Spalte
  `Kernaussage` selektiert zitierfähige Äußerungen, Zielquote 20 bis 25 Prozent.

Konventionen für Glättung, eckige Klammern, Bewertung, Belegmarkierung und
Sortierung: `references/codierung.md`.

**Format.** Führe die Codierung als **JSON-Codiertabelle** nach
`references/beispiel_codierung.json`; das autoritative Schema steht in
`references/excel-output.md` Abschnitt 9. Führe je Einheit zusätzlich
`zitat_roh` (unveränderter Originalspan, Pflicht) sowie `char_start` und
`char_end` (optional) mit. Die Skripte ignorieren diese drei Felder, und sie
kommen nicht in die Arbeitsmappe; sie sind das Prüfmittel des
Verifikationsdurchgangs weiter unten. Bezugsfassung der Offsets:
`references/codierung.md` Abschnitt 10.

**Die JSON-Codiertabelle ist vertraulich**, sobald sie `zitat_roh` oder
Klarnamen führt: Dateiname `VERTRAULICH_codierung_*.json`, Ablage in der
geschützten Projektablage, niemals in ein Repository. Der Rohspan trägt genau
die Namen und Orte, die in der Spalte `Äußerung` schon ersetzt sind. Gib für die
Registry-Gegenprüfung den Pseudonymschlüssel weiter, nicht die Codiertabelle.

Die Kategorienspalte bleibt in diesem Schritt vorläufig. **Niemals per Stichwort-
liste oder Regex kategorisieren.** Die Zuordnung ist inhaltliches Urteil.
Bash und Python dienen ausschließlich der Mechanik: Dateien schreiben, zählen,
Offsets vergleichen, greppen, Textüberlauf prüfen.

**Verifikationsdurchgang gegen das Transkript, je Interview, pflichtig.** Das
Zitat-Gate läuft in beide Richtungen. Die Richtung Dokument gegen Codierung
übernimmt später das Prüfskript; die Richtung Codierung gegen Transkript
übernimmst du hier, mit dem ausdrücklichen Auftrag zu widerlegen: Steht die
geglättete Äußerung so im Ausgangsmaterial? Wurde nur getilgt, oder wurde ein
inhaltstragender Begriff **ersetzt**? Vergib je Einheit einen Status:

| Status | Bedeutung | Einordnung |
|---|---|---|
| `VERIFIED` | wortgleiche Übernahme, deckungsgleich mit `zitat_roh` | Gutzustand, bleibt |
| `SMOOTHING_OK` | nur Füllwörter, Abbrüche, Wiederholungen getilgt | **erwarteter Gutzustand geglätteter Einheiten**, bleibt |
| `DRIFT` | ein inhaltstragender Begriff wurde ersetzt | Alarm: zurück in die Codierung, Originalbegriff wiederherstellen |
| `NOT_FOUND` | steht so nicht im Material | Alarm: Einheit raus, im Protokoll vermerken |

Zwei Gutzustände, zwei Alarmzustände: Glättung verändert den Rohspan fast immer,
und bei automatisch erzeugten Transkripten landet praktisch jede Einheit auf
`SMOOTHING_OK`. Das ist der Normalfall, kein Mangel. Der Blick gilt `DRIFT` und
`NOT_FOUND`; Näheres in `references/codierung.md` Abschnitt 10.

Bei vielen Interviews lohnt sich ein `Task`-Subagent je Interview. Der Durchgang
gilt pfadunabhängig: im Standardpfad genauso wie im Ultracode-Pfad.

### Schritt 3a: Analysekategorien induktiv bilden

Beginne mit zwei bis drei Interviews, bilde Kategorien aus leicht fassbaren
Aussagen, erweitere schrittweise, revidiere in höchstens zwei Durchgängen. Genau
zwei Ebenen. Keine Stärken/Schwächen-Hauptkategorien: thematische Kategorien
bilden, Bewertung als eigenes Attribut führen. Regeln, Gates und Satzmuster für
Definition, Ankerbeispiel und Codierregel: `references/kategoriensystem.md`.

### Schritt 3b: Berichtsgliederung festlegen (Checkpoint C1)

Das feingliedrige Analysesystem ist ein gutes Analyse- und ein schlechtes
Berichtsinstrument. Leite daraus eine flache Berichtsgliederung ab: 3 bis 4
Hauptkategorien, 10 bis 15 Unterkategorien, benannt nach dem Erkenntnisinteresse
des Auftraggebers.

**Das ist eine Beratungsentscheidung, keine Maschinenentscheidung.** Lege
höchstens drei Varianten vor und lass wählen. Nach der Wahl werden **alle**
Codiereinheiten gegen das gewählte System neu codiert, mit dokumentiertem
Mapping alt zu neu.

### Schritt 4: Auszählen

Berechne alle Kennzahlen skriptgestützt, nie aus dem Gedächtnis, und übernimm
kein vorhandenes Auszählungsblatt ungeprüft. Werkzeug ist `scripts/aggregate.py`:
vor Schritt 5 aus der JSON-Codiertabelle (`--input codierung.json`), danach aus
der geschriebenen Mappe (`--workbook …`). Drei Aggregationsebenen, die nicht
verwechselt werden dürfen:

| Ebene | Zähleinheit | Verwendung |
|---|---|---|
| Personen je Kategorie | distinkte Kennungen | Verbreitungsmaß „X von N“ |
| Äußerungen je Bewertung je Kategorie | Codiereinheiten | Sheet `Auszählung` |
| Personen je Bewertung je Kategorie | distinkte Kennungen | Zählzeilen im Ergebnisdokument |

**Lege die berechneten Kennzahlen dem User vor, bevor die erste Folie entsteht**
(`aggregate.py --level alle --format md`). Weichen sie von einem vorhandenen
Auszählungsblatt oder einem früher kommunizierten Stand ab, benenne die
Abweichung ausdrücklich, statt sie stillschweigend zu überschreiben.

Kategorien mit auffällig geringer Personenabdeckung schlägst du nach dem Zählen
zur Zusammenlegung vor. Näheres: `references/excel-output.md`.

### Schritt 5: Arbeitsmappe schreiben

Baue die vier Sheets `Aussagen`, `Kategoriensystem`, `Auszählung`, `Info` nach
`references/excel-output.md` mit `scripts/build_workbook.py`. Das Skript
validiert die Mappe nach dem Schreiben und meldet Struktur-, Feld- und
Konsistenzfehler.

**Zwischenstände: Wellen und einzelne Interviews.** Läuft die Erhebung in Wellen,
oder wird ein einzelnes Interview für sich ausgewertet, entsteht je Stand eine
eigene Mappe, gebaut mit **`--teilbestand`**. Das Flag stuft Prüfpunkt 19 (jede
Kategorie hat mindestens eine Codiereinheit) zur Warnung herab. Ein
Kategoriensystem, das aus einer größeren Erhebung stammt oder für die
Gesamterhebung entworfen ist, hat in einer einzelnen Welle fast immer unbesetzte
Kategorien; ohne das Flag müsstest du das System beschneiden und damit vom
Berichtssystem abweichen. **Das System bleibt vollständig.**

```bash
# Zwischenstand einer Welle
python3 scripts/build_workbook.py --input welle2.json \
  --output "Codierung_P07-P09_260320_v1.xlsx" --teilbestand

# Vollabschluss, ohne Flag: eine leere Kategorie ist wieder blockierend
python3 scripts/build_workbook.py --input codierung.json \
  --output "Codierung_P01-P14_260415_v3.xlsx"
```

Der Vollabschluss läuft ohne das Flag: Dort bedeutet eine leere Kategorie, dass
das System zu überarbeiten ist. Stammt das Kategoriensystem aus einer früheren
Erhebung, gehört dazu die Entscheidung über die Ankerbeispiele
(`references/kategoriensystem.md` Abschnitt 9): reale Anker aus dem neuen
Material setzen oder `--anchor-mode prototyp` wählen.

### Schritt 6: Ergebnisdokument bauen (Checkpoints C2 und C3)

Fordere zuerst die Gestaltungsvorlage des Auftraggebers an. Erklärt er, dass
keine existiert, verwende nach seiner Bestätigung das **neutrale Standarddesign**
aus `references/pptx-output.md` Abschnitt 1 und kennzeichne es im Dokument als
Platzhalter. Ohne Vorlage und ohne diese Bestätigung wird der Foliensatz nicht
gebaut. Dramaturgie, Folienbaupläne, Zähl- und Zitatregeln, Textsortenregeln:
`references/pptx-output.md`.

Trenne dabei drei Sorten von Aussagen:

- **berechenbar** (Zählzeilen, Überblick, Stichprobenangaben, Zitatpool) →
  skriptgestützt erzeugen, nie schätzen;
- **hybrid** (Unterthemen innerhalb einer Kategorie, Zuschnitt der Themenblöcke,
  Zitatauswahl) → gruppieren, bestätigen lassen, dann zählen;
- **beraterisches Urteil** (Befundüberschriften, Leitsätze, Spannungsfelder,
  Empfehlungen) → dem User zur Bestätigung vorlegen, nicht stillschweigend setzen.

Notiere beim Setzen jedes Zitats seine Quellzeile (`Aussagen!<Zeile>`) in einer
Begleitdatei; sie geht als `--zitatregistry` in die Prüfung ein.

Vor Abgabe laufen die Gates aus `references/gates.md`. Sie sind dort mit **[S]**
und **[A]** gekennzeichnet: `scripts/validate_deliverables.py` übernimmt die
[S]-Punkte, die [A]-Punkte prüfst du selbst. Lass Prosa vor der Abgabe durch die
Skills `stop-slop` und `humanizer` laufen.

**Der Abgabelauf ist ein Lauf in Modus B**, also mit `--deck` beziehungsweise
`--report`. Ein Lauf nur gegen die Arbeitsmappe (Modus A) prüft die Mappe, nicht
das Ergebnisdokument: Zitat-Gate, Kongruenz-Lint und die Dokumentteile von Zähl-
und Konsistenz-Gate haben dort kein Prüfobjekt. Das Protokoll führt sie im
Abschnitt **Nicht geprüft** auf; lies ihn, bevor du einen grünen Lauf als
Freigabe wertest.

## Checkpoints

| | Wann | Wer entscheidet | Was der Skill liefert |
|---|---|---|---|
| **C1** | nach Schritt 3b | Mensch | bis zu drei Gliederungsvarianten mit Personenabdeckung je Kategorie |
| **C2** | nach dem ersten vollständigen Ergebnisdokument | Mensch | Dokument zur Redline, dazu der Folientext-Export als Markdown (je Folie eine Überschrift, Absätze in Folienreihenfolge) als diff-fähige Grundlage |
| **C3** | nach jeder Redline | Maschine, meldet nur | Nachlese: Typografie, Anführungszeichen-Paarung, abgebrochene Sätze, doppelte Leerzeichen, Zahl-Text-Kongruenz, neue Anonymisierungslücken, neue Zitatabweichungen |

**Wortlaut-Sperre:** Nach der ersten Freigabe ändert ein Datenupdate
ausschließlich Zahlen, Tippfehler und nachweislich falsche Tatsachenaussagen.
Neue Erkenntnisse kommen als ausgewiesene Ergänzung, nie als Umformulierung.
Die maschinelle Nachlese meldet, sie formuliert nicht um.

## Quick-Reference

| Thema | Regel | Detail |
|---|---|---|
| Kodiereinheit | ein Kerngedanke, 1 bis 3 Sätze, Richtwert 80 bis 340 Zeichen, Median um 150 | `references/codierung.md` |
| Segmentierung | ein zusammenhängender Kerngedanke wird nie gesplittet, um einen Zeichenwert zu halten | `references/codierung.md` |
| Relevanzschwelle | reine Verfahrens-, Chronik- und Faktendarstellung ohne Bezug zum Untersuchungsziel wird nicht codiert | `references/codierung.md` |
| Bewertung | `+` `-` `o` `>`, Vorrang `>` vor `-`, `-`/`+` vor `o` | `references/codierung.md` |
| Belegmarkierung | `*` = zitierfähig, Zielquote 20 bis 25 Prozent gesamt, je Person 5 bis 45 Prozent | `references/codierung.md` |
| Verifikationsstatus | `SMOOTHING_OK` ist der erwartete Gutzustand; Befunde sind `DRIFT` und `NOT_FOUND` | `references/codierung.md` |
| Kennung | `Pnn`, stabil, Schlüssel separat und vertraulich | `references/codierung.md` |
| Codiertabelle | mit `zitat_roh` vertraulich: `VERTRAULICH_codierung_*.json`, nie in ein Repository | `references/codierung.md` |
| Zwischenstand | Welle oder Einzelinterview mit `build_workbook.py --teilbestand`, Vollabschluss ohne | `references/excel-output.md` |
| Kategorienebenen | genau zwei; codiert wird nur auf Unterkategorienebene | `references/kategoriensystem.md` |
| Codierregel | „Hier codieren, wenn …“ plus Abgrenzung oder Vorrang | `references/kategoriensystem.md` |
| Arbeitsmappe | vier Sheets, keine Formeln, Kategorie als Text | `references/excel-output.md` |
| Zählzeile | `X von N Personen (a +, b -, c o, d >)`, Personen, nicht Äußerungen | `references/pptx-output.md` |
| Zahlen | Rohwerte `X von N`, nie Prozent, nie „die Mehrheit“ | `references/pptx-output.md` |
| Zitate | nur aus dem `*`-Pool, ein Anführungszeichenpaar = eine Person | `references/gates.md` |
| Anführungszeichen | Zitat in `„…“`, **Binnenzitat in `‚…‘`**, keine Guillemets | `references/codierung.md` |
| Auslassungszeichen | nur im Ergebnisdokument, nie in der Arbeitsmappe; fließen nicht zurück | `references/codierung.md` |
| Anonymisierung | Zitate im Ergebnisdokument ohne Kennung und ohne Gruppenangabe; Denylist ab Schritt 1 | `references/gates.md` |

## Häufige Fehler

- **Ein Markdown-Bericht als Endprodukt.** Die Arbeitsmappe ist das primäre
  Artefakt; das Ergebnisdokument leitet sich aus ihr ab, nicht umgekehrt.
- **Personen- und Äußerungszahlen verwechselt.** Die Klammer `(a +, b -, c o, d >)`
  im Ergebnisdokument zählt Personen, das Sheet `Auszählung` zählt Äußerungen.
  Beide Zahlenreihen sehen gleich aus und bedeuten Verschiedenes.
- **Die Bewertungsklammer als Partition gelesen.** Eine Person kann in derselben
  Kategorie `+` und `-` beitragen; `a+b+c+d > X` ist normal und wird nicht repariert.
- **Freigegebene Prosa bei einem Datenupdate neu geschrieben.** Der teuerste
  vermeidbare Fehler: die Wortlaut-Sperre gilt ab der ersten Freigabe.
- **Zahl ersetzt, Satz nicht mitgelesen.** „2 von 12, beide aus der Fertigung“
  wird beim Update zu „3 von 14, beide …“. Nach jedem Zahlenupdate den
  Kongruenz-Lint laufen lassen.
- **Zitat aus zwei Personen zusammengesetzt** oder paraphrasiert und trotzdem in
  Anführungszeichen. Ein Anführungszeichenpaar ist eine Codiereinheit.
- **Wörtlich zitiert aus einer Mitschrift.** Wortlautqualität hängt an der
  Quellenart, nicht am Verifikationsstatus. Eine Kennzeichnung heilt das nicht:
  Solches Material wird ohne Anführungszeichen sinngemäß wiedergegeben.
- **Binnenzitat in denselben Anführungszeichen wie das Zitat.** Zwei schließende
  Zeichen hintereinander machen jede Zitatprüfung blind. Binnenzitate in `‚…‘`.
- **Gekürztes Zitat in die Arbeitsmappe zurückgeschrieben.** Die Mappe hält die
  vollständige Äußerung; `…` gehört ausschließlich ins Ergebnisdokument.
- **Überkodierung deskriptiver Passagen.** Erzählfreudige Interviews enthalten
  lange Chronik- und Verfahrensstrecken. Wer sie mitcodiert, verdoppelt den
  Bestand an neutralen Einheiten, verschiebt jede Zahl der Äußerungsebene und
  gewinnt keinen einzigen Befund.
- **Zu fein segmentiert.** Ein Kerngedanke wird nicht geteilt, um einen
  Zeichenrichtwert zu halten. Die Längenangaben sind Richtwerte, keine
  Schnittkante.
- **Kategorienwildwuchs.** Über 20 Unterkategorien werden nicht berichtsfähig;
  ein Systemwechsel spät im Prozess kostet die vollständige Neucodierung.
- **Stale Metadaten.** Auszählung, Info-Sheet und Stichprobenangaben werden bei
  jedem Stand neu berechnet, nie fortgeschrieben.
- **Der Auswerter als Handelnder im Bericht.** Das Ergebnisdokument referiert,
  was die Befragten gesagt haben, und was daraus folgt. Keine Selbstnennung des
  auswertenden Instituts, keine Leistungszusage; Prozessvorschläge gehören in ein
  eigenes Dokument.
- **Abstrakte Dreiklang-Überschriften** („Spannungsfeld zwischen A, B und C“).
  Befunde sind vollständige Aussagesätze im Indikativ Präsens.

## Referenzen und Skripte

| Datei | Inhalt |
|---|---|
| `references/codierung.md` | Codierkonventionen: Kodiereinheit, Glättung, eckige Klammern, Bewertung, Belegmarkierung, Pseudonymisierung, Sortierung |
| `references/kategoriensystem.md` | Zwei Ebenen, Satzmuster, MECE, Trennung Analyse- und Berichtssystem, Fortschreibung |
| `references/excel-output.md` | Arbeitsmappe Sheet für Sheet, Formatierung, drei Aggregationsebenen |
| `references/pptx-output.md` | Foliendramaturgie, Baupläne, Zähl- und Zitatregeln, Textsorte, Template-Anforderung |
| `references/gates.md` | Qualitäts-Gates auf den Endartefakten, Lints, Checkpoints |
| `references/ultracode-mode.md` | Multi-Agent-Orchestrierung |
| `references/beispiel_codierung.json` | lauffähiges Formatbeispiel der JSON-Codiertabelle (erfundener Übungsfall) |
| `scripts/build_workbook.py` | schreibt und validiert die Arbeitsmappe aus der JSON-Codiertabelle |
| `scripts/aggregate.py` | berechnet die drei Aggregationsebenen, liefert fertige Zählzeilen |
| `scripts/validate_deliverables.py` | prüft die Endartefakte gegen die Arbeitsmappe |
| `scripts/_kern.py` | gemeinsames Modul der drei Skripte, wird nicht direkt aufgerufen |

Jedes Skript erklärt sich selbst über `--help`; dort stehen Eingabeformat,
Optionen, Beispielaufrufe und die Bedeutung der Exit-Codes.
