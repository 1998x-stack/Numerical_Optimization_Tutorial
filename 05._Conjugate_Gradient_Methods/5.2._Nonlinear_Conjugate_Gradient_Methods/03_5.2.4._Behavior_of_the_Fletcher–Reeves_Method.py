"""Fletcher-Reeves on a Rosenbrock-like valley with Armijo backtracking."""
import math

def f(p):
    return (p[0]-1)**2 + 5*(p[1]-p[0]**2)**2

def grad(p):
    x, y = p
    return [2*(x-1) - 20*x*(y-x*x), 10*(y-x*x)]

def run(x0, tol=1e-6, cap=500):
    x, g = list(x0), grad(x0)
    p = [-g[0], -g[1]]
    angles = []
    for _ in range(cap):
        if math.hypot(*g) < tol:
            break
        slope = g[0]*p[0] + g[1]*p[1]
        a = 1.0
        for _ in range(40):
            if f([x[0]+a*p[0], x[1]+a*p[1]]) <= f(x) + 1e-4*a*slope:
                break
            a *= 0.5
        x = [x[0]+a*p[0], x[1]+a*p[1]]
        gn = grad(x)
        beta = (gn[0]**2 + gn[1]**2) / (g[0]**2 + g[1]**2)
        p = [-gn[0] + beta*p[0], -gn[1] + beta*p[1]]
        cos = -(gn[0]*p[0] + gn[1]*p[1]) / (math.hypot(*gn)*math.hypot(*p))
        angles.append(cos)
        g = gn
    return x, math.hypot(*g), angles

if __name__ == "__main__":
    x, norm, angles = run((-1.2, 1.0))
    assert norm < 1e-6
    assert min(angles) < 0.0
    print("final", [round(v, 6) for v in x],
          "| min descent angle cos =", round(min(angles), 6),
          "| steps =", len(angles))
