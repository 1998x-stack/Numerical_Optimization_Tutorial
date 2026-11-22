"""Trust-region Newton iteration for a strictly convex nonquadratic example."""
def f(x): return .5*x*x+.1*x**3+.05*x**4
def g(x): return x+.3*x*x+.2*x**3
def H(x): return 1+.6*x+.6*x*x
def run(x=.8,delta=.3):
    history=[]
    for i in range(20):
        grad,curv=g(x),H(x)
        if abs(grad)<1e-13: break
        newton=-grad/curv
        p=max(-delta,min(delta,newton))
        prediction=-grad*p-.5*curv*p*p
        if prediction<=0: raise RuntimeError("nonpositive decrease")
        rho=(f(x)-f(x+p))/prediction
        history.append((x,delta,p,newton,rho))
        if rho>=.1: x+=p
        if rho<.25: delta*=.25
        elif rho>.75 and abs(abs(p)-delta)<1e-12:
            delta=min(5.,2*delta)
    return x,history
if __name__=="__main__":
    x,history=run()
    print("final",x,"iterations",len(history))
    for row in history: print(row)
    assert abs(x)<1e-10
    assert history[0][2]==-.3
    assert abs(history[0][3])>.3
    assert any(abs(p-n)<1e-12 for _,_,p,n,_ in history[1:])
    assert abs(history[-1][-1]-1)<1e-5
