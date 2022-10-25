# Create
def adicionar_coisa(armazenamento, chave, dados):
  if chave not in armazenamento:
    armazenamento[chave] = dados

    return True
  return False

# Read
def buscar_coisa(armazenamento, chave):
  if chave in armazenamento:
    return armazenamento[chave]
  return None

# Update
def alterar_coisa(armazenamento, chave, posicao, dados):
  if chave not in armazenamento:
    return False
  
  temp = armazenamento[chave][::-1][::-1]
  temp[posicao] = dados

  armazenamento[chave] = temp
  return True

# Delete
def deletar_coisa(armazenamento, chave):
  if chave not in armazenamento:
    return False

  del armazenamento[chave]
  return True