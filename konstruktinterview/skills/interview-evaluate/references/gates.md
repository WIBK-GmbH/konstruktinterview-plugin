# Qualitäts-Gates

Diese Gates laufen auf den **Endartefakten**, nicht nur auf der Codierung, und
sie laufen **pfadunabhängig**: im Standardpfad genauso wie im Ultracode-Pfad, bei
drei Interviews genauso wie bei dreißig. Ein Gate, das nur im aufwendigen Pfad
läuft, schützt die kleinen, ebenso sensiblen Auswertungen nicht.

Beispiele stammen aus dem Übungsfall *Firma M.* (Möbelhersteller, Verlagerung der
Fertigung an einen zweiten Standort).

## Inhalt

1. [Grundsatz](#1-grundsatz)
2. [Zitat-Gate](#2-zitat-gate)
3. [Zähl-Gate](#3-zähl-gate)
4. [Zahl-Text-Kongruenz-Lint](#4-zahl-text-kongruenz-lint)
5. [Anonymisierungs-Lint](#5-anonymisierungs-lint)
6. [Konsistenz-Checks über alle Artefakte](#6-konsistenz-checks-über-alle-artefakte)
7. [Wortlaut-Sperre nach Freigabe](#7-wortlaut-sperre-nach-freigabe)
8. [Die drei Checkpoints](#8-die-drei-checkpoints)
9. [Skript](#9-skript)

---

## 1. Grundsatz

Drei Sätze tragen alle Gates:

1. **Die Arbeitsmappe gewinnt.** Weicht das Ergebnisdokument von ihr ab, wird das
   Dokument korrigiert, nicht die Mappe angepasst. Ausnahme: eine bewusste
   Redaktion am **Wortlaut** eines Zitats, die dann in die Mappe zurückfließt.
   Eine mit `…` markierte **Kürzung** ist keine solche Redaktion und fließt nicht
   zurück; sie zeigt weniger vom Wortlaut, sie ändert ihn nicht.
2. **Prüfen heißt neu berechnen.** Ein Gate, das eine Zahl mit sich selbst
   vergleicht, prüft nichts. Jede Zahl wird aus dem Sheet `Aussagen` neu
   berechnet und dann verglichen.
3. **Die Nachlese meldet, sie schreibt nicht um.** Nach einer menschlichen
   Eingriffsrunde darf der maschinelle Pass Befunde ausweisen und nichts
   umformulieren.

## 2. Zitat-Gate

**Jedes Zitat im Ergebnisdokument muss wortgleich in der Arbeitsmappe auffindbar
sein.** Das Gate läuft gegen das **fertige Dokument**, nicht nur gegen die
Codierung. Genau dort, im Schritt vom Codieren zum Berichten, entsteht Zitatdrift.

**Vier Status je Zitat:**

| Status | Bedeutung | Konsequenz |
|---|---|---|
| `VERIFIED` | zeichengleich in einer `*`-markierten Zeile gefunden | in Ordnung |
| `SMOOTHING_OK` | Abweichung ohne Substitution | zulässig, Konsequenz je nach Art der Abweichung, siehe unten |
| `DRIFT` | im Zitat steht ein inhaltstragendes Wort, das in der Ursprungszeile fehlt: ein Begriff wurde substituiert, paraphrasiert oder harmonisiert | zurück an die Codierung, Originalbegriff wiederherstellen |
| `NOT_FOUND` | keine Ursprungszeile zuordenbar | Zitat aus dem Dokument entfernen und protokollieren |

Der Abgleich läuft als Fuzzy-Match mit Ähnlichkeitswert. Die Grenze zwischen
`SMOOTHING_OK` und `DRIFT` zieht **nicht** der Ähnlichkeitswert allein, sondern
der Wortmengenvergleich: Ein Ähnlichkeitswert von 0,94 kann eine harmlose Tilgung
oder eine Ein-Wort-Substitution sein, die den Sinn dreht. Enthält das Zitat ein
inhaltstragendes Wort, das in der Ursprungszeile nicht vorkommt, ist es `DRIFT`.
Reine Tilgungen bleiben `SMOOTHING_OK`. Inhalte in eckigen Klammern zählen dabei
nicht als neue Wörter, sie sind erlaubte Redaktion.

**Zwei Arten von `SMOOTHING_OK`, mit verschiedener Konsequenz:**

| Art | Beispiel | Konsequenz |
|---|---|---|
| Kürzung | eine mit `…` markierte Auslassung, eine getilgte Wiederholung | bleibt im Ergebnisdokument, **kein Rückfluss**; die Arbeitsmappe behält die vollständige Äußerung |
| Wortlautredaktion | eckige Klammer, Übersetzung, Anonymisierung | **fließt in die Arbeitsmappe zurück**, bevor der Stand geschlossen wird |

**Zusätzliche harte Prüfungen:**

- [ ] Das Zitat stammt aus einer Zeile mit `*` in der Spalte `Kernaussage`.
- [ ] Der vorangestellte Marker entspricht **exakt** der `Bewertung` dieser Zeile.
- [ ] **Ein Anführungszeichenpaar ist eine Codiereinheit ist eine Person.**
      Zitat-Splicing über zwei Zeilen oder zwei Kennungen ist ein blockierender
      Fehler, auch wenn der zusammengesetzte Satz plausibel klingt.
- [ ] Keine Paraphrase in Anführungszeichen. Formulierungen, die im gesamten
      Korpus nicht vorkommen, sind kein Zitat.
- [ ] Auslassungen innerhalb einer Einheit sind mit `…` markiert, und zwar
      ausschließlich im Ergebnisdokument.
- [ ] Anführungszeichen nach Hausnorm: Zitate in `„…“`, Binnenzitate in `‚…‘`.
      Drei abweichende Formen werden zwar erkannt und geprüft, aber als
      Typografiebefund gemeldet: Guillemets, die **Mischform** (öffnendes `„`,
      schließendes gerades Zeichen) und durchgängig gerade Anführungszeichen.
      Keine Form bleibt unsichtbar: Ein Zitat, das das Gate nicht sieht,
      passiert es stumm, und genau das wäre ein grün protokolliertes Gate ohne
      Prüfung.
- [ ] Die Quellenart der Kennung erlaubt wörtliches Zitieren. Bei Mitschrift,
      Gedächtnisprotokoll oder Diktat ist wörtliches Zitat unzulässig, ohne
      Zwischenweg: Solches Material wird sinngemäß und ohne Anführungszeichen im
      Rahmentext wiedergegeben. Das Zitat-Gate prüft, ob der Text im Material
      **steht**; die Quellenart-Regel prüft, ob dieses Material
      **Wortlautqualität** hat. Beides ist nötig.
- [ ] Kein Zitat trägt Personenkennung, Interviewnummer oder Gruppenangabe.

**Zitat-Registry.** Beim Bauen des Ergebnisdokuments wird je Zitat die Quellzeile
notiert (`Aussagen!<Zeile>`), als Begleitdatei neben dem Dokument. Ohne sie
rekonstruiert das Gate die Zuordnung per Fuzzy-Match, und bei stark redigierten
Zitaten kann der Match auf die falsche Zeile zeigen, ohne dass es auffällt. Mit
`--zitatregistry` prüft das Skript den Match gegen die deklarierte Zeile.

**Gegen das Transkript** prüft dasselbe Gate in der Codierphase: Steht die
geglättete Äußerung im Ausgangsmaterial, oder wurde ein inhaltstragender Begriff
ersetzt? Dafür dient `zitat_roh` als Pflichtfeld, ergänzt um die optionalen
Zeichenoffsets. Beide Richtungen laufen, Codierung gegen Transkript und Dokument
gegen Codierung. Die Richtung gegen das Transkript ist ein
**Agentendurchgang**, kein Skriptlauf: Sie ist in `SKILL.md` Schritt 2 angewiesen
und gilt pfadunabhängig, im Standardpfad wie im Ultracode-Pfad. Bezugsfassung der
Offsets, Pflichtfeld und Statussemantik stehen in `codierung.md` Abschnitt 10.

**Zwei Gutzustände, zwei Alarmzustände.** Die vier Status sind keine Skala von
gut nach schlecht. `VERIFIED` heißt wortgleiche Übernahme; `SMOOTHING_OK` ist der
**erwartete Gutzustand geglätteter Einheiten** und bei automatisch erzeugten
Transkripten der Regelfall, weil praktisch jeder Satz Füllwörter oder Abbrüche
enthält. Die Befunde des Gates sind `DRIFT` und `NOT_FOUND`. Ein Protokoll ohne
`VERIFIED` ist deshalb kein Mangel; eines ohne `DRIFT` und `NOT_FOUND` ist das
Ziel.

## 3. Zähl-Gate

**Jede Zahl im Ergebnisdokument wird aus der Arbeitsmappe neu berechnet und
gegengeprüft. Keine Zahl wird getippt.**

| Prüfung | Regel |
|---|---|
| Zählzeilen | `X von N Personen (a +, b -, c o, d >)` gegen Ebene 3 der Aggregation, distinkte Kennungen je Kategorie und Bewertung |
| Plausibilität | `max(a, b, c, d) ≤ X ≤ N` in jeder Zählzeile |
| Unterthemen | jede `X von N`-Angabe im Management Summary ≤ Personenzahl ihrer Kategorie |
| Gesamtzahl Äußerungen | dokumentweit identisch und gleich der Zeilenzahl in `Aussagen` |
| Stichprobe | N und Gruppengrößen gleich der Registry, Registry gleich dem Pseudonymschlüssel |
| Bezugsgröße | einheitliche Schreibweise `X von N Personen` im ganzen Dokument, nicht „9 Personen“ neben „9 von 14“ neben „(11 von 14 Personen)“ |
| Zähleinheit | jede Zahl deklariert, ob sie Personen oder Äußerungen zählt; Äußerungszahlen nur an den zwei zugelassenen Stellen |
| Prozent | keine Prozentangaben außer solchen, die die Befragten selbst genannt haben |

**Zwei deklarierte Ausnahmen von der einheitlichen Bezugsgröße.** Sie sind
legitim und werden als Warnung geführt, nicht als Fehler:

| Ausnahme | Kennzeichen | typischer Ort |
|---|---|---|
| Gruppen-Bezugsgröße | der Nenner entspricht der Größe einer Perspektivgruppe der Registry, **und** der Gruppenname steht im Umfeld der Stelle, etwa in der Abschnittsüberschrift | nach Gruppen aufgeschlüsselte Tabellen der Prozessnotiz |
| Zahlen des früheren Standes | das Wort „Delta“ im Folientitel oder in der Abschnittsüberschrift | Delta-Folie, Delta-Abschnitt der Prozessnotiz |

Die Delta-Ausnahme hängt **nicht** am Nenner. Eine Neucodierung nach Checkpoint
C1 ordnet alle Einheiten neu zu und ändert damit die Bewertungszahlen, ohne dass
N sich ändert; die alte Zählzeile trägt dann dasselbe N und trotzdem andere
Zahlen. Im Delta-Kontext wird jede Zählzeile als Warnung geführt, gleiches N
eingeschlossen. Die Plausibilitätsprüfung `max(a, b, c, d) ≤ X ≤ N` bleibt auch
dort blockierend: Eine in sich unmögliche Zahl ist kein alter Stand, sondern ein
Rechenfehler.

Ohne diese Ausnahmen widersprächen sich die mitgelieferten Werkzeuge: Die
Gruppentabellen von `aggregate.py --group-by perspektive` nennen zwangsläufig
Gruppengrößen, und eine regelkonforme Delta-Folie nennt zwangsläufig alte Zahlen.

Das Gate ist deshalb wirksam, weil **alle** Übersichtszahlen aus dem Sheet
`Aussagen` exakt reproduzierbar sind. Generieren statt Tippen ist keine
Vorsichtsmaßnahme, sondern die einzige Methode, die zuverlässig stimmt.

## 4. Zahl-Text-Kongruenz-Lint

Der Lint, den fast jeder Prozess vergisst. **Beim mechanischen Zahlenupdate wird
die Ziffer ersetzt und der Satz drumherum nicht mitgelesen.**

Beispielhafter Fehler: Freigegeben war „Nur wenige wollen selbst mitplanen:
**2** von 12, **beide** aus der Fertigung.“ Nach dem Update auf N = 14 steht dort
„**3** von 14, **beide** aus der Fertigung.“ Der Satz ist jetzt falsch, obwohl die
Zahl stimmt.

Der Lint prüft im Umfeld jeder geänderten Ziffer:

| Klasse | Marker |
|---|---|
| Zahlwörter | beide, alle drei, zu zweit, ein einziger, die eine, das Paar |
| Numerus | Singular gegen Plural am Verb und am Substantiv |
| Vollständigkeitsaussagen | „keine Gegenstimme“, „ausnahmslos alle“, „niemand“ |
| Exklusivität | „die einzige Gruppe“, „als einziger“, „nur eine Stimme“ |
| Anteilswörter | „nahezu alle“, „die große Mehrheit“ |

Bei jedem Treffer meldet der Lint die Fundstelle mit Kontext zur menschlichen
Entscheidung. Er formuliert nicht um.

Nach jedem Datenupdate laufen Zähl-Gate und Kongruenz-Lint gemeinsam.

## 5. Anonymisierungs-Lint

Anonymisierung ist ein prüfbarer Lauf über **alle** Artefakte, keine Haltung.
Er läuft über Arbeitsmappe, Ergebnisdokument, Prozessnotiz und jeden Anhang.

**Denylist, blockierend.** Aus dem Pseudonymschlüssel und den Stichprobeninfos
wird eine Liste realer Namen, Orte, Einheiten- und Projektbezeichnungen gebildet.
Ein Grep über alle Artefakte muss **null Treffer** liefern.

Die Denylist entsteht **in Schritt 1**, zusammen mit dem Pseudonymschlüssel, und
wird beiden Skripten als `--denylist` übergeben. Ohne sie entfällt der
blockierende Abgleich; `build_workbook.py` und `validate_deliverables.py` melden
das dann ausdrücklich als „Denylist-Gate nicht geprüft“, statt still zu passieren.

**Kandidatenliste, zur menschlichen Entscheidung.** Diese Muster sind nicht
automatisch falsch, aber jedes einzelne ist zu prüfen:

| Kandidat | Beispiel | Warum riskant | Empfohlener Umgang |
|---|---|---|---|
| Beschäftigten-, Umsatz- und Standortzahlen | „die 200 Kolleginnen und Kollegen [im anderen Werk]“ | eine Zahl identifiziert den Bereich | generalisieren: „die anderen Beschäftigten“ |
| einmalig besetzte Funktionen | „[die Leitung der Arbeitsvorbereitung] sagt, …“ | eindeutig zuordenbar | Zitat streichen oder Funktion tilgen |
| Handlungszuschreibung im Aktiv an eine identifizierbare Rolle | „dass [ein Mitglied der Geschäftsleitung] das gezeigt hat“ | benennt den Akteur | ins Passiv setzen: „dass das gezeigt wurde“ |
| Possessivpronomen | „meine Abteilung“, „bei uns im Bereich“ | verrät die Rolle der sprechenden Person | Artikel statt Possessivum: „die Abteilung“ |
| Ebenen-Deiktika | „auf unserer Ebene“ | verortet die Person in der Hierarchie | „auf der oberen Führungsebene“ |
| regionsgebundene Instrumente und Projektnamen | | Rückschluss auf die Einheit | generalisieren |
| Gruppenangabe bei kleiner Gruppe | Perspektivgruppe mit weniger als drei Personen | re-identifizierend | Gruppenangabe weglassen |

**Konventionen, einmal festlegen und im Dokument erklären:** eckige Klammern für
Hinzufügungen und Ersetzungen, Auslassungszeichen für Kürzungen im
Ergebnisdokument. Wiederkehrende Ersetzungen wörtlich identisch halten. Die
Ersetzungen fließen in die Arbeitsmappe zurück, die Kürzungen nicht.

**Macht die Anonymisierung ein Zitat unverständlich, wird es gestrichen, nicht
verstümmelt.**

**Retroaktive Bereinigung.** Wird bei einer Systemrevision eine Lücke entdeckt,
werden **alle** bereits codierten Einheiten nachbereinigt, nicht nur die neuen.

**Restrisiko benennen.** Bei kleinen, strukturell erkennbaren Gruppen bleibt ein
Re-Identifikationsrisiko auch ohne Namen. Das gehört als Limitation ins Dokument.

## 6. Konsistenz-Checks über alle Artefakte

Diese Prüfungen fangen die Fehlerklasse, die weder Zitat- noch Zahlenfehler im
engen Sinn ist, und die deshalb regelmäßig unentdeckt bleibt.

**[S]** heißt: `scripts/validate_deliverables.py` prüft den Punkt.
**[A]** heißt: Der Agent prüft ihn selbst; das Skript sieht ihn nicht.
Die Kennzeichnung ist wichtig, weil C3 als „Maschine meldet“ definiert ist. Ein
Punkt, den niemand ausdrücklich übernimmt, fällt sonst zwischen beide.

- [ ] **[S] Gesamtzahlen dokumentweit identisch.** Jede in irgendeinem Artefakt
      genannte Gesamt- oder Kategorienzahl wird gegen die Arbeitsmappe geprüft:
      Rahmenfolie, Trennfolien, Detailfolien, Sheets, Prozessnotiz. Ein alter
      Wert auf einer Trennfolie ist der typische Fund.
- [ ] **[S] Kategoriennamen zwischen Überblick und Detail wörtlich identisch.**
      Zwei Namen für dieselbe Kategorie im selben Dokument sind ein häufiger
      Rest von Umbenennungen.
- [ ] **[S] Umbenennungen sind überall vollzogen.** Ein Glossar mit allen
      verbindlichen Begriffen, früh fixiert, wird über alle Artefakte gelintet
      (`--glossar`). Eine Umbenennung nur im Ergebnisdokument lässt die
      Datenbasis inkonsistent.
- [ ] **[S] Jede Registry gegen die Primärquelle gegengeprüft**, insbesondere die
      Perspektivgruppen-Registry gegen den Pseudonymschlüssel (`--key`). Ohne
      Gegenprüfung driftet sie; bleibt `--key` weg oder fehlt dort die Spalte
      `Perspektivgruppe`, meldet das Protokoll „Registry-Gegenprüfung nicht
      durchgeführt“.
- [ ] **[A] Folientitel und Folieninhalt decken dieselben Kategoriennummern ab.**
      Trägt die Folie ihre Kategorien-IDs als Metadatum, wäre das maschinell
      prüfbar; das Skript prüft es derzeit nicht.
- [ ] **[S] Beide Instanzen der Kategorienüberblicksfolie zeichengleich.**
- [ ] **[A] Version und Stand konsistent** zwischen Dateiname, Sheet `Info` und
      Titelfolie. Dateiname gegen `Info` prüft `build_workbook.py`; die Titelfolie
      liest der Agent.
- [ ] **[S] Keine abgebrochenen Sätze, keine unfertigen Karten.** Eine Karte, die
      mit einem Doppelpunkt endet und die angekündigte Aufzählung nicht bringt,
      ist ein Fund. **[A]** bleibt der optisch abgeschnittene Text, den erst der
      Blick auf die Folie zeigt.
- [ ] **[S] Typografie:** Anführungszeichen paarig, keine doppelten öffnenden
      Anführungszeichen, keine doppelten Leerzeichen, keine Gedankenstriche,
      Binnenzitate in `‚…‘`, Guillemets als Befund. **[A]** bleibt: kein Zitat
      ohne Anführungszeichen im Zitatblock.
- [ ] **[A] Rückfluss vollzogen:** Jede Änderung am Ergebnisdokument, die den
      **Wortlaut** einer Äußerung betrifft, steht in der Arbeitsmappe. Kürzungen
      mit `…` gehören ausdrücklich nicht dazu. Das Skript weist die betroffenen
      Zitate als `SMOOTHING_OK` mit der jeweiligen Konsequenz aus; ob der
      Rückfluss vollzogen wurde, entscheidet der nächste Lauf.

## 7. Wortlaut-Sperre nach Freigabe

**Nach der ersten Freigabe durch den Auftraggeber oder die verantwortlichen
Berater ändert ein Datenupdate ausschließlich:**

- Zahlen,
- Tippfehler,
- nachweislich falsche Tatsachenaussagen.

**Neue Erkenntnisse aus neuem Material kommen als separate, ausgewiesene
Ergänzung, nie als Umformulierung.** Freigegebene Prosa neu zu schreiben, weil
die Datenbasis gewachsen ist, ist der teuerste vermeidbare Fehler des gesamten
Verfahrens: Die Neuformulierung schleppt regelmäßig neue, sachlich riskantere
Behauptungen ein, die nie jemand freigegeben hat, und die ganze Runde muss
zurückgerollt werden.

**Praktische Umsetzung:**

1. Freigegebene Textstände als Referenzdatei ablegen.
2. Bei jedem neuen Stand einen Diff gegen die Referenz mitliefern
   (`validate_deliverables.py --baseline`).
3. Jede Prosaänderung einzeln begründen. Änderungen ohne Begründung sind Fehler,
   nicht Verbesserungen.

## 8. Die drei Checkpoints

| | Wann | Wer | Inhalt |
|---|---|---|---|
| **C1** | nach der Wahl der Berichtsgliederung | **Mensch entscheidet** | Freigabe der Berichtsgliederung. Der Skill legt höchstens drei Varianten vor, jeweils mit Personenabdeckung je Kategorie. Das ist eine Beratungsentscheidung und wird nicht automatisiert. Danach werden alle Einheiten neu codiert, mit dokumentiertem Mapping. |
| **C2** | nach dem ersten vollständigen Ergebnisdokument | **Mensch redigiert** | Redline durch die verantwortlichen Berater. Der Skill liefert das Dokument mit Änderungsmarkierung oder in diff-fähiger Form aus, damit die Redline nachvollziehbar bleibt. |
| **C3** | nach **jeder** Redline | **Maschine meldet** | Nachlese: Typografie, Anführungszeichen-Paarung, abgebrochene Sätze, doppelte Leerzeichen, Zahl-Text-Kongruenz, neue Anonymisierungslücken, neue Zitatabweichungen. Die Nachlese **formuliert nichts um**. |

**Diff-fähige Form einer `.pptx`** ist ein Folientext-Export als Markdown: je
Folie eine Überschrift `## Folie <Nummer>`, darunter die Absätze in
Folienreihenfolge. Diese Datei wird neben der `.pptx` ausgeliefert, dient der
Redline als Vergleichsgrundlage und wird beim nächsten Stand als `--baseline`
wiederverwendet. Die Wortlaut-Sperre vergleicht Absatz gegen Absatz und meldet
beide Richtungen: geänderte und **entfernte** Absätze.

C3 ist unverzichtbar, weil menschliche Eingriffsrunden eigene Defekte erzeugen,
die danach niemand mehr liest: doppelte öffnende Anführungszeichen, ein Zitat
ohne Anführungszeichen mitten im Block, ein Satz, der mitten im Wort abbricht,
ein neu eingeschleppter Tippfehler.

Nach C3 wird eine **Kennzahlentabelle als Prüfprotokoll** neben dem Dokument
ausgeliefert: Was wurde geprüft, mit welchem Ergebnis, welche Warnungen bleiben
offen.

## 9. Skript

`scripts/validate_deliverables.py` führt die mit **[S]** gekennzeichneten Gates
dieses Dokuments artefaktübergreifend aus. Die mit **[A]** gekennzeichneten
Punkte bleiben beim Agenten; das Skript ersetzt sie nicht. Die workbook-internen
Struktur- und Feldprüfungen laufen in `build_workbook.py` und sind in
`excel-output.md` beschrieben.

### Die beiden Modi

Das Skript kennt zwei Aufrufformen. Die Begriffe stehen so im Prüfprotokoll, in
`--help` und hier:

| Modus | Aufruf | Was läuft |
|---|---|---|
| **Modus A** | nur `--workbook` | die Arbeitsmappe gegen sich selbst: Sheetfolge, Wertebereiche, Dubletten, die aus dem Sheet `Aussagen` neu berechnete Auszählung gegen die geschriebene, Pflichtzeilen des Info-Sheets, Registry. Mit `--denylist` zusätzlich der Anonymisierungs-Lint auf `Aussagen`, mit `--key` die Registry-Gegenprüfung. |
| **Modus B** | `--workbook` plus `--deck` oder `--report` | zusätzlich jede Zahl und jedes Zitat der Endartefakte gegen die Arbeitsmappe. Erst hier greifen Zitat-Gate, Kongruenz-Lint, der Dokumentteil des Zähl-Gates und der Dokumentteil des Konsistenz-Gates. |

**Modus A ist eine Mappenprüfung, keine Vollprüfung.** Ohne Endartefakt haben
die artefaktgebundenen Gates kein Prüfobjekt und liefern zwangsläufig null
Befunde; ein grüner Lauf in Modus A sagt nichts über das Ergebnisdokument. Das
Protokoll führt deshalb am Ende jedes Laufs einen Abschnitt **Nicht geprüft**,
der die ausgefallenen Gates und den fehlenden Eingabeparameter benennt, etwa
„Zitat-Gate: nicht anwendbar ohne --deck oder --report“. Dieselbe Liste steht als
`nicht_geprueft` im JSON-Prüfprotokoll. Der Grundsatz aus Abschnitt 1 gilt auch
für das Protokoll selbst: Ein grün protokolliertes Gate, das nichts geprüft hat,
ist gefährlicher als gar keines.

```bash
python3 scripts/validate_deliverables.py \
  --workbook  "Codierung_P01-P14_260315_v3.xlsx" \
  [--deck     "Auswertung_v4.pptx"] \
  [--report   "Zwischenstand_260315.md"] \
  [--denylist VERTRAULICH_klarnamen.txt] \
  [--key      VERTRAULICH_Pseudonym_Schluessel_260315.md] \
  [--glossar  glossar.json] \
  [--zitatregistry zitatregistry.json] \
  [--baseline "Auswertung_v3_freigegeben.pptx"] \
  [--gate zitat|zaehl|kongruenz|anonym|konsistenz|wortlaut|alle] \
  [--json     pruefprotokoll.json]
```

| Option | Wirkung |
|---|---|
| `--workbook` | Pflicht; die Arbeitsmappe ist die Referenz für alle Vergleiche |
| `--deck`, `--report` | zu prüfende Endartefakte; für `zitat`, `kongruenz` und `wortlaut` ist mindestens eines Pflicht |
| `--denylist` | Klarnamen, Orte, Einheiten; ein Treffer ist blockierend |
| `--key` | Pseudonymschlüssel für Registry-Gegenprüfung und Quellenart-Regel; Format siehe `codierung.md` Abschnitt 2 |
| `--glossar` | verbindliche Begriffe und Kategoriennamen für den Umbenennungs-Lint |
| `--zitatregistry` | beim Bauen notierte Quellzeile je Zitat; prüft den Fuzzy-Match gegen die deklarierte Zeile |
| `--baseline` | freigegebener Stand; aktiviert die Wortlaut-Sperre und meldet jede Prosaänderung außerhalb von Zahlen und Tippfehlern, auch entfernte Absätze |
| `--gate` | einzelnes Gate statt aller, Default `alle` |
| `--json` | maschinenlesbares Prüfprotokoll zusätzlich zum stdout-Bericht |

Ausgabe: je Gate eine Tabelle mit Fundstelle, Status und Ähnlichkeitswert, dazu
die Kennzahlentabelle als Prüfprotokoll. Exit-Code ungleich null, sobald ein
blockierender Verstoß vorliegt (`NOT_FOUND`, `DRIFT`, Zitat-Splicing,
Denylist-Treffer, Zahlenabweichung, Zählzeile außerhalb `max(a,b,c,d) ≤ X ≤ N`,
Registry gegen Pseudonymschlüssel). Kandidatenlisten des Anonymisierungs-Lints
und Kongruenz-Treffer sind Warnungen zur menschlichen Entscheidung, kein Abbruch.

**Exit-Code 2 bei Bedienfehlern.** Dazu zählt ausdrücklich ein artefaktgebundenes
Gate ohne Artefakt: `--gate zitat`, `kongruenz` oder `wortlaut` ohne `--deck` und
`--report`, sowie `--gate wortlaut` ohne `--baseline`. Ein grün protokolliertes
Gate, das nichts geprüft hat, ist gefährlicher als gar keines.
