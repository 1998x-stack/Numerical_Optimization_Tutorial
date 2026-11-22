"""Warm-start line search with previous directional derivative."""
def initial_guess(alpha_prev, d_prev=-8.0, d_now=-4.0):
    if alpha_prev <= 0 or d_prev >= 0 or d_now >= 0:
        raise ValueError("positive previous step and negative slopes required")
    return max(0.1, min(4.0, alpha_prev*d_prev/d_now))

def conditions(alpha, c1=1e-4, c2=0.9):
    phi = lambda a: (a-2.0)**2
    dphi = lambda a: 2.0*(a-2.0)
    armijo = phi(alpha) <= phi(0.0)+c1*alpha*dphi(0.0)
    strong = armijo and abs(dphi(alpha)) <= c2*abs(dphi(0.0))
    return armijo, strong

if __name__ == "__main__":
    a = initial_guess(0.5)
    b = initial_guess(2.0)
    print("initial guesses:",a,b,"conditions:",conditions(a),conditions(b))
    assert a == 1.0 and b == 4.0
    assert conditions(a) == (True,True)
    assert conditions(b) == (False,False)
    assert abs(2.0*(3.0-5.0)/(-4.0)-1.0)<1e-12
