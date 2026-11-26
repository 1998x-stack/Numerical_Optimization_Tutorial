"""BFGS on Rosenbrock: print the final error ratios e_{k+1}/e_k."""
import math

def f(p):
    return 100.0*(p[1]-p[0]**2)**2 + (1.0-p[0])**2

def grad(p):
    return (-400.0*p[0]*(p[1]-p[0]**2) - 2.0*(1.0-p[0]), 200.0*(p[1]-p[0]**2))

def exact_search(x, p):
    lo, hi = 0.0, 2.0
    gr = (math.sqrt(5.0)-1.0)/2.0
    c, d = hi-gr*(hi-lo), lo+gr*(hi-lo)
    fc, fd = f((x[0]+c*p[0], x[1]+c*p[1])), f((x[0]+d*p[0], x[1]+d*p[1]))
    for _ in range(80):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi-gr*(hi-lo); fc = f((x[0]+c*p[0], x[1]+c*p[1]))
        else:
            lo, c, fc = c, d, fd
            d = lo+gr*(hi-lo); fd = f((x[0]+d*p[0], x[1]+d*p[1]))
    return 0.5*(lo+hi)

def run(x0):
    x = list(x0); H = [[1.0, 0.0], [0.0, 1.0]]
    star = (1.0, 1.0)
    def err(): return math.hypot(x[0]-star[0], x[1]-star[1])
    ratios, prev = [], None
    for it in range(20):
        d = err()
        if prev is not None and prev > 0:
            ratios.append(d/prev)
        prev = d
        g = grad(x)
        if math.hypot(*g) < 1e-10:
            break
        Hg = [H[0][0]*g[0]+H[0][1]*g[1], H[1][0]*g[0]+H[1][1]*g[1]]
        p = [-Hg[0], -Hg[1]]; a = exact_search(x, p)
        xn = [x[0]+a*p[0], x[1]+a*p[1]]; gn = grad(xn)
        s = [xn[i]-x[i] for i in range(2)]; y = [gn[i]-g[i] for i in range(2)]
        sy = s[0]*y[0]+s[1]*y[1]
        if sy > 1e-12:
            rho = 1.0/sy
            Hy = [H[i][0]*y[0]+H[i][1]*y[1] for i in range(2)]
            yHy = y[0]*Hy[0]+y[1]*Hy[1]
            H = [[H[i][j]-rho*(s[i]*Hy[j]+Hy[i]*s[j])+rho*rho*yHy*s[i]*s[j]+rho*s[i]*s[j]
                  for j in range(2)] for i in range(2)]
        x = xn
    return ratios

if __name__ == "__main__":
    ratios = run((-1.2, 1.0))
    print("last ratios:", [round(r, 4) for r in ratios[-4:]])
    assert ratios[-1] < 0.05          # final ratio is small: superlinear trend
