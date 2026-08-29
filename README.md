# Konstruktinterview Plugin Marketplace

Plugin Marketplace für Claude mit Skills zur Entwicklung und Auswertung von Konstruktinterviews nach König/Volmer (2018, Handbuch Systemische Organisationsberatung).

## Skills

| Skill | Beschreibung |
|---|---|
| `interview-develop` | Entwickelt strukturierte Interviewleitfäden (5 Schritte: Ziel, Stichprobe, Leitfragen, Revision, Abstimmung) |
| `interview-evaluate` | Wertet Interviews inhaltsanalytisch aus: Codierung, Kategoriensystem, Auszählung, Arbeitsmappe und Ergebnisdokument, abgesichert durch Prüfskripte |

## Artefakte von `interview-evaluate`

Das Ergebnis ist kein Fließtextbericht, sondern ein Artefaktpaar.

| Artefakt | Rolle |
|---|---|
| **Arbeitsmappe** (`.xlsx`, vier Blätter) | Datenwahrheit: jede Codiereinheit, das Kategoriensystem, die Auszählung, die Rahmendaten |
| **Ergebnisdokument** (`.pptx`, optional) | Bericht an den Auftraggeber; enthält keine Zahl und kein Zitat, das nicht in der Arbeitsmappe steht |
| **Prozessnotiz** (`.md`) | interner Zwischenstand je Erhebungswelle |

Zwei Grundsätze tragen das Modell: Zahlen werden aus der Arbeitsmappe generiert,
nie getippt, und jedes Zitat stammt wortgleich aus einer markierten Zeile
derselben Mappe. Drei Skripte setzen das durch: `build_workbook.py` schreibt und
validiert die Mappe, `aggregate.py` berechnet die drei Aggregationsebenen,
`validate_deliverables.py` prüft die Endartefakte gegen die Mappe (Zitat-, Zähl-,
Kongruenz-, Anonymisierungs- und Konsistenz-Gate sowie die Wortlaut-Sperre nach
der Freigabe). Jedes Skript erklärt sich über `--help`.

Ein lauffähiges Formatbeispiel liegt als `references/beispiel_codierung.json`
bei; es verwendet durchgängig den erfundenen Übungsfall *Firma M.* Eine echte
Codiertabelle ist dagegen ein vertrauliches Arbeitsdokument, sobald sie die
Rohzitate mitführt: Präfix `VERTRAULICH_`, geschützte Projektablage, nie in ein
Repository. Die `.gitignore` deckt `VERTRAULICH_*` ab.

Für größere Erhebungen lässt sich die Codierphase optional auf mehrere
Sub-Agenten verteilen (Ultracode-Modus). Die Prüf-Gates gelten pfadunabhängig und
laufen in beiden Fällen gleich.

## Installation

### Claude Cowork

Marketplace hinzufügen und Plugin installieren:

```
/plugin marketplace add bourdieuesk/konstruktinterview-plugin
/plugin install konstruktinterview@konstruktinterview-marketplace
```

### Claude Code

Skills nach `~/.claude/skills/` verlinken:

```bash
REPO=/pfad/zu/konstruktinterview-plugin
ln -s "$REPO/konstruktinterview/skills/interview-develop" ~/.claude/skills/interview-develop
ln -s "$REPO/konstruktinterview/skills/interview-evaluate" ~/.claude/skills/interview-evaluate
```

Die Skripte von `interview-evaluate` brauchen `openpyxl` und, für die Prüfung von
Foliensätzen, `python-pptx`.

### claude.ai / Claude Desktop

ZIP-Dateien der einzelnen Skills hochladen unter **Settings > Features > Skills**.

## Methodische Grundlage

Basierend auf dem Konstruktinterview-Ansatz von Eckard König und Gerda Volmer, einer besonderen Form des Experteninterviews mit dem **Fremdheitsgrundsatz** als Kernprinzip: Dem Interviewer ist die Konstruktion der Wirklichkeit des Gesprächspartners zunächst grundsätzlich fremd und erst durch gezieltes Nachfragen zu klären.

Auswertung angelehnt an die qualitative Inhaltsanalyse nach Mayring (2016).
