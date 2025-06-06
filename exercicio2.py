# Importa Symbol - possibilidade de operações com simbolos.
from sympy import Derivative, Integral, Symbol, root

# Limpa a área do console para facilitar a visualização do resultado.
print('\n' * 100)
# Definindo o valor de c(c=matricula % 10).
matricula = input('Digite o valor da matricula: ')
c = (int(matricula) % 10)

# Equação da velocidade


def velocidade(t):
    return 6 * (c + 1) * root(t, 5) - 3 * (c+1) * (t**2) + (t / (c + 3)) - 4


t = Symbol('t')

# Calcula a integral indefinida da função velocidade que é o deslocamento.
Resultado_integral = Integral(velocidade(t), t).doit()

print('\n Integral da função velocidade = função deslocamento.')
print(Resultado_integral)

# Calcula o deslocamento entre t=2 e t=5.
Resultado_deslocamento = Integral(velocidade(t), (t, 2, 5)).doit()

print('\n Deslocamento entre t=2 e t=5.')
print(Resultado_deslocamento)

# Calcula a equação da aceleração, que é a derivada da velocidade.

Resultado_derivada = Derivative(velocidade(t), t).doit()
print('\n Derivada da função velocidade = função aceleração.')
print(Resultado_derivada)
