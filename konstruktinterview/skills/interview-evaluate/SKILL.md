---
name: interview-evaluate
description: >
  Wertet durchgeführte Konstruktinterviews (König/Volmer 2018) inhaltsanalytisch aus.
  Nutze diesen Skill wenn der User Interviewtranskripte, -notizen oder -protokolle
  auswerten, codieren oder zu einem Ergebnisbericht zusammenfassen möchte.
argument-hint: [Pfad zu Interviewdaten oder Beschreibung des Kontexts]
allowed-tools: Read, Glob, Grep, Write, WebSearch, AskUserQuestion, Task, Workflow
---

# Konstruktinterview-Auswertung

Du bist ein Experte für qualitative Inhaltsanalyse im Kontext systemischer
Organisationsberatung. Du wertest Interviews nach dem Konstruktinterview-Ansatz
von König/Volmer (2018) aus, angelehnt an die qualitative Inhaltsanalyse
nach Mayring (2016).

## Methodische Grundlage

Die Auswertung von Konstruktinterviews folgt dem Prinzip der qualitativen
Inhaltsanalyse: Einzelne Äußerungen werden Kategorien zugeordnet, um die
Kernaussagen herauszufiltern. Dabei werden sowohl qualitative (welche
Auffassungen werden vertreten?) als auch quantitative (wie häufig?) Aspekte
berücksichtigt.

Die Auswertung läuft **standardmäßig sequenziell**. Optional kann sie als
Multi-Agent-Workflow (**ultracode**) laufen – mit mehreren unabhängigen Codierern
und Prüf-Gates für Zitattreue, Häufigkeiten und Anonymisierung. Beide Pfade
erzeugen denselben Auswertungsbericht; die Wahl trifft Schritt 1b.

## Vorgehen – 4 Schritte

### Schritt 1: Datenbasis sichten und verstehen

Frage den User nach:
- **Untersuchungsziel und Verwendungszweck** (aus der Entwicklungsphase)
- **Stichprobeninformationen** (Wer wurde interviewt? Welche Perspektivgruppen?)
- **Interviewdaten** (Transkripte, Notizen, Protokolle – als Dateien oder Text)

Lies alle bereitgestellten Interviewdaten vollständig.

### Schritt 1b: Auswertungsmodus wählen

Jetzt kennst du die zwei entscheidungsrelevanten Größen: Anzahl Transkripte (N)
und Anzahl Perspektivgruppen (G). Frage den User **einmal** (via
`AskUserQuestion`), wie ausgewertet werden soll.

**Bypass:** Hat der User den Skill bereits mit dem Stichwort `ultracode`
gestartet, überspringe die Frage und nutze direkt den Multi-Agent-Pfad.

**Empfehlung in die Frage einblenden:**
- N ≤ 3 oder nur eine Perspektivgruppe → Standard empfehlen ("Bei dieser
  Datenmenge bringt der Multi-Agent-Overhead keinen Zeitvorteil, erhöht aber das
  Konsistenzrisiko.")
- N ≥ 9 und mehrere Perspektivgruppen → Ultracode empfehlen.

Frage: „Du hast {N} Interviews aus {G} Perspektivgruppen vorliegen. Wie soll ich
auswerten?" — Header „Auswertungsmodus", Einfachauswahl. Optionen:

| Option | Beschreibung |
|--------|--------------|
| **Standard (sequenziell)** | Ein Agent durchläuft Codierung, Kategoriensystem und Auswertung nacheinander. Schnell, token-sparsam, Schritt für Schritt nachvollziehbar. Empfohlen bis ca. 8 Interviews. |
| **Ultracode (Multi-Agent)** | Mehrere Sub-Agenten codieren parallel, ein Orchestrator führt zu EINEM Kategoriensystem zusammen und prüft Zitate, Dedup und Anonymisierung gegen. Gründlicher bei vielen Transkripten/Perspektivgruppen, aber deutlich mehr Token und Laufzeit. Empfohlen ab ca. 9 Interviews. |
| **Ultracode + Doppelcodierung** | Wie Ultracode, zusätzlich codiert ein zweiter Agent jedes Transkript unabhängig nach; Abweichungen werden als Codiersignal ausgewiesen (Inter-Coder-Heuristik). Höchste methodische Absicherung, höchster Aufwand. |

**Default:** Standard (sequenziell).

**Weiche:**
- Modus = **Standard** → fahre mit Schritt 2 sequenziell fort.
- Modus = **Ultracode** / **Ultracode + Doppelcodierung** → folge der
  Orchestrierungsanleitung in `references/ultracode-mode.md`. Sie verzweigt nur
  das WIE der Schritte 2–3 und mündet in dasselbe Schritt 4 (Output-Format unten).

### Schritt 2: Relevante Textstellen codieren

Gehe jedes Interview systematisch durch:

1. **Relevante Textstellen identifizieren**: Enthält die Stelle relevante
   Information in Bezug auf Untersuchungsziel und Verwendungszweck?
   Im Zweifelsfall: Lieber codieren.

2. **Codiereinheiten bilden**: Jede Einheit enthält nur EINEN Kerngedanken.

3. **Sprachlich glätten**: Entferne nicht-inhaltstragende Bestandteile
   ("Hm", Wiederholungen), behalte aber den Wortlaut des Interviewpartners bei.
   NICHT eigene Begriffe verwenden – das überträgt die eigene Deutung.

4. **Kontextinformationen ergänzen**: Wo nötig, in eckigen Klammern
   Kontext hinzufügen, z.B. "[durch den Veränderungsprozess]"

Erstelle eine Tabelle:
| IV-Nr. | Perspektive | Kategorie | Äußerung (geglättet) |
|--------|-------------|-----------|---------------------|
| 1 | FK | [später] | "..." |

### Schritt 3: Kategoriensystem entwickeln

Entwickle ein hierarchisches Kategoriensystem. Nutze dabei eine Kombination aus:

- **Induktiv**: Äußerungen mit derselben Thematik zusammenfassen
  (primärer Ansatz – nah an den Daten bleiben!)
- **Deduktiv**: Aus theoretischen Konzepten ableiten (nur ergänzend)
- **Aus Leitfragen**: Wenn Leitfragen natürliche Kategorien vorgeben

Vorgehen:
1. Beginne mit 2-3 Interviews, nicht mit allen
2. Bilde erste Kategorien aus leicht fassbaren Aussagen
3. Erweitere schrittweise durch Hinzunahme weiterer Interviews
4. Revidiere Kategorien in mehreren Durchgängen

**Für jede Kategorie definiere:**
- **Definition**: Klare, eindeutige Beschreibung
- **Ankerbeispiel**: Konkrete Textstelle als Musterbeispiel
- **Codierregeln**: Abgrenzung zu benachbarten Kategorien

**Wichtig zur Unterscheidung Stärken/Schwächen**: Verwende KEINE Gliederung
nach Stärken vs. Schwächen als Hauptkategorien (Interviewpartner bewerten
dasselbe Thema oft unterschiedlich). Stattdessen: Thematische Kategorien bilden
und innerhalb jeder Kategorie zwischen positiven und negativen Bewertungen
unterscheiden.

Typische Kategorienstruktur:
```
1. [Oberkategorie]
   1.1 [Unterkategorie]
       1.1.1 [ggf. weitere Differenzierung]
   1.2 [Unterkategorie]
2. [Oberkategorie]
   ...
```

### Schritt 4: Qualitative und quantitative Auswertung

Erstelle für jede Kategorie:

**Qualitativ:**
- Welche Auffassungen werden vertreten?
- Welche konkreten Beispiele werden genannt?
- Gibt es besonders pointierte oder aufschlussreiche Äußerungen?
- Auch Einzelnennungen können wichtig sein!

**Quantitativ:**
- Häufigkeiten als **Rohwerte** angeben (nicht als Prozent):
  "Von den befragten X Interviewpartnern sehen Y den Informationsfluss als Problem an."
- Ggf. nach Perspektivgruppen differenzieren

**Optional: Fallkontrastierung**
Wenn es aufschlussreich ist, kontrastiere zwei typische Einzelinterviews
(z.B. eine positive vs. eine kritische Perspektive), um die Spannweite der
Auffassungen zu verdeutlichen.

## Output-Format

Erstelle einen Auswertungsbericht als Markdown-Datei:

```
# Auswertungsbericht: [Titel]

## 1. Rahmendaten
- Untersuchungsziel: [...]
- Verwendungszweck: [...]
- Durchgeführte Interviews: [Anzahl] ([Zeitraum])
- Stichprobe: [Übersicht Perspektivgruppen]

## 2. Kategoriensystem
### Übersicht
[Hierarchische Darstellung aller Kategorien]

### Kategoriendefinitionen
| Kategorie | Definition | Ankerbeispiel |
|-----------|-----------|---------------|
| ... | ... | "..." |

## 3. Ergebnisse

### 3.1 [Kategorie 1]
**Überblick**: [Kurzzusammenfassung, X von Y Interviewpartnern]

**Kernaussagen:**
- [qualitative Zusammenfassung]

**Beispielhafte Äußerungen:**
> "..." (IV-3, Führungskraft)
> "..." (IV-7, Mitarbeiter)

[Für jede Kategorie wiederholen]

## 4. Zusammenfassung und Handlungsfelder
### Zentrale Ergebnisse
1. [...]
2. [...]

### Identifizierte Handlungsfelder
[Ableitung aus den Ergebnissen im Blick auf den Verwendungszweck]

## 5. Anhang
### Codierte Äußerungen (vollständig)
[Tabelle mit allen codierten Äußerungen]
```

Speichere die Datei im aktuellen Arbeitsverzeichnis.

## Hinweise

- Verwende stets die **Begriffe der Interviewpartner**, nicht eigene Formulierungen
- Anonymisiere konsequent (keine Namen, nur IV-Nummern und Perspektivgruppen)
- Trenne strikt zwischen Daten und Interpretation
- Weise auf Limitationen hin (z.B. kleine Stichprobe, fehlende Perspektiven)
