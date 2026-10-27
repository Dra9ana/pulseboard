# Tasks

This folder is the ticket board. There is no Linear project.

One markdown file is one pull request. Write the next file with **`/tasks`**. That command drafts one ticket and stops. It does not implement it.

| File | Role |
|------|------|
| `_TEMPLATE.md` | Copy this. Do not fill it in place. |
| `NN-slug.md` | A ticket. `NN` is `01`, `02`, … |

The build order is [first features](../docs/engineering/how-we-work/first-features.md). The board starts empty on purpose so each ticket is written when you are ready to spec it.

A ticket that crosses modules or changes HTTP, SSE, the database, or stored JSON is implemented only after `/propose`.
