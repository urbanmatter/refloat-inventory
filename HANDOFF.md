# 📋 Projekt-Übergabe: ReFloat Inventory

> Diese Datei dient als Übergabe-/Wiedereinstiegspunkt. Inhalt kann in einen neuen Chat kopiert werden, um nahtlos weiterzuarbeiten.

## Rolle & Kontext
Du bist ein erfahrener Full-Stack-Entwickler und hilfst mir (Gründer in der Baubranche, **kein Entwickler**) beim Bau einer professionellen Web-App zur Erfassung und Verwaltung von **rückgebautem Flachglas** aus Gebäuderückbauten. Mein Team (2–10 Personen) erfasst Gläser, kategorisiert sie und stellt sie intern und für Kunden bereit. Die App läuft im Browser. **Erkläre Dinge einfach und sag direkt, wenn du dir unsicher bist.**

## Live-URL & Hosting
- **App online:** https://urbanmatter.github.io/refloat-inventory/
- **GitHub Repository:** https://github.com/urbanmatter/refloat-inventory (öffentlich, mit `robots.txt` von Suchmaschinen ausgeschlossen)
- **Hosting:** GitHub Pages (kostenlos, automatisch bei Push auf `main`)

## Technischer Stand
- **Eine einzige Datei:** `index.html` (HTML + CSS + JavaScript inline, ~80 KB)
- **Lokaler Speicherort:** `C:\Users\sebas\Desktop\Claude Projekte\ReFloat Inventory\`
- **Datenspeicher:**
  - **Primär:** Google Drive (`refloat-data.json`) — Team-Sync
  - **Cache/Fallback:** Browser `localStorage`, Key = `gdt_v1`
- **Fotos:** Einzelne JPEG-Dateien in Drive (gleicher Ordner wie JSON), Verknüpfung via Drive-File-ID
- **Umgebung:** Windows, Python 3.14 + Pillow 12.2 verfügbar
- **Vorschau-Server:** `.claude/launch.json` → Name `glass-static`, startet `python -m http.server 8777`

## Authentifizierung & Konfiguration
Alle Konstanten stehen ganz oben im `<script>`-Block in `index.html`:

| Konstante | Wert | Wo geändert |
|---|---|---|
| `APP_PASSWORD` | aktuell `'CHANGEME'` (Platzhalter) | Login-Block in JS |
| `DRIVE_API_KEY` | `AIzaSyDL1ZSe4DQcTlxe-4LCZGwcTSck6C5i3VQ` | Drive-Block (auf `https://urbanmatter.github.io/*` beschränkt) |
| `OAUTH_CLIENT_ID` | `383046788151-99h586mb9tmdup6aqsits1i3rgge4ena.apps.googleusercontent.com` | Drive-Block |
| `DRIVE_SCOPE` | `https://www.googleapis.com/auth/drive.file` | Restriktiv: nur App-erstellte oder via Picker gewählte Dateien |

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
### Erfassung & Verwaltung
- **Erfassung:** Projekt-Header (Gebäude, Adresse, Rückbaujahr) + beliebig viele **Glaspositionen** (P1, P2…) mit „+ Position hinzufügen" / „×" entfernen (mind. 1 Position).
- **Pro Position:** Glastyp, dynamischer **Glasaufbau** (je nach Typ), Farbe, Beschichtung (Kurzinfo), Breite/Höhe, automatische Glasdicke & Gewicht, Stückzahl, Lagerort, Preis, Status, R-Strategie, Tags, Notizen, Foto-Upload (Drag&Drop, automatisch komprimiert auf max. 900px / ~75% JPEG-Qualität).
- **Übersicht:** Tabellen- & Kartenansicht, Volltextsuche, Filter (Typ/Status/R-Strategie/Preisrange), Sortierung, Statistik-Leiste (Anzahl, Lagerwert).
- **Detailansicht:** alle Felder, Projekt-Banner, Fotogalerie mit Lightbox, Bearbeiten/Löschen.
- **Export:** CSV (alle Einträge) + PDF-Datenblatt (einzeln, gebrandet).

### Authentifizierung (Phase 2)
- **Login-Screen:** Passwort-Pflicht beim App-Start; Login gilt bis Browser-Tab schließt (sessionStorage).

### Drive-Sync (Phase 2)
- **OAuth-Verbindung:** Modaler Setup-Dialog mit zwei Wegen:
  1. **„Neue Datenbank erstellen"** → App legt `refloat-data.json` in „Meine Ablage" an.
  2. **„Bestehende Datenbank wählen"** → Google Picker für Datei in „Geteilt mit mir" oder „Meine Ablage".
- **Auto-Sync:** Jede Änderung wird ~1,5s debounced nach Drive geschrieben.
- **Auto-Reconnect:** Nach Reload stille Re-Authentifizierung mit `prompt:'none'` + E-Mail-Hint. Account-Picker erscheint praktisch nie.
- **Team-Sharing:** Datei (oder enthaltender Ordner) per Drive-UI mit Teammitgliedern teilen. Andere Teammitglieder wählen sie via Picker. Berechtigungen werden vom Ordner an alle enthaltenen Dateien (inkl. zukünftiger Fotos) vererbt.

### Fotos als Drive-Dateien (Phase 3)
- Beim Speichern werden neue Fotos als einzelne JPEG-Dateien in den **gleichen Drive-Ordner** wie `refloat-data.json` hochgeladen (Parent-Ordner wird via `drive.files.get(fields:parents)` ermittelt).
- In der JSON steht pro Foto nur noch `{id, n}` (Drive-File-ID + Dateiname) statt der vollen Base64-Daten.
- Anzeige lazy: Platzhalter sofort, im Hintergrund werden Fotos via Cache geladen (`photoCache` Map). Beim PDF-Export werden alle benötigten Fotos vorab geholt, bevor `window.print()` ausgelöst wird.
- **Backwards-kompatibel:** Alte Base64-Einträge funktionieren weiterhin; werden beim nächsten Editieren+Speichern automatisch auf Drive ausgelagert („Soft-Migration").
- Beim Löschen eines Eintrags / einer Position werden die zugehörigen Foto-Dateien aus Drive entfernt (fire-and-forget).

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
5. **Konfliktstrategie aktuell:** Last-write-wins. Kein Konflikterkennungs- oder Merge-Mechanismus.
6. **Photo-Lifecycle:** Beim Löschen einer Position werden zugehörige Drive-JPEGs gelöscht. Beim Entfernen einzelner Fotos aus einer Position werden diese beim nächsten Speichern aus Drive entfernt. Falls Drive-Auth zwischen Edit und Save abläuft, werden Fotos lokal als Base64 gespeichert (Fallback).

## ⚠️ Bekannte Schwachstellen (für später)
1. **Kein Auto-Refresh anderer Änderungen.** Wenn Person A speichert, sieht Person B die Änderung erst nach Page-Reload. Workaround: regelmäßig F5. **Fix:** Polling alle ~30s auf `modifiedTime` der Drive-Datei + neuladen bei Änderung.
2. **Last-write-wins-Konflikte.** Zwei parallele Bearbeitungen → der zweite Speichern überschreibt den ersten. **Fix:** Versions-Check beim Speichern (z.B. `modifiedTime` vor Save prüfen, warnen wenn neuer).

## ⏭️ Nächster Schritt
Erst **mit dem Team in der Praxis testen**. Danach Schwachstelle 1 (Auto-Refresh) angehen, wenn sie sich als störend zeigt — Schwachstelle 2 ist bei 2–3 Personen meist unkritisch.

## GitHub
- Öffentliches Repository: `urbanmatter/refloat-inventory`
- Branch: `main` (direkt commiten, kein PR-Workflow nötig)
- Commits werden via `git push origin main` direkt nach GitHub Pages deployed (~1 Min Verzögerung)
- Co-Author bei AI-unterstützten Commits: `Claude Sonnet 4.6 <noreply@anthropic.com>`
