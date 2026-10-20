"""Array operations, sequence processing, and a temperature demonstration."""
import argparse,json
import numpy as np

def matrix_features(matrix):
    matrix=np.asarray(matrix)
    if matrix.shape!=(7,7):raise ValueError("expected a 7x7 matrix")
    return {"first_row":matrix[0].copy(),"diagonal":np.diag(matrix).copy(),"submatrix":matrix[2:5,4:7].copy(),"odd_only":np.where(matrix%2==0,0,matrix)}

def process_numbers(numbers):
    kept=[n for n in numbers if n>=10];squared=[n*n for n in kept]
    return {"filtered":kept,"squared":squared,"sum_squared":sum(squared),"count_at_least_20":sum(n>=20 for n in numbers)}

def process_sentences(sentences):
    if len(sentences)>5:raise ValueError("at most five sentences")
    counts=[len(s.split()) for s in sentences];words=[s.split()[:2] for s in sentences if len(s.split())>6]
    return {"word_counts":counts,"long_sentences":[s for s in sentences if len(s.split())>4],"prefixes":words,"substituted_prefixes":[["".join('S' if c in 'aeiouAEIOU' else c for c in w) for w in pair] for pair in words]}

def matrix_inverse(matrix):
    a=np.asarray(matrix,dtype=float)
    if a.ndim!=2 or a.shape[0]!=a.shape[1]:raise ValueError("square matrix required")
    # A determinant comparison to exactly zero is numerically unreliable.
    if np.linalg.matrix_rank(a)<a.shape[0]:raise ValueError("matrix is singular")
    return {"determinant":float(np.linalg.det(a)),"condition_number":float(np.linalg.cond(a)),"inverse":np.linalg.inv(a)}

def temperature_summary(celsius):
    c=np.asarray(celsius,dtype=float)
    if c.ndim!=1 or not len(c) or not np.isfinite(c).all():raise ValueError("finite nonempty temperature vector required")
    f=c*9/5+32;days=np.arange(1,len(c)+1)
    return {"fahrenheit":f,"hottest_days":days[f==f.max()],"coldest_days":days[f==f.min()],"mean_fahrenheit":float(f.mean()),"days_above_average":days[f>f.mean()]}

def run(output=None):
    rng=np.random.default_rng(42)
    result={"matrix":matrix_features(rng.integers(1,11,size=(7,7))),"inverse":matrix_inverse(np.eye(5)*2),"numbers":process_numbers([-2,9,10,20,30]),"sentences":process_sentences(["A practical example with more than six words"]),"temperature":temperature_summary([22,24,23,25,28,35,39,41,29,27,39,25,24,22,22,25,27,28,30,31,30,40,30,26,24,23,22,21,20,19,18])}
    result=json.loads(json.dumps(result,default=lambda a:a.tolist()))
    if output:
        from pathlib import Path
        out=Path(output);out.mkdir(parents=True,exist_ok=True);(out/'results.json').write_text(json.dumps(result,indent=2))
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='outputs');a=p.parse_args();print(json.dumps(run(a.output),indent=2))
