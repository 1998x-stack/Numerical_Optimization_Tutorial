"""Check descent directions using the directional derivative g^T p."""
from math import cos, sin, radians, isclose

def directional_derivative(gradient: tuple[float, float], direction: tuple[float, float]) -> float:
    return sum(g * p for g, p in zip(gradient, direction))

def direction_at_angle(degrees: float) -> tuple[float, float]:
    # Gradient is (1, 0); angle is measured from the negative-gradient axis.
    theta = radians(degrees)
    return (-cos(theta), sin(theta))

if __name__ == "__main__":
    gradient = (1.0, 0.0)
    for angle in (0.0, 30.0, 60.0, 90.0, 120.0):
        direction = direction_at_angle(angle)
        slope = directional_derivative(gradient, direction)
        print(f"angle={angle:5.1f}°, g^T p={slope: .4f}, descent={slope < 0}")
    assert directional_derivative(gradient, direction_at_angle(0.0)) == -1.0
    assert directional_derivative(gradient, direction_at_angle(60.0)) < 0.0
    assert isclose(directional_derivative(gradient, direction_at_angle(90.0)), 0.0, abs_tol=1e-12)
    assert directional_derivative(gradient, direction_at_angle(120.0)) > 0.0
    # For H positive definite, the exact Newton direction is a descent direction.
    g = (2.0, -1.0)
    h_diag = (2.0, 4.0)
    p_newton = (-g[0] / h_diag[0], -g[1] / h_diag[1])
    assert directional_derivative(g, p_newton) < 0.0
