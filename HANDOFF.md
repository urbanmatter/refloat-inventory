# 📋 Projekt-Übergabe: ReFloat Inventory

> Diese Datei dient als Übergabe-/Wiedereinstiegspunkt. Inhalt kann in einen neuen Chat kopiert werden, um nahtlos weiterzuarbeiten.

## Rolle & Kontext
Du bist ein erfahrener Full-Stack-Entwickler und hilfst mir (Gründer in der Baubranche, **kein Entwickler**) beim Bau einer professionellen Web-App zur Erfassung und Verwaltung von **rückgebautem Flachglas** aus Gebäuderückbauten. Mein Team (2–10 Personen) erfasst Gläser, kategorisiert sie und stellt sie intern und für Kunden bereit. Die App läuft im Browser. **Erkläre Dinge einfach und sag direkt, wenn du dir unsicher bist.**

## Technischer Stand
- **Eine einzige Datei:** `index.html` (HTML + CSS + JavaScript inline, ~57 KB)
- **Speicherort:** `C:\Users\sebas\Desktop\Claude Projekte\Glass Data Tool\`
- **Datenspeicher aktuell:** Browser `localStorage`, Key = `gdt_v1` (noch KEINE Cloud-Anbindung)
- **Umgebung:** Windows, Python 3.14 + Pillow 12.2 verfügbar
- **Vorschau-Server:** `.claude/launch.json` → Name `glass-static`, startet `python -m http.server 8777`

## Dateien im Projektordner
| Datei | Zweck |
|---|---|
| `index.html` | Die komplette App (mit eingebettetem Base64-Icon) |
| `ReFloat.ico` | Multi-Größen-Icon für die Desktop-Verknüpfung (NICHT löschen/verschieben) |
| `make_icon.py` | Erzeugt das Icon (violetter Verlauf, 2 Glasscheiben + Kreislauf-Pfeile) |
| `embed_icon.py` | Bettet das Icon als Base64 in `index.html` ein (Favicon + Header) |
| `HANDOFF.md` | Diese Übergabe-Datei |
| `.claude/launch.json` | Preview-Server-Config |

- **Desktop-Verknüpfung:** `C:\Users\sebas\Desktop\ReFloat Inventory.lnk` → öffnet `index.html`, nutzt `ReFloat.ico`

## Branding
- **Name:** „ReFloat Inventory", Untertitel „Datenbank für Zirkuläres Flachglas"
- **Icon** im Header, im Browser-Tab (Favicon), als Desktop-Icon und im PDF-Datenblatt
- **Farben:** Primär `#5B4BE1` (Violett), Sekundär `#1E3A5F`, Akzent `#7C6EF0`, BG `#F8F8FC`, Karten `#FFF`, Text `#1A1A2E`, Subtext `#6B7280`, Rahmen `#E5E7EB`, Danger `#E5484D`. Radien: Karten 16px, Inputs 10px, Buttons 14px. System-Font, max. Inhaltsbreite 900px, mobile-first (1 Spalte, 2 Spalten ab 600px).

## Funktionsumfang (fertig & getestet)
- **Erfassung:** Projekt-Header (Gebäude, Adresse, Rückbaujahr) + beliebig viele **Glaspositionen** (P1, P2…) mit „+ Position hinzufügen" / „×" entfernen (mind. 1 Position).
- **Pro Position:** Glastyp, dynamischer **Glasaufbau** (je nach Typ), Farbe, Beschichtung (Kurzinfo), Breite/Höhe, automatische Glasdicke & Gewicht, Stückzahl, Lagerort, Preis, Status, R-Strategie, Tags, Notizen, Foto-Upload (Drag&Drop, automatisch komprimiert).
- **Übersicht:** Tabellen- & Kartenansicht, Volltextsuche, Filter (Typ/Status/R-Strategie/Preisrange), Sortierung, Statistik-Leiste (Anzahl, Lagerwert).
- **Detailansicht:** alle Felder, Projekt-Banner, Fotogalerie mit Lightbox, Bearbeiten/Löschen.
- **Export:** CSV (alle Einträge) + PDF-Datenblatt (einzeln, gebrandet).

## Datenmodell (ein Eintrag = eine Glasposition)
```js
localStorage Key: 'gdt_v1'  // Array von Einträgen
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
  photos: [],  // Base64-Data-URLs (JPEG, max 900px, ~75% Qualität)
  at, upd      // ISO-Timestamps (erstellt / aktualisiert)
}
```

## Wichtige Logik-Entscheidungen (auf Wunsch änderbar)
1. **ID-Schema:** `[KÜRZEL]-[JAHR]-[NR]-P[Position]`. Kürzel: FG, ISO2, ISO3, VSG, ESG, VG, SONST. Laufende Nummer pro (Jahr+Typ). Positionen **desselben Typs** in einem Projekt teilen sich die Nummer und unterscheiden sich nur über `-P1/-P2`. Unterschiedliche Typen → eigene Nummer.
2. **„Maße" zeigt Glasdicke ohne Abstandshalter** (= Gewichtsbasis). Physische Gesamtdicke inkl. Abstandshalter steht nur im „Glasaufbau".
3. Position-Feld „Beschichtung (Kurzinfo)" existiert **zusätzlich** zur Beschichtung pro Glaslage (bewusst beibehalten).

## ⏭️ Nächster Schritt: Phase 2 – Google Drive Anbindung
Ziel: Daten (inkl. Fotos) zwischen allen Teammitgliedern synchronisieren, statt nur lokal im Browser.

**⚠️ Technischer Knackpunkt zuerst klären:** Google OAuth/Drive API funktioniert **NICHT mit `file://`** (lokal geöffnete HTML-Datei). Es braucht einen echten `https://`-Ursprung. Zu besprechende Optionen:
- **Hosting** der App (GitHub Pages, Netlify, Vercel — kostenlos) → empfohlen, dann läuft Drive direkt im Browser
- Alternativ: kleiner lokaler Server / Desktop-Wrapper
- Sync-Strategie: zentrale JSON-Datei in geteiltem Drive-Ordner + Fotos als separate Dateien; Konfliktbehandlung bei gleichzeitigem Bearbeiten bedenken

**Phase 2 so starten:** zuerst Hosting-/OAuth-Optionen einfach erklären und mich entscheiden lassen, bevor Code geschrieben wird.

## GitHub
- Privates Repository, nur für den Eigentümer zugänglich (siehe Repo-URL im Chat / `git remote -v`).
