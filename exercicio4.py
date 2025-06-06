# Passo 1
# Resistores: R1 = 25; R2 = 10; R3 = 20
# Correntes: I1 = ?; I2 = I1 - I3; I3 = ?
# Tensões: V1 = 10 + 2 * c; V2 = 5 + 2 * c;
# c = (62 % 10) -> c = 2
# Tensões: V1 = 10 + 2 * 2 = 14; V2 = 5 + 2 * 2 = 9

# Passo 2 - Aplicar a lei das malhas de Kirchhoff
# Malha esquerda: V1 - R1 * I1 - R2 * (I1 - I3) = 0
# Malha direita: V2 - R3 * I3 - R2 * (I1 - I3) = 0

# Passo 3 - Resolver o sistema de equações
from sympy import Symbol, solve

# Limpa a área do console para facilitar a visualização do resultado.
print('\n' * 100)
# Definindo o valor de c (c = matricula % 10).
c = (62 % 10)
# c vai ser igual 2

# Definindo os valores dos resistores.
R1 = 25   # Ohms
R2 = 10   # Ohms
R3 = 20   # Ohms
print(f'R1: {R1} Ohms; R2: {R2} Ohms; R3: {R3} Ohms')

# Definindo as tensões.
V1 = 10 + 2 * c   # Volts
V2 = 5 + 2 * c    # Volts
print(f'V1: {V1} Volts; V2: {V2} Volts')


# Malha esquerda: V1 - R1 * I1 - R2 * (I1 - I3) = 0
def minha_funcao1(x, y):
    return V1 - R1 * x - R2 * (x - y)


# Malha direita: V2 - R3 * I3 - R2 * (I1 - I3) = 0
def minha_funcao2(x, y):
    return V2 - R3 * y - R2 * (x - y)


x = Symbol('x')
y = Symbol('y')

f = minha_funcao1(x, y)
print(f'\nEquação da malha esquerda: {f}')
g = minha_funcao2(x, y)
print(f'Equação da malha direita: {g}')

Resultado = solve((f, g))
print('\nResultado do sistema de equações:')
print(f'Resultado: {Resultado}')

I1 = Resultado[x]  # Corrente I1
I3 = Resultado[y]  # Corrente I3
I2 = I1 - I3  # Corrente I2

print('\nResultado do sistema de equações:')
print(f'I1 = {I1.evalf(4)} A; I3 = {I3.evalf(4)} A; I2 = {I2.evalf(4)} A')


# # Resultado final
# # I1 =  0,5111 A; I3 = 0,3889 A; I2 = I1 - I3 = 0,1222 A
