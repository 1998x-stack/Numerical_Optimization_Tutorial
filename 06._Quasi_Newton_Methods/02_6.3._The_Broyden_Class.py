"""Broyden-class Hessian update and the positive definiteness interval."""

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def mv(B, v):
    return [B[0][0]*v[0] + B[0][1]*v[1], B[1][0]*v[0] + B[1][1]*v[1]]

def broyden(B, s, y, phi):
    Bs = mv(B, s); sBs = dot(s, Bs); ys = dot(y, s)
    v = [y[i]/ys - Bs[i]/sBs for i in range(2)]
    return [[B[i][j] - Bs[i]*Bs[j]/sBs + y[i]*y[j]/ys + phi*sBs*v[i]*v[j]
             for j in range(2)] for i in range(2)]

def det(B):
    return B[0][0]*B[1][1] - B[0][1]*B[1][0]

if __name__ == "__main__":
    B0, s, y = [[1.0, 0.0], [0.0, 1.0]], (1.0, 0.0), (1.0, 2.0)
    for phi in (0.0, 0.5, 1.0, -1.0):
        B1 = broyden(B0, s, y, phi)
        assert abs(B1[0][0]*s[0] + B1[0][1]*s[1] - y[0]) < 1e-12   # secant, any phi
    for phi in (0.0, 0.5, 1.0):
        assert det(broyden(B0, s, y, phi)) > 0                      # positive definite
    assert abs(det(broyden(B0, s, y, -1.0)) + 3.0) < 1e-12        # indefinite
    print("det at phi=0,0.5,1,-1:",
          [round(det(broyden(B0, s, y, p)), 3) for p in (0.0, 0.5, 1.0, -1.0)])
