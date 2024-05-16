
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    else:
        return x / y

print("Selecione a operação desejada:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite sua opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))
elif opcao == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))
elif opcao == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
elif opcao == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))
else:
    print("Opção inválida")


