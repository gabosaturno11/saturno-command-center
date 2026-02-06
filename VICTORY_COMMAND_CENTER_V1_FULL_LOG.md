# VICTORY COMMAND CENTER V1 — Full Log
## THE ART OF CALISTHENICS
### By: Victory Belt & Gabo Saturno

---

**Application:** Saturno Command Center V3
**Built:** January 29, 2026
**Architect:** Claude Code (Opus 4.5) for Gabo Saturno
**Tech:** Single-file HTML app (~3,680 lines) | TITAN Design Language
**State:** localStorage under key `scc3`
**Deploy:** GitHub Pages via `npx gh-pages -d .`

---

## TABLE OF CONTENTS

1. [Architecture Overview](#1-architecture-overview)
2. [TITAN Stabilization Pass — 18 Fixes](#2-titan-stabilization-pass)
3. [Second Stabilization Pass — 9 Improvements](#3-second-stabilization-pass)
4. [Third Stabilization Pass (Apsis) — 24 Improvements](#4-third-stabilization-pass)
5. [Pass 6 — CEO Lens Excellence — 11 Improvements](#5-pass-6--ceo-lens-excellence)
6. [Pass 6B — Visual Gallery Grid](#6-pass-6b--visual-gallery-grid)
7. [Pass 6C — Design Polish (8px Grid + Mobile)](#7-pass-6c--design-polish)
8. [Pass 7 — Stability & Professional Polish](#8-pass-7--stability--professional-polish)
9. [Pass 8 — Final Refinements](#9-pass-8--final-refinements)
10. [Running Totals](#10-running-totals)
11. [State Schema](#11-state-schema)
12. [Locked Structures](#12-locked-structures)

---

## 1. ARCHITECTURE OVERVIEW

### 15 Tabs

| # | Tab | Purpose |
|---|-----|---------|
| 1 | **TOC** | Dual-pane Table of Contents editor with drag-reorder, version comparison, Part/Chapter/Section hierarchy, collapsible tree |
| 2 | **Writing** | Quill.js rich text editor with 7 voice modes, refinement sliders, per-chapter storage, preview pane |
| 3 | **Decisions** | Decision log + bottleneck tracker — drag-and-drop reorderable, inline scratchpad creation |
| 4 | **Research** | A/B/C/D research card framework — Core Concept, Supporting Evidence, Application, Contradictions |
| 5 | **HTMLs** | Visual gallery grid with modal preview, drag-and-drop upload, tag filtering, HTML + image support |
| 6 | **Matrix** | Cytoscape.js directed graph — 95+ nodes, 119+ edges, filterable + query engine (7 query types) |
| 7 | **Taxonomy** | Sortable/filterable table of all movement nodes with click-to-inspect editable detail panel |
| 8 | **Workout** | Drag-and-drop workout builder with Sets/Reps/Rest/Tempo/Notes, templates, analytics, PDF export |
| 9 | **Mind Map** | Freeform draggable node map with SVG connections, 5 shapes, curved edges, PNG/SVG export |
| 10 | **Barcode** | QR code generator (kjua) with presets and custom URL support |
| 11 | **Vault** | Knowledge Vault — document library with categories, cross-referencing, search |
| 12 | **Dashboard** | Overview dashboard — stats, writing progress, matrix coverage, decisions, bottlenecks |
| 13 | **Calendar** | Excel/CSV parser (SheetJS) with calendar grid renderer, PDF/CSV export |
| 14 | **Export** | Centralized export hub — JSON, MD, HTML, Word, PDF, CSV, Full State Backup, Export Bundle |
| 15 | **Internal** | Password-protected deployment forge — storage usage, locked structures, build info, state import/export |

### Tech Stack

| Library | Version | Purpose |
|---------|---------|---------|
| Quill.js | 1.3.6 | Rich text editing |
| Sortable.js | 1.15.0 | Drag-and-drop reordering |
| Cytoscape.js | 3.28.1 | Graph visualization |
| pdfmake | 0.2.7 | PDF generation |
| SheetJS | 0.18.5 | Excel/CSV parsing |
| kjua | 0.9.0 | QR code generation |

All loaded via CDN. No build step required.

### Design Language: TITAN

```css
--bg-void:    #0a0a0c
--bg-deep:    #0f1014
--bg-surface: #151519
--accent-gold: #ffaa00
--accent-glow: rgba(255,170,0,0.12)
```

**Fonts:** Sora (display) + JetBrains Mono (code/labels)
**Spacing:** 8px grid (`--sp-1` through `--sp-8`)
**Breakpoints:** 1024px, 768px, 480px

### Data Files

```
data/
  movement_matrix.json                     — 95 nodes, 119 edges, enums, toc_anchors
  research.json                            — 10 research cards with A/B/C/D blocks
  toc.json                                 — v1 (7 Parts) and v2 (25 Chapters) structures
  htmls.json                               — HTML file references
  saturno_7_patterns_complete.csv          — 72 movements (source)
  saturno_movement_matrix_foundation.csv   — 10 mobility roots (source)
  saturno_cross_cutting_categories.csv     — 13 infrastructure nodes (source)
  saturno_notes_to_matrix_integration.csv  — 12 chapter-to-node mappings (source)
```

---

## 2. TITAN STABILIZATION PASS

**Date:** January 29, 2026
**Scope:** Bug fixing + mandatory UX normalization. NO new features.
**Priority:** Data Safety > State Persistence > Export Reliability > Editing UX Consistency

### A. State & Data (4 fixes)

| ID | Fix | Detail |
|----|-----|--------|
| A1 | Confirmation dialogs | Added `confirm()` to all destructive actions: `delTOCItem()`, `resolveBottleneck()` |
| A2 | Save failure alerts | `save()` now alerts on localStorage failure; fixed `stageNames` reference orphan bug |
| A3 | Reset to last saved | New `resetToLastSaved()` function + header button; reloads from localStorage |
| A4 | Clean compare exit | `loadTOC()` clears `.mismatch` highlights when switching versions |

### B. Export (2 fixes)

| ID | Fix | Detail |
|----|-----|--------|
| B1 | Download reliability | `dl()` now DOM-appends anchor before click, removes with 100ms delay before revoking URL |
| B2 | Export Bundle | New `exportBundle()` — one-click export of TOC JSON, Research JSON, Matrix JSON, Writing MD, Full State Backup |

### C. TOC UX (4 fixes)

| ID | Fix | Detail |
|----|-----|--------|
| C1 | Double-click edit | `ondblclick="editTOCItem()"` on title spans |
| C2 | Visual hierarchy | Parts bold + gold border, Sections indented + italic + reduced opacity |
| C3 | Full labels | `typeLabel()` returns `Part`/`Chapter`/`Section` instead of `P`/`C` |
| C4 | Global sync | New `syncTOCEverywhere()` + `reorderTOCFromDOM()` — kernel bar, writing sidebar, TOC panels stay in sync |

### D. Writing Hub (2 fixes)

| ID | Fix | Detail |
|----|-----|--------|
| D1 | Preview toggle | Split-pane preview with Georgia serif rendering, toggled via toolbar button |
| D2 | Per-chapter storage | `selectWritingChapter()` loads from `scc_doc_{title}`; doc-title changes sync to TOC |

### E. Matrix (2 fixes)

| ID | Fix | Detail |
|----|-----|--------|
| E1 | Node deletion | `deleteMatrixNode(id)` with confirm; removes node + edges, rebuilds graph |
| E3 | Node selector | Searchable sidebar list, `focusMatrixNode(id)` animates camera to node |

### F. Codex/Taxonomy (3 fixes)

| ID | Fix | Detail |
|----|-----|--------|
| F1 | Stage name + number | Displays "Stage 1 — Creating the Base" throughout |
| F2 | Editable stage names | `editStageName()` persists to `S.stageNames` |
| F3 | Click-to-inspect | Slide-out context panel shows full node details (edges, function, prerequisites) |

**Subtotal: 18 fixes**

---

## 3. SECOND STABILIZATION PASS

**Date:** January 29, 2026 — Night Session

| ID | Feature | Detail |
|----|---------|--------|
| SS1 | Codex bug fix | Taxonomy overflow layout restructured, no-results message |
| SS2 | Exercises from Taxonomy | 115+ exercises auto-loaded from `matrixData`, stage color-coded (green/blue/yellow/red) |
| SS3 | Cloud links | Dropbox + OneDrive quick-access buttons in TOC sidebar |
| SS4 | CSV parser | `parseAllCSVs()` rebuilds matrix from 4 source CSVs (96 movements + 12 TOC anchors) |
| SS5 | Add Edge UI | Modal to create relationships between nodes (type + transfer scale) |
| SS6 | Matrix CRUD | Filter counts, search highlighting, Enter focus, Edit-in-Codex bridge |
| SS7 | Research A/B/C/D | Expandable cards, per-block copy with toast, usage tracking/filtering |
| SS8 | Workout builder | Stage filter, drag-to-build with Sets/Reps/Rest, named save, CSV export |
| SS9 | Mindmap | Connect Mode (click 2 nodes), PNG export, named save/load, edge labels |

**Subtotal: 9 improvements | Running total: 27**

---

## 4. THIRD STABILIZATION PASS

**Date:** January 29, 2026 — Late Night (Apsis Quality Polish)
**Objective:** Transform from functional to impressive for Victory Belt

### M. Writing Hub — Professional Author Tools

| ID | Feature | Detail |
|----|---------|--------|
| M1 | 8 writing modes | Raw, Teacher, Philosopher, Prophet, Mystic, Companion, Confessor, Rebel — color-coded pills, `color-mix()` editor tinting |
| M2 | Writing commands | Compress, Expand, Simplify, Deepen, Polish — generates Claude-ready prompts with active mode |
| M3 | Word count | Live word count on `text-change`, clickable target, progress bar, persists in `S._wordTarget` |

### N. TOC — Professional Book Structure

| ID | Feature | Detail |
|----|---------|--------|
| N1 | Typography | Part 16px bold CAPS gold / Chapter 14px white / Section 12px italic |
| N2 | Three versions | v3 ("Working Draft") added to dropdowns |
| N3 | Movement badges | Gold badges showing linked movements per chapter from matrix anchor edges |
| N4 | Analytics panel | Parts, Chapters, Sections, Total, Movement Links coverage % |

### O. Workout — Professional Training Tools

| ID | Feature | Detail |
|----|---------|--------|
| O1 | 6 templates | Full Body Foundation, Push Day, Pull Day, Leg Day, Mobility Flow, Core Circuit |
| O2 | Card display | Workout items as styled cards with stage-colored left border |
| O3 | Analytics | Exercises, total sets, total reps, estimated duration, pattern coverage |
| O4 | PDF export | pdfmake PDF table: Exercise / Sets / Reps / Rest |

### P. Taxonomy — Professional Data Table

| ID | Feature | Detail |
|----|---------|--------|
| P2 | Discipline colors | Color-coded pills per discipline |
| P3 | Sortable columns | Click headers to sort asc/desc |
| P4 | Discipline filter | Dropdown filter added to toolbar |

### Q. Knowledge Vault (NEW TAB)

| ID | Feature | Detail |
|----|---------|--------|
| Q1 | Document library | Search, category filter, CRUD operations |
| Q2 | Document viewer | Full viewer with pre-wrap rendering, Edit/Copy/Delete |
| Q3 | Cross-referencing | Auto-scans for references to research cards, TOC chapters, matrix movements |
| Q4 | Vault export | JSON export of entire vault |

### R. Persistent Memory

| ID | Feature | Detail |
|----|---------|--------|
| R1 | Version history | `saveWithHistory()` stores last 10 snapshots in `S._versions` |
| R2 | Session recovery | Notification on load if last session < 24h ago |

### S. Mindmap — Enhanced Creation

| ID | Feature | Detail |
|----|---------|--------|
| S1 | Shape palette | Rectangle, Circle, Diamond, Hexagon, Pill — with CSS clip-path |
| S2 | Connection tools | Curved bezier edges, bidirectional markers, edge labels |
| S4 | SVG export | Clean SVG output with TITAN dark background |

### T. Dashboard (NEW TAB)

| ID | Feature | Detail |
|----|---------|--------|
| T1 | Overview | 6 stat cards, writing progress, matrix coverage, recent decisions, active bottlenecks |

**Subtotal: 24 improvements | Running total: 51**

---

## 5. PASS 6 — CEO LENS EXCELLENCE

**Date:** January 29, 2026 — Final Session
**Objective:** Make the command center impossible for Victory Belt to reject

### U. Writing Hub — Voice Mode Redesign

| ID | Feature | Detail |
|----|---------|--------|
| U1 | Unified gold pills | Replaced per-color pills with unified gold active state; removed `color-mix()` complexity |
| U2 | Refinement sliders | Compression (0-100%) + Technical Depth (0-100%) sliders; integrated into `writingCommand()` prompts |

### V. HTML Upload System

| ID | Feature | Detail |
|----|---------|--------|
| V1 | Upload zone | Drag-and-drop zone with dashed border, accepts `.html`/`.htm` |
| V2 | Upload handler | `handleHTMLUpload()` reads via FileReader, stores content in state, supports `srcdoc` preview |
| V3 | Tag system | Tag filter dropdown, colored borders per tag, combined search + tag filtering |

### X. Calendar (NEW TAB)

| ID | Feature | Detail |
|----|---------|--------|
| X1 | SheetJS library | `xlsx@0.18.5` CDN added |
| X2 | Calendar tab | 15th tab with sidebar (upload, sheet list, export) and content area |
| X3 | Excel parser | `handleExcelUpload()` reads `.xlsx/.xls/.csv`, multi-sheet support |
| X4 | Calendar grid | Auto-detects day/week columns, CSS grid with gold headers |
| X5 | Data table | Fallback table for non-calendar sheets; PDF/CSV export; "Build Workout" extraction |

### Y. Matrix Query Engine

| ID | Feature | Detail |
|----|---------|--------|
| Y1 | 7 query types | Prerequisites, Unlocks, Path (BFS), Cluster (BFS), Pattern, Stage, Orphans — result highlighting in graph |

**Subtotal: 11 improvements | Running total: 62**

---

## 6. PASS 6B — VISUAL GALLERY GRID

**Date:** January 29, 2026

| Change | Detail |
|--------|--------|
| Card grid layout | Responsive gallery replacing dual-iframe layout (`repeat(auto-fill, minmax(200px, 1fr))`) |
| Modal preview | 92vw x 90vh overlay — iframe for HTML, `<img>` for images |
| Image upload | Extended to accept `.png/.jpg/.gif/.svg/.webp`, reads as DataURL |
| Type filter | Dropdown: All / HTML / PNG |
| Schema extension | `desc`, `date`, `fileType` fields on `htmlFiles` objects |

**Running total: 63**

---

## 7. PASS 6C — DESIGN POLISH

**Date:** January 29, 2026

### Spacing System
- 8px grid via `--sp-1` (4px) through `--sp-8` (48px)
- `--content-max: 960px`, `--prose-max: 720px`
- All padding, gap, margin values derived from spacing scale

### Card Consistency
- Unified `.card`, `.research-card`, `.internal-card` to `--radius-md` + `--sp-4` padding
- Card-header margin standardized to `--sp-3`

### Typography & Readability
- Quill editor: 15px font, 1.9 line-height, 720px max-width, paragraph spacing
- Card titles `line-height: 1.3`, exercise items `line-height: 1.4`
- Badge `line-height: 1` to prevent overflow

### Mode Pills (Premium)
- 32px fixed height with `inline-flex` centering
- Dual-layer glow on active: outer `box-shadow` + inner `inset`, gold border 50% opacity

### Mobile Responsive
- **1024px:** header/kernel wrap, sidebar 180px, internal grid 2-col
- **768px:** vertical stack, sidebar horizontal band, tabs scroll, kernel hidden, modals 92vw
- **480px:** pills 24px height, gallery single-column, font sizes reduced

**Running total: 64**

---

## 8. PASS 7 — STABILITY & PROFESSIONAL POLISH

**Date:** January 29-30, 2026

### TOC Hierarchy Redesign
- Removed ALL gold/yellow from TOC items (user: "noisy and unprofessional")
- White-opacity hierarchy: Part (`#ffffff` bold 14px) > Chapter (75% opacity 12px, +24px indent) > Section (45% opacity 11px, +48px indent)
- Part left-border: 3px solid `rgba(255,255,255,0.25)`
- Collapsible tree with solid chevron (▶), default collapsed
- State persists via `S._tocCollapse`
- `toggleTOCCollapse()` function with DOM + state sync

### Codex Checkbox Persistence (Bug Fix)
- **Root cause:** `buildMatrixFilters()` always set all checkboxes to `checked`, no persistence
- **Fix:** Added `S._matrixFilters` state object
- `persistMatrixFilters()` saves checked values on every change
- `isChecked(type, val)` helper restores state when filters rebuild
- `resetMatrixFilters()` clears persisted state
- `initMatrix()` calls `applyMatrixFilters()` after build

### Workout Creator — Full Input Rebuild
- Created `buildWoItemHTML(name, sets, reps, rest, tempo, notes)` shared renderer
- 5 labeled columns: Sets, Reps, Rest, Tempo, Notes — mono labels, centered inputs
- Stage color-coded dot + left border per exercise
- Notes field: transparent inline text input, shows border on focus
- Unified across all 4 callsites: `onAdd`, `loadSavedWorkout()`, `loadWorkoutTemplate()`, new item
- `saveWorkout()` captures tempo + notes
- CSV export: Exercise, Sets, Reps, Rest, Tempo, Notes
- TXT export: `name — SxR (Rs rest) @tempo [notes]`
- PDF export: 6-column table with Notes

**Running total: 67**

---

## 9. PASS 8 — FINAL REFINEMENTS

**Date:** January 30, 2026

### Decisions & Bottlenecks — Drag-and-Drop + Scratchpad

| Change | Detail |
|--------|--------|
| Drag-and-drop | Sortable.js on both `#decisions-list` and `#bottlenecks-list` with `animation: 150` |
| Drag handle | Hamburger icon (☰) on every card |
| Reorder persistence | `onEnd` splices and re-inserts in `S.decisions` / `S.bottlenecks`, saves |
| Scratchpad add (Decisions) | `+ Decision` creates inline draft card with gold border; type title + context directly; pick status (Resolved/Open/Deferred); click **Lock** to save |
| Scratchpad add (Bottlenecks) | `+ Bottleneck` creates inline draft; type title; pick priority (High/Normal); click **Lock** to save |
| Lock functions | `lockDecision(btn)` and `lockBottleneck(btn)` read inputs, prepend to array, save, toast confirmation |
| Dismiss | Draft cards have × button to cancel |

### Branding Update

| Change | Detail |
|--------|--------|
| Main title | `THE ART OF CALISTHENICS` (was "SATURNO COMMAND CENTER") |
| Subtitle | `By: Victory Belt & Gabo Saturno` — Sora font (removed mono override) |
| Page title | `<title>THE ART OF CALISTHENICS | Saturno Command Center</title>` |

**Running total: 70**

---

## 10. RUNNING TOTALS

| Pass | Changes | Cumulative | Line Count |
|------|---------|------------|------------|
| TITAN Stabilization | 18 | 18 | ~1,543 |
| Second Stabilization | 9 | 27 | ~2,325 |
| Third (Apsis) | 24 | 51 | ~2,944 |
| Pass 6 (CEO Lens) | 11 | 62 | ~3,343 |
| Pass 6B (Gallery) | 1 | 63 | ~3,400 |
| Pass 6C (Design Polish) | 1 | 64 | ~3,507 |
| Pass 7 (Stability) | 3 | 67 | ~3,604 |
| Pass 8 (Final) | 3 | **70** | **~3,680** |

### Functions Created (Key)

```
State:        save(), load(), resetToLastSaved(), saveWithHistory(), checkSessionRecovery()
TOC:          loadTOC(), editTOCItem(), delTOCItem(), syncTOCEverywhere(), reorderTOCFromDOM(),
              toggleTOCCollapse(), updateTOCAnalytics(), buildTOCText(), exportTOCMarkdown(),
              exportTOCWord(), exportTOCPDF()
Writing:      selectWritingChapter(), saveDocument(), togglePreview(), setWritingMode(),
              writingCommand(), updateWordCount(), setWordTarget()
Decisions:    initDecisions(), addDecision(), lockDecision(), addBottleneck(), lockBottleneck(),
              resolveBottleneck()
Research:     renderResearch(), toggleResearchExpand(), copyBlock(), toggleUsed(), addResearchCard()
Gallery:      renderGalleryGrid(), openGalleryModal(), closeGalleryPreview(), handleHTMLUpload(),
              getFileType(), filterHTMLs(), buildHTMLTagFilter()
Matrix:       buildCytoscape(), buildMatrixFilters(), applyMatrixFilters(), persistMatrixFilters(),
              resetMatrixFilters(), deleteMatrixNode(), focusMatrixNode(), buildMatrixNodeList(),
              openAddEdgeModal(), saveNewEdge(), editNodeInCodex(), runMatrixQuery(),
              bfsPath(), bfsCluster()
Taxonomy:     initTaxonomy(), renderTaxonomy(), sortTaxonomy(), buildTaxonomyFilters(),
              openTaxInspector(), saveTaxEdit()
Workout:      initWorkout(), buildWoItemHTML(), saveWorkout(), loadSavedWorkout(),
              loadWorkoutTemplate(), exportWorkout(), exportWorkoutTxt(), exportWorkoutPDF(),
              getWorkoutAnalytics(), updateWorkoutAnalytics(), syncExercisesFromTaxonomy()
Mindmap:      renderMindmap(), toggleConnectMode(), mmNodeClick(), exportMindmapPNG(),
              exportMindmapSVG(), saveNamedMindmap(), loadNamedMindmap()
Vault:        initVault(), filterVault(), addVaultDoc(), viewVaultDoc(), findXRefs(), exportVault()
Dashboard:    initDashboard()
Calendar:     handleExcelUpload(), renderCalendarSheet(), renderCalendarGrid(),
              renderDataTable(), exportCalendarCSV(), exportCalendarPDF()
Barcode:      initBarcode()
Export:       dl(), exportAs(), exportBundle()
CSV Parser:   parseAllCSVs()
Utility:      showToast()
```

---

## 11. STATE SCHEMA

All state lives in `S` object, serialized to `localStorage` key `scc3`.

```javascript
S = {
    tocs:               {},     // TOC versions (v1, v2, v3, custom)
    research:           [],     // Research cards with A/B/C/D blocks
    decisions:          [],     // Decision log entries {id, date, title, context, status}
    bottlenecks:        [],     // Active bottlenecks {id, title, priority}
    mindmap:            {},     // {nodes:[], edges:[]}
    documents:          {},     // Per-chapter writing content
    htmlFiles:          [],     // HTML/image file references {name, path, tag, content, desc, date, fileType}
    exercises:          [],     // Exercise library (synced from matrixData)
    matrixData:         {},     // {nodes:[], edges:[], enums:{}}
    stageNames:         {},     // Editable stage names {0:'...', 1:'...', 2:'...', 3:'...'}
    vault:              [],     // Knowledge Vault documents
    savedWorkouts:      [],     // Named workout saves {name, items[], date}
    savedMindmaps:      [],     // Named mindmap saves
    currentWritingMode: '',     // Active writing mode name
    _versions:          [],     // Version history (last 10 snapshots)
    _tocCollapse:       {},     // TOC collapse state per part/chapter
    _matrixFilters:     {},     // Matrix checkbox filter persistence
    _wordTarget:        null,   // Writing word count target
    _compression:       50,     // Writing compression slider value
    _technical:         50      // Writing technical depth slider value
}
```

---

## 12. LOCKED STRUCTURES

These are finalized and must not be modified:

| Structure | Version | Status |
|-----------|---------|--------|
| Mobility Big 7 | V4 | LOCKED |
| Movement Patterns (7) | V2 | LOCKED |
| Six Disciplines | — | LOCKED |
| Three Stages | — | LOCKED |
| TOC (7 Parts / 25 Chapters) | — | ACTIVE (still evolving) |

### Movement Matrix Schema

**Node Types:** MOVEMENT (72), MOBILITY (10), INFRASTRUCTURE (13), TOC (12)

**Stages:**
- Stage 0 — Mobility & Preparation (10 nodes)
- Stage 1 — Creating the Base (32 nodes)
- Stage 2 — Building the Structure (33 nodes)
- Stage 3 — Continuous Mastering (20 nodes)

**Edge Transfer Scale:** high (direct prerequisite), medium (supporting), low (indirect), direct (same-pattern)

---

## PROJECT FILES

```
saturno-command-center/
  index.html                              — Complete app (single file, ~3,680 lines)
  VICTORY_COMMAND_CENTER_V1_FULL_LOG.md   — This document
  CHANGELOG.md                            — Per-pass changelog
  BB_EDITS.md                             — Detailed bug fix documentation
  README.md                               — Project overview
  package.json                            — gh-pages deployment config
  data/                                   — JSON + CSV data files
  icons/                                  — SVG icons (dropbox, onedrive)
  htmls/                                  — HTML file collection
```

---

*Victory Command Center V1 — Full Log*
*Built for Gabo Saturno | Saturno Movement*
*Victory Belt Publishing | The Art of Calisthenics*
*January 29-30, 2026*
