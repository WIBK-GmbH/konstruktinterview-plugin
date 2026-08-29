# Kategoriensystem

Aufbau, Satzmuster und Entwicklungspfad des Kategoriensystems. Beispiele stammen
aus dem Übungsfall *Firma M.*, einem Möbelhersteller, der seine Fertigung an
einen zweiten Standort verlagert.

## Inhalt

1. [Genau zwei Ebenen](#1-genau-zwei-ebenen)
2. [Definition schreiben](#2-definition-schreiben)
3. [Ankerbeispiel](#3-ankerbeispiel)
4. [Codierregel](#4-codierregel)
5. [MECE-Prüfung](#5-mece-prüfung)
6. [Keine Stärken/Schwächen-Hauptkategorien](#6-keine-stärkenschwächen-hauptkategorien)
7. [Schritt 3a: Analysesystem](#7-schritt-3a-analysesystem)
8. [Schritt 3b: Berichtssystem](#8-schritt-3b-berichtssystem)
9. [Fortschreibung bei wachsender Datenbasis](#9-fortschreibung-bei-wachsender-datenbasis)
10. [Optionale Verfahren](#10-optionale-verfahren)

---

## 1. Genau zwei Ebenen

Das System hat **genau zwei Ebenen**, keine dritte Differenzierungsebene.

| Ebene | Nummer | Zeilentyp im Sheet | Felder |
|---|---|---|---|
| Hauptkategorie | `1.`, `2.`, `3.` | Oberkategorien-Zeile, fett, grau hinterlegt | Nummer, Bezeichnung, Definition. **Kein** Ankerbeispiel, **keine** Codierregel |
| Unterkategorie | `1.1.`, `1.2.`, … | normale Zeile | Nummer, Bezeichnung, Definition, Ankerbeispiel, Codierregel (alle drei Pflicht) |

**Codiert wird ausschließlich auf Unterkategorienebene.** Eine Hauptkategorien-
nummer erscheint nie in der Spalte `Kategorie` des Sheets `Aussagen` und nie im
Sheet `Auszählung`.

Beispiel für den Übungsfall:

```
1.  Anlass und Ausgangslage
    1.1  Gründe für die Verlagerung
    1.2  Erwartete Folgen für die eigene Arbeit
2.  Zusammenarbeit während der Verlagerung
    2.1  Information über den Stand des Vorhabens
    2.2  Einbindung der Belegschaft
3.  Verlagerung im Betriebsalltag
    3.1  Rolle der direkten Vorgesetzten
    3.2  Umgang mit dem Terminplan
```

**Nummernformat.** Zweistellige Unterkategoriennummern (`2.10`) vermeiden, sonst
bricht die numerische Sortierung und Tabellenkalkulationen kollabieren `2.10` zu
`2.1`. Lieber eine weitere Hauptkategorie öffnen.

## 2. Definition schreiben

**Hauptkategorie.** Ein Scope-Satz, der konventionell mit „Oberkategorie für …“
beginnt.

```
Oberkategorie für alles, was die Befragten über Anlass, Vorgeschichte und
Ausgangsbedingungen der Verlagerung sagen.
```

**Unterkategorie.** Ein Satz oder eine Satzgruppe, die den Gegenstandsbereich
benennt, gefolgt von einer **Facettenklammer** in runden Klammern, die die
typischen Themen der Kategorie aufzählt.

Muster: `<Gegenstandsbereich> (<Facette>, <Facette>, <Facette>, …).`

```
Aussagen darüber, wie die Befragten vom Stand des Vorhabens erfahren und wie sie
diesen Weg bewerten (Betriebsversammlung, Aushang, Weitergabe über Vorgesetzte,
informelle Wege, Aktualität und Verlässlichkeit der Information).
```

Die Facettenklammer macht die Kategorie für Codierende operationalisierbar und
dokumentiert zugleich, was induktiv aus dem Material aufgetaucht ist. Länge der
Definition: 120 bis 390 Zeichen.

## 3. Ankerbeispiel

Ein einziges Zitat in deutschen typografischen Anführungszeichen `„…“`, 120 bis
180 Zeichen.

**Variante B ist Default:** eine **reale, mit `*` markierte Codiereinheit** aus
dem Sheet `Aussagen`, wörtlich übernommen, mit Kennung in Klammern.

```
„Der Aushang hängt manchmal zwei Wochen, und wenn ich ihn lese, ist er schon
wieder überholt.“ (P06)
```

Nur so ist das Ankerbeispiel im Sinne Mayrings nachprüfbar im Material verankert.

**Variante A** ist ein konstruiertes Prototypzitat im O-Ton-Register ohne
Kennungsangabe, das mehrere Facetten der Definition bündelt. Sie ist zulässig,
methodisch aber schwächer. Wird sie gewählt, **muss** im Sheet `Info` eine Zeile
`Ankerbeispiele:` stehen, die das kenntlich macht, damit das konstruierte Zitat
nicht für ein echtes gehalten wird.

**In keinem Fall** enthält ein Ankerbeispiel eckige Klammern. Wo Anonymisierung
nötig wäre, wähle ein anderes Ankerbeispiel.

## 4. Codierregel

**Satz 1, verbindliches Muster:**

```
Hier codieren, wenn <Bedingung>.
```

**Satz 2, wo nötig, explizite Abgrenzung.** Drei erprobte Formulierungen:

| Muster | Beispiel |
|---|---|
| `Abgrenzung zu <X.Y>: <X.Y> behandelt <…>.` | `Abgrenzung zu 2.2: 2.2 behandelt die aktive Mitwirkung, nicht das bloße Erfahren.` |
| `<Gegenstand> gehört zu <X.Y>.` | `Kritik an einzelnen Vorgesetzten gehört zu 3.1.` |
| `Bei <Bedingung> hat <X.Y> Vorrang.` | `Nennt die Äußerung zugleich einen Terminwunsch, hat 3.2 Vorrang.` |

Vollständiges Beispiel für `2.1`:

```
Hier codieren, wenn die Äußerung den Weg, die Aktualität oder die
Verlässlichkeit von Informationen über das Vorhaben betrifft. Abgrenzung zu 2.2:
2.2 behandelt die aktive Mitwirkung an Entscheidungen, nicht das Erfahren von
Ergebnissen. Bewertungen einzelner Vorgesetzter gehören zu 3.1.
```

Die Vorrangregel ist der Mechanismus, mit dem die MECE-Eigenschaft durchgesetzt
wird. Für **jedes** Kategorienpaar mit erkennbarem Überlappungsrisiko muss eine
Abgrenzung oder Vorrangregel formuliert sein.

### Regel A: Sache und Kommunikation über die Sache brauchen einen Vorrang

Die häufigste stille Fehlzuordnung entsteht nicht zwischen weit entfernten
Kategorien, sondern zwischen **inhaltlich benachbarten Paaren**: dem Inhalt einer
Sache und der Kommunikation oder dem Prozess derselben Sache. Im Übungsfall trennt
`2.1` das **Erfahren** vom Stand der Verlagerung und `2.2` die **Mitwirkung** an
Entscheidungen darüber. Eine Aussage über die Form eines Aushangs erfüllt beide
Beschreibungen: Sie handelt vom Informationsweg und zugleich davon, wie die
Belegschaft eingebunden wird.

Solche Paare erkennt man daran, dass sich dasselbe Substantiv in beiden
Definitionen wiederfindet. Für jedes von ihnen gehört eine ausdrückliche
Vorrangregel in mindestens eine der beiden Codierregeln:

```
Bei Aussagen über Form, Länge oder Verständlichkeit einer Mitteilung hat 2.1
Vorrang; 2.2 greift erst, wenn die Äußerung die Beteiligung an der Entscheidung
selbst betrifft.
```

Ohne diese Regel entscheidet der Zufall der Formulierung, und zwei Codierende
ordnen dieselbe Passage verschiedenen Hauptkategorien zu. Die Gates fangen das
nicht ab: Sie prüfen Zitattreue, nicht Kategorienplausibilität.

### Regel B: keine markanten Einzelmetaphern in Definition und Codierregel

Definitionen und Codierregeln übernehmen **keine markante Einzelmetapher aus
einer konkreten Äußerung**. Eine bildhafte Wendung, die einmal gefallen ist,
klingt in einer Definition prägnant und zieht danach jede Äußerung an, die
dasselbe Bild benutzt, gleich in welcher Sache sie steht.

Im Übungsfall sagt eine befragte Person, der Verlagerungsplan sei „am Reißbrett
entstanden“. Wandert das Bild in die Codierregel, zieht es fortan jede Äußerung
an, in der ein Reißbrett vorkommt, auch die über die Konstruktionsabteilung:

| | |
|---|---|
| Schlecht | `Hier codieren, wenn von Planung am Reißbrett die Rede ist.` |
| Gut | `Hier codieren, wenn die Äußerung die Distanz zwischen planender und ausführender Stelle betrifft.` |

Die Metapher gehört ins **Ankerbeispiel**, wo sie als Zitat kenntlich ist und
nichts anzieht. Die Definition benennt den Gegenstandsbereich in der Sprache der
Sache.

## 5. MECE-Prüfung

Das System ist überschneidungsfrei und erschöpfend, wenn gilt:

- [ ] Jede Codiereinheit passt in genau eine Unterkategorie als Hauptzuordnung.
- [ ] Jedes Kategorienpaar mit Überlappungsrisiko trägt eine Abgrenzung oder
      Vorrangregel in mindestens einer der beiden Codierregeln.
- [ ] Keine Kategorie ist leer. Eine leere Kategorie bedeutet: System überarbeiten.
- [ ] Keine Kategorie hat weniger als drei verschiedene Kennungen. Sonst liegt
      eine Einzelmeinung vor, die keine eigene Kategorie rechtfertigt.
- [ ] Kein Material bleibt unzugeordnet, weil keine Kategorie passt. Dann fehlt
      eine Kategorie.
- [ ] Jeder Kategorienname schließt an die Sprache der Befragten an.

**Residualkategorie.** Eine Restkategorie („nicht eindeutig zuordenbar“) ist
ausschließlich als **temporäres Arbeitsmittel** während der Codierung zulässig.
Sie muss vor der Auswertung aufgelöst sein: entweder passen die Einheiten doch in
bestehende Kategorien, oder es fehlt eine Kategorie.

Mehrfachcodierung derselben Textstelle in **verschiedenen** Kategorien ist eine
bewusste Ausnahme und erlaubt. Überlappende Spans in **derselben** Kategorie sind
Duplikate und werden zusammengeführt.

## 6. Keine Stärken/Schwächen-Hauptkategorien

Verwende **keine** Gliederung nach Stärken gegen Schwächen, Chancen gegen
Risiken oder positiv gegen negativ als Hauptkategorien. Befragte bewerten
dasselbe Thema unterschiedlich; eine solche Gliederung zerreißt das Thema und
macht Dissens unsichtbar.

Stattdessen: **thematische Kategorien bilden, Bewertung als orthogonales Attribut
je Äußerung führen.** Erst diese Trennung erlaubt die zentrale Aussageform des
Ergebnisdokuments, nämlich Gemeinsamkeiten und Unterschiede innerhalb desselben
Themas gegenüberzustellen.

## 7. Schritt 3a: Analysesystem

Das Analysesystem entsteht **induktiv aus dem Material**, nah an den Daten.
Deduktive Ableitung aus Theorie und Ableitung aus den Leitfragen sind nur
ergänzend zulässig.

Vorgehen:

1. Beginne mit zwei bis drei Interviews, nicht mit allen.
2. Bilde erste Kategorien aus leicht fassbaren Aussagen.
3. Erweitere schrittweise durch Hinzunahme weiterer Interviews.
4. Revidiere in höchstens **zwei** Durchgängen. Stößt die Recodierung auf
   Material, das nicht passt, schärfe das **System** nach, statt das Material ins
   bestehende System zu pressen. Dann terminiere.

**Harte Gates:**

- höchstens 5 Unterkategorien je Hauptkategorie
- keine Stärken/Schwächen-Kategorien
- keine dauerhafte Restkategorie
- keine Klarnamen in Kategoriennamen, Definitionen oder Ankerbeispielen

**Größenobergrenze.** Ein feingliedriges Analysesystem darf breiter werden als
ein Berichtssystem, aber jenseits von etwa 20 Unterkategorien wächst der
Abgrenzungsapparat schneller als der Erkenntnisgewinn. Notiere bei jeder
Erweiterung, welcher konkrete Fall sie ausgelöst hat.

## 8. Schritt 3b: Berichtssystem

**Die zentrale Trennung dieses Skills.** Ein methodisch sauberes, feingliedriges
induktives System ist ein gutes *Analyse*-Instrument und ein schlechtes
*Berichts*-Instrument. 40 oder 50 Unterkategorien lassen sich nicht in ein
Managementdokument überführen. Der Übergang ist ein eigener Arbeitsschritt und
wird bewusst geplant, nicht spät und ungeplant vollzogen.

| | Analysesystem (3a) | Berichtssystem (3b) |
|---|---|---|
| Zweck | Material erschließen | Befunde vermitteln |
| Herkunft | induktiv aus dem Material | vom Erkenntnisinteresse des Auftraggebers her gegliedert |
| Form | hierarchisch, feingliedrig | flach, zwei Ebenen |
| Größe | bis etwa 20 Unterkategorien | 3 bis 4 Hauptkategorien, 10 bis 15 Unterkategorien |
| Namen | Sprache der Befragten | Fragen des Auftrags, anschlussfähig für die Leitungsebene |
| Entscheidung | Auswerter | **Mensch, Checkpoint C1** |

**Ablauf des Übergangs:**

1. Lege dem User **höchstens drei** Gliederungsvarianten vor, jeweils mit der
   Personenabdeckung je vorgeschlagener Kategorie aus der bisherigen Auszählung.
2. Der Mensch wählt oder setzt das System selbst. Das ist eine
   Beratungsentscheidung.
3. Definiere die gewählten Kategorien aus: Definition, Ankerbeispiel, Codierregel
   je Unterkategorie nach den Mustern oben.
4. **Codiere alle Einheiten neu** gegen das gewählte System. Die Neucodierung
   erfolgt durch inhaltliches Urteil, nie durch ein Mapping-Skript, das Bedeutung
   errät.
5. Dokumentiere das **Mapping alt zu neu** je Kategorie mit Begründung. Keine
   Einheit fällt stillschweigend weg.

**Verdichtung nach dem Zählen.** Kategorien mit auffällig geringer
Personenabdeckung, etwa unter einem Viertel der Stichprobe, schlägst du zur
Zusammenlegung mit einer sachlich benachbarten Kategorie vor. Auslöser ist die
Auszählung, nicht die Definition. Umbenennungen und Zusammenlegungen fließen in
**alle** Artefakte zurück, nicht nur in das Ergebnisdokument.

## 9. Fortschreibung bei wachsender Datenbasis

Kommen weitere Interviews hinzu:

1. Bestehende Arbeitsmappe laden. Bestehende Codierung bleibt gültig.
2. Neue Interviews nach dem Standardpfad codieren, Kennungen nur ergänzen.
3. Kategoriensystem **nachschärfen**, nicht neu erfinden. Ein Systemwechsel ist
   teuer: er zwingt zur Neucodierung des gesamten Materials.
4. Bei Kategorienänderung ein **Mapping alt zu neu** mit Begründung je Zuordnung
   protokollieren und alle bestehenden Einheiten umcodieren.
5. **Alle** abgeleiteten Sheets neu berechnen, nie fortschreiben. Ein stehen
   gebliebenes Auszählungsblatt aus einem früheren Stand ist ein typischer und
   schwer zu entdeckender Fehler.
6. Optional eine Delta-Zusammenfassung erzeugen: was hat sich an der Datenbasis
   geändert, wo haben sich Schwerpunkte verschoben, wo haben sich Befunde
   qualitativ zugespitzt.
7. **Wortlaut-Sperre beachten:** Ist ein Stand freigegeben, ändert das
   Datenupdate nur Zahlen, Tippfehler und nachweislich falsche
   Tatsachenaussagen (siehe `gates.md`).

**Ankerbeispiele bei übernommenem Kategoriensystem.** Wird ein bestehendes
System übernommen oder fortgeschrieben, stammen seine Ankerbeispiele aus dem
Material früherer Interviews und stehen nicht im `*`-Pool der neuen Mappe. Der
Modus `real` verlangt genau das und warnt sonst je Kategorie. Zwei zulässige
Wege:

1. **Reale Anker aus dem neuen Material setzen.** Der methodisch stärkere Weg:
   je Kategorie eine `*`-markierte Codiereinheit der aktuellen Erhebung, wörtlich
   übernommen, mit Kennung in Klammern.
2. **Modus `prototyp` wählen** (`--anchor-mode prototyp`). Dann sind die Anker
   ausdrücklich als konstruiert deklariert, und die Zeile `Ankerbeispiele:` im
   Sheet `Info` macht das kenntlich.

Die übernommenen Fremdanker einfach stehen zu lassen, ist kein dritter Weg: Sie
sind weder real im Sinne dieser Mappe noch als konstruiert deklariert, und die
Warnungen häufen sich bis zur Unlesbarkeit des Prüfberichts.

**Zwischenstände je Welle.** Solange nur ein Teil der Interviews codiert ist, hat
ein übernommenes Kategoriensystem fast immer unbesetzte Kategorien. Der
Zwischenstand wird deshalb mit `build_workbook.py --teilbestand` gebaut; das
Kategoriensystem bleibt vollständig und wird nicht beschnitten. Der Vollabschluss
läuft ohne das Flag.

## 10. Optionale Verfahren

**Kategoriensystem-Wettbewerb.** Drei unabhängige Entwürfe treten an
(sequenziell-induktiv, globales Clustering, Revision eines Vorentwurfs), ein
Richter bewertet nach einer Rubrik mit Trennschärfe, Vollständigkeit, Kohärenz,
Struktur, induktiver Bodenhaftung und Nutzen für den Verwendungszweck, und muss
für jedes Urteil konkrete Einheiten-Indizes als Beleg nennen. Vorgeschaltet sind
die harten Gates aus Abschnitt 7.

*Timing-Regel:* Der Wettbewerb lohnt **einmal**, und zwar erst dann, wenn die
Stichprobe die Perspektivbreite abdeckt. Zu früh durchgeführt, bei einem Bruchteil
der geplanten Interviews, ist das Ergebnis wertlos, weil das System bei
vollständiger Datenbasis ohnehin ersetzt wird.

**Änderungsprotokoll je Revision.** Bei **jeder** Systemrevision Pflicht: eine
nummerierte Liste der Änderungen gegenüber der Vorversion, jeweils mit den
auslösenden Fällen, plus die Abschnitte „Hinweise und Grenzfälle“, „Offene
Fragen“ und „Limitationen“. Das Protokoll gehört in die Prozessnotiz.

**Adversariale Zitatprüfung.** Lohnt immer und läuft gegen jedes Artefakt.
Beschrieben in `gates.md`.
