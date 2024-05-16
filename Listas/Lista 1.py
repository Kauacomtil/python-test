def encontrar_maior(lista_numeros):
  """
  Função que recebe uma lista de números e retorna o maior valor da lista.

  Argumentos:
    lista_numeros (list): A lista de números na qual o maior valor será buscado.

  Retorno:
    float: O maior valor encontrado na lista.
  """
  if not lista_numeros:
    raise ValueError("A lista não pode ser vazia.")

  maior_valor = lista_numeros[0]
  for numero in lista_numeros:
    if numero > maior_valor:
      maior_valor = numero

  return maior_valor

def main():
  """
  Função principal que solicita ao usuário a entrada de números e chama a função encontrar_maior para encontrar o maior valor.
  """
  try:
    # Solicita ao usuário que insira a quantidade de números
    quantidade_numeros = int(input("Digite a quantidade de números que você deseja inserir: "))

    # Cria uma lista vazia
    lista_numeros = []

    # Solicita ao usuário que insira cada número da lista
    for i in range(quantidade_numeros):
      numero = float(input(f"Digite o {i+1}º número: "))
      lista_numeros.append(numero)

    # Encontra o maior valor e imprime o resultado
    maior_valor_encontrado = encontrar_maior(lista_numeros)
    print(f"O maior valor da lista é: {maior_valor_encontrado}")

  except ValueError as e:
    # Imprime a mensagem de erro se a entrada do usuário for inválida
    print(f"Erro: {e}")

if __name__ == "__main__":
  main()
