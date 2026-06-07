from pydantic import BaseModel

class EmotionalState(BaseModel):
    joy: float = 0.6
    curiosity: float = 0.75
    # extend as needed

class SimpleAgent:
    def __init__(self, name: str):
        self.name = name
        self.emotional_state = EmotionalState()

    def perceive(self, stimulus: str):
        print(f"{self.name} perceived: {stimulus}")

    def act(self):
        print(f"{self.name} is acting...")

if __name__ == "__main__":
    agent = SimpleAgent("TemplateAgent")
    agent.perceive("Hello from start template")
    agent.act()