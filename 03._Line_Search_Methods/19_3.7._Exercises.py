"""Four original exercises on Wolfe, exact steps, Armijo and Newton curvature."""
def strong_wolfe(alpha, c1=1e-4, c2=0.1):
    phi = (alpha - 2.0)**2
    return (phi <= 4.0 - 4*c1*alpha
            and abs(2*(alpha-2)) <= 4*c2)

def exact_step():
    alpha = 17.0/65.0
    x = (1.0-4*alpha, 1.0-alpha)
    value = 0.5*(4*x[0]**2+x[1]**2)
    return alpha, x, value

def armijo_trials():
    trials = []
    for alpha in (8.0, 4.0, 2.0):
        accepted = (alpha-2)**2 <= 4-4e-4*alpha
        trials.append((alpha, accepted))
        if accepted:
            break
    return trials

def newton_slopes():
    return 1*(-0.5)+2*2, 1*(-0.25)+2*(-2)

if __name__ == "__main__":
    assert strong_wolfe(2.0)
    assert not strong_wolfe(0.5)
    a, x, value = exact_step()
    print("exact:", a, x, value)
    assert abs(a-17/65) < 1e-12 and value < 2.5
    assert armijo_trials() == [(8.0,False),(4.0,False),(2.0,True)]
    assert newton_slopes() == (3.5,-4.25)
