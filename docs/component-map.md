# Component Map

## Core Components

- **lyra**: Emotional self-improving agent framework (Python + async)
- **nexus**: Analytical / high-clarity mode
- **mesh**: Networking experiments (Yggdrasil, NovaNet, QNET)
- **chain**: Blockchain primitives (XCoin, QCoin, runes)
- **hardware**: Sensor / IoT prototypes

## Shared Layer (this repo)

- `shared/schemas/`: Message, EmotionalState, Task, AgentConfig
- `shared/protocols/`: Swarm communication rules
- `shared/config/`: Central configuration

All components should import from `start.shared` where possible for consistency.