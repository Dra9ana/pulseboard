---
name: committing
description: >-
  Split work into small conventional commits on a new branch. Use when the
  user asks to commit, write a commit message, or land local changes. Types
  include feat, fix, test, docs, refactor, and chore. Never commit on master
  and never merge to master.
---

# Committing

Commit on a feature branch. The owner merges to `master` by hand through a pull request.

## Branch

1. Run `git branch --show-current`.
2. If the branch is `master` or `main`, create a branch and switch to it before the first commit.
3. Name it from the ticket file: `tasks/01-workspace-quality-gate.md` becomes `01-workspace-quality-gate`. If there is no ticket, use a short lowercase kebab-case name for the change.
4. If the current branch is already a feature branch, stay on it.
5. Do not push, open a pull request, or merge unless the user explicitly asks.
6. Do not merge into `master` or `main`. Stop after the commits.

## Message

```
<type>: <imperative summary>
```

- English, lowercase after the colon, no trailing period
- One line is enough. Add a body only to say why
- Pass the message with a heredoc

| Type | Use |
|------|-----|
| `feat` | New behavior |
| `fix` | Bug fix |
| `test` | Tests only |
| `docs` | Docs, tickets, rules, skills |
| `refactor` | Same behavior, clearer structure |
| `chore` | Tooling, workspace, lockfile |

Use `build` or `ci` only when that system is the whole commit.

## Size

Each commit is one readable change. A reader can say what it does in one sentence.

- Do not mix a behavior change with an unrelated doc sweep or refactor
- Keep the test that locks a behavior in that behavior's commit
- Use `test:` when the commit only changes tests
- Leave the tree coherent: `make flct` still passes when that target exists

## Steps

1. Run `git status`, `git diff`, and `git log` in parallel. Then follow the types above.
2. Group the files into the small commits.
3. Create the branch if you are on `master` or `main`.
4. Stage one group, commit, then the next group.
5. Run `git status` after the last commit.

Do not update git config. Do not skip hooks. Do not force-push. Do not amend unless the user asks, the commit is yours, and it is not pushed.
