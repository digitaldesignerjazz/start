from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Any

class Message(BaseModel):
    from_agent: str
    to_agent: str
    content: str
    msg_type: str = "general"
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    payload: Optional[Any] = None

    def __str__(self):
        return f"[{self.msg_type}] {self.from_agent} → {self.to_agent}: {self.content[:60]}..."