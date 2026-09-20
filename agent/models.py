from dataclasses import dataclass, field
from typing import Literal
EvidenceKind = Literal["primary","marketplace","community","search","secondary","internal"]
@dataclass(frozen=True)
class Evidence:
    title: str
    url: str
    kind: EvidenceKind
    claim: str
    observed: str
    strength: int = 1
@dataclass
class Opportunity:
    name: str
    audience: str
    problem: str
    evidence: list[Evidence] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    score: float = 0.0
@dataclass
class TemplateBundle:
    name: str
    files: list[str]
    guide: str
    listing: dict[str,str]
@dataclass
class ReviewPacket:
    opportunity: Opportunity
    bundle: TemplateBundle
    unsupported_claims: list[str]
    approval_required: bool = True
