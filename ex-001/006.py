#Faça um algoritmo para ler dois números e imprimi-los em ordem crescente.
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

if n1>n2:
    print(n2, n1)
elif n2>n1:
    print(n1, n2)
elif n1==n2:
    print("são identicos")
