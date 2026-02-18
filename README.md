# Konstruktinterview Plugin

Claude Plugin zur Entwicklung und Auswertung von Konstruktinterviews nach König/Volmer (2018, Handbuch Systemische Organisationsberatung).

## Skills

| Skill | Beschreibung |
|---|---|
| `interview-develop` | Entwickelt strukturierte Interviewleitfäden (5 Schritte: Ziel, Stichprobe, Leitfragen, Revision, Abstimmung) |
| `interview-evaluate` | Wertet Interviews inhaltsanalytisch aus (4 Schritte: Datenbasis, Codieren, Kategorien, Auswertung) |

## Installation

### Claude Cowork

```bash
claude --plugin-dir ./konstruktinterview-plugin
```

### Claude Code

Skills nach `~/.claude/skills/` kopieren oder verlinken:

```bash
ln -s /pfad/zu/konstruktinterview-plugin/skills/interview-develop ~/.claude/skills/interview-develop
ln -s /pfad/zu/konstruktinterview-plugin/skills/interview-evaluate ~/.claude/skills/interview-evaluate
```

### claude.ai / Claude Desktop

ZIP-Dateien der einzelnen Skills hochladen unter **Settings > Features > Skills**.

## Methodische Grundlage

Basierend auf dem Konstruktinterview-Ansatz von Eckard König und Gerda Volmer, einer besonderen Form des Experteninterviews mit dem **Fremdheitsgrundsatz** als Kernprinzip: Dem Interviewer ist die Konstruktion der Wirklichkeit des Gesprächspartners zunächst grundsätzlich fremd und erst durch gezieltes Nachfragen zu klären.

Auswertung angelehnt an die qualitative Inhaltsanalyse nach Mayring (2016).
