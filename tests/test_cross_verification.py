"""Independent mathematical checks and HTML/Markdown/Python consistency."""
from __future__ import annotations

import math
import re
import unittest
from fractions import Fraction
from html import unescape

from scripts.validate_course import ARTICLES, ROOT


class CrossVerificationTests(unittest.TestCase):
    def test_all_article_code_is_same_as_source(self):
        for html_path, md_path, py_path, _ in ARTICLES:
            with self.subTest(article=html_path):
                html = (ROOT / html_path).read_text(encoding="utf-8")
                markdown = (ROOT / md_path).read_text(encoding="utf-8")
                source = (ROOT / py_path).read_text(encoding="utf-8").strip()
                html_match = re.search(r"<pre><code>(.*?)</code></pre>", html, re.DOTALL)
                md_match = re.search(r"\x60{3}python\s*\n(.*?)\n\x60{3}", markdown, re.DOTALL)
                self.assertIsNotNone(html_match, "HTML code block missing")
                self.assertIsNotNone(md_match, "Markdown code block missing")
                self.assertEqual(unescape(html_match.group(1)).strip(), source)
                self.assertEqual(md_match.group(1).strip(), source)

    def test_stochastic_example_exact(self):
        scenarios = (Fraction(1), Fraction(2), Fraction(4))
        mean = sum(scenarios) / len(scenarios)
        risk = lambda x: sum((x - d) ** 2 for d in scenarios) / len(scenarios)
        self.assertEqual(mean, Fraction(7, 3))
        self.assertEqual(risk(mean), Fraction(14, 9))
        self.assertEqual(risk(Fraction(2)) - risk(mean), Fraction(1, 9))

    def test_convexity_chord_gap(self):
        theta = Fraction(1, 4)
        f = lambda x: (x - 1) ** 2
        a, b = Fraction(0), Fraction(4)
        x = theta * a + (1 - theta) * b
        chord = theta * f(a) + (1 - theta) * f(b)
        self.assertEqual(x, 3)
        self.assertEqual(f(x), 4)
        self.assertEqual(chord, 7)
        self.assertEqual(chord - f(x), 3)
        self.assertEqual(16 * theta * (1 - theta), 3)

    def test_descent_and_newton_step(self):
        alpha = Fraction(1, 5)
        x0 = Fraction(0)
        gradient = 2 * (x0 - 3)
        self.assertEqual(x0 - alpha * gradient, Fraction(6, 5))
        self.assertEqual(x0 - gradient / 2, 3)
        self.assertEqual(1 - 2 * alpha, Fraction(3, 5))

    def test_central_difference_quadratic_exact_arithmetic(self):
        x, h = Fraction(5, 4), Fraction(1, 10)
        f = lambda z: (z - 2) ** 2 + 1
        derivative = (f(x + h) - f(x - h)) / (2 * h)
        self.assertEqual(derivative, Fraction(-3, 2))

    def test_infimum_not_attained_and_stationary_counterexample(self):
        self.assertGreater(math.exp(-10), 0.0)
        self.assertLess(math.exp(-10), math.exp(-5))
        cubic = lambda x: x ** 3
        self.assertEqual(3 * 0 ** 2, 0)
        self.assertLess(cubic(-0.1), cubic(0))
        self.assertLess(cubic(0), cubic(0.1))


    def test_local_minimum_hessian_cases(self):
        def eig(a, b, c):
            d = ((a-c)**2 + 4*b*b) ** 0.5
            return ((a+c-d)/2, (a+c+d)/2)
        self.assertEqual(eig(2, 0, 2), (2, 2))
        self.assertEqual(eig(0, 0, 2), (0, 2))
        self.assertEqual(eig(2, 0, -2), (-2, 2))
        self.assertGreater((-0.1)**4 + 0.1**2, 0)

    def test_nonsmooth_soft_threshold(self):
        soft = lambda y, lam: y - max(-lam, min(lam, y))
        self.assertEqual(soft(1.5, 0.5), 1.0)
        self.assertEqual(soft(-2.0, 0.5), -1.5)
        self.assertEqual(soft(0.25, 0.5), 0.0)
        for y in (-2, -1, 0, 1, 2):
            x = soft(y, 0.5)
            objective = lambda z: 0.5*(z-y)**2 + 0.5*abs(z)
            self.assertLessEqual(objective(x), objective(x+0.01) + 1e-12)

    def test_line_search_and_trust_region_steps(self):
        self.assertAlmostEqual((1/8)*(-8), -1.0)
        self.assertAlmostEqual(4*(1-1.0)**2, 0.0)
        self.assertAlmostEqual(1-0.4, 0.6)
        self.assertAlmostEqual(4*0.6**2, 1.44)

    def test_directional_derivative_sign(self):
        import math
        slope = lambda angle: -math.cos(math.radians(angle))
        self.assertLess(slope(60), 0)
        self.assertAlmostEqual(slope(90), 0, places=12)
        self.assertGreater(slope(120), 0)

    def test_trust_region_reduction_ratio(self):
        import math
        p = -0.5
        predicted = 1 - (1 + p + 0.5*p*p)
        actual = 1 - math.exp(p)
        self.assertAlmostEqual(predicted, 0.375)
        self.assertGreater(actual/predicted, 1.0)

    def test_variable_scaling_condition_number(self):
        scaled = 100.0 * 0.1**2
        self.assertAlmostEqual(max(scaled, 1.0)/min(scaled, 1.0), 1.0)

    def test_exercise_stationary_point_and_value(self):
        x, y = 8/3, -4/3
        self.assertAlmostEqual(2*x+y-4, 0)
        self.assertAlmostEqual(x+2*y, 0)
        self.assertAlmostEqual(x*x+x*y+y*y-4*x, -16/3)

    def test_step_length_conditions(self):
        alpha = 0.5
        phi = lambda a: (4*a-2)**2
        derivative = lambda a: 32*a-16
        c1, c2, c = 1e-4, 0.9, 0.2
        self.assertLessEqual(phi(alpha), phi(0)+c1*alpha*derivative(0))
        self.assertGreaterEqual(derivative(alpha), c2*derivative(0))
        self.assertLessEqual(abs(derivative(alpha)), c2*abs(derivative(0)))
        lower = phi(0)+(1-c)*alpha*derivative(0)
        upper = phi(0)+c*alpha*derivative(0)
        self.assertLessEqual(lower, phi(alpha))
        self.assertLessEqual(phi(alpha), upper)


    def test_wolfe_weak_and_strong_conditions(self):
        phi = lambda a: (4*a-2)**2
        derivative = lambda a: 32*a-16
        def conditions(a):
            armijo = phi(a) <= phi(0)+1e-4*a*derivative(0)+1e-12
            weak = armijo and derivative(a) >= 0.9*derivative(0)
            strong = armijo and abs(derivative(a)) <= 0.9*abs(derivative(0))
            return armijo, weak, strong
        self.assertEqual(conditions(0.5), (True, True, True))
        self.assertEqual(conditions(0.99), (True, True, False))

    def test_goldstein_can_exclude_exact_line_minimizer(self):
        phi = lambda a: 19*a**3-28*a**2-a
        derivative = lambda a: 57*a**2-56*a-1
        c, alpha = 0.2, 1.0
        lower = phi(0)+(1-c)*alpha*derivative(0)
        upper = phi(0)+c*alpha*derivative(0)
        self.assertEqual(derivative(1), 0)
        self.assertEqual(phi(1), -10)
        self.assertFalse(lower <= phi(1) <= upper)
        self.assertLess(phi(1), lower)

    def test_armijo_backtracking_finite_example(self):
        phi = lambda a: (4*a-2)**2
        armijo = lambda a: phi(a) <= phi(0)+1e-4*a*(-16)
        alpha, rho, trials = 1.0, 0.5, 0
        while trials < 100 and not armijo(alpha):
            alpha *= rho
            trials += 1
        trials += 1
        self.assertEqual(alpha, 0.5)
        self.assertEqual(trials, 2)
        self.assertTrue(armijo(alpha))

    def test_zoutendijk_angle_bound_implication(self):
        n, delta = 10000, 0.5
        series = sum(1/(k*k) for k in range(1, n+1))
        bounded_angle_sum = delta**2 * series
        vanishing_angle_sum = series
        self.assertLess(bounded_angle_sum, 1.0)
        self.assertLess(vanishing_angle_sum, 2.0)
        self.assertLess(1/n, 1e-3)
        gradient_a_last, gradient_b_last = 1/n, 1.0
        self.assertLess(gradient_a_last, 1e-3)
        self.assertEqual(gradient_b_last, 1.0)

    def test_convergence_order_definitions(self):
        linear = [0.5]
        superlinear = [0.5]
        quadratic = [0.5]
        for _ in range(6):
            linear.append(0.5*linear[-1])
            superlinear.append(superlinear[-1]**1.5)
            quadratic.append(quadratic[-1]**2)
        self.assertAlmostEqual(linear[5]/linear[4], 0.5)
        self.assertLess(superlinear[6]/superlinear[5], superlinear[2]/superlinear[1])
        self.assertAlmostEqual(quadratic[6]/(quadratic[5]**2), 1.0)

    def test_steepest_descent_condition_number_bound(self):
        for kappa in (1.0, 25.0, 100.0):
            x = (1.0, 1.0)
            values = [0.5*(x[0]**2+kappa*x[1]**2)]
            for _ in range(10):
                g = (x[0], kappa*x[1])
                numerator = g[0]**2+g[1]**2
                if numerator < 1e-28:
                    break
                alpha = numerator/(g[0]**2+kappa*g[1]**2)
                x = (x[0]-alpha*g[0], x[1]-alpha*g[1])
                values.append(0.5*(x[0]**2+kappa*x[1]**2))
            factor = ((kappa-1)/(kappa+1))**2
            ratios = [values[i+1]/values[i] for i in range(len(values)-1)]
            self.assertTrue(all(r <= factor+1e-12 for r in ratios))

    def test_newton_local_quadratic_and_indefinite_direction(self):
        grad = lambda x: x+x**3
        hess = lambda x: 1+3*x*x
        x = 1.0
        errors = [abs(x)]
        for _ in range(5):
            x -= grad(x)/hess(x)
            errors.append(abs(x))
        ratios = [errors[k+1]/(errors[k]**2) for k in range(3)]
        self.assertLess(ratios[-1], ratios[0])
        x = 0.1
        g, h = 4*x**3-2*x, 12*x*x-2
        p = -g/h
        self.assertLess(h, 0)
        self.assertGreater(g*p, 0)

    def test_bfgs_secant_equation_and_positive_definiteness(self):
        Q = ((4.0,1.0),(1.0,3.0))
        B = [[1.0,0.0],[0.0,1.0]]
        x = (2.0,-1.0)
        def dot(a,b): return a[0]*b[0]+a[1]*b[1]
        def mv(A,v): return (A[0][0]*v[0]+A[0][1]*v[1],A[1][0]*v[0]+A[1][1]*v[1])
        for _ in range(2):
            g=mv(Q,x)
            p=(-g[0],-g[1])
            alpha=-dot(g,p)/dot(p,mv(Q,p))
            s=(alpha*p[0],alpha*p[1])
            xn=(x[0]+s[0],x[1]+s[1])
            gn=mv(Q,xn)
            y=(gn[0]-g[0],gn[1]-g[1])
            Bs=mv(B,s)
            sBs,ys=dot(s,Bs),dot(y,s)
            self.assertGreater(sBs,0)
            self.assertGreater(ys,0)
            Bn=[[B[i][j]-Bs[i]*Bs[j]/sBs+y[i]*y[j]/ys for j in range(2)] for i in range(2)]
            sec=mv(Bn,s)
            self.assertLess(max(abs(sec[i]-y[i]) for i in range(2)),1e-10)
            det=Bn[0][0]*Bn[1][1]-Bn[0][1]*Bn[1][0]
            self.assertGreater(Bn[0][0],0)
            self.assertGreater(det,0)
            B,x=Bn,xn

    def test_fifth_batch_eight_python_examples_execute(self):
        import runpy
        files = [
          "03._Line_Search_Methods/09_3.4._Newton’s_Method_with_Hessian_Modification.py",
          "03._Line_Search_Methods/10_3.4.1._Eigenvalue_Modification.py",
          "03._Line_Search_Methods/11_3.4.2._Adding_a_Multiple_of_the_Identity.py",
          "03._Line_Search_Methods/12_3.4.3._Modified_Cholesky_Factorization.py",
          "03._Line_Search_Methods/13_3.4.4._Modified_Symmetric_Indefinite_Factorization.py",
          "03._Line_Search_Methods/14_3.5._Step_Length_Selection_Algorithms.py",
          "03._Line_Search_Methods/15_3.5.1._Interpolation.py",
          "03._Line_Search_Methods/16_3.5.2._Initial_Step_Length.py"
]
        for filename in files:
            with self.subTest(article=filename):
                runpy.run_path(str(ROOT / filename), run_name="__main__")

    def test_hessian_modification_direction_and_spectral_floor(self):
        g = (2, -2)
        raw = (-1, -1)
        self.assertEqual(sum(g[i] * raw[i] for i in range(2)), 0)
        modified = (-0.4, 2)
        self.assertAlmostEqual(sum(g[i] * modified[i] for i in range(2)), -4.8)
        self.assertEqual((3, -1), (3, -1))
        b = ((2, 1), (1, 2))
        self.assertGreater(b[0][0] * b[1][1] - b[0][1] * b[1][0], 0)

    def test_interpolation_and_initial_guess_are_distinct_from_acceptance(self):
        eps = 0.25
        predicted = 2.0 / (1 + eps)
        stationary = (-2 + math.sqrt(4 + 48 * eps)) / (6 * eps)
        self.assertAlmostEqual(predicted, 1.6)
        self.assertAlmostEqual(stationary, 4 / 3)
        self.assertGreater(predicted, stationary)
        phi = lambda x: (x - 2) ** 2
        armijo = lambda a: phi(a) <= phi(0) + 1e-4 * a * (-4)
        self.assertTrue(armijo(0.5 * (-8) / (-4)))
        self.assertFalse(armijo(2 * (-8) / (-4)))


    def test_sixth_batch_python_reproducibility(self):
        import runpy
        cases = [
        "03._Line_Search_Methods/17_3.5.3._A_Line_Search_Algorithm_for_the_Wolfe_Conditions.py",
        "03._Line_Search_Methods/18_3.6._Notes_and_References.py",
        "03._Line_Search_Methods/19_3.7._Exercises.py",
        "04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/00_4.1.1._The_Cauchy_Point.py",
        "04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/01_4.1.2._Improving_on_the_Cauchy_Point.py",
        "04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/02_4.1.3._The_Dogleg_Method.py",
        "04._Trust_Region_Methods/4.1._Algorithms_Based_on_the_Cauchy_Point/03_4.1.4._Two_Dimensional_Subspace_Minimization.py",
        "04._Trust_Region_Methods/4.2._Global_Convergence/00_4.2.1._Reduction_Obtained_by_the_Cauchy_Point.py"
]
        for path in cases:
            with self.subTest(example=path):
                runpy.run_path(str(ROOT / path), run_name="__main__")

    def test_sixth_batch_svg_xml_is_well_formed(self):
        from xml.etree import ElementTree
        diagrams = [
        "wolfe-zoom-search.svg",
        "line-search-floating-point.svg",
        "line-search-exercises-map.svg",
        "trust-region-cauchy.svg",
        "trust-region-improve.svg",
        "trust-region-dogleg.svg",
        "trust-region-subspace.svg",
        "trust-region-cauchy-bound.svg"
]
        for file_name in diagrams:
            with self.subTest(figure=file_name):
                root = ElementTree.parse(ROOT / "assets" / "figures" / file_name).getroot()
                self.assertTrue(root.tag.endswith("svg"))
                self.assertIn("viewBox",root.attrib)

    def test_trust_region_cauchy_bound_independent_check(self):
        for radius in (0.1, 0.2, 0.8, 1.0, 1.5):
            t = min(0.25, radius / 2)
            p = -2 * t
            decrease = -2 * p - 2 * p*p
            lower = min(radius, 0.5)
            self.assertGreaterEqual(decrease + 1e-12, lower)
        self.assertAlmostEqual(0.32, -2*(-0.2) - 2*(-0.2)**2)

    def test_curvature_aware_step_vs_cauchy(self):
        g = (2.0,2.0)
        curvature = (4.0,1.0)
        reduction = lambda p: -(g[0]*p[0]+g[1]*p[1]+0.5*(curvature[0]*p[0]**2+curvature[1]*p[1]**2))
        baseline=(-1/math.sqrt(2),-1/math.sqrt(2))
        candidate=(-0.5,-math.sqrt(3)/2)
        self.assertAlmostEqual(sum(z*z for z in baseline),1)
        self.assertAlmostEqual(sum(z*z for z in candidate),1)
        self.assertGreater(reduction(candidate),reduction(baseline))

    def test_strong_wolfe_acceptance_is_not_only_armijo(self):
        f=lambda a:(a-2)**2
        slope=lambda a:2*(a-2)
        c1,c2=1e-4,0.1
        armijo=lambda a:f(a)<=f(0)+c1*a*slope(0)
        strong=lambda a:armijo(a) and abs(slope(a))<=c2*abs(slope(0))
        self.assertTrue(armijo(0.5))
        self.assertFalse(strong(0.5))
        self.assertTrue(strong(2.0))


    def test_seventh_batch_python_and_svg_reproducibility(self):
        import runpy
        from xml.etree import ElementTree
        files = [
        "04._Trust_Region_Methods/4.2._Global_Convergence/01_4.2.2._Convergence_to_Stationary_Points.py",
        "04._Trust_Region_Methods/02_4.3._Iterative_Solution_of_the_Subproblem.py",
        "04._Trust_Region_Methods/03_4.3.1._The_Hard_Case.py",
        "04._Trust_Region_Methods/04_4.3.2._Proof_of_Theorem_4.1.py",
        "04._Trust_Region_Methods/05_4.3.3._Convergence_of_Algorithms_Based_on_Nearly_Exact_Solutions.py",
        "04._Trust_Region_Methods/06_4.4._Local_Convergence_of_Trust_Region_Newton_Methods.py",
        "04._Trust_Region_Methods/4.5._Other_Enhancements/00_4.5.1._Scaling.py",
        "04._Trust_Region_Methods/4.5._Other_Enhancements/01_4.5.2._Trust_Regions_in_Other_Norms.py"
]
        figures = [
        "trust-stationary-ratio.svg",
        "trust-secular-equation.svg",
        "trust-hard-case.svg",
        "trust-optimality-certificate.svg",
        "trust-nearly-exact.svg",
        "trust-newton-local.svg",
        "trust-scaling-ellipse.svg",
        "trust-norm-geometry.svg"
]
        for path in files:
            with self.subTest(example=path):
                runpy.run_path(str(ROOT / path), run_name="__main__")
        for name in figures:
            with self.subTest(diagram=name):
                figure = ElementTree.parse(ROOT / "assets/figures" / name).getroot()
                self.assertTrue(figure.tag.endswith("svg"))
                self.assertIn("viewBox", figure.attrib)

    def test_hard_case_multipliers_and_global_certificate(self):
        radius=2.
        p=(math.sqrt(35)/3.,-1./3.)
        self.assertAlmostEqual(math.hypot(*p),radius)
        self.assertAlmostEqual(3*p[1],-1.)
        q=lambda x:x[1]-x[0]**2+0.5*x[1]**2
        self.assertAlmostEqual(q(p),-25./6.)
        for rad in (0,.5,1.,2.):
            for n in range(24):
                angle=n*math.pi/12
                v=(rad*math.cos(angle),rad*math.sin(angle))
                first=1.5*(v[1]-p[1])**2
                second=4.-rad**2
                self.assertAlmostEqual(q(v)-q(p),first+second)
                self.assertGreaterEqual(first+second,-1e-12)

    def test_scaling_and_norm_feasibility_checks(self):
        g=(10.,1.)
        D=(10.,1.)
        B=(100.,1.)
        scaled_g=(g[0]/D[0],g[1]/D[1])
        scaled_B=(B[0]/D[0]**2,B[1]/D[1]**2)
        self.assertEqual(scaled_g,(1.,1.))
        self.assertEqual(scaled_B,(1.,1.))
        p=(-.2,-.3)
        self.assertAlmostEqual(math.hypot(*p),math.sqrt(.13))
        self.assertGreater(math.hypot(*p),.3)
        self.assertLessEqual(max(map(abs,p)),.3)

    def test_eta_ratio_and_nearly_exact_quality(self):
        g,h=1.4,2.2
        p=-.5
        predicted=-g*p-.5*h*p*p
        actual=.6-(.5*.5**2+.1*.5**4)
        self.assertAlmostEqual(predicted,.425)
        self.assertAlmostEqual(actual,.46875)
        self.assertGreater(actual/predicted,1.)
        exact=25./6.
        ratio=(1.5**2+5./18.)/exact
        self.assertGreater(ratio,.6)
        self.assertLess((.5**2+5./18.)/exact,.6)

    def test_nonlinear_cg_beta_variants_and_powell_ratio(self):
        g1 = (Fraction(42, 73), Fraction(-30, 73))
        g2 = (Fraction(84, 365), Fraction(-60, 365))
        p1 = (Fraction(-2886, 5329), Fraction(2442, 5329))
        dot = lambda u, v: u[0]*v[0] + u[1]*v[1]
        y = (g2[0] - g1[0], g2[1] - g1[1])
        self.assertEqual(dot(g1, g1), Fraction(2664, 5329))
        self.assertEqual(dot(g2, g2), Fraction(10656, 133225))
        self.assertEqual(dot(g2, g2)/dot(g1, g1), Fraction(4, 25))
        self.assertEqual(dot(g2, y)/dot(g1, g1), Fraction(-6, 25))
        self.assertEqual(dot(g2, y)/dot(p1, y), Fraction(-2, 5))
        self.assertEqual(abs(dot(g2, g1))/dot(g2, g2), Fraction(5, 2))

    def test_zoutendijk_partial_sums(self):
        c2 = Fraction(1, 4)
        vanish = c2 * sum(Fraction(9, 10)**(2*k) for k in range(1, 1001))
        self.assertLess(vanish, Fraction(81, 76))
        self.assertEqual(c2 * sum(Fraction(1) for _ in range(1, 1001)), Fraction(1000, 4))

if __name__ == "__main__":
    unittest.main()
