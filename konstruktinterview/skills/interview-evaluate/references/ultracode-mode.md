# Ultracode-Auswertungsmodus (Multi-Agent)

> Diese Anleitung gilt nur, wenn in **Schritt 1b** der Modus *Ultracode* oder
> *Ultracode + Doppelcodierung* gewählt wurde (bzw. der Skill mit dem Stichwort
> `ultracode` gestartet wurde). Andernfalls gilt der sequenzielle Standardpfad
> der `SKILL.md`.

Du bist hier **Orchestrator**, nicht Codierer. Du steuerst Sub-Agenten über das
Workflow-Tool (`agent` / `parallel` / `pipeline`) und sicherst die Methodik.
Schritt 1 (Datensichtung, Pseudonymisierung, Denylist) bleibt unverändert wie im
Standardpfad. Der Ultracode-Modus verzweigt die **Schritte 2 bis 3**; die
Schritte 4 bis 6 folgen denselben Regeln, werden hier aber als Phasen P5 und P6
mit ausdrücklicher Rollenzuweisung ausgeführt: die Auszählung deterministisch
durch dich selbst, die Artefaktsynthese durch **einen** Autor-Agenten.
**Am Ende stehen dieselben Artefakte wie im Standardpfad.**

## Inhalt

1. [Leitprinzipien](#leitprinzipien-nicht-verhandelbar)
2. [Tabellen-Erweiterung](#tabellen-erweiterung-voraussetzung-für-alle-prüfungen)
3. [Phasen P0 bis P6](#phasen)
4. [Gates auf den Endartefakten](#gates-auf-den-endartefakten-blockierend-vor-abgabe)
5. [Diskrepanzauflösung](#diskrepanzauflösung-kein-mehrheitsvotum)
6. [Fallback](#fallback)

---

## Leitprinzipien (nicht verhandelbar)

- **Parallelisieren nur, was unabhängig ist** (Codieren je Transkript).
  **Serialisieren, was geteilt ist**: Kategoriensystem, Dedup, Zählung, Bericht.
- **Das Kategoriensystem kommt aus EINER Hand** (ein Synthese-Schritt). Sonst
  driften Kategorien auseinander. Schritt 3a wird NICHT parallelisiert, Schritt
  3b ist ohnehin eine menschliche Entscheidung.
- **Die Arbeitsmappe ist Single Source of Truth.** Prosa und Zahlen im
  Ergebnisdokument werden gegen sie geprüft, nie umgekehrt.
- **Kategorisierung ist inhaltliches Urteil.** Bash und Python treffen niemals
  eine Kategorienzuordnung: kein Keyword-Match, kein Regex, kein automatisches
  Labeling als Ersatz für das Urteil des Codierenden. Zulässige Skripteinsätze
  sind ausschließlich mechanisch: Dateien schreiben, deterministisch aggregieren,
  Offsets vergleichen, greppen, Textüberlauf prüfen.
- Jeder Sub-Agent befolgt dieselben Regeln wie der Standardpfad: ein Kerngedanke
  pro Codiereinheit, die Relevanzschwelle gegen rein deskriptive Verfahrens- und
  Chronikdarstellungen, glätten OHNE eigene Begriffe, Kontext in eckigen
  Klammern, vierwertige Bewertung, Belegmarkierung. Verbindlich in
  `codierung.md`. Weil parallel codiert wird, driften Segmentierungstiefe und
  Relevanzschwelle zwischen den Agenten am schnellsten; sie gehören in jeden
  Sub-Agenten-Auftrag wörtlich hinein.
- **Attributionstiefe ist artefaktabhängig**, nicht einheitlich: Die Arbeitsmappe
  führt die Kennung `Pnn`, das Ergebnisdokument zitiert attributionsfrei, ohne
  Kennung und ohne Gruppenangabe.

## Tabellen-Erweiterung (Voraussetzung für alle Prüfungen)

Jede Codiereinheit führt zusätzlich zur geglätteten `Äußerung` drei Felder:
`zitat_roh` (unveränderter Originalspan, copy-paste, Pflicht), `char_start` und
`char_end` (Zeichenoffsets, optional). Ohne `zitat_roh` sind die
deterministischen Gates nicht umsetzbar. Die drei Felder bleiben in der
Arbeitsdatenstruktur und werden **nicht** in die Arbeitsmappe geschrieben.

Im Ultracode-Pfad sind die Offsets mehr als eine Beschleunigung: Die
Dedup-Prüfung in P3 vergleicht überlappende Spans, und dafür müssen alle
Agenten dieselbe Bezugsfassung benutzen. Lege sie deshalb **einmal zentral in
P0** an, den zusammenhängenden Klartext je Interview, bei Turn-Listen die
verketteten Turns mit einem Zeilenumbruch als Trenner, und gib genau diese
Fassung an die Codier-Agenten (`codierung.md` Abschnitt 10). Zwei Agenten mit
verschiedenen Bezugsfassungen erzeugen Offsets, die sich nicht vergleichen
lassen.

**Die Arbeitsdatenstruktur ist vertraulich**, sobald `zitat_roh` darin steht:
Dateiname `VERTRAULICH_codierung_*.json`, geschützte Projektablage, nie in ein
Repository (`codierung.md` Abschnitt 1).

## Phasen

**P0: Datensichtung und Pseudonymisierung (du selbst, kein Fan-out).**
Untersuchungsziel, Stichprobeninfo, Zuordnung Transkript zu Perspektivgruppe und
Quellenart. Vergib die stabilen Kennungen `Pnn` und lege den vertraulichen
Pseudonymschlüssel an; die Codier-Agenten sehen **nur** Kennungen, nie Klarnamen.
Lege die Namens-Denylist aus den Stichprobeninfos an (echte Namen, Orte,
Einheiten, Projektbezeichnungen) für das Anonymisierungs-Gate.

**P1: Offene Codierung (`pipeline`, kein Barrier).**
`pipeline(transkripte, codiere, glaette_pruefe)`. Jedes Transkript ist
unabhängig, deshalb `pipeline` und nicht `parallel`: ein langsames Transkript
blockiert die anderen nicht. Bei *Ultracode + Doppelcodierung* je Transkript
K = 2 Codierer-Jobs, sonst K = 1. `kategorie_vorschlag` ist hier induktiv und
vorläufig.

```json
{ "codiereinheiten": [{
    "kennung": "str",
    "quellenart": "transkript|mitschrift|protokoll|diktat",
    "zitat_roh": "str", "char_start": "int", "char_end": "int",
    "reihenfolge": "int",
    "geglaettet": "str",
    "bewertung": "+|-|o|>",
    "kernaussage": "bool",
    "kategorie_vorschlag": "str" }] }
```

Zur Bewertung gilt die Vorrangregel: `>` schlägt `-`; `-` und `+` schlagen `o`.
Zur Belegmarkierung gilt die Zielquote von 20 bis 25 Prozent; ein Codier-Agent
markiert nur innerhalb seines Transkripts, die Quote wird global in P5 geprüft.

**P2: Kategoriensystem-Synthese (`parallel`-Barrier, EIN Synthese-Agent).**
`parallel([() => agent(synthese, ...)])[0]`. Der Barrier garantiert, dass ALLE
P1-Codierungen vorliegen. Der Synthese-Agent dedupliziert synonyme Vorschläge zu
EINEM induktiven System mit **genau zwei Ebenen**. **Keine
Stärken/Schwächen-Hauptkategorien**: thematische Kategorien, Bewertung als
Attribut innerhalb. Kategorien, die nur ein Codierer sah, NICHT verwerfen,
sondern als Einzelnennung-Kandidat markieren. Jeder Kategorienname muss an die
Sprache der Befragten anschließen.

```json
{ "kategorien": [{
    "nummer": "str", "ebene": "haupt|unter", "bezeichnung": "str",
    "definition": "str",
    "ankerbeispiel": "str (nur bei ebene=unter, Zitat + Kennung)",
    "codierregel": "str (nur bei ebene=unter, beginnt mit 'Hier codieren, wenn')" }] }
```

Satzmuster, MECE-Prüfung und harte Gates: `kategoriensystem.md`.

**P3+P4: Re-Codierung und adversariale Verifikation (`pipeline`, kein Barrier).**
Alle Codiereinheiten gegen das FINALE System neu zuordnen und prüfen. Bei vielen
Einheiten zu Chunks bündeln (`chunk_size ≈ ceil(anzahl / 12)`), Items = Chunks.
`pipeline(chunks, rekodiere, verifiziere)`:

- *rekodiere*: ordnet jede Einheit dem konsolidierten System zu, auf
  Unterkategorienebene, nie auf Hauptkategorienebene.
- *verifiziere* (adversarial, Auftrag „widerlege“): prüft je Einheit gegen
  `zitat_roh` und Transkript. Steht das Zitat dort? Wurde nur getilgt
  (Füllwörter, Wiederholungen) oder ein inhaltstragender Begriff **substituiert**?

```json
{ "kennung": "str", "kategorie_final": "str", "zuordnung_korrekt": "bool",
  "status": "VERIFIED|SMOOTHING_OK|DRIFT|NOT_FOUND", "begruendung": "str" }
```

**Gates (blockierend):** `NOT_FOUND` → Einheit raus aus der Tabelle und
protokollieren. `DRIFT` → zurück an den Codierer, Originalbegriff wiederherstellen.
`VERIFIED` und `SMOOTHING_OK` sind beide Gutzustände; bei geglätteten Einheiten
ist `SMOOTHING_OK` der erwartete Wert und keine Auffälligkeit
(`codierung.md` Abschnitt 10). Ein Chunk, der ausschließlich `VERIFIED` meldet,
ist ein Anlass zur Rückfrage: Dort wurde vermutlich nicht geglättet.

**Mayring-Revision:** P2 → P3 einmal wiederholen, höchstens zwei Durchgänge.
Stößt die Re-Codierung auf Material, das nicht passt, das SYSTEM nachschärfen
(zurück in P2), nicht ins bestehende System pressen. Dann terminieren.

**Dedup (deterministisch, du selbst).** Zwei Einheiten sind ein Duplikat, wenn
ihre `zitat_roh`-Spans im selben Transkript überlappen (Offsets vergleichen, nicht
semantisch raten) UND dieselbe Kategorie tragen → auf eine Zeile mergen.
Überlappung bei VERSCHIEDENEN Kategorien ist erlaubte Mehrfachcodierung.

**P4b: Berichtsgliederung (menschlicher Entscheidungspunkt, Checkpoint C1).**
Das synthetisierte System ist ein Analysesystem. Leite daraus höchstens drei
flache Berichtsgliederungen ab (3 bis 4 Hauptkategorien, 10 bis 15
Unterkategorien, benannt nach dem Erkenntnisinteresse des Auftraggebers), lege sie
mit der Personenabdeckung je Kategorie vor und lass wählen. Danach werden alle
Einheiten gegen das gewählte System neu codiert, mit dokumentiertem Mapping alt zu
neu. Die Neucodierung ist ein Agentenlauf wie P3, kein Mapping-Skript. Details:
`kategoriensystem.md`.

**P5: Auszählung (deterministisch, du selbst, KEIN Agent).**
Aggregation aus der dedupten Tabelle per Skript, nicht durch Lesen rechnen; ein
Zähl-Agent verzählt sich. **Drei Aggregationsebenen, die nicht verwechselt werden
dürfen:**

| Ebene | Zähleinheit | Verwendung |
|---|---|---|
| Personen je Kategorie | distinkte Kennungen | Verbreitungsmaß `X von N` |
| Äußerungen je Bewertung je Kategorie | Codiereinheiten | Sheet `Auszählung`, Spalten `+ - o >` |
| Personen je Bewertung je Kategorie | distinkte Kennungen | Zählzeile `X von N Personen (a +, b -, c o, d >)` |

Ebene 2 und Ebene 3 sehen identisch aus und bedeuten Verschiedenes. Jede Kennzahl
trägt die Zähleinheit im Namen. Für Ebene 3 gilt `max(a,b,c,d) ≤ X ≤ N`, und die
vier Zahlen sind **keine Partition**: `a+b+c+d > X` ist normal.

**Rohwerte, nie Prozent.** Aufschlüsselung nach Perspektivgruppe ist optional und
kann qualitativ im Fließtext erfolgen; bei Gruppen unter drei Personen unterbleibt
die Gruppenangabe. Einzelnennungen explizit kennzeichnen, nicht wegfiltern. Bei
Doppelcodierung: Codierer-Dissens je Stelle als Befund ausweisen, nicht wegmitteln.

Zusätzlich prüfen: `*`-Quote global 15 bis 30 Prozent, keine Kategorie mit Quote
null, jede Kategorie mit mindestens drei verschiedenen Kennungen.

Werkzeug: `scripts/aggregate.py --level alle --format md` zur Vorlage,
`--format zeilen` für die einsetzbaren Zählzeilen.

**P6: Artefaktsynthese (EIN Autor-Agent).**
Baut Arbeitsmappe und Ergebnisdokument aus Kategoriensystem (P2/P4b), Auszählung
(P5) und dem Belegpool.

**Feld-Mapping P1 auf die finale JSON-Codiertabelle** (Schema:
`excel-output.md` Abschnitt 9). Die Arbeitsstruktur der Phasen trägt andere
Feldnamen als die Eingabe der Skripte:

| P1 / P3 | JSON-Codiertabelle | Anmerkung |
|---|---|---|
| `geglaettet` | `aeusserung` | |
| `kategorie_vorschlag`, dann `kategorie_final` | `kategorie` | als Zeichenkette, nie als Zahl |
| `kennung`, `bewertung`, `kernaussage`, `reihenfolge` | gleichnamig | |
| `zitat_roh`, `char_start`, `char_end` | dürfen mitgeführt werden | Skripte ignorieren sie, sie kommen nicht in die Mappe |
| `quellenart` | `personen[].quellenart` | wandert auf die Personenebene |

**Zitiert wird die geglättete `Äußerung` aus dem `*`-Pool der Arbeitsmappe, nicht
`zitat_roh`.** Die Arbeitsmappe ist die
Datenwahrheit des Berichts; `zitat_roh` und die Offsets bleiben das Prüfmittel
des Zitat-Gates in Richtung Transkript. Marker vor dem Zitat entspricht exakt der
`Bewertung` der zitierten Zeile.

Bei Doppelcodierung kommt ein Zusatzabschnitt **„Codierübereinstimmung und
Diskrepanzen“** hinzu: Rohwerte, qualitativ beschrieben, kein Kappa und keine
Scheingenauigkeit bei kleinem N. Er gehört in die Prozessnotiz, nicht in das
Ergebnisdokument für den Auftraggeber.

Baupläne: `excel-output.md` und `pptx-output.md`.

## Gates auf den Endartefakten (blockierend, vor Abgabe)

Die Gates laufen gegen **Arbeitsmappe und Ergebnisdokument**, nicht nur gegen die
Codierung. Genau im Schritt vom Codieren zum Berichten entsteht Drift. Vollständig
in `gates.md`, ausgeführt durch `scripts/validate_deliverables.py`:

- **Zitat-Gate** gegen das fertige Dokument: jedes Zitat wortgleich in einer
  `*`-Zeile auffindbar, Marker gleich Bewertung, ein Anführungszeichenpaar gleich
  eine Codiereinheit gleich eine Person, keine Paraphrase in Anführungszeichen,
  Quellenart erlaubt wörtliches Zitieren.
- **Zähl-Gate**: jede Zahl aus der Arbeitsmappe neu berechnet, Zählzeilen
  plausibel, Gesamtzahlen dokumentweit identisch.
- **Zahl-Text-Kongruenz-Lint** nach jedem Zahlenupdate.
- **Anonymisierungs-Gate**: EIN adversarialer Redaction-Durchgang über die
  FERTIGEN Artefakte, nicht verteilt in den Codier-Agenten. Backstop: Grep gegen
  die Denylist aus P0 über **alle** Artefakte muss null Treffer liefern. Der
  Anhang mit allen Rohzitaten ist der größte Leckkandidat, deshalb bleibt
  `zitat_roh` außerhalb der ausgelieferten Dateien.
- **Konsistenz-Checks** über alle Artefakte: Kategoriennamen wörtlich identisch,
  Registry gegen den Pseudonymschlüssel, beide Überblicksfolien zeichengleich,
  keine abgebrochenen Sätze.
- **Wortlaut-Sperre**: Nach einer Freigabe ändert ein Datenupdate nur Zahlen,
  Tippfehler und nachweislich falsche Tatsachenaussagen. Nie umformulieren.

Der Abgabelauf ist ein Lauf in **Modus B**, also mit `--deck` beziehungsweise
`--report` (`gates.md` Abschnitt 9). Ein Lauf nur gegen die Arbeitsmappe prüft
die Mappe, nicht das Ergebnisdokument; das Protokoll führt die ausgefallenen
Gates im Abschnitt **Nicht geprüft** auf.

## Diskrepanzauflösung (kein Mehrheitsvotum)

Abweichungen sind Befund, nicht Störung. Auslegungsfehler am Material korrigieren;
unscharfe Codierregel → System nachschärfen; echte Mehrdeutigkeit einer Stelle →
beide Lesarten ausweisen, Stelle als ambig markieren. Tragfähige Einzelnennungen
bleiben drin. Strittiges transparent in die Limitationen.

## Fallback

Steht das Workflow-Tool nicht zur Verfügung oder ist N sehr klein, sauber auf den
sequenziellen Standardpfad zurückfallen. Die Prüf-Gates gelten dort unverändert:
Ultracode ist schneller, nicht qualitativ niedriger, und die Gates sind
pfadunabhängig.
