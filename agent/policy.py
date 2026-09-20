from dataclasses import dataclass

@dataclass(frozen=True)
class AgentPolicy:
    approval_required: bool = True
    can_publish: bool = False
    can_claim_revenue: bool = False
    can_fabricate_evidence: bool = False
    can_fabricate_testimonials: bool = False
    must_preserve_source_urls: bool = True
    must_flag_uncertain_claims: bool = True

POLICY = AgentPolicy()
