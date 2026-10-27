# sabren/untitled

> A July 2013 Flask experiment that forked three ways in a single day:
> a Dojo front end, a YUI datasheet, and — the branch that kept
> growing — a from-scratch Oberon-to-JavaScript compiler built out of
> grammar combinators.
> Repo: https://github.com/sabren/untitled — public, default branch
> `master`, created 2013-07-01. **All three branches are documented
> here, not just the default branch** (the default branch holds almost
> nothing — see below).

## The branches

The repo has four branches. `master` contains exactly one file, a
README that says only "This file was created by PyCharm 2.7 for
binding GitHub repository" — a placeholder, not a project. All of the
code lives on the three spike branches, which share a common base and
diverged on 2013-07-01 (with one later commit on `gramcombos`):

| Branch | Last commit | Files | What it is |
|--------|-------------|-------|-------------|
| `master` | 2013-07-01 "First commit" | 1 (README) | PyCharm placeholder |
| `dojo-spike` | 2013-07-01 "dojo stuff from the other day" | 9 | Dojo front end + Oberon compiler sketch |
| `yui-spike` | 2013-07-01 "encapsulated my stuff in a module" | 8 | YUI datasheet front end |
| `gramcombos` | 2013-10-20 "ob2js: actually create a data structure" | 7 | Grammar combinators + design notes |

### Shared base (identical on all three spike branches)

`untitled.py` is byte-identical across `dojo-spike`, `yui-spike`,
and `gramcombos`. Its docstring: "A small database designer for the
web." It is a Flask app backed by SQLite (`untitled.sdb`, debug on)
with a single route `/` rendering `templates/hello.html`. `schema.sql`
defines a single table:

```sql
create table tables(
  id integer primary key,
  name string,
  note text
)
```

So the "database designer" is, at this stage, one table with three
columns and a hello page — a scaffold, not a tool. (The name
"minrelite" appears in static filenames on two branches; the repo
never explains the name. Flagged as unverified rather than expanded.)

### `dojo-spike`: the Dojo front end + the compiler is born

- `templates/hello.html` — "Tutorial: Hello Dojo!" page loading
  Dojo from a local path with a `dojoConfig` registering a `demo`
  package.
- `static/js/dojo-init.js` — Dojo config (`baseUrl` `/static/`,
  packages `dojo`/`dijit`/`dojox`/`my`) requiring
  `minrelite-dojo.js`.
- `static/js/minrelite-dojo.js` — the Dojo-side module (contents not
  detailed here; it is the front-end counterpart of the Flask app).
- `ob2js.py` (158 lines) — "oberon to js compiler". At this stage
  it is a sketch: every combinator function (`rex`, `gra`, `sep`,
  `alt`, `seq`, `dfn`, `ref`, `opt`, `rep`, …) is a stub containing
  only `pass`, and the grammar that follows is a commented aspiration
  ("okay, this is hideous, but it's at least nicer than writing the
  entire parser out by hand"). The branch README says: "An experiment
  with: Dojo, D3, Flask."
- The commit message that introduces the compiler is the mission
  statement: "I got fed up with how ugly javascript modules are and
  started writing an oberon compiler in earnest."

(Flagged: the README names D3, but no D3 code appears in any
branch's file list. Either it was planned and never added, or it lived
elsewhere; the repo does not say.)

### `yui-spike`: the YUI datasheet

Same Flask base and schema, but the front end is Yahoo's YUI instead
of Dojo:

- `static/datasheet.js` — "a basic editable data grid, powered by
  YUI", built on the `blunderalong/dt_cellinline.html` inline-editing
  example. A `Y.DataTable` with columns `id` (read-only), `name`
  (inline editor), `price`; sortable, editable on click, with sample
  rows (gadget $6.99, sprocket $3.75, widget $4.25) captioned
  "Example table with simple columns" / "Price sheet for inventory
  parts".
- `static/minrelite-yui.css` + `static/minrelite.css` — styling,
  including a YUI "purecss" skin (per the commit "cleaned up the look
  and feel with a yui skin and their purecss framework").
- Commit trail: "added a tiny sortable datasheet" → skin/purecss →
  "inline cell editing" → "add new rows to the table" →
  "encapsulated my stuff in a module". A tidy one-day UI spike.

### `gramcombos`: the compiler grows up

This is the branch that kept going, to 2013-10-20, and it drops the
front-end experiments entirely (no `static/` directory) in favor of
the compiler idea:

- `ob2js.py` (124 lines) — the combinators now **return data
  structures** instead of `pass`: `rex` returns `('rex', pattern)`,
  `gra` returns `('gra', pattern)`, and so on for `sep`, `alt`,
  `seq`, `dfn`, `ref`, `opt`, `rep`, `known`, `new`, `hold`,
  `drop`, `take`, `same`, `other`, `scope`, `fwd`. The file then
  builds a complete `grammar` data structure for Oberon/retro Pascal:
  MODULE/IMPORT, CONST/TYPE/VAR/PROCEDURE declarations, records,
  arrays, procedure signatures with VAR/CONST parameters, and a
  statement language (IF/ELIF, blocks). The October commit message
  marks the transition: "ob2js: actually create a data structure."
- `oberon-trail.org` — design notes ("oberon trail") arguing the
  thesis: hand-written parsers are opaque programs; parser generators
  and parser combinators both leave the grammar itself opaque; the
  goal here is combinators that build "a transparent graph
  representation of an individual grammar, which can then be
  transformed and modified to produce various language-specific
  tools." This is the intellectual core of the branch — the compiler
  as a grammar-manipulation project, not just a parser.

## Tech stack

Python 2 (`cStringIO`, `print_function` future import), Flask,
SQLite, Dojo (dojo-spike), YUI 3 + Pure CSS (yui-spike). No license
file, no tests, no dependency list in any branch.

## Inventory (by branch)

| Branch | Files |
|--------|-------|
| `master` | `README` (PyCharm placeholder) |
| all spikes | `untitled.py` (Flask app, identical), `schema.sql`, `templates/hello.html`, `README`, `.idea/sqldialects.xml` |
| `dojo-spike` | + `ob2js.py` (stub combinators), `static/js/dojo-init.js`, `static/js/minrelite-dojo.js`, `setup.py` |
| `yui-spike` | + `static/datasheet.js`, `static/minrelite-yui.css`, `static/minrelite.css` |
| `gramcombos` | + `ob2js.py` (data-structure combinators + `grammar`), `oberon-trail.org` |

## Surprising / notable

- **One day, three UI directions, one survivor:** the Dojo and YUI
  branches both died on 2013-07-01; the compiler branch lived four
  more months and produced the only idea with a written thesis
  (`oberon-trail.org`).
- **The compiler's arc is visible in miniature:** stubs → tuples →
  a full grammar value. The commit messages narrate it honestly
  ("crazy grammar combinator thing" → "actually create a data
  structure").
- **The Flask app never changes.** Every branch's `untitled.py` is
  identical — the front-end spikes and the compiler spike all orbit
  a scaffold that stayed a hello page over a one-table database.
- No linked streams or videos were found in the repo.

## Status

Documented (this file), all branches. The repo itself records no
triage decision, and none is asserted here. If anything here has a
future, it is the `gramcombos` idea — grammar-as-data-structure —
which connects directly to Michal's later language work; the two UI
spikes are period pieces (Dojo and YUI 3, both long obsolete).
