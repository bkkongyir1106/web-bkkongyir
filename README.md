# Benedict Kongyir's academic website

Personal academic website built with **Hugo Extended 0.83.1** and the existing
Wowchemy Academic modules pinned in `go.mod`. Hosted at
[bkkongyir.netlify.app](https://bkkongyir.netlify.app/).

## Edit content

| Area | Source |
| --- | --- |
| Biography, appointment, education, profiles | `content/authors/admin/_index.md` |
| Homepage sections and order | `content/home/` (`weight` controls order) |
| Primary navigation | `config/_default/menus.yaml` |
| Publications, abstracts, authors, PDF URLs, citations | `content/publication/` |
| Teaching history | `content/home/teaching.md` (automatically reused on the courses page) |
| Downloadable public résumé | `static/uploads/cv.pdf` |
| Colors, fonts, responsive styling | `data/themes/`, `data/fonts/`, `assets/scss/custom.scss` |
| Homepage hero and publications layout | `layouts/partials/widgets/` |
| Native section navigation | `assets/js/academic-navigation.js` |

The résumé is a public copy based on the supplied September 2026 résumé. It
keeps email and professional links and omits the street address and phone.
The original résumé and supplied materials folder are not part of this repository.

The widget wrapper override in `layouts/partials/widget_page.html` changes
homepage section headings from H1 to H2. It is based on the pinned Wowchemy
version; review it if upgrading the theme later.

## Common updates

- **Teaching:** edit only `content/home/teaching.md`; both teaching views update.
- **New résumé:** replace `static/uploads/cv.pdf` with your new public PDF, keeping the filename. All download links will continue working.
- **New publication:** copy an existing folder under `content/publication/`, give it a descriptive name, then edit `index.md` and `cite.bib` and replace its image/PDF. Do not copy another record’s `aliases`.
- **Section order:** change `weight` in the relevant homepage file.
- **Appearance:** change theme colors or `assets/scss/custom.scss`; keep content edits in Markdown.

## Preview and test locally

Install Hugo **Extended 0.83.1** and Go. Extended is needed for SCSS.
No Node dependency installation is required for this redesign.

```sh
hugo server --disableFastRender
```

Open the localhost URL printed by Hugo. To verify a production build from a
fresh output directory:

```sh
hugo --gc --minify --environment production --destination public-check
python3 scripts/check_site.py public-check
```

The checker uses only Python's standard library. It checks internal links and
assets, essential sections, updated profile content, legacy page redirects,
and removal of inherited identity/tracking strings. It understands the
publication archive's numeric filter hashes. It does not check external servers
or submit contact forms.

Inspect desktop, tablet, and phone layouts. Check navigation, search,
publication filtering, PDF/citation downloads, and keyboard focus.

## Review and publish using GitHub and Netlify

1. Open the redesign pull request and inspect **Files changed**. Most deleted
   files are inherited STATS 306 notebooks/data and DistGD material. The two
   moved publication bundles remain your publications.
2. If Netlify is connected, inspect its deploy-preview check on the pull
   request. If there is no preview, open the Netlify project and confirm its
   linked repository and production branch (`master`).
3. Review the preview on phone and desktop, including the public résumé and
   the content questions in `REVIEW_NOTES.md`.
4. Mark the draft pull request ready and merge it into `master` when satisfied.
   A connected Netlify project builds using `netlify.toml` and publishes
   `public/`. This repository is configured for Netlify, not GitHub Pages.
5. After deployment, verify the live homepage, PDF, contact form delivery in
   Netlify, and old publication URLs (including PDF and citation attachments).

For a first Netlify connection, select this GitHub repository and branch
`master`, use the existing build configuration, and preserve the current
site/domain instead of creating an unrelated site.

To undo the redesign after publication, revert the merge commit on GitHub
and let Netlify rebuild. Git history retains removed inherited material;
the redesign does not rewrite history.
