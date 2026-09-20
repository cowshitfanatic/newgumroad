from .claims import audit_text
from .evidence import score_opportunity, validate_opportunity
from .models import Opportunity,TemplateBundle,ReviewPacket
def build_bundle(o:Opportunity)->TemplateBundle:
    name=o.name.strip() or "Untitled Template Bundle"
    guide=f"Guide: how to use {name}.\\nAudience: {o.audience}.\\nProblem: {o.problem}.\\nThis guide describes a workflow and makes no outcome guarantee."
    listing={"title":name,"description":f"A practical template bundle for {o.audience} dealing with {o.problem.lower()}.","what_you_get":"Editable templates, a usage guide, and a setup checklist.","proof_note":"Research evidence is documented separately; no unsupported demand or income claims are made."}
    return TemplateBundle(name,["README.md","templates/START-HERE.md","templates/TEMPLATE-01.md","templates/CHECKLIST.md"],guide,listing)
def run(o:Opportunity)->ReviewPacket:
    errors=validate_opportunity(o)
    o.score=score_opportunity(o) if not errors else 0.0
    b=build_bundle(o)
    issues=errors+audit_text(" ".join(b.listing.values())+" "+b.guide,o.evidence)
    return ReviewPacket(o,b,sorted(set(issues)),True)
