# Git Submodules in `start`

This repository uses Git Submodules to include `lyra` and `nexus` as live, versioned dependencies under `experiments/`.

## Why Submodules?

- Keeps `start` as the central architecture hub without duplicating code.
- Allows independent development of Lyra and Nexus while still referencing exact versions.
- Clean separation between the "meta" project (`start`) and the concrete implementations.

## Current Submodules

| Path                | Repository                                      | Purpose                          |
|---------------------|-------------------------------------------------|----------------------------------|
| `experiments/lyra`  | https://github.com/digitaldesignerjazz/lyra.git | Core emotional AI agent system   |
| `experiments/nexus` | https://github.com/digitaldesignerjazz/nexus.git| Analytical / high-clarity mode   |

## How to Initialize Submodules (after cloning `start`)

```bash
# 1. Clone the start repository
cd start

# 2. Initialize and update all submodules
git submodule update --init --recursive

# Optional: If you want to update a submodule to the latest commit on its main branch later:
# cd experiments/lyra
# git pull origin main
# cd ../..
# git add experiments/lyra
# git commit -m "chore: update lyra submodule"
```

## Adding a New Submodule (for future projects)

```bash
# Example: adding another project as submodule
mkdir -p experiments

git submodule add https://github.com/digitaldesignerjazz/your-new-repo.git experiments/your-new-repo

git add .gitmodules experiments/your-new-repo
git commit -m "chore: add your-new-repo as submodule"
git push
```

## Important Notes

- After `git clone https://github.com/digitaldesignerjazz/start.git`, the submodule directories will be **empty** until you run `git submodule update --init --recursive`.
- Do **not** commit the contents of `experiments/lyra` or `experiments/nexus` directly — they are managed via submodules.
- If you see "Submodule commit ... is not up to date", run the update command above.

## Troubleshooting

```bash
# If submodules are in a detached HEAD state or out of sync:
git submodule update --init --recursive --remote

# To remove a submodule completely (advanced):
# git submodule deinit -f experiments/lyra
# git rm -f experiments/lyra
# rm -rf .git/modules/experiments/lyra
# git commit -m "chore: remove lyra submodule"
```

This setup gives you a clean, professional monorepo-like experience while keeping each major project independently maintainable.
