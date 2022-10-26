with open('dados.txt', 'r') as arquivo:
  linha_grande = ''.join(arquivo.readlines())
  lista_grande = linha_grande.split('\n')
  lista_grande = [_.split(';') for _ in lista_grande]
  # print(lista_grande)

  armazenamento = {}

  for dados in lista_grande:
    chave = dados.pop(0)
    armazenamento[chave] = dados

  print(armazenamento)
  print()
  print("\n".join("{}\t{}".format(k, v) for k, v in armazenamento.items()))

  arquivo.close()