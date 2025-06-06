# Equações a serem resolvidas em relação a x:
# 2cos[4(c+1)x]=-5
# 5raiz(x)-4x^2+(x/2)=c
# e^(x+1)+e^(x-2)+e^x=c+4

from sympy import Symbol, solve, cos, exp, sqrt
# Definindo o valor de c (c = matricula % 10).
c = (62 % 10)
# c vai ser igual 2


def primeira_equacao(x):
    return 2 * cos(4 * (c + 1) * x) + 5


def segunda_equacao(x):
    return 5 * sqrt(x) - 4 * x**2 + (x / 2) - c


def terceira_equacao(x):
    return exp(x + 1) + exp(x - 2) + exp(x) - (c + 4)


# Limpa a área do console para facilitar a visualização do resultado.
print('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Calcula as raízes da primeira equação.
resultado_primeira = solve(primeira_equacao(x), x)
print('\nRaízes da primeira equação:')
print(resultado_primeira)

# Calcula as raízes da segunda equação.
resultado_segunda = solve(segunda_equacao(x), x)
print('\nRaízes da segunda equação:')
print(resultado_segunda)

# Calcula as raízes da terceira equação.
resultado_terceira = solve(terceira_equacao(x), x)
print('\nRaízes da terceira equação:')
print(resultado_terceira)
