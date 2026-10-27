# Pulseboard — Documentation

## Where to go

| I am… | Start here |
|-------|------------|
| Reading the product in one page | [Product](product/overview.md) |
| Starting engineering work | [Engineering](engineering/README.md) |
| Looking for the build map | [Project plan](engineering/project-plan.md) |
| Using Cursor | [Cursor for the team](engineering/how-we-work/cursor-for-the-team.md) |
| An AI assistant | [AGENTS.md](../AGENTS.md) |

## Layout

```
docs/
├── README.md
├── product/            ← what the product is, no module paths
└── engineering/        ← architecture, decisions, how we work
    ├── project-plan.md ← map of this effort (not a feature handbook)
    ├── architecture/
    ├── decisions/
    ├── how-we-work/
    └── changes/        ← empty inbox for /propose
```

Product pages say what a person can do. Engineering pages say where code goes. Feature behavior, once it ships, gets a handbook under `engineering/architecture/`.
