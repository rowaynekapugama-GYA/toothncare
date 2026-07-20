# Tooth n Care — Homepage

Dark-theme homepage concept for Tooth n Care Dental Clinic, 135 Lawes Street, East Maitland NSW.

## Deploying with GitHub Pages

`index.html` at the repository root is fully self-contained (all local images are embedded), so GitHub Pages works out of the box:

1. Push this repository to GitHub.
2. Settings → Pages → Source: "Deploy from a branch" → branch `main`, folder `/ (root)`.
3. The site will be live at `https://<username>.github.io/<repo>/`.

## Structure

- `index.html` — the production page (self-contained build; deploy this).
- `src/index.html` — editable source that references images in `src/assets/` instead of embedding them.
- `src/assets/` — the local source images (clinic photos, logo).
- `src/build.py` — inlines `src/assets/` images into a single self-contained file. Run from `src/`: `python3 build.py` (writes `src/dist/toothncare-home.html`; copy it to the repo root as `index.html`).

## Notes

- Fonts load from Google Fonts (Playfair Display, Figtree); an internet connection is needed for full typography.
- Some imagery is hot-linked and marked for replacement with `data-placeholder` attributes:
  - `data-placeholder="stock"` — Unsplash placeholders in the Services mega menu.
  - `data-placeholder="old-site"` — team portraits from the current toothncare.com.au site.
  - `data-placeholder="higgsfield"` / `"higgsfield-ba"` — AI-generated placeholder imagery (Smile Transformations panels are illustrative renders; disclaimer included on-page).
  - Featured service tiles and team photos also hot-link imgur/live-site URLs.
  Replace these with final photography before launch; local fallbacks (gradients/initials) display automatically if a link fails.
- Internal links to sub-pages (`/services/...`, `/our-team`, `/offers`, `/payment-options`, `/conditions-we-treat`, `/contact`, `/emergency`) are placeholders for pages yet to be built. On a GitHub Pages *project* site these would also need the repo base path.
- The theme toggle (footer) switches light/dark via `data-theme` on `<html>`; default is dark. Preference intentionally isn't persisted.
- Booking links point to the live DentalHub booking system.
- All offers/pricing and the before/after imagery should be confirmed with the practice (and their AHPRA compliance advisor) before launch.
