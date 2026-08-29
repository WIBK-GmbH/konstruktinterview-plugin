# Ergebnisdokument

Aufbau des Foliensatzes, der die Auswertung an den Auftraggeber übergibt. Er ist
zugleich Präsentationsmedium und Nachschlagewerk. Beispiele stammen aus dem
Übungsfall *Firma M.* (Möbelhersteller, Verlagerung der Fertigung an einen
zweiten Standort, 14 Interviews).

## Inhalt

1. [Template anfordern, nichts erfinden](#1-template-anfordern-nichts-erfinden)
2. [Dramaturgie in vier Teilen](#2-dramaturgie-in-vier-teilen)
3. [Folientypen](#3-folientypen)
4. [Das Paarmuster](#4-das-paarmuster)
5. [Die Detailfolie](#5-die-detailfolie)
6. [Zählregeln](#6-zählregeln)
7. [Zitatregeln](#7-zitatregeln)
8. [Rohwerte und Aussagenstärke](#8-rohwerte-und-aussagenstärke)
9. [Textsortenregeln](#9-textsortenregeln)
10. [Was berechnet, was bestätigt wird](#10-was-berechnet-was-bestätigt-wird)
11. [Prüfungen vor Abgabe](#11-prüfungen-vor-abgabe)

---

## 1. Template anfordern, nichts erfinden

**Der Skill erfindet kein Corporate Design.** Er fordert eine Vorlagendatei an
und liest die Gestaltungsparameter aus ihr aus. Begründung gegenüber dem User:
Der Foliensatz geht an die Leitungsebene des Auftraggebers und muss dessen
Gestaltungsvorgaben entsprechen.

Anzufordern sind:

1. eine `.pptx` oder `.potx` mit dem Corporate Design des Auftraggebers; ohne sie
   wird der Foliensatz nicht erzeugt;
2. das Layout für die randlose Bildtrennfolie (Titel, Untertitel, Bildplatzhalter);
3. das Layout für die neutrale Inhaltsfolie (Titel und Foliennummer, idealerweise
   zwei Inhaltsplatzhalter);
4. Bildmaterial für die Trennfolien samt Bildnachweis, oder die Freigabe,
   die Trennfolien ohne Bild zu setzen;
5. den Wortlaut der Herkunftszeile (`Auftraggeber | ausführende Stelle | Monat Jahr`).

Aus der Vorlage ausgelesen statt gesetzt werden: Schrift für Überschriften,
Schrift für Fließtext, **eine Akzentfarbe**, **zwei neutrale Tönungen** für
Karten, die Textfarbe, ein Grauton für die Fußzeile und das Folienformat. Sind
diese Parameter in der Vorlage nicht eindeutig bestimmbar, **frage nach, statt zu
raten**.

**Fallback, wenn ausdrücklich keine Vorlage existiert.** Erklärt der
Auftraggeber, dass es keine Gestaltungsvorlage gibt, wird weder improvisiert noch
auf Markdown ausgewichen: Lege ein **neutrales Standarddesign** vor und lass es
bestätigen.

| Parameter | Standardwert |
|---|---|
| Schrift | eine serifenlose Schrift für Überschriften und Fließtext |
| Akzentfarbe | ein einziger kräftiger Ton, für Kartennummern, Zählzeilen und Zitatmarker |
| Tönungen | zwei neutrale Grautöne für das Schachbrett der Karten |
| Textfarbe | Schwarz oder ein sehr dunkles Grau |
| Fußzeile | mittleres Grau |
| Format | 16:9 |

Der so gebaute Foliensatz trägt auf der Rahmendaten-Folie den Hinweis, dass das
Design ein **Platzhalter** ist und vor einer Weitergabe über den Auftraggeber
hinaus durch dessen Vorlage ersetzt wird. Markdown bleibt dem sehr kleinen N
vorbehalten und ist kein Ersatz für die fehlende Vorlage.

**Bauweise.** Nur Trennfolien und die Rahmendaten-Folie nutzen echte
Layout-Platzhalter. Alle Inhaltsfolien bauen ihren Inhalt aus **freien Formen**:
abgerundete Rechtecke als Karten, füllungsfreie Rechtecke als Zitatflächen,
Textfelder für Titel und Rubriken. Verlass dich nicht darauf, dass die Vorlage
passende Platzhalter mitbringt.

**Raster** auf einer 16:9-Folie, Maße in cm. Die Zahlen sind **anpassbare
Referenzwerte eines beliebigen 16:9-Rasters**, keine Vorgabe: Was zählt, sind die
Verhältnisse (gleicher Satzspiegel links und rechts, gleich breite Spalten,
konstante Fußzeilenhöhe). Weicht das Folienformat der Vorlage ab, werden die
Werte proportional umgerechnet.

| Element | Wert |
|---|---|
| Satzspiegel | linker Rand 1,04, rechter Rand 1,03, nutzbare Breite 31,80 |
| Zwei Spalten | x = 1,04 und 17,14, Breite je 15,27 |
| Drei Spalten | x = 1,04 / 11,76 / 22,50, Breite je 9,80 bis 10,32 |
| Titelblock | x = 1,04, y = 0,97, Höhe 1,62 (zweizeilig) oder 3,10 (dreizeilig) |
| Inhaltsbeginn | y = 3,51 bis 4,17 je nach Titelhöhe |
| Fußzeile | y = 17,98, Höhe 0,71; links Herkunftszeile, rechts Foliennummer bei x = 30,48 |

**Schriftgrade** als Verhältnis zum Folientitel (Grundwert): Titelzeile 2 etwa
0,73, Kartenüberschrift 0,61, Kartennummer 0,59, Rubriken 0,55, Zählzeile 0,5,
Kartenfließtext 0,5, Zitate 0,48, Herkunftszeile 0,39, Titel der
Empfehlungsfolien 1,09, Trennfolientitel 1,8. Der Kartenfließtext darf zum
Unterbringen von Inhalt skaliert werden; wird weniger als etwa 85 Prozent des
Regelwerts gebraucht, **ist der Text zu kürzen, nicht die Schrift zu verkleinern**.

**Kartenfüllung im Schachbrett**, zeilenweise versetzt:

```
3 Karten nebeneinander:  hell · dunkel · hell
2 × 2 Karten:            hell   dunkel        3 × 2:  hell   dunkel hell
                         dunkel hell                  dunkel hell   dunkel
```

## 2. Dramaturgie in vier Teilen

Ein Dokument, vier Teile, durch Trennfolien abgesetzt.

| Teil | Funktion |
|---|---|
| **A Rahmen und Methodik** | Titel, Verwendungszweck, Untersuchungsziele, Stichprobe, methodisches Vorgehen, Anonymisierungszusage; optional eine Delta-Folie |
| **B Management Summary** | Trenner, Kategorienüberblick, je Themenblock ein Folienpaar Gemeinsamkeiten und Unterschiede, dazu Vertiefungsfolien zu den Kernfragen des Auftrags |
| **C Detailauswertung** | Trenner, Kategorienüberblick erneut, genau eine Folie je Unterkategorie |
| **D Ableitung** | Brückenfolie zum Auftrag, Empfehlungen, nächste Schritte |

**Sequenzregel.** Der Detailteil kommt **nach** dem Management Summary. Die
Verdichtung ist die Botschaft, der Detailteil der Beleg. Wer den Detailteil nach
vorn zieht, zwingt die Leitungsebene durch das Material statt durch die Befunde.

**Skalierungsregel.** Teil C hat zwingend genau eine Folie je Unterkategorie.
Teil B hat je Themenblock ein Folienpaar; die Themenblöcke entstehen durch
Zusammenfassung benachbarter Kategorien, ihre Nummern werden im Untertitel
offengelegt.

**Regel doppelter Überblick.** Die Kategorienüberblicksfolie erscheint zweimal
identisch: als Landkarte vor dem Management Summary und als Inhaltsverzeichnis
vor dem Detailteil. Beide Instanzen müssen bei jeder Änderung **zeichengleich**
bleiben.

**Regel Delta-Folie.** Nur einfügen, wenn es einen kommunizierten Zwischenstand
gab. Sie beantwortet drei Fragen in drei Karten: was hat sich an der Datenbasis
geändert, wo haben sich Schwerpunkte verschoben, wo haben sich Befunde qualitativ
zugespitzt.

**Ihr Titel enthält das Wort „Delta“**, etwa „Delta zum Zwischenstand vom
<Datum>“. Das ist keine Stilfrage: Eine Delta-Folie nennt zwangsläufig Zahlen des
früheren Standes, und das Zähl-Gate erkennt an diesem Wort, dass es hier nicht
gegen die aktuelle Arbeitsmappe prüfen darf. Dasselbe gilt für den
Delta-Abschnitt der Prozessnotiz: Die Abschnittsüberschrift trägt das Wort. Ohne
diese Kennzeichnung meldet das Gate jede alte Zahl als Fehler.

**Regel Survey Feedback.** Die Rückspiegelung der aggregierten Diagnose an die
Befragten gehört als eigener nächster Schritt in das Dokument. Sie validiert die
Befunde und ist zugleich der erste Beteiligungsschritt.

## 3. Folientypen

| Typ | Zweck | Aufbau |
|---|---|---|
| **T1 Trennfolie** | Kapiteleinstieg, genau dreimal: Dokumenttitel, Beginn Teil B, Beginn Teil C | randlose Bildfolie, Titel einzeilig groß, Untertitel 2 bis 4 Zeilen: Erhebungsform und Kontext, Standzeile „Ergebnisse nach X von N Interviews“, Umfangszeile des Teils, ausführende Stelle |
| **T2 Rahmendaten** | einzige Folie mit echten Platzhaltern | links Verwendungszweck, Untersuchungsziele, Stichprobe; rechts methodisches Vorgehen, Datengrundlage, Anonymisierung |
| **T3 Kategorienüberblick** | Landkarte und Inhaltsverzeichnis | eine Karte je Hauptkategorie nebeneinander, konstante Kartenhöhe; je Unterkategorie zwei Zeilen |
| **T4 Paar** | Kern des Formats | 2 × 2 Karten, siehe Abschnitt 4 |
| **T5 Zitate und Anregungen** | Vertiefung | links Rubrik „Stimmen aus den Interviews:“ über einer **füllungsfreien** Fläche mit 4 bis 6 Zitaten, rechts Rubrik „Anregungen:“ über einer **gefüllten** Karte mit 2 bis 3 fetten Zwischenüberschriften und je 3 bis 4 Punkten |
| **T6 Gegenüberstellung** | ein einzelnes, besonders gewichtetes Thema | wie T5, aber beide Spalten gefüllt: links `X von N: <Befund>`, rechts `<Dimension>: <Pol A> (X von N) gegenüber <Pol B> (Y von N)` |
| **T7 Kartenfolie** | Delta, Übersichten, gebündelte Anregungen | drei Karten nebeneinander, Aufbau wie T4 mit mehr Raum |
| **T8 Detailfolie** | eine je Unterkategorie | fester Bauplan, siehe Abschnitt 5 |
| **T8-Variante Brückenfolie** | Befunde zur Architektur des eigenen Auftrags | wie T8, aber Titelzeile 1 benennt den Auftrag, Titelzeile 2 nennt die Kategoriennummern, aus denen die Befunde stammen, rechte Spalte enthält eine nummerierte Handlungsliste statt Zitaten |
| **T9 Empfehlungskarten** | Empfehlungen und nächste Schritte | Titel 24 pt fett ohne Unterzeile, 3 oder 6 Karten; je Karte Nummer in der Akzentfarbe, Empfehlung als Imperativ- oder Infinitivphrase fett, 1 bis 3 Sätze Erläuterung: wer tut was, bis wann, mit welchem Ergebnis |

**T1, zwei Regeln zum Titel.** Die Titelfolie benennt den **Zweck der Erhebung**,
nicht die Methode: „Wie die Verlagerung im Betrieb ankommt“ statt „Durchführung
von Konstruktinterviews“. Wer die Methode in den Titel setzt, verschiebt die
Aufmerksamkeit vom Ergebnis auf das Verfahren. Und **jede Trennfolie trägt den
Namen ihres Abschnitts**; kein Trennertitel wiederholt sich. Dreimal derselbe
Trennertitel macht die Gliederung unsichtbar, die er markieren soll.

**T3 Karteninhalt** je Unterkategorie zwei Zeilen:

```
<Nummer> <Kurzname der Unterkategorie>
→ X von N Personen (a +, b -, c o, d >)
```

**T2 rechte Spalte** nennt im Abschnitt „Methodisches Vorgehen“ genau vier Dinge:
die qualitative Inhaltsanalyse mit Quellenangabe; die Vollcodierung („jede
relevante Äußerung wurde erfasst und mit einer Bewertung versehen“); das
Bewertungsschema im Klartext (`+ positiv, - negativ, o neutral, > Wunsch`); die
induktive Kategorienbildung mit Kategorienzahl und Zahl der Hauptkategorien nebst
Beleghinweis. Der Abschnitt „Anonymisierung“ enthält die ausdrückliche Zusage:
Zitate ohne Personenkennung und ohne Kennzeichnung der Perspektivgruppe,
rollenspezifische Angaben generalisiert.

**T9 zweimal.** Empfehlungsfolie und Nächste-Schritte-Folie sind derselbe Typ und
unterscheiden sich nur im Zeitbezug: Empfehlungen betreffen die Ausgestaltung des
Vorhabens, nächste Schritte die unmittelbar anstehenden Handlungen.

## 4. Das Paarmuster

Für jeden Themenblock **immer zwei Folien im Paar**:

- **Folie A, Gemeinsamkeiten.** Untertitel: „Was die Befragten teilen
  (Kategorien x.x, x.x …)“
- **Folie B, Unterschiede.** Untertitel: „Wo die Einschätzungen auseinandergehen
  (Kategorien x.x, x.x …)“, Variante „Wo die Vorstellungen auseinandergehen“, wenn
  es um Gestaltungsvorstellungen statt um Lagebeurteilungen geht.

Beide Folien: 2 × 2 Karten. **Kartenbauplan:**

1. Zeile 1: laufende Nummer `01` bis `04`, zweistellig, klein, fett, Akzentfarbe
2. Zeile 2: **Befundsatz als Überschrift**, ein vollständiger, wertender
   Aussagesatz, kein Etikett
3. Zeilen 3 bis 6: zwei bis fünf Belegzeilen ohne Aufzählungszeichen

**Karten-Grammatik, Gemeinsamkeiten.** Die Zahl steht **am Satzanfang**, nie in
Klammern am Ende:

```
X von N <Verb des Deutens> <Befund>[: <Konkretisierung, Konkretisierung>]
```

Verben stufen die Stärke der Aussage ab: sehen, beschreiben, nennen, halten … für,
fordern, wollen, bestimmen … als, begründen … mit, berichten, machen … zur
Bedingung, kritisieren.

```
9 von 14 nennen die Information über den Stand als Hauptproblem: späte
Weitergabe, wechselnde Kanäle, fehlende Verbindlichkeit der Zusagen.
```

**Karten-Grammatik, Unterschiede.** Das Spannungsverhältnis steht im Kartenkopf,
die Belegzeilen stellen die Pole gegenüber, die Zahl **nachgestellt**:

```
<Position A>: X von N[, <Zusatz zur Verteilung über Perspektivgruppen>]
<Position B>: Y von N[, <Zusatz>]
[<vermittelnde Position>: Z von N]
```

```
Wer bei der Maschinenaufstellung mitentscheidet
Selbst über die Aufstellung bestimmen: 6 von 14, getragen von der Fertigung
Nur informiert werden, um arbeitsfähig zu bleiben: 5 von 14
Mitreden in einer festen Runde mit klarem Mandat: 3 von 14
```

Eine dritte, vermittelnde Position wird ausgewiesen, wenn sie in den Daten
vorkommt; sie ist der beraterisch wertvollste Teil der Folie.

**Verteilungshinweise.** Auf Unterschiedsfolien wird ergänzt, **wo** eine Position
sitzt, als Perspektivgruppe, nie als Person. Auf Gemeinsamkeitenfolien wird
umgekehrt die Breite betont („aus allen vier Perspektivgruppen“, „dazu findet sich
keine Gegenstimme“).

**Sachwiderspruch.** Widersprechen zwei Aussagen einander sachlich, statt nur in
der Bewertung zu differieren, wird das ausdrücklich benannt: „Ein offener
Sachwiderspruch: Der Zeitplan wird von einer Seite als gesichert, von der anderen
als bereits gerissen beschrieben.“ Das ist ein Kernstück der Außenperspektive.

Eine Unterschiedsfolie ohne echte Gegensätze ist ein Analysefehler, kein
Harmoniebefund.

## 5. Die Detailfolie

Der am striktesten standardisierte Typ: **immer genau acht Formen**, immer in
derselben Anordnung.

```
┌─ Titelblock  x1,04 y0,97 b31,80 h3,10 ────────────────────────────┐
│ Z1  <Nr>. <Name der Hauptkategorie>            22 pt fett          │
│ Z2  <Nr.Nr> <Name der Unterkategorie>          16 pt normal        │
│ Z3  X von N Personen (a +, b -, c o, d >)      11 pt fett, Akzent  │
└────────────────────────────────────────────────────────────────────┘
┌─ Kurzfassung  x1,04 y4,17 b31,80 h3,43  (gefüllte Karte) ─────────┐
│ <Leitsatz>: <Fließtext, 3 bis 5 Sätze, mit Rohwertbelegen>        │
└────────────────────────────────────────────────────────────────────┘
  Rubrik links x1,04 y8,05          Rubrik rechts x17,14 y8,05
  „Stimmen aus den Interviews:“     „<kategoriespezifisches Label>:“
┌─ Zitate links  x1,04 y8,81 ──┐ ┌─ Zitate rechts  x17,14 y8,81 ──┐
│ b15,27 h8,84, ohne Füllung   │ │ b15,27 h8,84, ohne Füllung     │
│ 5 bis 6 Zitate               │ │ 5 bis 6 Zitate                 │
└──────────────────────────────┘ └────────────────────────────────┘
  Herkunftszeile y17,98            Foliennummer x30,48 y17,98
```

**Zählzeile.** Format exakt `X von N Personen (a +, b -, c o, d >)`. Siehe
Abschnitt 6.

**Kurzfassung.** Beginnt mit einem **fett gesetzten Leitsatz**, der das
Spannungsfeld der Kategorie in einer Nominalphrase benennt, danach drei bis fünf
Sätze Fließtext, in denen mindestens einmal eine Rohwertangabe steht. Der
Leitsatz benennt bewusst die **Spannung**, nicht das Thema. Das ist der
Unterschied zwischen einer Überschrift und einem Befund.

**Rechtes Rubriklabel.** Variiert je Kategorie und benennt, was rechts an
Erwartungen oder Ableitungen steht. Muster: zwei mit `&` verbundene Substantive
oder eine kurze Nominalphrase, immer mit Doppelpunkt, etwa „Sorgen &
Bedingungen:“ oder „Wünsche an den Ablauf der Verlagerung:“.

**Ausnahme Chancen und Risiken.** Fasst eine Kategorie Chancen und Risiken
zusammen, werden **beide** Spalten nach Inhalt statt nach Status geteilt:
„Risiken und Fallstricke:“ links, „Chancen und Erfolgsbedingungen:“ rechts. Dann
enthalten beide Spalten Zitate.

## 6. Zählregeln

**Die wichtigste und am leichtesten falsch zu machende Regel des Formats: Alle im
Foliensatz ausgewiesenen Zahlen sind Personenzählungen.**

| Angabe | Definition |
|---|---|
| `X von N Personen` | Zahl der distinkten Befragten mit mindestens einer Äußerung in dieser Kategorie |
| `a +` | Zahl der distinkten Befragten mit mindestens einer **positiven** Äußerung in dieser Kategorie |
| `b -`, `c o`, `d >` | analog |

Vier Folgeregeln:

1. **Die vier Bewertungszahlen sind keine Partition.** Eine Person kann in
   derselben Kategorie positiv und negativ codiert sein, `a+b+c+d` ist deshalb
   regelmäßig **größer** als `X`. Das ist korrekt und wird nicht repariert.
2. **Prüfregel** `max(a, b, c, d) ≤ X ≤ N`. Verletzt eine Zahl das, liegt ein
   Rechenfehler vor.
3. **Das Auszählungsblatt der Arbeitsmappe darf nicht ungeprüft übernommen
   werden.** Es enthält Äußerungszahlen, optisch dieselbe Struktur, inhaltlich
   etwas anderes. Berechne die Personenzahlen selbst: gruppieren nach Kategorie
   und Bewertung, distinkte Kennungen zählen (`scripts/aggregate.py --level
   personen-bewertung --format zeilen`).
4. **Äußerungszahlen erscheinen an genau zwei Stellen:** als Gesamtzahl auf der
   Rahmendaten-Folie und in der Untertitelzeile der Trennfolie des Detailteils.
   Niemals in einer Befundaussage.

**Unterthemen im Management Summary.** Wird innerhalb einer Kategorie ein
Unterthema gebildet, werden ihm Äußerungen zugeordnet und danach die distinkten
Personen gezählt. Prüfregel: **Personenzahl des Unterthemas ≤ Personenzahl der
zugehörigen Kategorie.**

## 7. Zitatregeln

**Auswahl.** Zitate stammen ausschließlich aus Äußerungen, die in der
Arbeitsmappe mit `*` markiert sind. Ohne Markierung kein Zitat.

**Menge.** 5 bis 6 Zitate je Spalte, 10 bis 12 je Detailfolie, 4 bis 6 auf
Vertiefungsfolien. Länge um 150 Zeichen, Spanne 30 bis 400.

**Format.** Jedes Zitat ist ein eigener Absatz:

```
<Marker><zwei Leerzeichen>„<Zitattext>“
```

- Marker ist eines von `+`, `-`, `o`, `>` und entspricht **exakt der Bewertung
  der zitierten Zeile** in der Arbeitsmappe
- Marker fett und in der Akzentfarbe, Zitattext normal in der Textfarbe
- deutsche typografische Anführungszeichen `„…“`, **Binnenzitate in `‚…‘`**;
  keine Guillemets, keine geraden Anführungszeichen und **keine Mischform**, also
  kein gerades Zeichen als Schluss eines mit `„` geöffneten Zitats. Das
  Zitat-Gate erkennt und prüft alle drei Abweichungen, meldet sie aber als
  Typografiebefund.
- **keine Personenkennung, keine Interviewnummer, keine Perspektivgruppe**

**Ein Anführungszeichenpaar ist eine Codiereinheit ist eine Person.**
Zusammensetzen aus mehreren Einheiten oder mehreren Personen ist verboten. Ein
Binnenzitat in denselben Anführungszeichen wie das Zitat selbst zerstört genau
diese Prüfbarkeit; deshalb steht es in `‚…‘`.

**Kürzen.** Auslassungen innerhalb einer Einheit sind mit `…` zu markieren. Die
gekürzte Fassung lebt **nur im Ergebnisdokument**; die Arbeitsmappe behält die
vollständige Äußerung und enthält selbst nie Auslassungszeichen. Eine Kürzung
fließt deshalb **nicht** zurück.

**Erlaubte Redaktion am Wortlaut:** eckige Klammern für generalisierte Rollen- und
Kontextangaben, Reparatur eindeutiger Transkriptionsfehler, minimale grammatische
Glättung, Übersetzung mit Kennzeichnung. **Nicht erlaubt:** Bedeutungsänderung,
Zusammenziehen von Äußerungen, Zuspitzung, Paraphrase in Anführungszeichen,
Terminologie-Harmonisierung im Zitat. Wird ein Begriff im Bericht vereinheitlicht,
geschieht das im Rahmentext; im Zitat nur mit eckiger Klammer.

**Jede Redaktion am Wortlaut fließt in die Arbeitsmappe zurück**, bevor der Stand
geschlossen wird. Sonst schlägt das Zitat-Gate beim nächsten Lauf an. Für
Kürzungen gilt das ausdrücklich nicht.

**Quellzeile mitführen.** Notiere beim Setzen jedes Zitats seine Quellzeile
(`Aussagen!<Zeile>`) in einer Begleitdatei neben dem Dokument. Sie geht als
`--zitatregistry` in die Prüfung ein und fängt den Fall, dass der Fuzzy-Match
eines stark redigierten Zitats auf die falsche Zeile zeigt.

**Zitierfähigkeit.** Beruht die Kennung auf Mitschrift, Gedächtnisprotokoll oder
Diktat, darf nicht wörtlich zitiert werden. Solches Material erscheint sinngemäß
und **ohne Anführungszeichen** im Rahmentext; einen Zwischenweg über eine
Kennzeichnung gibt es nicht. Die Quellenart steht im Pseudonymschlüssel und in
der JSON-Codiertabelle.

**Verteilung.** Innerhalb einer Spalte werden Zitate unterschiedlicher Bewertung
gemischt. Eine Spalte, in der alle Marker gleich sind, ist nur zulässig, wo die
Rubrik das ankündigt.

**Streuung.** Die Zitate einer Folie sollen von möglichst vielen verschiedenen
Personen stammen; keine Person dominiert eine Spalte.

## 8. Rohwerte und Aussagenstärke

Befunde werden **ausschließlich in Rohwerten** ausgewiesen: `X von N`. Nie
„45 Prozent“, nie „die Mehrheit“, nie „viele“. Bei qualitativen Stichproben
suggerieren Prozentangaben eine Repräsentativität, die das Verfahren nicht
beansprucht.

**Ausnahme:** Zahlen, die die Befragten selbst nennen, bleiben in ihrer
Originalform erhalten, auch als Prozentwert. Sie sind Gegenstand der Aussage,
nicht Auswertungsstatistik.

Spannen werden als „X bis Y“ geschrieben, nicht mit Bindestrich.

**Aussagenstärke an die Personenzahl koppeln:**

| Personenzahl | zulässige Formulierung |
|---|---|
| alle N | „ausnahmslos alle“, „alle N von N“ |
| ≥ ¾ von N | „nahezu alle“, „die große Mehrheit“ |
| ½ bis ¾ | schlichte Rohwertangabe, kein Mengenwort |
| ¼ bis ½ | schlichte Rohwertangabe |
| 1 bis 3 | „einzelne Stimmen“, „eine Stimme formuliert“; nur ausweisen, wenn die Aussage inhaltlich etwas beiträgt, etwa als Brückenposition |

Ein Befund darf **ohne Zahl** formuliert werden, wenn er ein Fehlen feststellt
(„dazu findet sich keine Gegenstimme“, „niemand lehnt das im Grundsatz ab“).
Solche Negativbefunde sind besonders wertvoll und ausdrücklich zu suchen.

## 9. Textsortenregeln

**Der Auswerter kommt im Bericht nicht als Handelnder vor.** Kein Satz nennt das
auswertende Institut als Akteur oder sagt eine Leistung zu. Empfehlungen werden
als Folgerung aus den Daten formuliert („Aus den Interviews folgt …“, „Die
Befragten erwarten …“). Ist ein Prozessvorschlag gewünscht, entsteht er als
**eigenes Dokument**.

**Satzbau.**

- Befunde sind **vollständige Aussagesätze im Indikativ Präsens**. Kein
  Nominalstil als Überschrift, keine Stichwortliste als Befund.
  Gut: „Die Information über den Stand kommt in der Fertigung zu spät an.“
  Schlecht: „Informationsproblematik in der Fertigung“.
- **Die Zahl trägt den Satz**, sie steht nicht in Klammern hinterher.
- Über die Befragten wird in der dritten Person gesprochen, nie in der ersten
  Person Plural.
- Kurze Sätze, Aufzählungen mit höchstens drei Gliedern.
- **Keine Gedankenstriche.** Spannen als „X bis Y“, Erläuterungen mit Doppelpunkt
  oder Komma.

**Verbotene Konstruktionen.**

| Verboten | Warum |
|---|---|
| abstrakte Dreiklang-Überschriften („Spannungsfeld zwischen A, B und C“) | typische Maschinenprosa, sagt nichts |
| Wortneubildungen und ungebräuchliche Komposita | erfundene Fachlichkeit |
| Fachbegriffe, die im Material nicht vorkommen | überträgt fremde Deutung auf die Befragten |
| Metaphern-Nominalisierungen | Behauptung statt Befund |
| Beratungsfloskeln („ganzheitlich“, „nachhaltig verankern“, „mitnehmen“) | inhaltsleer |
| Anglizismen ohne Not | |

**Tonalität.** Beschreibend und belegt, nicht wertend über Personen. Bewertet
werden Sachverhalte und Muster, nicht Befragte. Spannungen werden benannt, nicht
geglättet: Das Format existiert, um Unterschiede sichtbar zu machen.

**Zitatsprache gleich Berichtssprache.** Ein fremdsprachiges Zitat wird für den
Bericht übersetzt und die Übersetzung gekennzeichnet, oder es entfällt.

**Anonymisierung.** Zitate ohne jede Personenkennung. Rollenangaben generalisiert
und in eckigen Klammern. Perspektivgruppen dürfen als Gruppe benannt werden, wenn
die Gruppe groß genug ist; bei weniger als drei Personen unterbleibt die
Gruppenangabe. Die Anonymisierungszusage steht ausdrücklich auf der
Rahmendaten-Folie. Der Pseudonymschlüssel bleibt außerhalb des Foliensatzes.

**Vor der Abgabe** läuft die Prosa durch die Skills `stop-slop` und `humanizer`.

## 10. Was berechnet, was bestätigt wird

| Sorte | Beispiele | Umgang |
|---|---|---|
| **berechenbar** | Zählzeilen, Kategorienüberblick, Gesamtzahl der Äußerungen, Stichproben- und Gruppengrößen, Zitatkandidatenpool, Konsistenzprüfungen | **skriptgestützt erzeugen**, nie schätzen |
| **hybrid** | `X von N` im Management Summary, Zuschnitt der Themenblöcke, Verteilungshinweise auf Gruppen, Auswahl der 5 bis 6 Zitate | gruppieren, **bestätigen lassen**, dann zählen |
| **beraterisches Urteil** | Befundüberschriften, Leitsätze der Kurzfassungen, rechte Rubriklabels, Zuspitzung eines Gegensatzes, Feststellung eines Sachwiderspruchs, Erkennen einer Brückenposition, Empfehlungen, nächste Schritte, Delta-Deutung | dem User **zur Bestätigung vorlegen**, nicht stillschweigend setzen |

## 11. Prüfungen vor Abgabe

Vollständige Gate-Beschreibung in `gates.md`. **[S]** heißt: ausgeführt durch
`scripts/validate_deliverables.py`. **[A]** heißt: Der Agent prüft selbst, das
Skript sieht diesen Punkt nicht. Foliensatz-spezifisch:

- [ ] **[S]** Gesamtzahl der Äußerungen auf **allen** Folien identisch, inklusive
      Trenn- und Rahmenfolien
- [ ] **[S]** Stichproben- und Gruppengrößen stimmen mit der Arbeitsmappe überein
- [ ] **[S]** Kategoriennamen im Überblick und auf der Detailfolie **wörtlich
      identisch**
- [ ] **[S]** beide Instanzen der Kategorienüberblicksfolie zeichengleich
- [ ] **[S]** jede Zählzeile erfüllt `max(a,b,c,d) ≤ X ≤ N`
- [ ] **[S]** jede `X von N`-Angabe im Management Summary ist ≤ der Personenzahl
      ihrer Kategorie
- [ ] **[S]** jedes Zitat wortgleich in der Arbeitsmappe auffindbar, jeder Marker
      entspricht der Bewertung dieser Zeile
- [ ] **[S]** kein Zitat aus einer nicht zitierfähigen Quellenart (nur mit
      `--key`)
- [ ] **[S]** kein Zitat mit Personen- oder Gruppenkennung
- [ ] **[A]** Folientitel und Folieninhalt decken dieselben Kategoriennummern ab
- [ ] **[S]** keine abgebrochenen Sätze und Karten: ein letzter Absatz, der mit
      Doppelpunkt oder Komma endet. **[A]** bleibt der optisch abgeschnittene
      Text, den erst der Blick auf die Folie zeigt
- [ ] **[A]** Textmenge je Karte geprüft: bei den Referenzmaßen passen rund 55
      Zeichen je Zeile in eine 15,27 cm breite Karte, die 2 × 2-Karte fasst rund
      acht Zeilen
- [ ] **[A]** jede Folie trägt Herkunftszeile und Foliennummer
- [ ] **[A]** Titelfolie benennt den Zweck, nicht die Methode; kein Trennertitel
      wiederholt sich
- [ ] **[A]** Prosa durch `stop-slop` und `humanizer` gelaufen
