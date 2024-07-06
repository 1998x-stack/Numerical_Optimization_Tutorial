structure = {
    "01._Introduction": [
        "1.1._Mathematical_Formulation",
        "1.2._Example:_A_Transportation_Problem",
        "1.3._Continuous_vs._Discrete_Optimization",
        "1.4._Constrained_and_Unconstrained_Optimization",
        "1.5._Global_and_Local_Optimization",
        "1.6._Stochastic_and_Deterministic_Optimization",
        "1.7._Convexity",
        "1.8._Optimization_Algorithms",
        "1.9._Notes_and_References"
    ],
    "02._Fundamentals_of_Unconstrained_Optimization": [
        "2.1._What_Is_a_Solution?",
        "2.2._Recognizing_a_Local_Minimum",
        "2.3._Nonsmooth_Problems",
        {
            "2.4._Overview_of_Algorithms": [
                "2.4.1._Two_Strategies:_Line_Search_and_Trust_Region",
                "2.4.2._Search_Directions_for_Line_Search_Methods",
                "2.4.3._Models_for_Trust-Region_Methods",
                "2.4.4._Scaling"
            ]
        },
        "2.5._Exercises"
    ],
    "03._Line_Search_Methods": [
        "3.1._Step_Length",
        "3.1.1._The_Wolfe_Conditions",
        "3.1.2._The_Goldstein_Conditions",
        "3.1.3._Sufficient_Decrease_and_Backtracking",
        "3.2._Convergence_of_Line_Search_Methods",
        "3.3._Rate_of_Convergence",
        "3.3.1._Convergence_Rate_of_Steepest_Descent",
        "3.3.2._Newton’s_Method",
        "3.3.3._Quasi-Newton_Methods",
        "3.4._Newton’s_Method_with_Hessian_Modification",
        "3.4.1._Eigenvalue_Modification",
        "3.4.2._Adding_a_Multiple_of_the_Identity",
        "3.4.3._Modified_Cholesky_Factorization",
        "3.4.4._Modified_Symmetric_Indefinite_Factorization",
        "3.5._Step-Length_Selection_Algorithms",
        "3.5.1._Interpolation",
        "3.5.2._Initial_Step_Length",
        "3.5.3._A_Line_Search_Algorithm_for_the_Wolfe_Conditions",
        "3.6._Notes_and_References",
        "3.7._Exercises"
    ],
    "04._Trust-Region_Methods": [
        {
            "4.1._Algorithms_Based_on_the_Cauchy_Point": [
                "4.1.1._The_Cauchy_Point",
                "4.1.2._Improving_on_the_Cauchy_Point",
                "4.1.3._The_Dogleg_Method",
                "4.1.4._Two-Dimensional_Subspace_Minimization"
            ]
        },
        {
            "4.2._Global_Convergence": [
                "4.2.1._Reduction_Obtained_by_the_Cauchy_Point",
                "4.2.2._Convergence_to_Stationary_Points"
            ]
        },
        "4.3._Iterative_Solution_of_the_Subproblem",
        "4.3.1._The_Hard_Case",
        "4.3.2._Proof_of_Theorem_4.1",
        "4.3.3._Convergence_of_Algorithms_Based_on_Nearly_Exact_Solutions",
        "4.4._Local_Convergence_of_Trust-Region_Newton_Methods",
        {
            "4.5._Other_Enhancements": [
                "4.5.1._Scaling",
                "4.5.2._Trust_Regions_in_Other_Norms"
            ]
        },
        "4.6._Notes_and_References",
        "4.7._Exercises"
    ],
    "05._Conjugate_Gradient_Methods": [
        {
            "5.1._The_Linear_Conjugate_Gradient_Method": [
                "5.1.1._Conjugate_Direction_Methods",
                "5.1.2._Basic_Properties_of_the_Conjugate_Gradient_Method",
                "5.1.3._A_Practical_Form_of_the_Conjugate_Gradient_Method",
                "5.1.4._Rate_of_Convergence",
                "5.1.5._Preconditioning",
                "5.1.6._Practical_Preconditioners"
            ]
        },
        {
            "5.2._Nonlinear_Conjugate_Gradient_Methods": [
                "5.2.1._The_Fletcher–Reeves_Method",
                "5.2.2._The_Polak–Ribiere_Method_and_Variants",
                "5.2.3._Quadratic_Termination_and_Restarts",
                "5.2.4._Behavior_of_the_Fletcher–Reeves_Method",
                "5.2.5._Global_Convergence",
                "5.2.6._Numerical_Performance"
            ]
        },
        "5.3._Notes_and_References",
        "5.4._Exercises"
    ],
    "06._Quasi-Newton_Methods": [
        {
            "6.1._The_BFGS_Method": [
                "6.1.1._Properties_of_the_BFGS_Method",
                "6.1.2._Implementation"
            ]
        },
        {
            "6.2._The_SR1_Method": [
                "6.2.1._Properties_of_SR1_Updating"
            ]
        },
        "6.3._The_Broyden_Class",
        {
            "6.4._Convergence_Analysis": [
                "6.4.1._Global_Convergence_of_the_BFGS_Method",
                "6.4.2._Superlinear_Convergence_of_the_BFGS_Method",
                "6.4.3._Convergence_Analysis_of_the_SR1_Method"
            ]
        },
        "6.5._Notes_and_References",
        "6.6._Exercises"
    ],
    "07._Large-Scale_Unconstrained_Optimization": [
        {
            "7.1._Inexact_Newton_Methods": [
                "7.1.1._Local_Convergence_of_Inexact_Newton_Methods",
                "7.1.2._Line_Search_Newton–CG_Method",
                "7.1.3._Trust-Region_Newton–CG_Method",
                "7.1.4._Preconditioning_the_Trust-Region_Newton–CG_Method",
                "7.1.5._Trust-Region_Newton–Lanczos_Method"
            ]
        },
        {
            "7.2._Limited-Memory_Quasi-Newton_Methods": [
                "7.2.1._Limited-Memory_BFGS",
                "7.2.2._Relationship_with_Conjugate_Gradient_Methods",
                "7.2.3._General_Limited-Memory_Updating",
                "7.2.4._Compact_Representation_of_BFGS_Updating",
                "7.2.5._Unrolling_the_Update"
            ]
        },
        "7.3._Sparse_Quasi-Newton_Updates",
        "7.4._Algorithms_for_Partially_Separable_Functions",
        "7.5._Perspectives_and_Software",
        "7.6._Notes_and_References",
        "7.7._Exercises"
    ],
    "08._Calculating_Derivatives": [
        {
            "8.1._Finite-Difference_Derivative_Approximations": [
                "8.1.1._Approximating_the_Gradient",
                "8.1.2._Approximating_a_Sparse_Jacobian",
                "8.1.3._Approximating_the_Hessian",
                "8.1.4._Approximating_a_Sparse_Hessian"
            ]
        },
        {
            "8.2._Automatic_Differentiation": [
                "8.2.1._An_Example",
                "8.2.2._The_Forward_Mode",
                "8.2.3._The_Reverse_Mode",
                "8.2.4._Vector_Functions_and_Partial_Separability",
                "8.2.5._Calculating_Jacobians_of_Vector_Functions",
                "8.2.6._Calculating_Hessians:_Forward_Mode",
                "8.2.7._Calculating_Hessians:_Reverse_Mode",
                "8.2.8._Current_Limitations"
            ]
        },
        "8.3._Notes_and_References",
        "8.4._Exercises"
    ],
    "09._Derivative-Free_Optimization": [
        "9.1._Finite_Differences_and_Noise",
        {
            "9.2._Model-Based_Methods": [
                "9.2.1._Interpolation_and_Polynomial_Bases",
                "9.2.2._Updating_the_Interpolation_Set",
                "9.2.3._A_Method_Based_on_Minimum-Change_Updating"
            ]
        },
        {
            "9.3._Coordinate_and_Pattern-Search_Methods": [
                "9.3.1._Coordinate_Search_Method",
                "9.3.2._Pattern-Search_Methods"
            ]
        },
        "9.4._A_Conjugate-Direction_Method",
        "9.5._Nelder–Mead_Method",
        "9.6._Implicit_Filtering",
        "9.7._Notes_and_References",
        "9.8._Exercises"
    ],
    "10._Least-Squares_Problems": [
        "10.1._Background",
        "10.2._Linear_Least-Squares_Problems",
        {
            "10.3._Algorithms_for_Nonlinear_Least-Squares_Problems": [
                "10.3.1._The_Gauss–Newton_Method",
                "10.3.2._Convergence_of_the_Gauss–Newton_Method",
                "10.3.3._The_Levenberg–Marquardt_Method",
                "10.3.4._Implementation_of_the_Levenberg–Marquardt_Method",
                "10.3.5._Convergence_of_the_Levenberg–Marquardt_Method",
                "10.3.6._Methods_for_Large-Residual_Problems"
            ]
        },
        "10.4._Orthogonal_Distance_Regression",
        "10.5._Notes_and_References",
        "10.6._Exercises"
    ],
    "11._Nonlinear_Equations": [
        {
            "11.1._Local_Algorithms": [
                "11.1.1._Newton’s_Method_for_Nonlinear_Equations",
                "11.1.2._Inexact_Newton_Methods",
                "11.1.3._Broyden’s_Method",
                "11.1.4._Tensor_Methods"
            ]
        },
        {
            "11.2._Practical_Methods": [
                "11.2.1._Merit_Functions",
                "11.2.2._Line_Search_Methods",
                "11.2.3._Trust-Region_Methods"
            ]
        },
        {
            "11.3._Continuation/Homotopy_Methods": [
                "11.3.1._Motivation",
                "11.3.2._Practical_Continuation_Methods"
            ]
        },
        "11.4._Notes_and_References",
        "11.5._Exercises"
    ],
    "12._Theory_of_Constrained_Optimization": [
        "12.1._Local_and_Global_Solutions",
        "12.2._Smoothness",
        {
            "12.3._Examples": [
                "12.3.1._A_Single_Equality_Constraint",
                "12.3.2._A_Single_Inequality_Constraint",
                "12.3.3._Two_Inequality_Constraints"
            ]
        },
        "12.4._Tangent_Cone_and_Constraint_Qualifications",
        "12.5._First-Order_Optimality_Conditions",
        {
            "12.6._First-Order_Optimality_Conditions:_Proof": [
                "12.6.1._Relating_the_Tangent_Cone_and_the_First-Order_Feasible_Direction_Set",
                "12.6.2._A_Fundamental_Necessary_Condition",
                "12.6.3._Farkas’_Lemma",
                "12.6.4._Proof_of_Theorem_12.1"
            ]
        },
        {
            "12.7._Second-Order_Conditions": [
                "12.7.1._Second-Order_Conditions_and_Projected_Hessians"
            ]
        },
        "12.8._Other_Constraint_Qualifications",
        "12.9._A_Geometric_Viewpoint",
        "12.10._Lagrange_Multipliers_and_Sensitivity",
        "12.11._Duality",
        "12.12._Notes_and_References",
        "12.13._Exercises"
    ],
    "13._Linear_Programming:_The_Simplex_Method": [
        {
            "13.1._Optimality_and_Duality": [
                "13.1.1._Optimality_Conditions",
                "13.1.2._The_Dual_Problem"
            ]
        },
        {
            "13.2._Geometry_of_the_Feasible_Set": [
                "13.2.1._Bases_and_Basic_Feasible_Points",
                "13.2.2._Vertices_of_the_Feasible_Polytope"
            ]
        },
        {
            "13.3._The_Simplex_Method": [
                "13.3.1._Outline",
                "13.3.2._A_Single_Step_of_the_Method"
            ]
        },
        "13.4._Linear_Algebra_in_the_Simplex_Method",
        {
            "13.5._Other_Important_Details": [
                "13.5.1._Pricing_and_Selection_of_the_Entering_Index",
                "13.5.2._Starting_the_Simplex_Method",
                "13.5.3._Degenerate_Steps_and_Cycling"
            ]
        },
        "13.6._The_Dual_Simplex_Method",
        "13.7._Presolving",
        "13.8._Where_Does_the_Simplex_Method_Fit?",
        "13.9._Notes_and_References",
        "13.10._Exercises"
    ],
    "14._Linear_Programming:_Interior-Point_Methods": [
        {
            "14.1._Primal-Dual_Methods": [
                "14.1.1._Outline",
                "14.1.2._The_Central_Path",
                "14.1.3._Central_Path_Neighborhoods_and_Path-Following_Methods"
            ]
        },
        {
            "14.2._Practical_Primal-Dual_Algorithms": [
                "14.2.1._Corrector_and_Centering_Steps",
                "14.2.2._Step_Lengths",
                "14.2.3._Starting_Point",
                "14.2.4._A_Practical_Algorithm",
                "14.2.5._Solving_the_Linear_Systems"
            ]
        },
        {
            "14.3._Other_Primal-Dual_Algorithms_and_Extensions": [
                "14.3.1._Other_Path-Following_Methods",
                "14.3.2._Potential-Reduction_Methods",
                "14.3.3._Extensions"
            ]
        },
        "14.4._Perspectives_and_Software",
        "14.5._Notes_and_References",
        "14.6._Exercises"
    ],
    "15._Fundamentals_of_Algorithms_for_Nonlinear_Constrained_Optimization": [
        "15.1._Categorizing_Optimization_Algorithms",
        "15.2._The_Combinatorial_Difficulty_of_Inequality-Constrained_Problems",
        {
            "15.3._Elimination_of_Variables": [
                "15.3.1._Simple_Elimination_using_Linear_Constraints",
                "15.3.2._General_Reduction_Strategies_for_Linear_Constraints",
                "15.3.3._Effect_of_Inequality_Constraints"
            ]
        },
        {
            "15.4._Merit_Functions_and_Filters": [
                "15.4.1._Merit_Functions",
                "15.4.2._Filters"
            ]
        },
        "15.5._The_Maratos_Effect",
        {
            "15.6._Second-Order_Correction_and_Nonmonotone_Techniques": [
                "15.6.1._Nonmonotone_(Watchdog)_Strategy"
            ]
        },
        "15.7._Notes_and_References",
        "15.8._Exercises"
    ],
    "16._Quadratic_Programming": [
        {
            "16.1._Equality-Constrained_Quadratic_Programs": [
                "16.1.1._Properties_of_Equality-Constrained_QPs"
            ]
        },
        {
            "16.2._Direct_Solution_of_the_KKT_System": [
                "16.2.1._Factoring_the_Full_KKT_System",
                "16.2.2._Schur-Complement_Method",
                "16.2.3._Null-Space_Method"
            ]
        },
        {
            "16.3._Iterative_Solution_of_the_KKT_System": [
                "16.3.1._CG_Applied_to_the_Reduced_System",
                "16.3.2._The_Projected_CG_Method"
            ]
        },
        {
            "16.4._Inequality-Constrained_Problems": [
                "16.4.1._Optimality_Conditions_for_Inequality-Constrained_Problems",
                "16.4.2._Degeneracy"
            ]
        },
        {
            "16.5._Active-Set_Methods_for_Convex_QPs": [
                "16.5.1._Specification_of_the_Active-Set_Method_for_Convex_QP",
                "16.5.2._Further_Remarks_on_the_Active-Set_Method",
                "16.5.3._Finite_Termination_of_Active-Set_Algorithm_on_Strictly_Convex_QPs",
                "16.5.4._Updating_Factorizations"
            ]
        },
        {
            "16.6._Interior-Point_Methods": [
                "16.6.1._Solving_the_Primal-Dual_System",
                "16.6.2._Step_Length_Selection",
                "16.6.3._A_Practical_Primal-Dual_Method"
            ]
        },
        {
            "16.7._The_Gradient_Projection_Method": [
                "16.7.1._Cauchy_Point_Computation",
                "16.7.2._Subspace_Minimization"
            ]
        },
        "16.8._Perspectives_and_Software",
        "16.9._Notes_and_References",
        "16.10._Exercises"
    ],
    "17._Penalty_and_Augmented_Lagrangian_Methods": [
        {
            "17.1._The_Quadratic_Penalty_Method": [
                "17.1.1._Motivation",
                "17.1.2._Algorithmic_Framework",
                "17.1.3._Convergence_of_the_Quadratic_Penalty_Method",
                "17.1.4._Ill_Conditioning_and_Reformulations"
            ]
        },
        {
            "17.2._Nonsmooth_Penalty_Functions": [
                "17.2.1._A_Practical_L1_Penalty_Method",
                "17.2.2._A_General_Class_of_Nonsmooth_Penalty_Methods"
            ]
        },
        {
            "17.3._Augmented_Lagrangian_Method:_Equality_Constraints": [
                "17.3.1._Motivation_and_Algorithmic_Framework",
                "17.3.2._Properties_of_the_Augmented_Lagrangian"
            ]
        },
        {
            "17.4._Practical_Augmented_Lagrangian_Methods": [
                "17.4.1._Bound-Constrained_Formulation",
                "17.4.2._Linearly_Constrained_Formulation",
                "17.4.3._Unconstrained_Formulation"
            ]
        },
        "17.5._Perspectives_and_Software",
        "17.6._Notes_and_References",
        "17.7._Exercises"
    ],
    "18._Sequential_Quadratic_Programming": [
        {
            "18.1._Local_SQP_Method": [
                "18.1.1._SQP_Framework",
                "18.1.2._Inequality_Constraints"
            ]
        },
        {
            "18.2._Preview_of_Practical_SQP_Methods": [
                "18.2.1._IQP_and_EQP",
                "18.2.2._Enforcing_Convergence"
            ]
        },
        {
            "18.3._Algorithmic_Development": [
                "18.3.1._Handling_Inconsistent_Linearizations",
                "18.3.2._Full_Quasi-Newton_Approximations",
                "18.3.3._Reduced-Hessian_Quasi-Newton_Approximations",
                "18.3.4._Merit_Functions",
                "18.3.5._Second-Order_Correction"
            ]
        },
        "18.4._A_Practical_Line_Search_SQP_Method",
        {
            "18.5._Trust-Region_SQP_Methods": [
                "18.5.1._A_Relaxation_Method_for_Equality-Constrained_Optimization",
                "18.5.2._Sequential_L1_Quadratic_Programming_(SLQP)",
                "18.5.3._Sequential_Linear-Quadratic_Programming_(SLQP)",
                "18.5.4._A_Technique_for_Updating_the_Penalty_Parameter"
            ]
        },
        "18.6._Nonlinear_Gradient_Projection",
        {
            "18.7._Convergence_Analysis": [
                "18.7.1._Rate_of_Convergence"
            ]
        },
        "18.8._Perspectives_and_Software",
        "18.9._Notes_and_References",
        "18.10._Exercises"
    ],
    "19._Interior-Point_Methods_for_Nonlinear_Programming": [
        "19.1._Two_Interpretations",
        "19.2._A_Basic_Interior-Point_Algorithm",
        {
            "19.3._Algorithmic_Development": [
                "19.3.1._Primal_vs._Primal-Dual_System",
                "19.3.2._Solving_the_Primal-Dual_System",
                "19.3.3._Updating_the_Barrier_Parameter",
                "19.3.4._Handling_Nonconvexity_and_Singularity",
                "19.3.5._Step_Acceptance:_Merit_Functions_and_Filters",
                "19.3.6._Quasi-Newton_Approximations",
                "19.3.7._Feasible_Interior-Point_Methods"
            ]
        },
        "19.4._A_Line_Search_Interior-Point_Method",
        "19.5._A_Trust-Region_Interior-Point_Method",
        {
            "19.5.1._An_Algorithm_for_Solving_the_Barrier_Problem": [
                "19.5.2._Step_Computation",
                "19.5.3._Lagrange_Multipliers_Estimates_and_Step_Acceptance",
                "19.5.4._Description_of_a_Trust-Region_Interior-Point_Method"
            ]
        },
        "19.6._The_Primal_Log-Barrier_Method",
        {
            "19.7._Global_Convergence_Properties": [
                "19.7.1._Failure_of_the_Line_Search_Approach",
                "19.7.2._Modified_Line_Search_Methods",
                "19.7.3._Global_Convergence_of_the_Trust-Region_Approach"
            ]
        },
        "19.8._Superlinear_Convergence",
        "19.9._Perspectives_and_Software",
        "19.10._Notes_and_References",
        "19.11._Exercises"
    ],
    "Appendix_A._Background_Material": [
        {
            "A.1._Elements_of_Linear_Algebra": [
                "A.1.1._Vectors_and_Matrices",
                "A.1.2._Norms",
                "A.1.3._Subspaces",
                "A.1.4._Eigenvalues,_Eigenvectors,_and_the_Singular-Value_Decomposition",
                "A.1.5._Determinant_and_Trace",
                "A.1.6._Matrix_Factorizations:_Cholesky,_LU,_QR",
                "A.1.7._Symmetric_Indefinite_Factorization",
                "A.1.8._Sherman–Morrison–Woodbury_Formula",
                "A.1.9._Interlacing_Eigenvalue_Theorem",
                "A.1.10._Error_Analysis_and_Floating-Point_Arithmetic",
                "A.1.11._Conditioning_and_Stability"
            ]
        },
        {
            "A.2._Elements_of_Analysis,_Geometry,_Topology": [
                "A.2.1._Sequences",
                "A.2.2._Rates_of_Convergence",
                "A.2.3._Topology_of_the_Euclidean_Space_IRn",
                "A.2.4._Convex_Sets_in_IRn",
                "A.2.5._Continuity_and_Limits",
                "A.2.6._Derivatives",
                "A.2.7._Directional_Derivatives",
                "A.2.8._Mean_Value_Theorem",
                "A.2.9._Implicit_Function_Theorem",
                "A.2.10._Order_Notation",
                "A.2.11._Root-Finding_for_Scalar_Equations"
            ]
        }
    ],
}


import os
from typing import Dict, Any

def create_directories_and_files(
        base_path: str, 
        structure: Dict[str, Any], 
        readme_file, 
        parent_path: str = "", 
        level: int = 1
    ):
    heading = "#" * level

    for key, value in structure.items():
        current_path = os.path.join(base_path, key.replace(" ", "_").replace("/", "_").replace("-", "_"))

        # 创建目录
        os.makedirs(current_path, exist_ok=True)

        # 在README中添加章节标题
        if parent_path:
            readme_file.write(f"{heading} {parent_path}/{key}\n\n")
        else:
            readme_file.write(f"{heading} {key}\n\n")

        # 递归调用创建子目录和文件
        if isinstance(value, dict) and value:
            create_directories_and_files(
                current_path, 
                value, 
                readme_file, 
                parent_path + "/" + key if parent_path else key, 
                level + 1
            )
        elif isinstance(value, list) and value:
            for idx, item in enumerate(value):
                if isinstance(item, dict) and item:
                    create_directories_and_files(
                        current_path, 
                        item, 
                        readme_file, 
                        parent_path + "/" + key if parent_path else key, 
                        level + 1
                    )
                else:
                    item = f"{idx:02d}_{item}"
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {item}\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.py)\n")
                    
                    
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {item}\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.md)\n")
        else:
            # 创建文件并写入初始内容
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {key}\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")
            
            
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {key}\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")

        # 添加空行以分隔不同的章节
        readme_file.write("\n")

def main():
    root_dir = './'
    # 创建根目录
    os.makedirs(root_dir, exist_ok=True)

    # 创建 README.md 文件
    with open(os.path.join(root_dir, "README.md"), 'w', encoding='utf-8') as readme_file:
        readme_file.write("# Numerical Optimization\n\n")
        readme_file.write("这是一个关于Numerical Optimization的目录结构。\n\n")
        create_directories_and_files(root_dir, structure, readme_file)

    print("目录和文件结构已生成，并创建 README.md 文件。")

if __name__ == "__main__":
    main()