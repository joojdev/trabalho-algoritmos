import os

def existe_arquivo(nome):
  return os.path.exists(nome)

def imprime_caixa(lista_mensagens):
  lista_len = [len(_) for _ in lista_mensagens]
  maior_len = max(lista_len)
  
  horizontais = '  +' + '-' * (maior_len + 2) + '+'

  print(horizontais)

  for mensagem in lista_mensagens:
    print('  | ' + mensagem + ' ' * (maior_len - len(mensagem)) + ' |')

  print(horizontais)

def limpa_tela():
  os.system('cls' if os.name == 'nt' else 'clear')