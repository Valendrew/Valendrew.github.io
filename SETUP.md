# Maintenance and publishing

This directory is an independent Git repository. Run all commands from this directory, never from the parent career repository.

Create the empty **public** repository `Valendrew/Valendrew.github.io` on GitHub (do not initialise it with a README, licence or .gitignore), then run:

```bash
cd "/home/valendrew/Projects/resume-portfolio/github-profile/portfolio"
git remote add origin git@github.com:Valendrew/Valendrew.github.io.git
git add .
git commit -m "Add portfolio" 
git push -u origin main
```

If a remote is already attached, inspect `git remote -v` and skip `remote add` when it is correct. Never replace the parent repository's remote. Later updates use `git add .`, `git commit`, and `git push` from this directory.

In GitHub Settings → Pages, select **Deploy from a branch**, **main**, **/ (root)** and Save. The site will be available at https://valendrew.github.io/ after deployment completes. `.nojekyll` serves the HTML/CSS directly; no build step or custom Actions workflow is needed.

## Local preview

Run `python3 -m http.server 8000` here, then open http://localhost:8000/. Stop with Ctrl+C.

## Content updates

Edit `index.html` for the introduction and project cards and `styles.css` for appearance.

The single source of truth for CV content is the current LaTeX CV under `application-materials/portfolio/` in the parent workspace, as identified by its `index.md`. The website currently mirrors **portfolio CV v2** (`cv-v2.tex` and `v2/Andrea-Valente-CV.pdf`).

For each CV update, copy the canonical PDF unchanged to `assets/Andrea-Valente-CV.pdf` and mirror the canonical wording in `cv/index.html`. Never rebuild, redact, or maintain a separate PDF variant for this website. Make any requested CV changes in the canonical source first. Verify that the copied PDF has the same SHA-256 checksum as the source, and check the HTML against that version. Keep the homepage consistent with the current public CV's contact and location wording. Source archives and private career evidence do not belong here.

Keep project descriptions and links aligned with the profile README. Preserve academic/team attribution and qualified claims. Check mobile layout, keyboard focus, print preview, internal links and PDF download after changes. No external runtime dependencies or analytics are used.

[GitHub Pages setup](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
