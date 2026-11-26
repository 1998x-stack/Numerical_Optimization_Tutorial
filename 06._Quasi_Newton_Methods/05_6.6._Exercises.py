"""Assertions for the Chapter 6 exercises (B0=I, s=(1,0))."""

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def mv(B, v):
    return [B[0][0]*v[0] + B[0][1]*v[1], B[1][0]*v[0] + B[1][1]*v[1]]

def det(B):
    return B[0][0]*B[1][1] - B[0][1]*B[1][0]

def bfgs(B, s, y):
    Bs = mv(B, s); sBs = dot(s, Bs)
    return [[B[i][j] - Bs[i]*Bs[j]/sBs + y[i]*y[j]/dot(y, s)
             for j in range(2)] for i in range(2)]

def sr1(B, s, y):
    Bs = mv(B, s); v = [y[i]-Bs[i] for i in range(2)]; vs = dot(v, s)
    return None if abs(vs) < 1e-12 else [[B[i][j] + v[i]*v[j]/vs for j in range(2)] for i in range(2)]

def broyden_phi(B, s, y, phi):
    Bs = mv(B, s); sBs = dot(s, Bs); ys = dot(y, s)
    v = [y[i]/ys - Bs[i]/sBs for i in range(2)]
    return [[B[i][j] - Bs[i]*Bs[j]/sBs + y[i]*y[j]/ys + phi*sBs*v[i]*v[j]
             for j in range(2)] for i in range(2)]

if __name__ == "__main__":
    B0, s = [[1.0, 0.0], [0.0, 1.0]], (1.0, 0.0)
    a, b = 0.9, 2.0
    y = (a, b)
    Bb = bfgs(B0, s, y)
    assert abs(Bb[0][0]*s[0] + Bb[0][1]*s[1] - y[0]) < 1e-12     # exercise 1
    Bs_ = sr1(B0, s, y)
    assert abs(det(Bs_) - (a + b*b/(a-1))) < 1e-12                 # exercise 3
    for phi in (-2.0, 0.0, 0.5, 1.0):
        Bh = broyden_phi(B0, s, y, phi)
        assert abs(det(Bh) - (a + phi*b*b/a)) < 1e-12              # exercise 4
    assert det(Bs_) < 0 and det(Bb) > 0
    print("SR1 det =", round(det(Bs_), 4), "| BFGS det =", round(det(Bb), 4))
