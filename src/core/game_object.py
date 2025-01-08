import re
from enum import Enum
from typing_extensions import Self

from pydantic import BaseModel, ConfigDict, model_validator


class Type(Enum):
    PLAYER = ''
    SPRITE = ''
    ANIMATION = ''
    UI = ''
    SCRIPT = ''
    NPC = ''
    EVENT = ''
    COLLISION = ''
    PARENT = ''


class GameObject(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    object_type: Type

    @model_validator(mode='after')
    def check_name_length(self) -> Self:
        allowed_names = re.compile(r'^[A-Za-z0-9_-]+$')
        if not allowed_names.match(self.name):
            raise ValueError("GameObject name can only contain A-Z, 0-9, _, or -")
        return self


class Parent(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    children: list[GameObject]

    @model_validator(mode='after')
    def check_if_game_object(self, values) -> Self:
        if not isinstance(self.children, list):
            for child in self.children:
                if not isinstance(child, GameObject):
                    raise ValueError("Children are not GameObjects!")
        return self


class GameObjectCls:
    def __init__(self, *, name: str, object_type: Type):
        self.name = name
        self.object_type = object_type


class ParentObjectCls:
    def __init__(self, *, name: str, object_type: Type, children: list[GameObjectCls]):
        self.name = name
        self.object_type = object_type
        self.children = children

