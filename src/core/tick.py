from pydantic import BaseModel
from datetime import timedelta


class GameTick(BaseModel):
    fps: float
    paused: bool
    tick: timedelta  # 0:00:00


