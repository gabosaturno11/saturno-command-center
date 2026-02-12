# Saturno Command Center V3

## TITAN Design System

**Codename:** TITAN  
**Aesthetic:** Deep-space dark UI, gold accent, surgical precision  
**Architecture:** Single-file HTML app (~4400 lines), zero build tools, zero frameworks  
**Password:** `saturno2026`

---

### Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg-void` | `#0a0a0c` | Body background, deepest layer |
| `--bg-deep` | `#0f1014` | Canvas, inputs, card interiors |
| `--bg-surface` | `#151519` | Cards, panels, toolbar |
| `--bg-elevated` | `#1a1a1f` | Modals, popups |
| `--accent-gold` | `#ffaa00` | Primary accent, active states, CTA |
| `--accent-success` | `#00ff88` | Resolved, positive states |
| `--accent-warning` | `#ff6b35` | Open items, alerts |
| `--accent-danger` | `#ff4466` | Delete, destructive actions |
| `--accent-blue` | `#00cfff` | Informational |
| `--accent-purple` | `#a855f7` | Tertiary accent |
| `--text-primary` | `#ffffff` | Headlines, values |
| `--text-secondary` | `rgba(255,255,255,0.6)` | Body text |
| `--text-tertiary` | `rgba(255,255,255,0.3)` | Labels, timestamps |
| `--border-subtle` | `rgba(255,255,255,0.06)` | Default borders |
| `--border-hover` | `rgba(255,255,255,0.12)` | Hover state borders |
| `--border-active` | `rgba(255,170,0,0.4)` | Focus/active borders |

### Typography

| Token | Font | Usage |
|-------|------|-------|
| `--font-display` | Sora (300-700) | All UI text, headings, body |
| `--font-mono` | JetBrains Mono (400-700) | Labels, counters, code |

### Spacing (8px Grid)

| Token | Value |
|-------|-------|
| `--sp-1` | 4px |
| `--sp-2` | 8px |
| `--sp-3` | 12px |
| `--sp-4` | 16px |
| `--sp-5` | 24px |
| `--sp-6` | 32px |
| `--sp-8` | 48px |

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 6px | Buttons, inputs, badges |
| `--radius-md` | 10px | Cards, nodes |
| `--radius-lg` | 14px | Panels, modals |

### Layout

| Element | Size |
|---------|------|
| Header | 52px |
| Kernel bar | 40px |
| Sidebar | 220px / 260px wide |
| Content max-width | 960px |
| Prose max-width | 720px |
| Floating toolbar | auto, centered 12px from top |
| Tool buttons | 36x36px |

### Canvas Engine (Whiteboard)

- CSS `transform: translate(panX, panY) scale(zoom)` viewport
- Zoom: 0.1x - 4.0x
- Dot grid: 20px minor / 100px major, viewport-locked
- 5px drag threshold, 50-step undo, node locking
- 4 arrowhead styles: triangle, open, diamond, dot

### External Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| Sora + JetBrains Mono | Google Fonts | Typography |
| Quill.js | 1.3.6 | Rich text editor |
| Sortable.js | 1.15.0 | Drag-and-drop |
| Cytoscape.js | 3.28.1 | Graph rendering |
| pdfmake | 0.2.7 | PDF export |
| kjua | 0.9.0 | QR/barcode |
| SheetJS | 0.18.5 | Excel export |

### Persistence

- `localStorage` key: `scc3` (main state)
- `localStorage` key: `scc_doc` (Quill editor)
- Auto-save on every mutation
- Error handling for quota exceeded

---

*Built for The Art of Calisthenics by Gabo Saturno*  
*Saturno Movement | 2026*

[Live App](https://github.com/gabosaturno11/victory-belt-cc)