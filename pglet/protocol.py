import json
from dataclasses import dataclass, field

@dataclass
class Command:
    indent: int
    name: str
    values: list[str] = field(default_factory=list)
    attrs: dict[str, str] = field(default_factory=dict)
    lines: list[str] = field(default_factory=list)
    commands: list[any] = field(default_factory=list)

@dataclass
class Message:
    id: str
    action: str
    payload: any

@dataclass
class PageCommandRequestPayload:
    pageName: str
    sessionID: str
    command: Command

@dataclass
class PageCommandResponsePayload:
    result: str
    error: str

@dataclass
class PageCommandsBatchRequestPayload:
    pageName: str
    sessionID: str
    commands: list[Command]

@dataclass
class PageCommandsBatchResponsePayload:
    results: list[str]
    error: str

@dataclass
class PageEventPayload:
    pageName: str
    sessionID: str
    eventTarget: str
    eventName: str
    eventData: str

@dataclass
class RegisterHostClientRequestPayload:
    hostClientID: str
    pageName: str
    isApp: bool
    authToken: str
    permissions: str

@dataclass
class RegisterHostClientResponsePayload:
    hostClientID: str
    pageName: str
    sessionID: str
    error: str

@dataclass
class SessionCreatedPayload:
    pageName: str    
    sessionID: str