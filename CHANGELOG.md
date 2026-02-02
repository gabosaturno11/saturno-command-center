# CHANGELOG — Saturno Command Center V3

## PASS 8: Mind Map V2 — Canvas Engine Rebuild (2026-02-02)

### Viewport Transform System (Phase 1A)
- Replaced scroll-based panning with CSS `transform: translate() scale()` on `#mm-viewport`
- `mmScreenToCanvas()` coordinate converter for all interactions
- Mouse wheel zoom (toward cursor), +/-/0 keyboard zoom, Cmd+/Cmd- zoom
- Space+drag or middle-click to pan from any tool
- Fit-to-view button sizes canvas to show all nodes

### Dot Grid Overlay (Phase 1B)
- Miro-style viewport-locked dot grid (not content-attached)
- Minor dots (20px, `rgba(255,255,255,0.07)`) + major dots (100px, `rgba(255,255,255,0.18)`)
- Auto-hides when zoomed out too far (grid spacing < 4px screen)
- Grid toggle (G key), snap-to-grid toggle (S key)

### Tools & Interaction
- **Arrow/Select tool**: click-select, box-select (rubber band), multi-drag
- **Hand tool**: pan canvas, cursor: grab/grabbing
- **Shape tool**: rectangle, circle, diamond, pill — subpanel picker
- **Text tool**: pure floating text (no box), auto-delete empty text
- **Sticky note tool**: 5 color options, auto-place with color
- **Connect/Line tool**: click source → click target, straight/curved/step styles
- Auto-return to arrow after placing any shape, text, or sticky

### Undo/Redo
- `Cmd+Z` undo, `Cmd+Shift+Z` redo, 50-step history
- Full state snapshot before every mutation (add, delete, move, resize, style change)

### Floating Toolbar (Miro-style)
- Converted vertical 44px sidebar to horizontal floating top bar
- Centered at top of canvas with rounded corners + shadow
- Submenus pop down instead of right
- Zoom controls + grid/snap toggles inline, separated by vertical dividers
- All events isolated — toolbar clicks don't trigger canvas actions

### Bug Fixes
- Node disappearing after switching from hand→arrow (DOM rebuild retarget guard)
- Accidental node snap-on-click (5px drag threshold)
- Box-select clearing immediately (mouseup→click race condition flag)
- Tool switch state cleanup (panning, drag, multi-drag, box-select reset)
- Node cursor: `move` icon (cross) in select mode, distinct from hand `grab`

### Files Changed
- `index.html` — Canvas engine rebuild + floating toolbar (4255 lines)
- `CHANGELOG.md` — Updated (this entry)

---

## ROADMAP — Next Phases

### Phase 2: Enhanced Node Types
- Image nodes (paste/drag-drop images onto canvas)
- Container/group nodes (parent frames that hold children)
- Hexagon, triangle, parallelogram shapes

### Phase 3: Interactions & Polish
- Copy/paste nodes (`Cmd+C` / `Cmd+V`)
- Duplicate nodes (`Cmd+D`)
- Multi-node alignment (align left, center, distribute)
- Connection labels (text on lines)
- Minimap navigator (bottom-right corner)

### Phase 4: Collaboration & Export
- Real-time cursor trails (multi-user prep)
- PNG/SVG export with proper zoom/bounds
- JSON import/export for sharing boards
- Template boards (brainstorm, flow chart, mind map tree)

### Phase 5: Sidebar & Navigation
- Side-to-side mouse panning (edge scroll)
- Layers panel (show/hide groups of nodes)
- Node search/filter
- Keyboard navigation between nodes (Tab, arrow keys)

---

## PASS 6: Design Polish (2026-01-29)

### Spacing System
- Introduced 8px grid via CSS custom properties (`--sp-1` through `--sp-8`)
- All padding, gap, and margin values now derive from the spacing scale
- Added `--content-max: 960px` and `--prose-max: 720px` for readable line-lengths

### Card Consistency
- Unified `.card`, `.research-card`, `.internal-card` to shared radius (`--radius-md`) and spacing tokens
- Card padding standardized to `--sp-4` (16px), card-header margin to `--sp-3` (12px)
- TOC items use spacing tokens for padding and gap

### Typography & Readability
- Quill editor: font-size 15px, line-height 1.9, max-width 720px, paragraph spacing
- Quill toolbar padded to `--sp-2 --sp-3`
- Card titles set to `line-height: 1.3`, exercise items to `line-height: 1.4`
- Input fields get `line-height: 1.4` for consistent text baselines
- Badge component uses `line-height: 1` to prevent vertical overflow

### Mode Pills (Premium)
- Fixed height (32px) with `inline-flex` centering
- Inactive: subtle `#52525b` text, `#27272a` border (darker, less noisy)
- Hover: surface background + soft border lift
- Active: dual-layer glow — outer `box-shadow` + inner `inset` glow, gold border at 50% opacity
- Range slider thumbs gain `box-shadow` glow

### Mobile Responsive
- **1024px**: header/kernel wrap, sidebar shrinks to 180px, internal grid 2-col
- **768px**: full vertical stack — sidebar becomes horizontal band (max-height: 240px), tabs scroll horizontally, kernel bar hidden, matrix sidebar stacks above graph, voice pills wrap, modals go 92vw, gallery grid adapts to 160px min
- **480px**: pills shrink to 24px height, gallery goes single-column, font sizes reduced

### Files Changed
- `index.html` — CSS design system overhaul (3507 lines)
- `CHANGELOG.md` — Created (this file)

---

## PASS 7: Stability & Professional Polish (2026-01-29)

### TOC Hierarchy Redesign
- Removed all gold/yellow styling from TOC items (user feedback: "noisy and unprofessional")
- New white-opacity hierarchy: Part (#ffffff bold 14px) → Chapter (75% opacity 12px) → Section (45% opacity 11px)
- Consistent indentation: Part flush, Chapter +24px, Section +48px
- Part left-border: 3px solid white at 25% opacity
- Collapsible tree: solid chevron (▶), default collapsed, state persists in `S._tocCollapse`

### Codex Checkbox Persistence (Bug Fix)
- Root cause: `buildMatrixFilters()` always set all checkboxes to checked with no persistence
- Added `S._matrixFilters` state object to persist filter selections across tab switches
- `persistMatrixFilters()` called on every checkbox change
- `isChecked()` helper restores saved state when filters rebuild
- `resetMatrixFilters()` clears persisted state
- `initMatrix()` now applies saved filters after build

### Workout Creator Inputs
- Created `buildWoItemHTML()` shared renderer for all workout item display
- Four labeled columns: Sets, Reps, Rest, Tempo — mono labels, centered inputs
- Stage color-coded dot + left border per exercise
- Unified rendering across: drag-and-drop add, saved workout load, template load
- All exports (CSV, TXT, PDF) now include Tempo field
- `saveWorkout()` captures Tempo in saved state

### Files Changed
- `index.html` — TOC, Matrix, Workout stability fixes (3596 lines)
- `CHANGELOG.md` — Updated (this entry)
