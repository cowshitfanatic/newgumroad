from agent.claims import audit_text
from agent.evidence import score_opportunity
from agent.models import Evidence,Opportunity
from agent.pipeline import run
def evidence(): return [Evidence("Observed discussion","https://example.com/source","community","People discuss weekly planning friction","Discussion contains requests for a reusable workflow",2)]
def test_requires_evidence():
    p=run(Opportunity("Planner","freelancers","weekly planning friction"))
    assert p.approval_required and p.unsupported_claims and p.opportunity.score==0
def test_scoring_is_not_sales_prediction():
    assert score_opportunity(Opportunity("Planner","freelancers","weekly planning friction",evidence()))>0
def test_guarantee_flagged(): assert audit_text("This will make you money.",evidence())
def test_bundle_never_auto_publishes(): assert run(Opportunity("Planner","freelancers","weekly planning friction",evidence())).approval_required
