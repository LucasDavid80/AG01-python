# Importa Symbol - possibilidade de operações com simbolos.
from sympy import Integral, Symbol, exp, solve, log, N

# Limpa a área do console para facilitar a visualização do resultado.
print('\n' * 100)
# Definindo o valor de c(c=matricula % 10).
matricula = input('Digite o valor da matricula: ')
c = (int(matricula) % 10)


def minha_funcao(x):
    return exp(3 * x + c) - 4 * log(x ** 2) + 5 * x - c


x = Symbol('x')

# Calcula a integral definida entre 2 e 8 da função minha_funcao.
Resultado = Integral(minha_funcao(x), (x, 2, 8)).doit()


print('\n Calculo da área sob a curva da função:')
print(Resultado)

# Calcula o valor numérico aproximado da integral definida.
Resultado_final = N(Resultado)

print('\n Valor numérico aproximado da área:')
print(Resultado_final)
