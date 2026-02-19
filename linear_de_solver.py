from sympy import *
x=Symbol('x')
y=Function('y')(x)
DE=Eq(y.diff(x)+y/x,x**3)
sol=dsolve(DE,y)
display(sol)
