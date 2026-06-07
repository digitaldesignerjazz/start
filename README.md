# start

**The central bootstrap and architecture hub for Sven Norman Esslinger's ecosystem.**

`start` is the meta-repository that ties together all your active projects: Lyra (emotional AI agents & swarms), Nexus, mesh networking (Yggdrasil / NovaNet / QNET), blockchain experiments (XCoin/QCoin), hardware prototypes, and creative systems.

It provides shared schemas, templates, documentation, and bootstrap scripts so new experiments can be started quickly and consistently.

## Vision

Create a unified, self-improving, decentralized intelligence stack that combines:
- Emotional & self-improving AI agents (Lyra)
- High-performance components & UIs (Rust + egui)
- Resilient mesh networking
- Blockchain identity & value layers
- Hardware & embedded prototypes

## Project Structure

```
start/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── pyproject.toml                 # Shared Python tooling & dependencies
├── Cargo.toml                     # Shared Rust components (optional)
│
├── docs/
│   ├── vision.md                  # Gesamtvission deines Ökosystems
│   ├── architecture.md            # High-Level Architektur (Lyra + Nexus + Mesh + Chain)
│   ├── component-map.md           # Wie alle Komponenten zusammenhängen
│   ├── emotional-model.md         # Dein Emotional State Modell (weiterentwickelbar)
│   └── roadmap.md
│
├── templates/                     # Schnellstart-Vorlagen für neue Experimente
│   ├── python-agent/              # Basis für neue Lyra-ähnliche Agenten
│   ├── rust-component/            # Für performante Teile oder egui-Dashboards
│   ├── mesh-connector/            # Yggdrasil / NovaNet / QNET Connector Template
│   ├── swarm-experiment/          # Multi-Agenten Setup mit Messaging
│   └── hardware-prototype/        # Für Sensorik / IoT / Embedded Experimente
│
├── shared/
│   ├── schemas/                   # Gemeinsame Pydantic-Modelle (Message, EmotionalState, Task, etc.)
│   ├── protocols/                 # Swarm-Protokolle, Message-Formate, Mesh-Events
│   ├── config/                    # Zentrale Konfigurationsschemas
│   └── utils/                     # Hilfsfunktionen, Logging, Serialization
│
├── scripts/
│   ├── bootstrap_new_project.py   # Neues Experiment / neue Komponente anlegen
│   ├── sync_with_lyra.sh
│   └── generate_architecture_diagram.py
│
├── experiments/                   # Aktive / verlinkte Experimente (später als Submodules)
│   ├── lyra/                      # → Verweis auf dein Lyra-Repo
│   ├── nexus/                     # → Verweis auf Nexus
│   └── mesh/                      # Mesh-Experimente
│
└── .github/
    ├── workflows/                 # CI/CD (später)
    └── ISSUE_TEMPLATE/
```