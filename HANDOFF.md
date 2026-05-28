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
- **Workflow:** Datei per Drag&Drop oder Klick auf Dropzone laden → Anfragen-Tabelle erscheint → Einzelabgleich (Zeile aufklappen) oder Listen-Abgleich („↻ Alle abgleichen") → aufklappbare Trefferliste pro Anfrage im gleichen Stil wie Bestandsübersicht.
- **Excel-Vorlage zum Download:** Button „📥 Excel-Vorlage herunterladen" generiert `refloat-anfrage-vorlage.xlsx` mit Header (App-eigene deutsche Spaltennamen), 4 Beispielzeilen und zweitem Sheet „Hinweise" (Spaltenbedeutung + erlaubte Werte).
- **Harte Kriterien (UND-Verkettung):** Status = Verfügbar (immer); Glastyp/Dicke/Beschichtung exakt; Maße passt-rein (Bestand ≥ Anfrage, inkl. gedrehter Lage — Drehung mit ↻-Badge markiert); Stückzahl ≥; Farbe exakt (optional, falls in Anfrage gesetzt). Leere Felder in der Anfrage = „egal", werden übersprungen.
- **Kriterien-Kapselung:** Jedes Kriterium ist eine eigene Funktion (`crit_type`, `crit_thickness`, `crit_dims`, `crit_coating`, `crit_qty`, `crit_color`, `crit_status`) in der Liste `MATCH_CRITERIA`. Erweiterung um Scoring/weiche Kriterien später möglich, ohne die Struktur neu zu schreiben.
- **Spalten-/Werte-Aliasse:** Erkennt sowohl App-eigene deutsche Bezeichnungen (`Glastyp`, `Glasdicke (mm)`, `Breite`, `Höhe`, `Beschichtung (Kurzinfo)`, `Stückzahl`, `Farbe / Tönung`) als auch englische Spaltennamen (`glass_type`, `thickness_mm`, `min_width_mm`, `min_height_mm`, `coating`, `quantity_required`, `color`) und Kürzel (`Float`→`Floatglas`, `ISO2`/`ISO3`, `Low-E`→`Wärmeschutz`).
- **Transparenz bei 0/wenig Treffern:** Pro Kriterium wird gezählt, wie viele Bestandsposten passen würden, wenn genau dieses eine Kriterium ignoriert wäre. Anzeige z. B. „Wenn Dicke ignoriert würde → 2 Posten würden passen". So sieht der User sofort, welches Kriterium klemmt.
- **Sub-Treffer aus ISO-Aufbauten (Floatglas-Anfragen):** Bei `req.type === 'Floatglas'` wird der Bestand vor dem Matching durch `expandDbForRequest()` um virtuelle Posten erweitert. Pro 2-/3-fach Isolierglas-Eintrag wird je vorkommender unbeschichteter Floatglas-Lagen-Dicke EIN virtueller Sub-Posten erzeugt (`_virtual:true`, `_parentId`, `_layerNums`), mit `type:'Floatglas'`, `d=Lagen-Dicke`, `coating:'Keine'`, `qty = ISO.qty × Anzahl passender Lagen` und übernommenen Maßen/Farbe/Status. Die normalen Kriterien greifen unverändert. Anzeige in der Trefferliste: zusammengesetzte ID wie `ISO2-2018-001-P1 · Pos 1/2` (bei mehreren Lagen `+`-verkettet, z. B. `Pos 1/2+Pos 3/4`) plus dunkelblaues Badge **„📦 aus ISO-Aufbau"**. Klick auf Sub-Treffer öffnet den **Parent-ISO** in der Detail-Ansicht. VSG/Verbundglas wird bewusst NICHT zerlegt (Lagen verklebt). Beschichtete Lagen werden nie als Sub-Treffer geliefert.
- **Mehrfach-Zuschnitt + Multi-Posten-Kombination (Phase 4.1):**
  - **Geometrie:** `analyzeDimsFit(req, e)` liefert `{n, rotated, wastePct}`. Aus einem Bestandsstück können `floor((B−15)/b) × floor((H−15)/h)` Anfrage-Scheiben entnommen werden (beste Orientierung). Die 15 mm (`MATCH_SAFETY_MM`) sind harte Randabschnitt-Reserve, kein Pro-Schnittfugen-Verlust. Zwischen geschnittenen Scheiben fällt kein zusätzlicher Verlust an.
  - **Kriterien:** `crit_dims` nutzt `analyzeDimsFit().n >= 1`, `crit_qty` rechnet `e.qty × cuts >= req.qty` (Multi-Cut wird gegen die qty-Anforderung verrechnet). Konsequenz: Bestand mit gleichen Maßen wie Anfrage passt nicht mehr (15 mm-Reserve fehlt) — bewusste strikte Interpretation der Praxisanforderung.
  - **Annotation pro Treffer:** `_cuts`, `_rotated`, `_wastePct`, `_deliverable` (= cuts × qty). Trefferliste wird nach `_wastePct` aufsteigend sortiert (beste Ausbeute zuerst).
  - **Greedy-Kombi (`buildCombo`):** Nimmt Posten in Verschnitt-Reihenfolge und buchhält Bestand-Stücke (`Math.ceil(remaining / cuts)`, gecappt auf `e.qty`) bis `req.qty` gedeckt ist. Liefert `{picks, covered, remaining, complete, multiPosten, comboWastePct}`. Sub-Treffer aus ISO werden wie normale Posten behandelt (kein Sub-/Parent-Konflikt, weil bei Floatglas-Anfragen der Original-ISO über `crit_type` rausfällt).
  - **UI:** Über der Trefferliste erscheint die `.recommend`-Box, wenn Multi-Posten nötig sind ODER Mehrfach-Zuschnitt pro Stück greift ODER der Bestand nicht reicht. Headline `🎯 Empfohlene Kombination — Deckt X/Y · ⌀ Verschnitt Z%`, Pro Pick eine Card mit `<sheetsTaken>× aus <ID> → <delivered> Anfrage-Scheiben (je N Scheiben/Stück · gedreht · Verschnitt M%)`. Klick öffnet Detail-Ansicht des Bestandspostens. Bei Teildeckung wechselt die Box auf Orange (`.recommend.partial`). Trefferliste bekommt zwei neue Spalten **Liefert** und **Verschnitt**.

### Demo-Daten (Auto-Seed)
- Beim ersten Start auf einem Browser werden einmalig **20 Demo-Glasposten** mit Präfix „DEMO – " im Projektnamen automatisch in den Bestand geseedet (`seedDemoIfNeeded()`). Verteilung: 8× Floatglas, 8× 2-fach Isolierglas, 4× 3-fach Isolierglas mit realistischen Maßen, Beschichtungen und Projekten.
- Steuerung via Flag `refloat_demo_seeded_v2` in localStorage. Bei Flag-Version-Bump (v2 → v3 …) wird erneut geseedet, ohne lokale Daten zu zerstören.
- `seedDemoIfNeeded` wird in INIT (nach `load()`) und nach `driveLoad()` aufgerufen. ID-Kollisions-Schutz: bereits vorhandene IDs werden nicht überschrieben.
- Werden über `persist()` auch nach Drive synchronisiert. Race-Schutz in `driveLoad()` verhindert Datenverlust beim Initial-Seed (siehe Drive-Sync).
- **Reset für sauberen Re-Seed:** Browser-Konsole → `localStorage.removeItem('gdt_v1'); localStorage.removeItem('refloat_demo_seeded_v2'); location.reload();` Drive-Datei ggf. zusätzlich manuell leeren oder neu erstellen.

## Datenmodell (ein Eintrag = eine Glasposition)
```js
localStorage-Key: 'gdt_v1'  // Array von Einträgen (Cache der Drive-Datei)
Drive-Datei:     'refloat-data.json' (gleicher Inhalt, sync'd)

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
  tags: [],
  notes,
  rStrat,      // reuse | repair | remanufacturing | repurpose | recycling
  photos: [],  // GEMISCHT MÖGLICH:
               //   - {id:'drive-file-id', n:'photo-xxxx.jpg'}  ← seit Phase 3 (Standard)
               //   - 'data:image/jpeg;base64,…'                ← Legacy, wird beim nächsten Edit migriert
  at, upd      // ISO-Timestamps (erstellt / aktualisiert)
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
10. **Zuschnitt-Modell: einfacher Raster-Schnitt mit 15 mm Randreserve.** Pro Bestandsstück wird die beste Einzelorientierung gewählt (`floor((B−15)/b) × floor((H−15)/h)`); KEIN Mixed-Orientation auf derselben Scheibe (manche quer, manche längs), KEIN Schnittfugen-Pro-Schnitt-Verlust. Die 15 mm sind eine harte Maße-Anforderung — Bestand muss in beiden Achsen ≥ Anfrage + 15 sein. Greedy-Kombi sortiert nach Pro-Stück-Verschnitt aufsteigend; nicht global optimal, aber in der Praxis nahe am Optimum und für den User nachvollziehbar (jeder Pick lässt sich einzeln begründen).

## ⚠️ Bekannte Schwachstellen (für später)
1. **Kein Auto-Refresh anderer Änderungen.** Wenn Person A speichert, sieht Person B die Änderung erst nach Page-Reload. Workaround: regelmäßig F5. **Fix:** Polling alle ~30s auf `modifiedTime` der Drive-Datei + neuladen bei Änderung.
2. **Last-write-wins-Konflikte.** Zwei parallele Bearbeitungen → der zweite Speichern überschreibt den ersten. **Fix:** Versions-Check beim Speichern (z.B. `modifiedTime` vor Save prüfen, warnen wenn neuer).

## ⏭️ Nächster Schritt
**Phase 4 Matching + Phase 4.1 Multi-Posten/Verschnitt + Phase 5 Landing Page sind live.** Praxis-Test mit dem Team auf folgende Punkte:
- **Multi-Posten-Kombination & Verschnitt**: Floatglas-Anfrage mit hoher Stückzahl (z. B. 50) importieren → Empfehlungs-Box prüfen (deckt die Anfrage, Verschnitt-Anteil plausibel?). Anfrage mit kleinen Maßen → Mehrfach-Zuschnitt sollte greifen (Spalte „Liefert" zeigt z. B. `60 (3/Stk)`). Anfrage mit Maßen knapp unter Bestandsmaß → kein Treffer (15 mm-Reserve fehlt).
- **Floatglas-Sub-Treffer aus ISO-Aufbauten**: Floatglas-Anfrage importieren, prüfen ob unbeschichtete ISO-Lagen mit `📦 aus ISO-Aufbau`-Badge erscheinen, ob Stückzahl-Summierung intuitiv ist, ob Klick auf Sub-Treffer korrekt den Parent-ISO öffnet.
- **Durchgängige Position-Notation**: Detail/CSV/PDF/Matching zeigen ISO-Lagen jetzt als „Position 1/2 / 3/4 / 5/6" statt „L1/L2/L3" — vom Team auf Verständlichkeit prüfen.
- **Landing Page**: Wege „Logo klicken" und „🏠 Start"-Button als Heimweg dokumentieren / dem Team zeigen.

Danach **Schwachstelle 1 (Auto-Refresh)** angehen, wenn sie sich als störend zeigt — Schwachstelle 2 ist bei 2–3 Personen meist unkritisch. Optional Phase 4.2: echte 2D-Verschnittoptimierung mit Mixed-Orientation (Guillotine-Heuristik), falls die einfache Raster-Variante zu pessimistisch ist.

## GitHub
- Öffentliches Repository: `urbanmatter/refloat-inventory`
- Branch: `main` (direkt commiten, kein PR-Workflow nötig)
- Commits werden via `git push origin main` direkt nach GitHub Pages deployed (~1 Min Verzögerung)
- Co-Author bei AI-unterstützten Commits: `Claude Opus 4.7 <noreply@anthropic.com>` (vorherige Commits noch mit Sonnet 4.6 markiert)
