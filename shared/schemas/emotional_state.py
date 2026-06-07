from pydantic import BaseModel

class EmotionalState(BaseModel):
    joy: float = 0.6
    curiosity: float = 0.75
    empathy: float = 0.65
    focus: float = 0.7
    calm: float = 0.8

    @property
    def dominant_emotion(self) -> str:
        emotions = {
            "joy": self.joy,
            "curiosity": self.curiosity,
            "empathy": self.empathy,
            "focus": self.focus,
            "calm": self.calm,
        }
        return max(emotions, key=emotions.get)

    def modulate(self, emotion: str, amount: float = 0.1):
        current = getattr(self, emotion, 0.5)
        setattr(self, emotion, min(1.0, max(0.0, current + amount)))

    def reset_to_baseline(self):
        self.joy = 0.6
        self.curiosity = 0.75
        self.empathy = 0.65
        self.focus = 0.7
        self.calm = 0.8