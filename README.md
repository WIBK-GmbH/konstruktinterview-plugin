# Konstruktinterview Plugin Marketplace

Plugin Marketplace für Claude mit Skills zur Entwicklung und Auswertung von Konstruktinterviews nach König/Volmer (2018, Handbuch Systemische Organisationsberatung).

## Skills

| Skill | Beschreibung |
|---|---|
| `interview-develop` | Entwickelt strukturierte Interviewleitfäden (5 Schritte: Ziel, Stichprobe, Leitfragen, Revision, Abstimmung) |
| `interview-evaluate` | Wertet Interviews inhaltsanalytisch aus (4 Schritte: Datenbasis, Codieren, Kategorien, Auswertung) |

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
ln -s "$REPO/plugins/konstruktinterview/skills/interview-develop" ~/.claude/skills/interview-develop
ln -s "$REPO/plugins/konstruktinterview/skills/interview-evaluate" ~/.claude/skills/interview-evaluate
```

### claude.ai / Claude Desktop

ZIP-Dateien der einzelnen Skills hochladen unter **Settings > Features > Skills**.

## Methodische Grundlage

Basierend auf dem Konstruktinterview-Ansatz von Eckard König und Gerda Volmer, einer besonderen Form des Experteninterviews mit dem **Fremdheitsgrundsatz** als Kernprinzip: Dem Interviewer ist die Konstruktion der Wirklichkeit des Gesprächspartners zunächst grundsätzlich fremd und erst durch gezieltes Nachfragen zu klären.

Auswertung angelehnt an die qualitative Inhaltsanalyse nach Mayring (2016).
