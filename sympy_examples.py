from sympy import (
    symbols, expand, factor, solve, simplify,
    diff, integrate, limit, Matrix, init_printing
)
import sympy as sp

def demonstrate_sympy():
    """Demonstrate key features of SymPy library"""
    # Enable pretty printing
    init_printing(use_unicode=True)
    
    print("SymPy Mathematics Examples")
    print("=========================\n")
    
    # Define symbolic variables
    x, y, z = symbols('x y z')
    
    # 1. Basic Algebra
    print("1. Basic Algebra")
    print("--------------")
    expr = (x + y)**2
    print(f"Expand (x + y)²:")
    print(f"Result: {expand(expr)}")
    
    expr2 = x**2 + 2*x*y + y**2
    print(f"\nFactor x² + 2xy + y²:")
    print(f"Result: {factor(expr2)}")
    
    # 2. Equation Solving
    print("\n2. Equation Solving")
    print("-----------------")
    equation = x**2 - 5*x + 6
    print(f"Solve x² - 5x + 6 = 0:")
    print(f"Solutions: {solve(equation, x)}")
    
    # 3. Calculus
    print("\n3. Calculus")
    print("-----------")
    
    # Differentiation
    expr3 = x**3 + x**2 + x + 1
    derivative = diff(expr3, x)
    print(f"Derivative of x³ + x² + x + 1:")
    print(f"Result: {derivative}")
    
    # Integration
    integral = integrate(x**2, x)
    print(f"\nIntegral of x²:")
    print(f"Result: {integral}")
    
    # Limits
    lim = limit(sp.sin(x)/x, x, 0)
    print(f"\nLimit of sin(x)/x as x → 0:")
    print(f"Result: {lim}")
    
    # 4. Linear Algebra
    print("\n4. Linear Algebra")
    print("----------------")
    matrix = Matrix([[1, 2], [3, 4]])
    print(f"Matrix:")
    print(matrix)
    print(f"\nDeterminant: {matrix.det()}")
    print(f"Eigenvalues: {matrix.eigenvals()}")
    
    # 5. Series Expansion
    print("\n5. Series Expansion")
    print("-----------------")
    series = sp.series(sp.exp(x), x, 0, 5)
    print(f"Taylor series of e^x around 0 (up to 4th term):")
    print(series)
    
    # 6. Trigonometry
    print("\n6. Trigonometry")
    print("--------------")
    trig_expr = sp.sin(x)**2 + sp.cos(x)**2
    print(f"Simplify sin²(x) + cos²(x):")
    print(f"Result: {simplify(trig_expr)}")
    
    # 7. Solving Systems of Equations
    print("\n7. Systems of Equations")
    print("---------------------")
    eq1 = sp.Eq(2*x + y, 8)
    eq2 = sp.Eq(x + 2*y, 10)
    solution = solve((eq1, eq2), (x, y))
    print(f"Solve system:")
    print("2x + y = 8")
    print("x + 2y = 10")
    print(f"Solution: x = {solution[x]}, y = {solution[y]}")

def main():
    demonstrate_sympy()
    
    print("\nSymPy Features Summary:")
    print("1. Symbolic Mathematics: Work with mathematical expressions symbolically")
    print("2. Algebra: Expand, factor, and simplify expressions")
    print("3. Calculus: Derivatives, integrals, limits")
    print("4. Linear Algebra: Matrices, determinants, eigenvalues")
    print("5. Series: Taylor series, power series")
    print("6. Equation Solving: Solve equations and systems of equations")
    print("7. Trigonometry: Simplify trigonometric expressions")
    print("8. Pretty Printing: Display mathematical expressions beautifully")

if __name__ == "__main__":
    main()
