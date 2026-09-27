import argparse, csv, json, math, random, sys
from pathlib import Path

FEATURES=("entropy","imports","strings","sections","signed","debug_symbols")

def load(path):
    rows=[]
    with path.open(encoding="utf-8",newline="") as f:
        for n,r in enumerate(csv.DictReader(f),2):
            try: rows.append({"id":r["id"],"label":int(r["label"]),**{k:float(r[k]) for k in FEATURES}})
            except (KeyError,ValueError) as e: raise ValueError(f"{path}:{n}: invalid row: {e}") from e
    if not rows or {r['label'] for r in rows}!={0,1}: raise ValueError("dataset needs both label 0 and label 1")
    return rows

def standardize(rows):
    stats={}
    for k in FEATURES:
        mean=sum(r[k] for r in rows)/len(rows); var=sum((r[k]-mean)**2 for r in rows)/len(rows)
        stats[k]=(mean,math.sqrt(var) or 1.0)
    return [[(r[k]-stats[k][0])/stats[k][1] for k in FEATURES] for r in rows],stats

def train(rows,steps=800,rate=.08):
    xs,stats=standardize(rows); w=[0.0]*(len(FEATURES)+1)
    for _ in range(steps):
        grad=[0.0]*len(w)
        for x,r in zip(xs,rows):
            z=w[0]+sum(a*b for a,b in zip(w[1:],x)); p=1/(1+math.exp(-max(-30,min(30,z))))
            err=p-r["label"]; grad[0]+=err
            for j,v in enumerate(x,1): grad[j]+=err*v
        for j in range(len(w)): w[j]-=rate*grad[j]/len(rows)
    return {"weights":w,"stats":stats}

def score(model,row):
    x=[(row[k]-model['stats'][k][0])/model['stats'][k][1] for k in FEATURES]
    z=model['weights'][0]+sum(a*b for a,b in zip(model['weights'][1:],x))
    return 1/(1+math.exp(-max(-30,min(30,z))))

def mutate(row,rng,strength):
    out=dict(row)
    # Feature-space simulation only. It never reads, writes, or transforms executable files.
    out["entropy"]=max(0,min(8,out["entropy"]+rng.uniform(-2.8,-.4)*strength))
    out["strings"]=max(0,out["strings"]*(1+rng.uniform(.15,.9)*strength))
    out["imports"]=max(0,out["imports"]*(1+rng.uniform(.1,.7)*strength))
    out["sections"]=max(1,out["sections"]+rng.choice((-1,0,1))*strength)
    if rng.random()<min(1,.45*strength): out["signed"]=1
    if rng.random()<min(1,.25*strength): out["debug_symbols"]=1
    return out

def metrics(rows,scores,threshold=.5):
    tp=fp=tn=fn=0
    for r,s in zip(rows,scores):
        pred=s>=threshold
        if r['label'] and pred: tp+=1
        elif r['label']: fn+=1
        elif pred: fp+=1
        else: tn+=1
    return {"tp":tp,"fp":fp,"tn":tn,"fn":fn,"recall":round(tp/(tp+fn),4) if tp+fn else 0,
            "false_positive_rate":round(fp/(fp+tn),4) if fp+tn else 0}

def experiment(rows,seed=7,strength=1.0,threshold=.5):
    model=train(rows); base=[score(model,r) for r in rows]
    rng=random.Random(seed); changed=[mutate(r,rng,strength) if r['label'] else dict(r) for r in rows]
    after=[score(model,r) for r in changed]
    cases=[]
    for old,new,a,b in zip(rows,changed,base,after):
        if old['label'] and (a>=threshold)!=(b>=threshold):
            cases.append({"id":old['id'],"before_score":round(a,4),"after_score":round(b,4),
                          "feature_delta":{k:round(new[k]-old[k],4) for k in FEATURES if new[k]!=old[k]}})
    return {"schema":"lr-detector-resilience/v1","seed":seed,"strength":strength,"threshold":threshold,
            "baseline":metrics(rows,base,threshold),"after_feature_drift":metrics(changed,after,threshold),
            "flipped_malicious_samples":cases,"boundary":"Feature-vector simulation only; no executable mutation or AV bypass payloads."}

def main(argv=None):
    p=argparse.ArgumentParser(description="Measure detector robustness under safe feature-space drift")
    p.add_argument("dataset",type=Path); p.add_argument("--seed",type=int,default=7)
    p.add_argument("--strength",type=float,default=1.0); p.add_argument("--threshold",type=float,default=.5)
    p.add_argument("--output",type=Path)
    a=p.parse_args(argv)
    try:r=experiment(load(a.dataset),a.seed,a.strength,a.threshold)
    except ValueError as e:p.error(str(e))
    text=json.dumps(r,ensure_ascii=False,indent=2)+"\n"
    a.output.write_text(text,encoding="utf-8") if a.output else print(text,end="")
    return 0
if __name__=="__main__":sys.exit(main())
