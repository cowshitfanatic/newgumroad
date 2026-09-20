from .models import Evidence, Opportunity
WEIGHTS={"primary":5,"marketplace":4,"community":3,"search":2,"secondary":1,"internal":1}
def evidence_quality(e: Evidence)->int:
    return max(1,WEIGHTS.get(e.kind,1))*max(1,min(e.strength,3))
def validate_opportunity(o: Opportunity)->list[str]:
    errors=[]
    if not o.evidence: errors.append("Opportunity has no evidence.")
    for e in o.evidence:
        if not e.url.startswith(("http://","https://")): errors.append(f"Invalid evidence URL: {e.title}")
        if not e.claim.strip() or not e.observed.strip(): errors.append(f"Incomplete evidence: {e.title}")
    return errors
def score_opportunity(o: Opportunity)->float:
    if not o.evidence: return 0.0
    quality=sum(evidence_quality(e) for e in o.evidence)
    diversity=len({e.kind for e in o.evidence})
    return round(min(100.0,quality*6+diversity*5+min(5,len(o.problem)//40)*5-len(o.risks)*.25),1)
