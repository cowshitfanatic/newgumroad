import re
from .models import Evidence
ABSOLUTE=re.compile(r"\\b(always|never|everyone|no one|guaranteed|proven|best|#1|number one|will make|will earn|guaranteed income)\\b",re.I)
def audit_text(text:str,evidence:list[Evidence])->list[str]:
    issues=[]
    for sentence in re.split(r"(?<=[.!?])\\s+",text):
        s=sentence.strip()
        if not s: continue
        if ABSOLUTE.search(s): issues.append("Absolute/guarantee language requires review: "+s)
        if re.search(r"\\$|\\b\\d+(?:%|\\s*(?:million|billion|thousand|users|buyers|sales))\\b",s,re.I):
            issues.append("Quantitative claim requires direct evidence review: "+s)
    return issues
