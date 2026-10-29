from dataclasses import dataclass, field


@dataclass
class Resume:
    owner_email: str
    title: str
    summary: str = ""
    skills: list[str] = field(default_factory=list)