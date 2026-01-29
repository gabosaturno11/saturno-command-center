# CHANGELOG — Saturno Command Center V3

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
