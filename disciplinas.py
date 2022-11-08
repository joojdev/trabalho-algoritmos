from ctypes import util
import utilidades
import lib

disciplinas_txt = 'disciplinas.txt'

armazenamento_disciplinas = {}

if utilidades.existe_arquivo(disciplinas_txt):
  with open(disciplinas_txt, 'r') as arquivo:
    lista_linhas = arquivo.readlines()
    lista_linhas = ''.join(lista_linhas)
    lista_linhas = lista_linhas.split('\n')
    lista_linhas = [_.split(';') for _ in lista_linhas]

    for dados in lista_linhas:
      chave = dados.pop(0)
      armazenamento_disciplinas[chave] = dados

    arquivo.close()

def lista_dados(sigla, dados):
  return [
    f'Sigla: {sigla}',
    f'Nome: {dados[0]}',
    f'Ementa: {dados[1]}',
    f'Número de créditos: {dados[2]}',
    f'Carga horária: {dados[3]}'
  ]

def submenu_disciplinas():
  rod_disciplinas = True

  while rod_disciplinas:
    print()

    menu = [
      'Submenu de Disciplinas:',
      '  1. Listar todos as disciplinas',
      '  2. Buscar disciplina por sigla',
      '  3. Incluir disciplina',
      '  4. Alterar dados',
      '  5. Excluir',
      '  6. Voltar'
    ]

    utilidades.imprime_caixa(menu)

    print()

    entrada = input(' > ')

    if (entrada == '1'):
      utilidades.limpa_tela()
      lista_disciplinas = list(armazenamento_disciplinas.items())

      for (sigla, dados) in lista_disciplinas:
        print()
        utilidades.imprime_caixa(lista_dados(sigla, dados))
    elif (entrada == '2'):
      utilidades.limpa_tela()
      sigla = input('  Digite a sigla da disciplina: ')
      print()
      disciplina = lib.buscar_coisa(armazenamento_disciplinas, sigla)

      utilidades.limpa_tela()
      if not disciplina:
        utilidades.imprime_caixa(['ATENÇÃO!', 'Não existe nenhuma disciplina com esta sigla.'])
      else:
        utilidades.imprime_caixa(lista_dados(sigla, disciplina))
    elif (entrada == '3'):
      utilidades.limpa_tela()
      sigla = input('  Digite a sigla da disciplina: ')
      sigla = ''.join(sigla.split(';'))
      print()
      nome = input('  Digite o nome da disciplina: ')
      ementa = input('  Digite a ementa da disciplina: ')
      print()
      creditos = input('  Digite o número de créditos: ')
      carga = input('  Digite a carga horária da disciplina: ')

      dados = [nome, ementa, creditos, carga]
      dados = [''.join(_.split(';')) for _ in dados]

      sucesso = lib.adicionar_coisa(armazenamento_disciplinas, sigla, dados)

      utilidades.limpa_tela()
      if sucesso:
        utilidades.imprime_caixa(['ATENÇÃO!', 'Disciplina adicionada com sucesso.'])
      else:
        utilidades.imprime_caixa(['ATENÇÃO!', 'Já existe uma disciplina com esta sigla.'])
    elif (entrada == '4'):
      utilidades.limpa_tela()
      sigla = input('  Digite a sigla da disciplina: ')

      if sigla not in armazenamento_disciplinas:
        utilidades.limpa_tela()
        utilidades.imprime_caixa(['ATENÇÃO!', 'Não existe nenhuma disciplina com esta sigla.'])
      else:
        posicao = menu_alteracao()
        antigo_valor = armazenamento_disciplinas[sigla][posicao]
        novo_valor = input('  Digite um novo valor: ')
        print()

        utilidades.imprime_caixa(['ATENÇÃO!', '  Você tem certeza que quer mudar esta informação? (S/N)', f'   Valor antigo: {antigo_valor}', f'   Valor novo: {novo_valor}'])

        print()

        opcao = input(' > ')

        utilidades.limpa_tela()

        if opcao.lower() == 's':
          sucesso = lib.alterar_coisa(armazenamento_disciplinas, sigla, posicao, novo_valor)

          if sucesso:
            utilidades.imprime_caixa(['Dados alterados com sucesso!'])
          else:
            utilidades.imprime_caixa(['Houve um problema!'])
        else:
          utilidades.imprime_caixa(['Operação cancelada!'])
    elif (entrada == '5'):
      utilidades.limpa_tela()
      sigla = input('  Digite a sigla da disciplina: ')

      if sigla not in armazenamento_disciplinas:
        utilidades.limpa_tela()
        utilidades.imprime_caixa(['ATENÇÃO!', 'Não existe nenhuma disciplina com esta sigla.'])
      else:
        nome = armazenamento_disciplinas[sigla][0]

        print()
        utilidades.imprime_caixa(['ATENÇÃO!', f'  Você tem certeza que quer deletar a disciplina de {nome}? (S/N)'])
        print()

        opcao = input(' > ')

        utilidades.limpa_tela()

        if opcao.lower() == 's':
          sucesso = lib.deletar_coisa(armazenamento_disciplinas, sigla)

          if sucesso:
            utilidades.imprime_caixa(['Disciplina removida com sucesso!'])
          else:
            utilidades.imprime_caixa(['Houve um problema!'])
        else:
          utilidades.imprime_caixa(['Operação cancelada!'])
    elif (entrada == '6'):
      lista_linhas = []

      for (chave, dados) in list(armazenamento_disciplinas.items()):
        dados_formatados = ';'.join(dados)
        linha = f'{chave};{dados_formatados}'

        lista_linhas.append(linha)

      with open(disciplinas_txt, 'w') as arquivo:
        for indice in range(len(lista_linhas)):
          arquivo.write(lista_linhas[indice])

          if indice != len(lista_linhas) - 1:
            arquivo.write('\n')

      arquivo.close()

      rod_disciplinas = False
      utilidades.limpa_tela()
    else:
      utilidades.limpa_tela()
      utilidades.imprime_caixa(['ATENÇÃO!', 'Essa opção não existe.'])

def menu_alteracao():
  rod_alteracao = True
  opcoes_esperadas = list(range(1, 4 + 1))
  opcoes_esperadas = [str(_) for _ in opcoes_esperadas]

  resposta = None

  while rod_alteracao:
    print()

    menu = [
      'O que você deseja alterar?',
      '  1. Nome',
      '  2. Ementa',
      '  3. Número de créditos',
      '  4. Carga horária'
    ]

    utilidades.imprime_caixa(menu)

    print()

    entrada = input(' > ')

    if entrada in opcoes_esperadas:
      resposta = int(entrada) - 1
      rod_alteracao = False
    else:
      utilidades.imprime_caixa(['ATENÇÃO!', 'Essa opção não existe.'])

  return resposta