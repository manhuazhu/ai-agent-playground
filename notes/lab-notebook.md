# Lab Notebook

Add a dated entry every time you make a change to this repo. Newest entries at the top.

## 2026-09-16 — Claude Code
- `analysis/summarize.py` crashed with `KeyError: 'cohort'` on line 14 — the script looked up `row["cohort"]`, but `data/reaction_times.csv` has no such column.
- Root cause: the CSV's grouping column is actually named `group` (header: `subject_id,group,response_time_ms`), not `cohort`.
- Fix: changed `row["cohort"]` to `row["group"]` in `load_groups()`.
- Verified fix by rerunning the script; output: `control: n=10, mean=504.7 ms`, `treatment: n=10, mean=430.8 ms`.
- Committed as `7e47f02` and pushed to `claude/zealous-pasteur-3kf4xp`.

## Example — 2026-01-01 — A. Researcher
- Ran `analysis/summarize.py` for the first time; confirmed the repo and my tool are connected.
- No changes made yet — just checking the pipeline works end to end.

<!-- Add your own entry above this line -->
