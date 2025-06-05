# Importa operação Limit (limite) da biblioteca sympy.
# Importa Symbol - possibilidade de operações com simbolos.
from sympy import Limit, Symbol, sqrt, S

# Definindo o valor de c(c=matricula % 10).
c = (62 % 10)
# c vai ser igual 2

# Definindo as funções a serem resolvidas.


def minha_funcao1(x):
    return ((c+1)*x-(c+1))/(sqrt(x) - 1)


def minha_funcao2(x):
    return ((c+1)*(x**4)+(3*x ** 2)-2)/(4-x ** 4)


# Limpa a área do console para facilitar a visualização do resultado.
print('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Calcula limite da função quando x -> 1.
Resultado1 = Limit(minha_funcao1(x), x, 1).doit()

# Calcula limite da função quando x -> +infinito.
Resultado2 = Limit(minha_funcao2(x), x, S.Infinity).doit()

# Calcula limite da função quando x -> -infinito.
Resultado3 = Limit(minha_funcao2(x), x, -S.Infinity).doit()

print('\n Limite da função minhaFunção para x->1.')
print(Resultado1)
print('\n Limite da função minhaFunção2 para x->+infinito.')
print(Resultado2)
print('\n Limite da função minhaFunção2 para x->-infinito.')
print(Resultado3)
