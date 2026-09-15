# CV website — Ángel Domínguez

Personal CV website built with Django and published as a static site on GitHub Pages.

Django is only used as a template renderer for local development: `build_static.py`
renders the page to plain HTML into `docs/`, which is what GitHub Pages serves.
Nothing runs server-side in production.

## Structure

- `angel_cv/` — Django project.
  - `portfolio/templates/portfolio/home.html` — the whole page (all content lives here).
  - `static/` — source assets (CSS, JS, fonts, images, PDFs).
  - `staticfiles/` — `collectstatic` output; generated, not tracked in git.
- `build_static.py` — renders the template and copies assets into `docs/`.
- `docs/` — generated static site served by GitHub Pages. Regenerate it, don't edit by hand.

## Local preview

```bash
cd angel_cv
pip install -r requirements.txt
python manage.py runserver
```

Then open http://127.0.0.1:8000/. Template changes show up on browser refresh.

## Publishing

```bash
python build_static.py
git add -A
git commit -m "Update CV"
git push
```

`build_static.py` rebuilds `docs/` from scratch, so always run it before committing
if the template or any asset changed.

## Credits

Based on the "Minimal" template by [Untree.co](https://untree.co/), licensed under
[CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). See
`angel_cv/portfolio/templates/portfolio/README.txt` for the full template credits.
