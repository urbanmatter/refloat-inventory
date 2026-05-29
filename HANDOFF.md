# 📋 Projekt-Übergabe: ReFloat Inventory

> Diese Datei dient als Übergabe-/Wiedereinstiegspunkt. Inhalt kann in einen neuen Chat kopiert werden, um nahtlos weiterzuarbeiten.

## Rolle & Kontext
Du bist ein erfahrener Full-Stack-Entwickler und hilfst mir (Gründer in der Baubranche, **kein Entwickler**) beim Bau einer professionellen Web-App zur Erfassung und Verwaltung von **rückgebautem Flachglas** aus Gebäuderückbauten. Mein Team (2–10 Personen) erfasst Gläser, kategorisiert sie, stellt sie intern und für Kunden bereit und gleicht eingehende Anfragen gegen den Bestand ab. Die App läuft im Browser. **Erkläre Dinge einfach und sag direkt, wenn du dir unsicher bist.**

## Live-URL & Hosting
- **App online:** https://urbanmatter.github.io/refloat-inventory/
- **GitHub Repository:** https://github.com/urbanmatter/refloat-inventory (öffentlich, mit `robots.txt` von Suchmaschinen ausgeschlossen)
- **Hosting:** GitHub Pages (kostenlos, automatisch bei Push auf `main`)

## Technischer Stand
- **Eine einzige Datei:** `index.html` (HTML + CSS + JavaScript inline, ~150 KB)
- **Lokaler Speicherort:** `C:\Users\sebas\Desktop\Claude Projekte\ReFloat Inventory\`
- **Datenspeicher:**
  - **Primär:** Google Drive (`refloat-data.json`) — Team-Sync
  - **Cache/Fallback:** Browser `localStorage`, Key = `gdt_v1`
- **Fotos:** Einzelne JPEG-Dateien in Drive (gleicher Ordner wie JSON), Verknüpfung via Drive-File-ID
- **Externe Bibliotheken:** SheetJS (`xlsx-0.20.3`) via CDN, ausschließlich für Excel-Parsing / Vorlage-Download im Matching-Tab.
- **Umgebung:** Windows, Python 3.14 + Pillow 12.2 verfügbar
- **Vorschau-Server:** `.claude/launch.json` → Name `glass-static`, startet `python -m http.server 8777` (gapi/Drive funktioniert auf localhost nicht — API-Key ist HTTP-Referrer-restricted)

## Authentifizierung & Konfiguration
Alle Konstanten stehen ganz oben im `<script>`-Block in `index.html`:

| Konstante | Wert | Wo geändert |
|---|---|---|
| `APP_PASSWORD` | aktuell `'CHANGEME'` (Platzhalter) | Login-Block in JS |
| `DRIVE_API_KEY` | `AIzaSyDL1ZSe4DQcTlxe-4LCZGwcTSck6C5i3VQ` | Drive-Block (auf `https://urbanmatter.github.io/*` beschränkt) |
| `OAUTH_CLIENT_ID` | `383046788151-99h586mb9tmdup6aqsits1i3rgge4ena.apps.googleusercontent.com` | Drive-Block |
| `DRIVE_SCOPE` | `https://www.googleapis.com/auth/drive.file` | Restriktiv: nur App-erstellte oder via Picker gewählte Dateien |
| `DEMO_SEED_FLAG` | `'refloat_demo_seeded_v2'` | Matching-Block (Version hochzählen bei erneutem Demo-Bedarf) |

**Google Cloud:** Projekt „ReFloat Inventory", Drive API aktiviert, OAuth-Consent im Test-Modus mit Testnutzern. API-Key ist auf `https://urbanmatter.github.io/*` HTTP-Referrer beschränkt und auf Drive API limitiert.

## Dateien im Projektordner
| Datei | Zweck |
|---|---|
| `index.html` | Die komplette App |
| `robots.txt` | Disallow für alle Crawler |
| `ReFloat.ico` | Multi-Größen-Icon für Desktop-Verknüpfung (NICHT löschen) |
| `make_icon.py` | Erzeugt das Icon (violetter Verlauf, 2 Glasscheiben + Kreislauf-Pfeile) |
| `embed_icon.py` | Bettet das Icon als Base64 in `index.html` ein |
| `HANDOFF.md` | Diese Übergabe-Datei |
| `.claude/launch.json` | Preview-Server-Config |

- **Desktop-Verknüpfung:** `C:\Users\sebas\Desktop\ReFloat Inventory.lnk` → öffnet `index.html` (lokal), nutzt `ReFloat.ico`. Für Live-App: Browser-URL nutzen.

## Branding
- **Name:** „ReFloat Inventory", Untertitel „Datenbank für Zirkuläres Flachglas"
- **Icon** im Header, im Browser-Tab (Favicon), als Desktop-Icon und im PDF-Datenblatt sowie auf dem Login-Screen
- **Farben:** Primär `#5B4BE1` (Violett), Sekundär `#1E3A5F`, Akzent `#7C6EF0`, BG `#F8F8FC`, Karten `#FFF`, Text `#1A1A2E`, Subtext `#6B7280`, Rahmen `#E5E7EB`, Danger `#E5484D`. Radien: Karten 16px, Inputs 10px, Buttons 14px. System-Font, max. Inhaltsbreite 1400px, mobile-first (1 Spalte, 2 Spalten ab 600px).

## Funktionsumfang
### Landing Page / Startseite (Phase 5)
- **Beim App-Start landet der User auf `section-home`** mit Begrüßungstext und drei gestackten Tile-Buttons: **Übersicht** → `nav('list')`, **Neue Erfassung** → `newEntry()`, **Matching** → `nav('match')`.
- **Zurück zur Startseite:** Header-Button „🏠 Start" (`nav-home`) oder Klick aufs Logo (`hd-logo` ist `onclick="nav('home')"`).
- CSS-Klassen: `.home-hero` (zentrierte Begrüßung), `.home-tiles` (vertikaler Stack, max-width 720px), `.home-tile` (Card mit Icon-Quadrat links, Titel+Beschreibung mittig, Pfeil rechts, Hover hebt sich an).
- Keine Daten-Abhängigkeit — Landing Page funktioniert auch ohne Drive-Login.

### Erfassung & Verwaltung
- **Erfassung:** Projekt-Header (Gebäude, Adresse, Rückbaujahr) + beliebig viele **Glaspositionen** (P1, P2…) mit „+ Position hinzufügen" / „×" entfernen (mind. 1 Position).
- **Pro Position:** Glastyp, dynamischer **Glasaufbau** (je nach Typ), Farbe, Beschichtung (Kurzinfo), Breite/Höhe, automatische Glasdicke & Gewicht, Stückzahl, Lagerort, Preis, Status, R-Strategie, Tags, Notizen, Foto-Upload (Drag&Drop, automatisch komprimiert auf max. 900px / ~75% JPEG-Qualität).
- **Übersicht:** Tabellen- & Kartenansicht, Volltextsuche, Filter (Typ/Status/R-Strategie/Preisrange), Sortierung, Statistik-Leiste (Anzahl, Lagerwert).
- **Detailansicht:** alle Felder, Projekt-Banner, Fotogalerie mit Lightbox, Bearbeiten/Löschen.
- **Export:** CSV (alle Einträge) + PDF-Datenblatt (einzeln, gebrandet).

### ISO-Aufbau-Beschriftung (Phase 3.1)
- Bei 2-/3-fach Isolierglas werden die Glaslagen nach **Glasoberflächen-Position** beschriftet (Standard im Glasbau):
  - 2-fach ISO: „Position 1/2" + „Position 3/4"
  - 3-fach ISO: „Position 1/2" + „Position 3/4" + „Position 5/6"
- **Diese Notation gilt überall einheitlich:** Erfassungsformular, Detailansicht, Volltextsuche-Index (`buildSummary`), CSV-Export, PDF-Datenblatt und Matching-Sub-Treffer-IDs. VSG/Verbundglas behält bewusst „L1/L2…" (keine ISO-Positions-Semantik).
- Beschichtung wird auf konkreter Position (1–6) angegeben statt früher „innen/außen". Das Feld `cside` enthält die Positionsnummer als String (`'1'` … `'6'`).
- **Backwards-kompatibel:** Alte Einträge mit `cside='innen'`/`'außen'` werden beim Öffnen automatisch auf Position gemappt (`außen` → niedrigere, `innen` → höhere Nummer der jeweiligen Lage). Anzeige in Summary/PDF/CSV: `Pos N`.

### Authentifizierung (Phase 2)
- **Login-Screen:** Passwort-Pflicht beim App-Start; Login gilt bis Browser-Tab schließt (sessionStorage).

### Drive-Sync (Phase 2)
- **OAuth-Verbindung:** Modaler Setup-Dialog mit zwei Wegen:
  1. **„Neue Datenbank erstellen"** → App legt `refloat-data.json` in „Meine Ablage" an.
  2. **„Bestehende Datenbank wählen"** → Google Picker für Datei in „Geteilt mit mir" oder „Meine Ablage".
- **Auto-Sync:** Jede Änderung wird ~1,5s debounced nach Drive geschrieben.
- **Auto-Reconnect:** Nach Reload stille Re-Authentifizierung mit `prompt:'none'` + E-Mail-Hint. Account-Picker erscheint praktisch nie.
- **Team-Sharing:** Datei (oder enthaltender Ordner) per Drive-UI mit Teammitgliedern teilen. Andere Teammitglieder wählen sie via Picker. Berechtigungen werden vom Ordner an alle enthaltenen Dateien (inkl. zukünftiger Fotos) vererbt.
- **Race-Schutz beim Initial-Seed:** `driveLoad()` merged lokal frisch geseedete DEMO-Posten, die in Drive noch fehlen, in die zurückgeladenen Daten — sonst würden sie beim Überschreiben verloren gehen, bevor der debounced Drive-Save sie hochladen konnte.

### Fotos als Drive-Dateien (Phase 3)
- Beim Speichern werden neue Fotos als einzelne JPEG-Dateien in den **gleichen Drive-Ordner** wie `refloat-data.json` hochgeladen (Parent-Ordner wird via `drive.files.get(fields:parents)` ermittelt).
- In der JSON steht pro Foto nur noch `{id, n}` (Drive-File-ID + Dateiname) statt der vollen Base64-Daten.
- Anzeige lazy: Platzhalter sofort, im Hintergrund werden Fotos via Cache geladen (`photoCache` Map). Beim PDF-Export werden alle benötigten Fotos vorab geholt, bevor `window.print()` ausgelöst wird.
- **Backwards-kompatibel:** Alte Base64-Einträge funktionieren weiterhin; werden beim nächsten Editieren+Speichern automatisch auf Drive ausgelagert („Soft-Migration").
- Beim Löschen eines Eintrags / einer Position werden die zugehörigen Foto-Dateien aus Drive entfernt (fire-and-forget).

### Matching-Tool (Phase 4)
- **Neuer Tab „🔍 Matching"** zum Import von Kundenanfragen (.xlsx oder .csv) und Abgleich gegen den Bestand.
- **Workflow:** Datei per Drag&Drop oder Klick auf Dropzone laden → Anfragen-Tabelle erscheint, **direkt vorberechnet** mit Vorschlag 1 pro Position als Auto-Auswahl → unter jeder Anfrage-Zeile sind die Vorschlags-Karten dauerhaft sichtbar (Grid nebeneinander). User kann pro Position eine andere Karte anklicken; nachfolgende Positionen werden dann automatisch neu berechnet (Bestand fließend dekrementiert).
- **Excel-Vorlage zum Download:** Button „📥 Excel-Vorlage herunterladen" generiert `refloat-anfrage-vorlage.xlsx` mit Header (App-eigene deutsche Spaltennamen), 4 Beispielzeilen und zweitem Sheet „Hinweise" (Spaltenbedeutung + erlaubte Werte).
- **Harte Kriterien (UND-Verkettung):** Status = Verfügbar (immer); Glastyp/Dicke/Beschichtung exakt; Maße passt-rein (Bestand ≥ Anfrage, inkl. gedrehter Lage — Drehung mit ↻-Badge markiert); Stückzahl ≥; Farbe exakt (optional, falls in Anfrage gesetzt). Leere Felder in der Anfrage = „egal", werden übersprungen.
- **Kriterien-Kapselung:** Jedes Kriterium ist eine eigene Funktion (`crit_type`, `crit_thickness`, `crit_dims`, `crit_coating`, `crit_qty`, `crit_color`, `crit_status`) in der Liste `MATCH_CRITERIA`. Erweiterung um Scoring/weiche Kriterien später möglich, ohne die Struktur neu zu schreiben.
- **Spalten-/Werte-Aliasse:** Erkennt sowohl App-eigene deutsche Bezeichnungen (`Glastyp`, `Glasdicke (mm)`, `Breite`, `Höhe`, `Beschichtung (Kurzinfo)`, `Stückzahl`, `Farbe / Tönung`) als auch englische Spaltennamen (`glass_type`, `thickness_mm`, `min_width_mm`, `min_height_mm`, `coating`, `quantity_required`, `color`) und Kürzel (`Float`→`Floatglas`, `ISO2`/`ISO3`, `Low-E`→`Wärmeschutz`).
- **Transparenz bei 0/wenig Treffern:** Pro Kriterium wird gezählt, wie viele Bestandsposten passen würden, wenn genau dieses eine Kriterium ignoriert wäre. Anzeige z. B. „Wenn Dicke ignoriert würde → 2 Posten würden passen". So sieht der User sofort, welches Kriterium klemmt.
- **Sub-Treffer aus ISO-Aufbauten (Floatglas-Anfragen):** Bei `req.type === 'Floatglas'` wird der Bestand vor dem Matching durch `expandDbForRequest()` um virtuelle Posten erweitert. Pro 2-/3-fach Isolierglas-Eintrag wird je vorkommender unbeschichteter Floatglas-Lagen-Dicke EIN virtueller Sub-Posten erzeugt (`_virtual:true`, `_parentId`, `_layerNums`), mit `type:'Floatglas'`, `d=Lagen-Dicke`, `coating:'Keine'`, `qty = ISO.qty × Anzahl passender Lagen` und übernommenen Maßen/Farbe/Status. Die normalen Kriterien greifen unverändert. Anzeige in der Trefferliste: zusammengesetzte ID wie `ISO2-2018-001-P1 · Pos 1/2` (bei mehreren Lagen `+`-verkettet, z. B. `Pos 1/2+Pos 3/4`) plus dunkelblaues Badge **„📦 aus ISO-Aufbau"**. Klick auf Sub-Treffer öffnet den **Parent-ISO** in der Detail-Ansicht. VSG/Verbundglas wird bewusst NICHT zerlegt (Lagen verklebt). Beschichtete Lagen werden nie als Sub-Treffer geliefert.
- **Mehrfach-Zuschnitt mit 15 mm-Randreserve (Phase 4.1):**
  - **Geometrie:** `analyzeDimsFit(req, e)` liefert `{n, rotated, wastePct}`. Aus einem Bestandsstück können `floor((B−15)/b) × floor((H−15)/h)` Anfrage-Scheiben entnommen werden (beste Einzelorientierung — KEIN Mixed-Orientation auf derselben Scheibe). Die 15 mm (`MATCH_SAFETY_MM`) sind harte Randabschnitt-Reserve, kein Pro-Schnittfugen-Verlust. Zwischen geschnittenen Scheiben fällt kein zusätzlicher Verlust an.
  - **Kriterien:** `crit_dims` nutzt `analyzeDimsFit().n >= 1`. Bestand mit gleichen Maßen wie Anfrage passt nicht mehr (15 mm-Reserve fehlt) — strikte Interpretation der Praxisanforderung.
- **Interaktiver Allokator mit Vorschlags-Karten (Phase 4.2):**
  - **Konzept:** Pro Anfrage-Position berechnet das Tool max. 3 Vorschläge gegen den **verbleibenden** Bestand (greedy ab `matches[0..4]` als Startpunkte). Vorschlag 1 wird beim Upload automatisch vorausgewählt — der Plan ist sofort fertig, der User übersteuert nur wo er anders entscheiden will. KEIN Mixed-Cutting verschiedener Anfrage-Positionen aus einer Bestand-Scheibe (bewusst entfernt, weil Schnittpläne dadurch eindeutig werden und der Verschnitt für Werkstätten besser nachvollziehbar ist).
  - **Allokator-Funktionen:** `findMatchesAgainst(req, stockList)` (Match-Suche mit `_remaining`-Buchhaltung), `expandStockWithRemaining(req, stockList)` (ISO-Sub-Treffer mit eigenständigem Verbrauchszähler), `greedyFromStart(req, matches, startIdx, qty)` (Greedy ab Posten `startIdx`, dann Reihenfolge fortgesetzt), `buildOptions(req, matches)` (5 Kandidaten erzeugen, sortieren, Top 3 zurückgeben).
  - **Sortierung der Vorschläge:** (1) **voll deckend zuerst**, (2) bei gleicher Deckungsklasse: **höhere Deckung zuerst**, (3) bei gleicher Deckung: **niedrigster Combo-Verschnitt zuerst**. So ist „Vorschlag 1 — geringster Verschnitt" garantiert ehrlich — und nicht etwa der Vorschlag mit dem theoretisch besten Pro-Stück-Verschnitt, der aber das letzte Bestand-Stück halb verschwendet.
  - **State:** `matchOptions[idx]` (Array der 3 Vorschläge), `matchPicks[idx]` (gewählter Vorschlag), `matchResults[idx]` (Transparenz-Info aus `matchOne` — separat).
  - **Re-Auswahl:** `selectOption(idx, optionIdx)` setzt den Pick und ruft `recomputeFromIdx(idx+1)` auf — alle nachfolgenden Auswahlen werden mit dem dann verbleibenden Bestand neu berechnet (Auto-Vorauswahl Vorschlag 1). `resetPick(idx)` setzt diese Position auf Auto-Vorauswahl zurück.
  - **Bestand-Snapshot:** `computeAvailableAt(uptoIdx)` rechnet aus `db` und den Picks 0..uptoIdx-1 den verbleibenden Bestand. Sub-Treffer-Picks dekrementieren den Parent-ISO mit `ceil(sheetsTaken / layerCount)` Stücken (vereinfachte Buchhaltung; siehe Schwachstelle 3).
  - **UI:** Über der Anfragen-Tabelle die Auswahl-Summary-Box (`renderSummary`) mit Gesamt-Deckung und gewichtetem ⌀-Verschnitt über alle Picks. Unter jeder Anfrage-Zeile dauerhaft die Vorschlags-Karten als Grid (`auto-fit, minmax(280px, 1fr)` — 3 nebeneinander auf breiten Screens, stapeln sich automatisch). Pro Karte: Tag, Deckungs-Badge, EINE Verschnitt-Zahl (Combo-Verschnitt — die ehrliche Größe), Posten-Liste. Aktive Karte mit lila Highlight (`.option-card.active`).

### Projekte-Tab (Phase 6)
- **Neuer Tab „📁 Projekte"** zum dauerhaften Speichern einer Matching-Auswahl als Projekt-Dokument. Im Matching-Tab erscheint im Auswahl-Summary-Header ein Button **„📁 Projekt anlegen"** sobald mind. ein Vorschlag gewählt ist.
- **Anlegen-Modal:** Projektname (Pflicht), Kunde (optional), Notizen (optional), Checkbox „Original-Anfrage-Datei mit ablegen". Beim Anlegen wird die importierte .xlsx/.csv (RAM-only via `matchSourceFile`) in den Foto-Drive-Ordner hochgeladen und im Projekt als `sourceFile:{id,n}` verlinkt. Wenn die Original-Datei nicht mehr im RAM ist (z. B. nach Page-Reload), wird die Checkbox ausgeblendet — das Projekt entsteht trotzdem mit Anfrage-Snapshot.
- **Reservierungs-Buchhaltung pro Bestand-Eintrag:** Neue Felder `reservedQty` (aktiv in Projekten gebunden) und `soldQty` (durch abgeschlossene Projekte unwiderruflich verkauft). Helper `availableQty(e) = qty − reservedQty − soldQty`. Beim Anlegen werden auf allen referenzierten Posten Reservierungen gebucht; bei Sub-Treffern aus ISO wird der Parent-ISO mit `ceil(sheetsTaken / layerCount)` Stücken reserviert (gleiche Buchhaltung wie im Allokator).
- **Lifecycle:** `aktiv → abgeschlossen` (Reservierungen werden zu Verkäufen umgebucht: `reservedQty -= n; soldQty += n`) oder `aktiv → storniert` (Reservierungen zurück: `reservedQty -= n`). Löschen eines aktiven Projekts gibt Reservierungen zurück. **(Stand Phase 7.1 — siehe unten:** abgeschlossene Projekte sind NICHT mehr löschbar, sondern archivierbar bzw. per „Abschluss rückgängig" reaktivierbar.)
- **Status-Ableitung:** `recomputeStatus(e)` setzt `e.status` automatisch: `soldQty ≥ qty → 'Verkauft'`, `reservedQty + soldQty ≥ qty → 'Reserviert'`, `reservedQty = 0 && soldQty = 0 && status ≠ 'Verkauft' → 'Verfügbar'`. Status ändert sich also nur an den Stückzahl-Übergängen; teilreservierte Posten bleiben „Verfügbar", das Matching nutzt `availableQty(e)` als ehrliche Verfügbarkeit.
- **Matching-Integration:** `crit_status` prüft `status === 'Verfügbar' && availableQty(e) > 0` (**Stand Phase 7 — korrigiert**: vorher nur `availableQty > 0 && status ≠ 'Verkauft'`, wodurch ein manuell im Formular auf „Reserviert" gesetzter Posten mit Zählern = 0 fälschlich gematcht wurde). `computeAvailableAt` und ISO-Sub-Treffer-Erzeugung nutzen `availableQty` statt `qty` — projekt-teilreservierte Posten bleiben mit ihrem Restbestand matchbar (deren Status bleibt „Verfügbar"), voll- oder manuell-reservierte verschwinden aus den Treffern.
- **Schneidskizze (SVG, `cutLayoutSVG`):** Pro gewählter Bestand-Scheibe ein proportional skaliertes Rechteck (max 240×200 px für Detail-View, 640×480 px für PDF). Anfrage-Zuschnitte (violett) als Raster `floor((B−15)/b) × floor((H−15)/h)`. **Geometrie wichtig:** Die Cuts beginnen oben-links und kleben an zwei Bestand-Seiten direkt am Rand — die 15 mm Randreserve wird in `analyzeDimsFit` nur EINMAL pro Achse abgezogen, nicht zweimal. Der Verschnittstreifen (hellgelb, dezent) liegt deshalb nur rechts und unten der Bestand-Scheibe. Maße sind außen beschriftet, oben rechts die Zuschnitt-Anzahl als `cols×rows = N Stk`. **Gruppierung:** Allokationen innerhalb derselben Anfrage-Position mit identischem Schnittplan (gleiche Stock-Maße, Anfrage-Maße, Rotation, cuts/Stück) werden zu EINER Skizze mit „× N Scheiben"-Badge zusammengefasst (`groupAllocsByCutPlan`).
- **Projekt-Detailansicht:** Header (Name, Kunde, Status-Badge, Stats-Chips, Aktions-Buttons), pro Anfrage-Position eine Card mit Anfrage-Meta + Deckungs-Badge + Grid aus Schneidskizzen-Karten. **Layout:** `.alloc-grid` ist fix 2-spaltig (`repeat(2, minmax(0,1fr))`), bei Bildschirmbreite < 760 px stacken die Karten zu einer Spalte. Klick auf Stock-ID öffnet den Parent-Posten im Übersicht-Tab (`closeMatchAndOpen`). „📥 Original-Anfrage"-Button (`downloadProjectSource`) lädt die verlinkte Drive-Datei.
- **PDF-Export (`pdfProject`):** Mehrseitiges Layout:
  - **Seite 1:** Projekt-Header (Branding), Meta-Info (Kunde, Datum, Status), Notizen, Stats (Anfrage-Pos / Scheiben gedeckt / Bestand-Stück / ⌀ Verschnitt) und die komplette Anfrage-Tabelle. Hier KEINE Skizzen.
  - **Seiten 2..N:** je EINE Skizze pro PDF-Seite, in `large`-Größe (640×480). Pro Seite: Sub-Header („Schneidplan X/N" + Anfrage-Position), Chip-Reihe mit Bestand-ID / Scheiben-Verhältnis / Verschnitt, dann zentrierte große Skizze, darunter eine kurze Lesehilfe.
  - **Print-CSS-Mechanik:** `@media print` setzt `body > *:not(#parea){display:none !important}` und `#parea{position:static}`. Vorher (Phase 6 initial) war `#parea{position:fixed}` — das hat bei langem Inhalt dazu geführt, dass der Browser den Druck nicht sauber umbrechen konnte und denselben Block dreimal hintereinander rendert. Mit `display:none` + `static` fließt der Content jetzt natürlich seitenweise; `.pdf-page{page-break-after:always}` erzwingt sauberen Seitenwechsel.

### Bestand-Visualisierung & Dashboard (Phase 7)
- **Verfügbarkeits-Balken pro Position:** In der Übersicht-Tabelle (Spalte heißt jetzt **„Bestand"** statt „Stk."), in der Karten-Ansicht und in der Detailansicht zeigt ein gestapelter Mini-Balken die Aufteilung der Stückzahl: **grün = frei, bernstein = reserviert, rot = verkauft**, mit Label „x/y frei" und Hover-Tooltip. Farben aus der bestehenden Status-Badge-Palette (`#1F7A45` / `#E0A012` / `#C0392B`).
- **`availSplit(e)` ist die zentrale Anzeige-Quelle:** zerlegt `qty` in `{total, free, res, sold}`. Basis sind die exakten Projekt-Zähler (`reservedQty`, `soldQty`); **anschließend übersteuert ein MANUELL gesetzter Status den freien Rest** (`status==='Reserviert'` → Rest wird reserviert, `'Verkauft'` → Rest wird verkauft, `'Verfügbar'` → unverändert). Dadurch wirkt ein im Formular manuell gebundener Posten (Zähler = 0) trotzdem komplett gebunden, und „frei" entspricht **exakt** dem, was das Matching anbietet.
- **Helfer:** `availSplit`, `availabilityBar(e, showLabel)` (Liste/Karten), `availabilityBreakdown(e)` (Detailansicht mit farbcodierter Legende). In der Detailansicht heißt das Feld jetzt „Stückzahl gesamt" + neue Zeile „Bestand (Verfügbarkeit)".
- **Cockpit-Dashboard** oben in der Übersicht (`renderDashboard()`, Container `#dashboard`, in `render()` aufgerufen; **aggregiert über ALLE Bestandsgläser in `db`, filter-unabhängig**):
  - **KPI-Kacheln:** Positionen · Fläche gesamt (m²) · Fläche frei (m²) · Lagerwert frei (€). Fläche je Scheibe = `entryArea(e) = (w/1000)·(h/1000)`, m²-Formatierung via `fmtM2()`.
  - **Ring-Diagramm „Verfügbarkeit":** frei/reserviert/verkauft, „% frei" in der Mitte, Legende mit absoluten Zahlen. **Umschalter Stück ↔ m²** (State `dashMode`, `setDashMode()`). Ring via CSS `conic-gradient` — keine SVG-Mathematik, **keine neue Bibliothek**.
  - **m²-Balken je Glastyp:** horizontale Balken (nach Fläche absteigend), gestapelt frei (grün) / gebunden (amber), m²-Wert rechts, Hover-Tooltip mit Aufteilung.
  - Alle Werte kommen durchgängig aus `availSplit` → konsistent mit den Bestand-Balken in der Liste und mit dem Matching.
- **Statistik-Chips entschlackt:** „Gesamt" und „Lagerwert" sind ins Dashboard gewandert; die Chip-Leiste unter den Filtern zeigt nur noch Status-Verteilung (Verfügbar/Reserviert/Verkauft), Balken-Legende und ggf. die gefilterte Anzeige-Anzahl.

### Projekt-Lifecycle: Archivieren statt Löschen + Bestand-Abgleich (Phase 7.1)
- **Abgeschlossene Projekte sind NICHT mehr löschbar.** `deleteProject()` blockt sie mit Hinweis-Dialog. Grund: ein gebuchter Verkauf ist eine dokumentierte Tatsache; ihn durch Löschen des Dokuments verschwinden zu lassen, hinterlässt „verwaiste" Verkäufe im Bestand (genau der Bug, der zu FG-2026-001-P1 führte). Aktive und stornierte Projekte bleiben löschbar.
- **„↩ Abschluss rückgängig" (`reactivateProject`):** `abgeschlossen → aktiv`, bucht Verkauft → Reserviert zurück (`bookAllocUnsold` pro Allokation, Gegenstück zu `bookAllocSold`) und setzt `archived=false`. Von „aktiv" aus kann der User dann wie gewohnt stornieren (Bestand komplett freigeben) oder erneut abschließen. So ist die Rücknahme eines Verkaufs **bewusst und nachvollziehbar**, kein Nebeneffekt eines Löschvorgangs.
- **„🗄 Archivieren" / „📤 Aus Archiv holen" (`archiveProject` / `unarchiveProject`):** setzt nur das Flag `archived`. Archivierte (abgeschlossene) Projekte werden in der Projektliste standardmäßig ausgeblendet, der Verkaufs-Beleg bleibt aber vollständig erhalten. Sichtbar über den neuen Filter-Eintrag **„Archiviert"**; Badge `archiviert` in Liste und Detail-Header. `proj-cnt` zählt die gerade angezeigte (gefilterte) Liste.
- **„🔧 Bestand abgleichen" (`repairStockFromProjects`):** Button im Projekte-Header. Rechnet `reservedQty`/`soldQty` JEDES Bestand-Postens neu aus den vorhandenen Projekten (aktiv → reserviert, abgeschlossen inkl. archiviert → verkauft, storniert → nichts) und ruft `recomputeStatus`. Repariert verwaiste Buchungen (z. B. von früher gelöschten abgeschlossenen Projekten) und Drift. **Manuell gesetzter Status bleibt unangetastet**, weil `recomputeStatus` nur bei tatsächlicher Zähler-Änderung aufgerufen wird (Posten ohne Projekt-Bezug behalten ihre 0-Zähler und damit ihren manuellen Status). Damit lässt sich der bestehende FG-2026-001-P1-Fall per Klick sauber korrigieren.

### Demo-Daten (Auto-Seed)
- Beim ersten Start auf einem Browser werden einmalig **20 Demo-Glasposten** mit Präfix „DEMO – " im Projektnamen automatisch in den Bestand geseedet (`seedDemoIfNeeded()`). Verteilung: 8× Floatglas, 8× 2-fach Isolierglas, 4× 3-fach Isolierglas mit realistischen Maßen, Beschichtungen und Projekten.
- Steuerung via Flag `refloat_demo_seeded_v2` in localStorage. Bei Flag-Version-Bump (v2 → v3 …) wird erneut geseedet, ohne lokale Daten zu zerstören.
- `seedDemoIfNeeded` wird in INIT (nach `load()`) und nach `driveLoad()` aufgerufen. ID-Kollisions-Schutz: bereits vorhandene IDs werden nicht überschrieben.
- Werden über `persist()` auch nach Drive synchronisiert. Race-Schutz in `driveLoad()` verhindert Datenverlust beim Initial-Seed (siehe Drive-Sync).
- **Reset für sauberen Re-Seed:** Browser-Konsole → `localStorage.removeItem('gdt_v1'); localStorage.removeItem('refloat_demo_seeded_v2'); location.reload();` Drive-Datei ggf. zusätzlich manuell leeren oder neu erstellen.

## Datenmodell

### JSON-Format (seit Phase 6)
```js
localStorage-Key: 'gdt_v1'        // Cache der Drive-Datei
Drive-Datei:     'refloat-data.json'

{
  glass:    [...Glaseinträge],   // siehe unten
  projects: [...Projekte]         // siehe weiter unten
}

// BACKWARDS-COMPAT: Wenn `data` ein Array ist (altes Format vor Phase 6),
// wird es als `glass` interpretiert und `projects` mit [] initialisiert.
// driveSave() schreibt immer das neue Objekt-Format.
```

### Glaseintrag (ein Eintrag = eine Glasposition)
```js
{
  id,          // z.B. "ISO2-2019-001-P1"
  projId,      // z.B. "PRJ-2019-0001" (gemeinsam für Positionen eines Projekts)
  projLabel,   // = building
  pos,         // Positionsnummer (1,2,3…)
  building, address, year,
  type,        // Floatglas | 2-fach Isolierglas | 3-fach Isolierglas | VSG | ESG | Verbundglas | Sonstiges
  build,       // null ODER:
               //  ISO:   {kind:'iso', n, lagen:[{art,d,coat,ctype,cside}], spacers:[..], glassMm}
               //         cside ist Positionsnummer als String ('1'…'6'); Legacy 'innen'/'außen' wird beim Laden gemappt.
               //  VSG/VG:{kind:'lam', lc, lagen:[{art,d}], inter, glassMm}
               //  ESG:   {kind:'esg', d, kante, glassMm}
  glassMm,     // Gesamt-Glasdicke (Summe Lagen, ohne Abstandshalter)
  w, h, d,     // d = glassMm bei Aufbau-Typen
  wt,          // Gewicht = (w/1000)*(h/1000)*(glassMm/1000)*2500 kg, 1 Nachkommastelle, nicht editierbar
  color, coating, qty, loc, price, status,
  reservedQty, // Phase 6: aktuell in aktiven Projekten gebundene Stückzahl (default 0)
  soldQty,     // Phase 6: durch abgeschlossene Projekte verkauft (default 0)
               // availableQty(e) = qty − reservedQty − soldQty
               // Status wird via recomputeStatus() automatisch aus diesen Stückzahlen abgeleitet.
  tags: [],
  notes,
  rStrat,      // reuse | repair | remanufacturing | repurpose | recycling
  photos: [],  // GEMISCHT MÖGLICH:
               //   - {id:'drive-file-id', n:'photo-xxxx.jpg'}  ← seit Phase 3 (Standard)
               //   - 'data:image/jpeg;base64,…'                ← Legacy, wird beim nächsten Edit migriert
  at, upd      // ISO-Timestamps (erstellt / aktualisiert)
}
```

### Projekt (Phase 6)
```js
{
  id,            // "PRJ-MATCH-YYYY-###" (eigener Counter, getrennt von PRJ-YYYY-####
                 // der Erfassung — Matching-Projekte und Rückbau-Projekte teilen keinen Namensraum)
  name,          // Pflicht, vom User im Anlegen-Modal eingegeben
  customer,      // optional
  notes,         // optional
  status,        // 'aktiv' | 'abgeschlossen' | 'storniert'
  archived,      // Phase 7.1: true = aus der Projektliste ausgeblendet (nur bei abgeschlossenen;
                 // Verkaufs-Beleg bleibt erhalten). Fehlt/undefined = nicht archiviert.
  createdAt,     // ISO-Timestamp
  updatedAt,     // ISO-Timestamp (Statusänderung etc.)
  sourceFile,    // null ODER {id, n} — Drive-File-ID + Name der originalen .xlsx/.csv
  requests:      // Snapshot der importierten Anfrage-Zeilen (nur die übernommenen Felder)
    [{reqId, type, d, w, h, coating, color, qty}],
  allocations:   // Welche Bestand-Scheibe für welche Anfrage-Position
    [{
      reqIdx,        // Index in requests[]
      stockId,       // ID des Bestand-Eintrags (bei Sub-Treffer: ISO-ID + " · Pos X/Y")
      virtual,       // true wenn Sub-Treffer aus ISO-Aufbau
      parentId,      // Parent-ISO-ID (nur bei virtual=true)
      layerCount,    // Anzahl Sub-Lagen im Parent (für Buchhaltung: ceil(sheetsTaken/layerCount) ISOs)
      stockW, stockH, // Bestand-Maße (für Skizze)
      reqW, reqH,    // Anfrage-Maße (für Skizze)
      rotated,       // Schnitt erfolgte um 90° gedreht
      sheetsTaken,   // Anzahl Bestand-Scheiben entnommen
      cuts,          // Anfrage-Scheiben pro Bestand-Stück (Raster-Schnitt)
      delivered,     // gelieferte Anfrage-Scheiben (sheetsTaken × cuts, gekappt durch req.qty)
      wastePct,      // Verschnitt pro Bestand-Scheibe
      type, projLabel // Anzeige-Metadaten
    }]
}
```

## Wichtige Logik-Entscheidungen
1. **ID-Schema:** `[KÜRZEL]-[JAHR]-[NR]-P[Position]`. Kürzel: FG, ISO2, ISO3, VSG, ESG, VG, SONST. Laufende Nummer pro (Jahr+Typ). Positionen **desselben Typs** in einem Projekt teilen sich die Nummer und unterscheiden sich nur über `-P1/-P2`. Unterschiedliche Typen → eigene Nummer.
2. **„Maße" zeigt Glasdicke ohne Abstandshalter** (= Gewichtsbasis). Physische Gesamtdicke inkl. Abstandshalter steht nur im „Glasaufbau".
3. Position-Feld „Beschichtung (Kurzinfo)" existiert **zusätzlich** zur Beschichtung pro Glaslage (bewusst beibehalten).
4. **Drive-Scope absichtlich restriktiv (`drive.file`):** Die App hat KEINEN Zugriff auf andere Drive-Inhalte des Users. Bei „Bestehende Datei wählen" zwingend Picker verwenden.
5. **Konfliktstrategie aktuell:** Last-write-wins. Kein Konflikterkennungs- oder Merge-Mechanismus — mit einer Ausnahme: `driveLoad()` rettet lokal frisch geseedete DEMO-Posten, die in Drive noch nicht angekommen sind, vor dem Überschreiben (Race-Schutz beim Initial-Seed).
6. **Photo-Lifecycle:** Beim Löschen einer Position werden zugehörige Drive-JPEGs gelöscht. Beim Entfernen einzelner Fotos aus einer Position werden diese beim nächsten Speichern aus Drive entfernt. Falls Drive-Auth zwischen Edit und Save abläuft, werden Fotos lokal als Base64 gespeichert (Fallback).
7. **Matching-Kriterien sind UND-verkettet und binär** (passt / passt nicht). Kein Scoring. Kriterien gekapselt als Funktionen in `MATCH_CRITERIA`. Maße-Logik berücksichtigt gedrehte Lage (Glaszuschnitt). Nur Status=Verfügbar wird gematcht.
8. **Spalten-Erkennung im Matching-Import** ist tolerant: case-insensitiv, normalisiert Whitespace/Klammern/Unterstriche. Werte werden über Alias-Maps (`MATCH_TYPE_ALIAS`, `MATCH_COAT_ALIAS`, `MATCH_COLOR_ALIAS`) auf die App-eigenen kanonischen Bezeichnungen gemappt.
9. **Bestand-Erweiterung im Matching ist Anfragen-getrieben, nicht datenmodell-getrieben:** Virtuelle Sub-Posten werden nur erzeugt, wenn die Anfrage explizit Floatglas wünscht (`req.type === 'Floatglas'`). So bleibt das Datenmodell unverändert (kein Persistieren virtueller IDs), keine Phantom-Treffer bei anderen Anfragetypen, keine Sonderfälle in den Kriterien-Funktionen. Die Sub-Posten haben `coating:'Keine'`, fallen also automatisch raus, wenn die Anfrage eine konkrete Beschichtung fordert. Bei `qty` wird **summiert** (ISO.qty × Anzahl unbeschichteter Lagen gleicher Dicke) — entspricht der Anzahl entnehmbarer Scheiben.
10. **Zuschnitt-Modell: einfacher Raster-Schnitt mit 15 mm Randreserve.** Pro Bestandsstück wird die beste Einzelorientierung gewählt (`floor((B−15)/b) × floor((H−15)/h)`); KEIN Mixed-Orientation auf derselben Scheibe (manche quer, manche längs), KEIN Schnittfugen-Pro-Schnitt-Verlust. Die 15 mm sind eine harte Maße-Anforderung — Bestand muss in beiden Achsen ≥ Anfrage + 15 sein. Pro Bestand-Scheibe wird IMMER NUR EINE Anfrage-Position geschnitten (kein Mixed-Cutting verschiedener Positionen) — das macht Schnittpläne für die Werkstatt eindeutig.
11. **Tool als Berater, User entscheidet (Phase 4.2):** Der Allokator schlägt pro Position drei Vorschläge vor, der User klickt. Beim Upload wird Vorschlag 1 vorausgewählt (Plan ist sofort fertig), Änderungen einer früheren Position invalidieren ALLE nachfolgenden Picks (`recomputeFromIdx(idx+1)`) und setzen sie auf neue Auto-Vorauswahl — sonst entstehen Bestand-Inkonsistenzen. Sortierung der Vorschläge: voll deckend zuerst, dann höhere Deckung, dann niedrigster Combo-Verschnitt. **Eine** Verschnitt-Zahl pro Karte (Combo-Verschnitt), die Pro-Stück-Verschnitt-Zahl wurde bewusst aus der UI entfernt (war doppelte Information, hat User irritiert).
12. **Reservierungs-Zähler statt Posten-Split (Phase 6):** Beim Anlegen eines Projekts wird ein Bestand-Posten NICHT in „2 reserviert + 3 verfügbar" gesplittet — stattdessen führt jeder Posten `reservedQty` und `soldQty` als Stückzahl-Buchhaltung. So bleibt die Erfassungs-Historie sauber (eine ID, eine Inventur-Stückzahl), Reservierungen lassen sich kollisionsfrei auf- und abbauen, und das Matching nutzt `availableQty(e) = qty − reservedQty − soldQty` als ehrliche Verfügbarkeit. Pro Allokation wird auf dem referenzierten Posten gebucht (bei Sub-Treffer auf dem Parent-ISO mit `ceil(sheetsTaken/layerCount)`).
13. **Projekt-Lifecycle ist eine Buchhaltungs-Transition (Phase 6):** `aktiv → abgeschlossen` ist semantisch eine Umbuchung von Reserviert zu Verkauft (nicht: Lieferung an den Kunden erfasst). `aktiv → storniert` gibt frei. Löschen eines abgeschlossenen Projekts lässt die Verkäufe stehen, weil eine Lieferung sich nicht durch Löschen des Projekt-Dokuments rückgängig machen lässt — der Posten ist und bleibt verkauft. Löschen eines aktiven Projekts gibt Reservierungen zurück.
14. **JSON-Format-Migration (Phase 6):** Drive-Datei und localStorage wechseln von `[...]` zu `{glass:[...], projects:[...]}`. `driveLoad` und `load` akzeptieren beide Formate; `driveSave` und `persist` schreiben immer das neue Objekt-Format. Bestehende Drive-Dateien werden beim ersten Sync nach dem Update automatisch ins neue Format überführt — kein Datenverlust, kein Migrations-Skript nötig.
15. **Schneidskizze deckt sich mit `analyzeDimsFit` (Phase 6.1):** Die 15-mm-Randreserve wird in `analyzeDimsFit` nur einmal pro Achse abgezogen (`floor((avail − 15) / need)`) — entsprechend werden die Anfrage-Scheiben in EINER Ecke der Bestand-Glasplatte geschnitten und liegen an zwei Seiten direkt am Bestand-Rand ohne Randabschnitt. Die Skizze stellt das genau so dar (Cuts oben-links, Verschnitt nur rechts+unten). Frühere Skizzen-Version (Phase 6 initial) hatte fälschlich 15 mm Reserve auf allen vier Seiten dargestellt — visuell falsch, Mathematik der Matches war aber schon damals korrekt.
16. **Print-Container muss `position:static` sein (Phase 6.1):** `position:fixed` für `#parea` funktioniert nur bei kurzem Inhalt (z. B. einseitigem Datenblatt). Sobald der Inhalt über eine Druckseite hinausgeht (typisch für Projekt-PDFs mit mehreren Skizzen), kann der Browser nicht umbrechen und rendert denselben Block mehrfach. Lösung: bei Print `body > *:not(#parea){display:none}` plus `#parea{position:static}` — der Druckinhalt fließt dann seitenweise, `page-break-after:always` auf `.pdf-page` erzwingt die Seitenwechsel. Gilt jetzt einheitlich für `pdfEntry` (Datenblatt) und `pdfProject` (Projekt-Schneidplan).
17. **`availSplit` ist die Anzeige-Wahrheit, `availableQty` die Buchungs-Wahrheit (Phase 7):** `availableQty(e) = qty − reservedQty − soldQty` bleibt die reine Zähler-Verfügbarkeit für die Reservierungs-Buchhaltung (Projekte buchen/entbuchen darauf). `availSplit(e)` baut darauf auf und übersteuert zusätzlich den freien Rest mit einem manuell gesetzten Status — das ist die Basis aller Bestand-Visualisierungen (Balken + Dashboard) und entspricht der **effektiven** Matching-Verfügbarkeit (`crit_status` verlangt `status === 'Verfügbar'`). Wer eine neue „Verfügbarkeit"-Anzeige baut, nimmt `availSplit`; wer Reservierungen bucht, nimmt die Zähler.
18. **Dashboard ohne Chart-Bibliothek (Phase 7):** Ring = CSS `conic-gradient`, Balken = Flexbox-Breiten. Bewusst keine externe Lib (Konsistenz mit der Ein-Datei-Architektur, kein CDN-Risiko, sofort verfügbar). `renderDashboard()` aggregiert immer über `db` (alle Gläser), **nicht** über die gefilterte Liste `fd` — das Dashboard zeigt die Gesamtlage, unabhängig von gesetzten Filtern.
19. **Abgeschlossene Projekte sind unveränderliche Belege (Phase 7.1):** Ein Verkauf wird nicht durch Löschen rückgängig gemacht, sondern entweder bewusst reaktiviert (`reactivateProject`, Verkauft→Reserviert) oder das Projekt wird archiviert (ausgeblendet, Beleg bleibt). Damit hat jede verkaufte Scheibe immer ein dokumentierendes Projekt — keine verwaisten Verkäufe mehr. Die **Projekte sind die Quelle der Wahrheit** für `reservedQty`/`soldQty`; `repairStockFromProjects()` kann die Zähler jederzeit daraus neu ableiten (behebt Altlasten/Drift, schont manuell gesetzten Status). Ergänzt Schwachstelle 5: die alte Aussage „Löschen eines abgeschlossenen Projekts lässt Verkäufe stehen" (Logik-Entscheidung 13) ist damit überholt — solche Projekte lassen sich gar nicht mehr löschen.

## ⚠️ Bekannte Schwachstellen (für später)
1. **Kein Auto-Refresh anderer Änderungen.** Wenn Person A speichert, sieht Person B die Änderung erst nach Page-Reload. Workaround: regelmäßig F5. **Fix:** Polling alle ~30s auf `modifiedTime` der Drive-Datei + neuladen bei Änderung.
2. **Last-write-wins-Konflikte.** Zwei parallele Bearbeitungen → der zweite Speichern überschreibt den ersten. **Fix:** Versions-Check beim Speichern (z.B. `modifiedTime` vor Save prüfen, warnen wenn neuer).
3. **Sub-Treffer-Buchhaltung im Matching-Allokator ist vereinfacht.** Wenn ein ISO-Sub-Treffer für eine Floatglas-Anfrage gewählt wird, wird der Parent-ISO mit `ceil(sheetsTaken / layerCount)` Stücken dekrementiert. Wenn parallel jemand denselben ISO als ISO-Anfrage haben will, gibt es keinen Konflikt-Check — der ISO könnte rechnerisch doppelt vergeben werden (einmal zerlegt für Floatglas-Sub-Treffer, einmal als Ganzes für ISO-Anfrage). In der Praxis selten, weil Anfragetypen meist eindeutig sind. **Fix später:** Cross-Type-Verbrauchsverfolgung auf Parent-ISO-Ebene mit gemeinsamen `_remaining`-Pool.
4. **Greedy ist nicht global optimal.** Der Allokator ist greedy nach Position-Reihenfolge (mit 5 Startpunkten und Combo-Verschnitt-Sortierung). Bei sehr heterogenen Anfragen-Listen könnte eine globale Optimierung (DP/Branch-and-Bound) bessere Gesamt-Verschnitt-Werte liefern. **Workaround:** User kann manuell andere Vorschläge wählen.
5. **Manueller „Reserviert"-Status wird durch Projekt-Lifecycle überschrieben.** Wenn ein User in der Erfassung einen Posten manuell auf „Reserviert" setzt (z.B. weil ein Interessent ohne formale Anfrage vorgemerkt ist), und später wird ein Projekt auf diesen Posten gelegt und wieder storniert, setzt `recomputeStatus()` den Status auf „Verfügbar" zurück — die manuelle Vormerkung geht verloren. In der Praxis vermutlich kein Problem, weil Vormerkungen ohnehin nicht über Storno-Zyklen tragen sollen. **Fix später (falls relevant):** ein separates Feld `manualHold:bool` führen, das `recomputeStatus` respektiert.
6. **Source-File-Upload braucht Drive-Verbindung im Moment des Projekt-Anlegens.** Wenn Drive grade getrennt ist, schlägt der Upload still fehl (Toast-Warnung, Projekt entsteht trotzdem ohne `sourceFile`). Wenn man später eine Datei nachreichen will, gibt es bisher keinen UI-Weg. **Fix später:** Nachträglich „Original-Datei hochladen"-Button im Projekt-Detail.

## ⏭️ Nächster Schritt
**Live: Phase 4 Matching · Phase 4.1 Mehrfach-Zuschnitt · Phase 4.2 Interaktiver Allokator · Phase 5 Landing Page · Phase 6 Projekte-Tab + Reservierungs-Buchhaltung + Schneidskizze + PDF-Export · Phase 6.1 Skizze-Geometrie- und PDF-Layout-Korrektur · Phase 7 Bestand-Visualisierung (Verfügbarkeits-Balken + Cockpit-Dashboard) + crit_status-Fix (nur „Verfügbar" wird gematcht) · Phase 7.1 Projekt-Lifecycle (Archivieren statt Löschen, „Abschluss rückgängig", „Bestand abgleichen").**

Vom User bereits live bestätigt: Projekt-Anlegen aus Matching funktioniert sauber.

Noch praxis-zu-testen mit dem Team:
- **Reservierungs-Buchhaltung im Mehrpersonen-Betrieb**: Person A legt Projekt an → Person B sieht reduzierte Verfügbarkeit erst nach Reload (Schwachstelle 1). Bei zwei parallel angelegten Projekten auf demselben Posten → Last-write-wins (Schwachstelle 2).
- **Lifecycle**: Projekt abschließen → Übersicht zeigt für betroffene Posten Status `Verkauft`, wenn alle Stücke weg sind. Stornieren → Reservierung muss komplett zurückfließen. Wenn ein Posten vorher manuell auf „Reserviert" gesetzt war, wird er nach Storno auf „Verfügbar" zurückgesetzt (Schwachstelle 5).
- **Schneidskizze-Geometrie (Phase 6.1)**: bei Anfragen mit Maßen weit unter Bestandsmaß zeigt die Skizze ein Raster, Cuts kleben oben-links, Verschnitt liegt nur rechts und unten. Bei mehreren identischen Schnittplänen in derselben Position → eine Skizze mit „× N"-Badge.
- **PDF-Export (Phase 6.1)**: Druck erzeugt jetzt Seite 1 = Text+Anfrage-Tabelle, Seiten 2..N = je eine Skizze. KEIN dreifaches Rendering mehr (war `position:fixed`-Bug, Logik-Entscheidung 16). Beim ersten Live-Test Skalierung der großen Skizzen prüfen (640×480-Variante, sollte ~17 cm breit drucken).
- **JSON-Migration**: Bestehende Drive-Datei wird beim ersten Sync ins neue `{glass, projects}`-Format überführt — beim ersten Update einmal manuell prüfen, dass kein Eintrag fehlt.
- **Drive-Upload der Original-Datei**: `uploadSourceFileToDrive` läuft im Live-Test (auf localhost nicht prüfbar). Sollte funktionieren da gleiche Multipart-Mechanik wie `uploadPhotoToDrive`.
- **Phase 7 (lokal verifiziert):** Verfügbarkeits-Balken in Liste/Karten/Detail, manuell auf „Reserviert"/„Verkauft" gesetzte Posten erscheinen korrekt gebunden (nicht mehr „frei"), Dashboard-KPIs/Ring/m²-Balken und der Stück↔m²-Umschalter rechnen plausibel. Im Live-/Team-Betrieb noch im Blick behalten: dass die m²-Summen mit der realen Erfassung übereinstimmen und das Dashboard auf Mobil (1-spaltig ab < 760 px) gut aussieht.

Danach: **Schwachstelle 1 (Auto-Refresh)** ist der nächste sinnvolle Schritt, sobald mehr als eine Person regelmäßig Projekte anlegt — sonst sehen die anderen reduzierte Verfügbarkeit erst nach F5. Schwachstellen 3 + 4 + 5 + 6 sind Edge-Cases, erst bei konkretem Trigger fixen.

## GitHub
- Öffentliches Repository: `urbanmatter/refloat-inventory`
- Branch: `main` (direkt commiten, kein PR-Workflow nötig)
- Commits werden via `git push origin main` direkt nach GitHub Pages deployed (~1 Min Verzögerung)
- Co-Author bei AI-unterstützten Commits: aktuell `Claude Opus 4.8 <noreply@anthropic.com>` (frühere Commits mit Opus 4.7 bzw. Sonnet 4.6 markiert)
