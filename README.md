# Financial Regulation Hub

Financial regulatory information for finance professionals: RBI, SEBI and IRDAI rules, key court rulings and other regulators, organised by regulator.

Not legal advice. An independent, unofficial summary for general information. Verify every point against the official text before relying on it.

## Static pages and sitemap

`tools/build_pages.py` writes one plain HTML page per instrument (`<section>/i/<ID>/`) and per judgment (`judgments/j/<ID>/`), plus `sitemap.xml`, `robots.txt` and link-preview tags on the main pages. The "Rebuild static pages and sitemap" workflow runs it after any data change on `main`; run it locally with `python3 -I tools/build_pages.py`. Set `site_url` in `hub.json` when the site moves to its own domain.

`tools/build_entity.py` writes `entity/data/entity.json` for the "What applies to my entity" page (`entity/`) from the section registers and graphs and the rules in `tools/entity_rules.py` (lens mapping, activity and role pointers, combination rules, instruments that appear in two sections). It stops with an error if a rule names an instrument, lens or RBI paragraph that does not exist. The same workflow runs it; locally: `python3 -I tools/build_entity.py`.
