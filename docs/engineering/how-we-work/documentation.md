# Documentation quality

## Claims

Write **planned** until the code is in the tree. The project plan and the architecture overview are allowed to name future packages. They must not say those packages run today.

`docs/engineering/project-plan.md` is the map. When a capability ships, its behavior goes in a handbook. Do not paste the handbook back into the plan.

## Same change as the behavior

A change that alters what a caller can do updates the handbook in that change. If no handbook exists yet, add one from `docs/engineering/architecture/_HANDBOOK_TEMPLATE.md` and a row in `docs/engineering/README.md`.

## Change notes

`/propose` writes a note under `docs/engineering/changes/`. Delete that note in the change that updates the handbook. The template and this folder's README stay.

## Language

English for docs, rules, skills, and code. See `.cursor/rules/english-only.mdc`.
