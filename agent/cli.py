import argparse,json
from .models import Evidence,Opportunity
from .pipeline import run
def main():
    p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("--out",default="review-packet.json");a=p.parse_args()
    data=json.load(open(a.input,encoding="utf-8"))
    o=Opportunity(data["name"],data["audience"],data["problem"],[Evidence(**x) for x in data.get("evidence",[])],data.get("assumptions",[]),data.get("risks",[]))
    packet=run(o)
    json.dump({"approval_required":True,"opportunity":packet.opportunity.__dict__,"bundle":packet.bundle.__dict__,"unsupported_claims":packet.unsupported_claims},open(a.out,"w",encoding="utf-8"),indent=2,default=lambda x:x.__dict__)
    print("Review packet written; approval_required=true")
if __name__=="__main__": main()
