# Codierkonventionen

Verbindliche Konventionen für die Spalten des Sheets `Aussagen`. Alle Beispiele
sind erfunden und stammen aus einem Übungsfall: Der mittelständische
Möbelhersteller *Firma M.* verlagert seine Fertigung an einen zweiten Standort;
befragt werden Geschäftsleitung, Fertigung, Vertrieb und Verwaltung.

## Inhalt

1. [Datenmodell der Codiereinheit](#1-datenmodell-der-codiereinheit)
2. [Pseudonymisierung, Perspektivgruppe, Quellenart](#2-pseudonymisierung-perspektivgruppe-quellenart)
3. [Kodiereinheit bilden](#3-kodiereinheit-bilden)
4. [Glättung](#4-glättung)
5. [Eckige Klammern: drei Funktionen](#5-eckige-klammern-drei-funktionen)
6. [Bewertung: vier Werte](#6-bewertung-vier-werte)
7. [Belegmarkierung mit `*`](#7-belegmarkierung-mit-)
8. [Sortierung](#8-sortierung)
9. [Prüfliste vor dem Schreiben](#9-prüfliste-vor-dem-schreiben)
10. [Verifikationsdurchgang: Bezugsfassung und Status](#10-verifikationsdurchgang-bezugsfassung-und-status)

---

## 1. Datenmodell der Codiereinheit

| Feld | Pflicht | Inhalt |
|---|---|---|
| `Kennung` | ja | Pseudonym der befragten Person, Format `Pnn` |
| `Kategorie` | ja | Unterkategoriennummer, Format `x.y`, **als Text** |
| `Bewertung` | ja | genau ein Zeichen aus `+`, `-`, `o`, `>` |
| `Kernaussage` | nein | `*` oder leer |
| `Äußerung` | ja | geglättete Codiereinheit, ein Kerngedanke |

Zusätzlich werden während der Codierung mitgeführt, aber nicht in die
Arbeitsmappe geschrieben: der unveränderte Originalspan `zitat_roh` sowie
`char_start` und `char_end`. Sie sind das Prüfmittel des Zitat-Gates und die
Grundlage der Deduplizierung. Die Bezugsfassung der Offsets und die
Statussemantik stehen in Abschnitt 10.

**Kategorisierung ist inhaltliches Urteil.** Ordne niemals per Stichwortliste,
Regex oder automatischem Labeling zu. Ein Keyword-Klassifikator erzeugt stille
Fehlzuordnungen, die kein Gate abfängt, weil die Gates Zitattreue prüfen und
nicht Kategorienplausibilität.

**Die JSON-Codiertabelle ist ein vertrauliches Arbeitsdokument**, sobald sie
`zitat_roh` oder Klarnamen führt. `zitat_roh` hält den unveränderten Rohspan und
damit genau die Namen, Orte und Einheitenbezeichnungen, die in der Spalte
`Äußerung` bereits durch eckige Klammern ersetzt sind. Deshalb gilt für sie
dasselbe wie für Pseudonymschlüssel und Denylist:

- Dateiname mit dem Präfix `VERTRAULICH_`, etwa
  `VERTRAULICH_codierung_P01-P14_260315.json`,
- Ablage in der geschützten Projektablage, nicht in einer für den Klienten
  bestimmten Ablage,
- **niemals in ein Repository.** Die mitgelieferte `.gitignore` deckt
  `VERTRAULICH_*` bereits ab; das ersetzt die bewusste Ablageentscheidung nicht.

Der Aufruf `validate_deliverables.py --key <codierung.json>` reicht diese Datei
weiter. Wer sie weitergibt, gibt die Rohzitate mit. Für die Registry-Gegenprüfung
genügt der Pseudonymschlüssel im Format aus Abschnitt 2.

## 2. Pseudonymisierung, Perspektivgruppe, Quellenart

Zwei getrennte Namensräume:

- **Interne Interviewnummer** nach Durchführungsreihenfolge. Sie erscheint in
  keinem Artefakt.
- **Kennung `Pnn`**, zweistellig mit führender Null (`P01`, `P02`, … `P14`).
  Sie ist die einzige Personenangabe, die in der Arbeitsmappe auftaucht. Die
  Zuordnung ist zufällig und fixpunktfrei: aus der Kennung darf sich die
  Interviewreihenfolge nicht rekonstruieren lassen.

Die Zuordnung liegt in einer eigenen Datei mit dem Präfix `VERTRAULICH_`, die
**nicht** in einer für den Klienten bestimmten Ablage liegt.

**Normiertes Format des Schlüssels.** Der Schlüssel ist eine Markdown-Datei mit
**einer Tabelle**, deren Kopfzeile genau diese Spaltennamen trägt. Das Skript
`validate_deliverables.py --key` liest die Spalten über ihre Namen; abweichende
Überschriften machen die Gegenprüfung unmöglich.

| Spalte | Zweck |
|---|---|
| `Kennung` | Verbindung zu allen Artefakten, Format `Pnn` |
| `Klarname` | Rückverfolgung |
| `Interviewnummer` | interne Durchführungsreihenfolge |
| `Perspektivgruppe` | Gegenprüfung der Registry, Auswertung nach Gruppen |
| `Quellenart` | Zitierfähigkeit |
| `Hinweise` | unsichere Gruppenzuordnung, Re-Identifikationsrisiko |

```markdown
| Kennung | Klarname | Interviewnummer | Perspektivgruppe | Quellenart | Hinweise |
|---|---|---|---|---|---|
| P01 | Anna Berger | 4 | Fertigung | transkript | |
| P06 | Frank Gruber | 3 | Fertigung | mitschrift | kein wörtliches Zitat |
```

Fehlt die Spalte `Perspektivgruppe`, meldet das Prüfskript ausdrücklich
„Registry-Gegenprüfung nicht durchgeführt“. Eine still passierende Prüfung ist
gefährlicher als eine, die es gar nicht gibt.

**Stabilitätsregel.** Bei Fortschreibung werden Kennungen nur ergänzt, nie neu
vergeben. Eine Person behält ihre Kennung über alle Versionsstände.

**Quellenart und Zitierfähigkeit.** Die Quellenart hält fest, ob der Wortlaut
gesichert ist:

| Quellenart | Wörtlich zitierfähig |
|---|---|
| Aufnahme mit Transkript | ja |
| Mitschrift während des Gesprächs | nein |
| Gedächtnisprotokoll, nachträgliches Diktat | nein |

**Kein Zwischenweg.** Was nicht wörtlich zitierfähig ist, erscheint im
Ergebnisdokument **ohne Anführungszeichen** als sinngemäße Wiedergabe im
Rahmentext. Eine „gekennzeichnete“ wörtliche Wiedergabe aus einer Mitschrift gibt
es nicht: Der Wortlaut ist dort nicht gesichert, und eine Kennzeichnung macht ihn
nicht gesichert. Das Zitat-Gate blockiert deshalb jedes Zitat aus einer nicht
zitierfähigen Quellenart ausnahmslos.

Das Zitat-Gate prüft, ob eine Äußerung im Ausgangsmaterial *steht*. Es prüft
nicht, ob dieses Material Wortlautqualität hat. Beides ist zu unterscheiden.

**Perspektivgruppen-Registry.** Die Gruppenzuordnung steht an genau einer Stelle
im Workbook, im Sheet `Info`. Das Sheet `Aussagen` führt bewusst keine
Perspektivspalte, damit bei vielen Zeilen keine Inkonsistenz entstehen kann. Die
Registry muss partitionierend sein: jede Kennung genau einmal, Summe der
Gruppengrößen gleich N. Vor jedem Abschluss eines Standes wird sie gegen den
Pseudonymschlüssel gegengeprüft; ungeprüft driftet sie.

## 3. Kodiereinheit bilden

**Eine Codiereinheit trägt einen Kerngedanken.** Wo eine Passage zwei Gedanken
enthält, wird sie in zwei Zeilen zerlegt, auch wenn beide dieselbe Kategorie und
dieselbe Bewertung tragen.

**Im Zweifel codieren, aber nicht alles.** Enthält die Stelle Information mit
Bezug auf Untersuchungsziel und Verwendungszweck, kommt sie in die Tabelle. Der
Grundsatz gilt für **inhaltstragende, deutungsrelevante** Aussagen: Bewertungen,
Erwartungen, Wünsche, Deutungen, benannte Spannungen, beschriebene Regeln und
Abläufe, an denen etwas hängt.

**Relevanzschwelle, das Gegengewicht.** Rein deskriptive Verfahrens-, Chronik-
und Faktendarstellungen ohne Bezug zu Untersuchungsziel und Verwendungszweck
werden **nicht** codiert. Gemeint sind die langen Erzählstrecken, die jedes
Interview enthält: der Ablauf eines Projekts in seiner zeitlichen Folge, die
Aufzählung von Gremien, Terminen und Zuständigkeiten, die Vorgeschichte einer
Entscheidung, Zahlenwerk, das die Person referiert. Ohne diese Schwelle
verdoppelt sich der Bestand an neutralen Einheiten, ohne dass ein einziger
Befund hinzukommt. Zwei Prüffragen:

1. Trägt die Stelle etwas zur Beantwortung einer Leitfrage bei, oder erklärt sie
   nur, wie etwas abgelaufen ist?
2. Stünde der Bericht ohne sie ärmer da?

Ist die Antwort zweimal nein, bleibt die Stelle draußen. Deskriptives Material,
das eine Bewertung, einen Wunsch oder eine Deutung **rahmt**, wird nicht separat
codiert, sondern in die Einheit hineingenommen, zu der es gehört.

Formale Zielwerte:

| Merkmal | Zielwert |
|---|---|
| Länge | Richtwert 80 bis 340 Zeichen, Median um 150 |
| Wörter | etwa 12 bis 50 |
| Sätze | 1 bis 3 |
| Satzanfang | Großbuchstabe |
| Satzende | `.` oder `?` |

**Die Zielwerte sind Richtwerte, keine Schnittkante.** Ein zusammenhängender
Kerngedanke wird **nicht** gesplittet, um einen Zeichenwert einzuhalten.
Entscheidet der Gedanke, entscheidet nicht die Länge: Trägt eine Passage aus drei
Sätzen einen Gedanken, bleibt sie eine Einheit, auch wenn sie über 340 Zeichen
liegt. Umgekehrt wird ein Halbsatz nicht künstlich zur Einheit aufgefüllt.
Systematisch feiner zu segmentieren, als der Gedanke es verlangt, verschiebt jede
Zahl auf der Äußerungsebene, ohne einen Befund zu gewinnen.

**Keine Dubletten.** Kein Äußerungstext darf zweimal im Sheet stehen. Prüfe das
programmatisch, nicht durch Lesen.

## 4. Glättung

1. Nicht-inhaltstragende Bestandteile entfernen: Füllwörter, Verzögerungslaute,
   Abbrüche, Wiederholungen, Rückversicherungsfloskeln.
2. **Wortlaut und Register der befragten Person bleiben erhalten.** Keine
   Übersetzung in Beratersprache, keine eigenen Fachbegriffe. Das überträgt
   sonst die Deutung des Auswerters auf das Material.
3. Grammatisch vollständiger, lesbarer Satz. Anakoluthe werden geglättet, der
   Inhalt nicht.
4. **Ich- und Wir-Perspektive bleiben erhalten.** Nicht in indirekte Rede
   umschreiben.

Beispiel. Rohtext: *„Also, ähm, wir kriegen das ja, wir kriegen das meistens,
also die Neuigkeiten, das kriegen wir zuerst so in der Kantine mit.“* Geglättet:
`Wir erfahren Neuigkeiten meistens zuerst in der Kantine.`

**Typografie, verbindlich:**

| Zeichen | Regel |
|---|---|
| Gedankenstrich `–` `—` | verboten; Spannen als „X bis Y“ |
| Auslassungspunkte `…` `...` | in der Arbeitsmappe verboten; die Äußerung steht dort immer vollständig |
| Ausrufezeichen | verboten |
| Zeilenumbruch, Tabulator | verboten |
| runde Klammern | nicht für Zusätze; dafür sind eckige Klammern da |
| Doppelpunkt | erlaubt und häufig: trennt Rahmung von Aussage, leitet Binnenzitate ein |
| Fragezeichen | erlaubt: rhetorische Fragen der sprechenden Person bleiben Fragen |
| Anführungszeichen | **Binnenzitate stehen in einfachen deutschen Zeichen `‚…‘`**, nicht in `„…“` und nicht in `"…"` |

**Warum einfache Anführungszeichen im Binnenzitat.** Im Ergebnisdokument steht
jede Äußerung selbst in `„…“`. Ein Binnenzitat in denselben Zeichen erzeugt zwei
schließende Anführungszeichen hintereinander, und jede maschinelle Prüfung liest
das innere Fragment als das ganze Zitat. Mit `‚…‘` bleibt das äußere Paar
eindeutig. Die Regel gilt in Arbeitsmappe und Ergebnisdokument gleich; das
Zitat-Gate erkennt altformatierte `„…“`-Verschachtelungen zusätzlich über die
Klammertiefe, damit Altbestände nicht fälschlich als `NOT_FOUND` blockieren.

**Das schließende Zeichen ist `“` (U+201C), nicht das gerade.** Die Mischform aus
deutschem öffnendem und geradem schließendem Zeichen sieht gesetzt fast gleich
aus und ist deshalb der häufigste Typografiefehler in Altbeständen. Das
Zitat-Gate erkennt und prüft sie, meldet sie aber als Typografiebefund; dasselbe
gilt für Guillemets und für durchgängig gerade Anführungszeichen. Setze in
Arbeitsmappe, Ergebnisdokument und in dieser Dokumentation selbst die
Hausnormzeichen, sonst prüft das Gate an der Regel vorbei, die es durchsetzen
soll.

**Auslassungszeichen und der Ort der Kürzung.** Die Arbeitsmappe hält immer die
**vollständige** Codiereinheit; deshalb kommt dort kein `…` vor, und die
Validierung meldet jedes. Wird ein Zitat für das Ergebnisdokument gekürzt, steht
die gekürzte Fassung **nur dort** und die Auslassung ist mit `…` markiert. Eine
solche Kürzung fließt **nicht** in die Arbeitsmappe zurück: Sie ändert den
Wortlaut nicht, sie zeigt weniger davon. Zurück fließen nur Eingriffe in den
Wortlaut selbst, also Ersetzungen, Übersetzungen und Anonymisierungen.

**Sprache.** Die Interviewsprache bleibt erhalten; ein fremdsprachig geführtes
Interview wird in seiner Sprache codiert und nicht übersetzt. Für das
Ergebnisdokument gilt umgekehrt: Zitatsprache gleich Berichtssprache. Wird ein
Zitat übersetzt, ist die Übersetzung als solche zu kennzeichnen und in die
Arbeitsmappe zurückzuschreiben.

**Register bei Mitschriften.** Liegt kein Wortprotokoll vor, ist ein
telegrafischer, verdichteter Stil zulässig und wird nicht künstlich zu einem
Volltextsatz aufgeblasen. Beispiel:
`Montage: Lange Wartezeiten [an der Kantenanleimmaschine] und wenig Rückmeldung [aus der Planung].`

## 5. Eckige Klammern: drei Funktionen

Eckige Klammern sind das einzige Mittel für Eingriffe der auswertenden Person in
den Wortlaut. Sie erfüllen drei Funktionen, die auseinandergehalten werden.

**Funktion 1: Anonymisierung.** Klarnamen, Rollen- und Funktionsbezeichnungen,
identifizierende Orts- und Einheitennamen werden durch eine generische
Nominalphrase ersetzt. Die Klammer steht **an der Stelle** des ersetzten
Ausdrucks und übernimmt dessen Kasus.

| Untertyp | Beispiel |
|---|---|
| Nominalphrase mit Artikel | `Das hat [ein Mitglied der Geschäftsleitung] auf der Betriebsversammlung zugesagt.` |
| mit Präposition | `Die Abläufe [am zweiten Standort] kenne ich bisher nur vom Hörensagen.` |
| Einzelwort | `Für [eine Fachabteilung] ist der Termin viel zu eng gesetzt.` |

Wiederkehrende Ersetzungen müssen **wörtlich identisch** sein, damit Lesende sie
als dieselbe Entität erkennen. Führe dafür eine Ersetzungstabelle mit.

**Funktion 2: vorangestellte Kontextrahmung.** Wo die Äußerung nur mit der Frage
oder dem Gesprächsanlass verständlich ist, steht am Satzanfang eine Klammer,
meist mit Doppelpunkt innerhalb der Klammer.

Muster: `[<Rahmung>:] <Äußerung>`

```
[Zum Zeitplan:] Der zweite Standort soll im Frühjahr laufen.
[Größte Sorge:] Dass die eingespielten Teams auseinandergerissen werden.
```

**Funktion 3: grammatische Ergänzung und Referenzauflösung.** Kleine Einschübe,
die den geglätteten Satz schließen oder ein Pronomen auflösen, meist ein bis drei
Wörter.

```
Die Zusage steht, schriftlich haben wir sie bis heute nicht [bekommen].
Ohne sie [die Kolleginnen aus der Endmontage] lässt sich der Ablauf nicht planen.
Wir haben das [den Umbau der Lackiererei] damals in vier Wochen geschafft.
```

**Quantitative Konvention:**

| Kennzahl | Zielwert |
|---|---|
| Anteil Äußerungen mit Klammer | 20 bis 25 Prozent |
| Klammern je Äußerung | 0 bis 2, im Ausnahmefall mehr |
| Länge Klammerinhalt | um 20 Zeichen |
| Klammerpaare | immer geschlossen |

**Anti-Regel.** Klammern ersetzen nicht die Glättung. Eine Äußerung, die erst
durch drei oder mehr Klammern verständlich wird, ist zu kontextabhängig: neu
zuschneiden oder nicht als Beleg markieren. Macht Anonymisierung ein Zitat
unverständlich, wird es gestrichen, nicht verstümmelt.

## 6. Bewertung: vier Werte

Genau ein Zeichen, keine Kombinationen, keine Leerzeichen.

| Zeichen | Bedeutung | Codierfrage |
|---|---|---|
| `+` | positiv | Bewertet die Person den Ist-Zustand ausdrücklich zustimmend? |
| `-` | negativ | Bewertet die Person den Ist-Zustand ausdrücklich kritisch, als Mangel, Problem, Sorge? |
| `o` | neutral | Beschreibt die Person einen Sachverhalt, ohne ihn zu bewerten (Bericht, Chronologie, Rollenbeschreibung, Faktendarstellung)? |
| `>` | Veränderungswunsch | Formuliert die Person ein Soll, eine Forderung, einen Vorschlag, einen Bedarf für die Zukunft? |

**Vorrangregel bei Mehrdeutigkeit:** `>` schlägt `-`; `-` und `+` schlagen `o`.
Enthält eine Einheit Kritik am Ist und einen daraus abgeleiteten Wunsch, wird `>`
codiert: Der Veränderungswunsch ist das handlungsleitende Signal, die implizite
Kritik ist redundant. In Veränderungs- und Strategiekontexten ist `>` deshalb
regelmäßig die größte Klasse.

**Sprachliche Marker** als Heuristik, nicht als Regel:

| Zeichen | Typische Marker |
|---|---|
| `>` | sollte, müsste, muss, braucht, wäre, würde, wichtig ist, es geht darum, entwickeln, schaffen; Zukunftsbezug |
| `-` | kein, keine, fehlt, schwierig, wenig, zu viel, zu spät, nicht genug |
| `+` | gut, besser, richtig, erfolgreich, deutlich, hat funktioniert; oft im Perfekt als Erfolgsbericht |
| `o` | gab, hatte, war, unsere Rolle, Verantwortung, in den letzten Jahren; Aufzählungen von Zuständigkeiten |

Codiert wird die **Sprechhandlung**, nicht das Vokabular:
`Wir müssen die Kollegen aus der Montage früher einbeziehen.` ist `>`,
`Wir beziehen die Kollegen aus der Montage nicht früh genug ein.` ist `-`,
obwohl beide dasselbe Defizit benennen.

**Plausibilitätskorridor.** In Veränderungskontexten machen `>` und `-` zusammen
typischerweise 60 bis 70 Prozent aus. Fällt `>` unter 15 Prozent, ist vermutlich
zu viel als `-` codiert und die Vorrangregel nicht angewandt. Liegt `o` über
40 Prozent, ist die Codierung zu deskriptiv und der Beratungsnutzen gering.

## 7. Belegmarkierung mit `*`

Die Spalte `Kernaussage` enthält ausschließlich `*` oder nichts. **Sie enthält
niemals einen formulierten Text.** Der Stern ist ein Selektionszeichen, keine
Umformulierung: Er markiert den kuratierten Zitatpool für das Ergebnisdokument.
Die Verdichtung passiert eine Ebene höher, beim Schreiben des Befunds je
Kategorie. So bleibt jedes Zitat bis in die Quelle rückverfolgbar.

**Setze `*`, wenn die Äußerung ohne Zusatzerklärung auf einer Ergebnisfolie
stehen könnte**, also wenn sie:

1. **selbsttragend** ist, verständlich ohne Kontextwissen aus dem Interview,
2. den **Kern der Kategorie prägnant** trifft, nicht nur ein Detail oder eine
   Wiederholung,
3. **pointiert oder bildhaft** formuliert ist,
4. **anschlussfähig für die Auftraggeberseite** ist, diagnostisch oder
   handlungsleitend, nicht nur biographisch.

**Nicht markieren:** reine Sachdarstellungen, Wiederholungen desselben Gedankens
innerhalb eines Blocks, stark kontextabhängige Halbsätze, Äußerungen, deren
Gehalt erst durch mehrere eckige Klammern entsteht, Äußerungen aus nicht
zitierfähigen Quellenarten, fremdsprachige Äußerungen bei anderssprachigem
Bericht.

**Verteilung:**

| Regel | Zielwert |
|---|---|
| Gesamtquote | 20 bis 25 Prozent aller Codiereinheiten |
| Streuung über Kategorien | jede Kategorie braucht markierte Aussagen, sonst ist sie im Bericht nicht belegbar |
| Streuung über Bewertungen | `>` wird am häufigsten markiert, `o` am seltensten |
| Streuung über Personen | keine feste Quote je Person; die Dichte darf schwanken, aber nicht bis zum Ausreißer: über 45 Prozent, oder bei mindestens zehn Einheiten unter 5 Prozent, meldet `build_workbook.py` eine Warnung |
| Position im Block | kein Muster; die erste Aussage eines Blocks ist nicht automatisch die Kernaussage |
| Blockabdeckung | nicht jeder Block braucht eine Markierung; typisch sind ein bis drei je Block |

Die Markierung ist **notwendige, nicht hinreichende** Bedingung für Zitierung:
Nur ein Teil des Pools landet im Dokument. Umgekehrt gilt hart: kein Zitat im
Ergebnisdokument ohne Markierung in der Arbeitsmappe.

## 8. Sortierung

Dreistufig:

1. **Kategorie aufsteigend**, numerisch sortiert, nicht lexikographisch
   (`1.1`, `1.2`, `2.1`, … also `[int(t) for t in kategorie.split(".")]`).
2. **Kennung aufsteigend** (`P01`, `P02`, …).
3. **Auftretensreihenfolge im Gespräch** innerhalb eines Blocks aus Kategorie und
   Kennung.

**Nicht nach Bewertung sortieren.** Die chronologische Binnenordnung erhält den
Argumentationsgang der Person und ist beim Nachlesen wertvoll.

Der Effekt: Das Sheet liest sich als **Kategorienbuch**, alle Stimmen zu einem
Thema stehen beieinander. Das ermöglicht Querlesen und Zitatauswahl und ist der
Grund, warum nicht nach Person sortiert wird.

Bei Nachträgen wird die **vollständige** Tabelle neu sortiert. Neue Interviews
werden nie unsortiert ans Dateiende gehängt.

## 9. Prüfliste vor dem Schreiben

- [ ] Keine Leerwerte in `Kennung`, `Kategorie`, `Bewertung`, `Äußerung`
- [ ] `Bewertung` genau ein Zeichen aus `+ - o >`
- [ ] `Kernaussage` nur `*` oder leer
- [ ] `Kennung` passt auf `^P\d{2}$` und steht in der Registry
- [ ] `Kategorie` passt auf `^\d+\.\d+$` und existiert im Kategoriensystem
- [ ] keine doppelten Äußerungstexte
- [ ] alle eckigen Klammern paarig geschlossen
- [ ] Binnenzitate in `‚…‘`, alle Paare geschlossen
- [ ] keine Zeilenumbrüche, Tabulatoren, Gedankenstriche, Auslassungspunkte
- [ ] keine führenden, nachlaufenden oder doppelten Leerzeichen
- [ ] Sortierung nach Kategorie, dann Kennung, dann Gesprächsverlauf
- [ ] `*`-Quote zwischen 15 und 30 Prozent, keine Kategorie mit Quote null
- [ ] `*`-Quote je Person höchstens 45 Prozent, bei zehn und mehr Einheiten
      mindestens 5 Prozent
- [ ] `zitat_roh` je Einheit vorhanden, Status vergeben, kein `DRIFT` und kein
      `NOT_FOUND` offen
- [ ] Klammeranteil unter 40 Prozent

`scripts/build_workbook.py` führt diese Prüfungen nach dem Schreiben
automatisch aus; die vollständige Liste steht in `excel-output.md`.

## 10. Verifikationsdurchgang: Bezugsfassung und Status

Der Durchgang aus `SKILL.md` Schritt 2 prüft die Richtung **Codierung gegen
Transkript**: Steht die geglättete Äußerung so im Ausgangsmaterial, oder wurde
ein inhaltstragender Begriff ersetzt? Er ist ein Agentendurchgang, kein
Skriptlauf, und deshalb braucht er eine festgelegte Mechanik. Ohne sie gehen zwei
Anwender verschieden vor und die Statuswerte werden unvergleichbar.

**Bezugsfassung der Offsets.** `char_start` und `char_end` beziehen sich auf den
**zusammenhängenden Klartext des Interviews**, nicht auf die Datei, in der er
liegt. Liegt das Material als Liste von Sprecher-Turns vor, also als JSON, als
Tabelle oder als Untertiteldatei, ist die Bezugsfassung die Verkettung der Turns
in Gesprächsreihenfolge mit **genau einem Zeilenumbruch als Trenner**. Sprecher-
kennungen, Zeitmarken und Formatierungsreste gehören nicht in diese Fassung. Wird
sie einmal erzeugt und mitgeführt, sind die Offsets reproduzierbar.

**Pflicht und Kür.**

| Feld | Status |
|---|---|
| `zitat_roh` | **Pflicht.** Ohne den Originalspan hat der Durchgang nichts zu vergleichen. |
| `char_start`, `char_end` | optional. Sie beschleunigen das Wiederfinden und die Deduplizierung überlappender Spans; die Prüfung selbst läuft über `zitat_roh`. |

Bleiben die Offsets weg, wird das im Protokoll vermerkt, statt sie zu raten.

**Statussemantik.** Die vier Werte sind keine Qualitätsskala von gut nach
schlecht, sondern zwei Gutzustände und zwei Alarmzustände:

| Status | Bedeutung | Einordnung |
|---|---|---|
| `VERIFIED` | wortgleiche Übernahme, kein Zeichen geändert | Gutzustand, typisch für bereits sauber gesprochene oder redigierte Passagen |
| `SMOOTHING_OK` | nur Füllwörter, Verzögerungslaute, Abbrüche und Wiederholungen getilgt | **der erwartete Gutzustand geglätteter Einheiten** |
| `DRIFT` | ein inhaltstragender Begriff wurde ersetzt | Alarm: zurück in die Codierung, Originalbegriff wiederherstellen |
| `NOT_FOUND` | steht so nicht im Material | Alarm: Einheit raus, im Protokoll vermerken |

**Eine Codierung ohne `VERIFIED` ist kein Befund.** Glättung nach Abschnitt 4
verändert den Rohspan fast immer; bei automatisch erzeugten Transkripten enthält
praktisch jeder Satz Füllwörter oder Abbrüche. Dass alle Einheiten auf
`SMOOTHING_OK` landen, ist dort der Normalfall und kein Mangel. Umgekehrt ist
eine Codierung, die durchgängig `VERIFIED` meldet, ein Grund zur Rückfrage:
Entweder ist das Material bereits redigiert, oder es wurde gar nicht geglättet.

Der Blick gilt `DRIFT` und `NOT_FOUND`. Sie sind die Befunde des Durchgangs; die
beiden anderen Werte dokumentieren, dass geprüft wurde.
