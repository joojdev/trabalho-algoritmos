import utilidades
import lib

professores_txt = 'professores.txt'

armazenamento_professores = {}

if utilidades.existe_arquivo(professores_txt):
  with open(professores_txt, 'r') as arquivo:
    lista_linhas = arquivo.readlines()
    lista_linhas = ''.join(lista_linhas)
    lista_linhas = lista_linhas.split('\n')
    lista_linhas = [_.split(';') for _ in lista_linhas]

    for dados in lista_linhas:
      chave = dados.pop(0)
      armazenamento_professores[chave] = dados
    
    arquivo.close()

def lista_dados(registro_funcional, dados):
  return [
    f'Registro funcional: {registro_funcional}',
    f'Nome: {dados[0]}',
    f'Data de nascimento: {dados[1]}',
    f'Área de pesquisa: {dados[2]}',
    f'Titulação: {dados[3]}',
    f'E-mail: {dados[4]}'
  ]

def submenu_professores():
  rod_professores = True

  while rod_professores:
    print()

    menu = [
      'Submenu de Professores:',
      '  1. Listar todos os professores',
      '  2. Buscar professor por registro funcional',
      '  3. Incluir professor',
      '  4. Alterar dados',
      '  5. Excluir',
      '  6. Voltar'
    ]

    utilidades.imprime_caixa(menu)

    print()

    entrada = input(' > ')

    if (entrada == '1'):
      lista_professores = list(armazenamento_professores.items())

      for (registro_funcional, dados) in lista_professores:
        print()
        utilidades.imprime_caixa(lista_dados(registro_funcional, dados))
    elif (entrada == '2'):
      registro_funcional = input('  Digite o registro funcional: ')
      print()
      professor = lib.buscar_coisa(armazenamento_professores, registro_funcional)
      if not professor:
        utilidades.imprime_caixa(['ATENÇÃO!', 'Não existe nenhum professor com este registro funcional.'])
      else:
        utilidades.imprime_caixa(lista_dados(registro_funcional, professor))
    elif (entrada == '3'):
      registro_funcional = input('  Digite o registro funcional: ')
      registro_funcional = ''.join(registro_funcional.split(';'))
      print()
      nome = input('  Digite o nome do professor: ')
      nascimento = input('  Digite a data de nascimento do professor: ')
      print()
      area = input('  Digite a área de pesquisa do professor: ')
      titulacao = input('  Digite a titulação do professor: ')
      print()
      email = input('  Digite o e-mail do professor: ')

      dados = [nome, nascimento, area, titulacao, email]
      dados = [''.join(_.split(';')) for _ in dados]

      lib.adicionar_coisa(armazenamento_professores, registro_funcional, dados)
    elif (entrada == '4'):
      registro_funcional = input('  Digite o registro funcional: ')

      if registro_funcional not in armazenamento_professores:
        utilidades.imprime_caixa(['ATENÇÃO!', 'Não existe nenhum professor com este registro funcional.'])
      else:
        posicao = menu_alteracao()
        antigo_valor = armazenamento_professores[registro_funcional][posicao]
        novo_valor = input('  Digite um novo valor: ')
        print()

        utilidades.imprime_caixa(['ATENÇÃO!', '  Você tem certeza que quer mudar esta informação? (S/N)', f'   Valor antigo: {antigo_valor}', f'   Valor novo: {novo_valor}'])

        print()

        opcao = input(' > ')

        if opcao.lower() == 's':
          sucesso = lib.alterar_coisa(armazenamento_professores, registro_funcional, posicao, novo_valor)

          if sucesso:
            utilidades.imprime_caixa(['Dados alterados com sucesso!'])
          else:
            utilidades.imprime_caixa(['Houve um problema!'])
        else:
          utilidades.imprime_caixa(['Operação cancelada!'])
    elif (entrada == '5'):
      registro_funcional = input('  Digite o registro funcional: ')

      if registro_funcional not in armazenamento_professores:
        utilidades.imprime_caixa(['ATENÇÃO!', 'Não existe nenhum professor com este registro funcional.'])
      else:
        nome = armazenamento_professores[registro_funcional][0]

        print()
        utilidades.imprime_caixa(['ATENÇÃO!', f'  Você tem certeza que quer deletar o professor {nome}? (S/N)'])
        print()

        opcao = input(' > ')

        if opcao.lower() == 's':
          sucesso = lib.deletar_coisa(armazenamento_professores, registro_funcional)

          if sucesso:
            utilidades.imprime_caixa(['Professor removido com sucesso!'])
          else:
            utilidades.imprime_caixa(['Houve um problema!'])
        else:
          utilidades.imprime_caixa(['Operação cancelada!'])
    elif (entrada == '6'):
      lista_linhas = []

      for (chave, dados) in list(armazenamento_professores.items()):
        dados_formatados = ';'.join(dados)
        linha = f'{chave};{dados_formatados}'

        lista_linhas.append(linha)

      with open(professores_txt, 'w') as arquivo:
        for indice in range(len(lista_linhas)):
          arquivo.write(lista_linhas[indice])
          
          if indice != len(lista_linhas) - 1:
            arquivo.write('\n')
      
        arquivo.close()

      rod_professores = False
    else:
      utilidades.imprime_caixa(['ATENÇÃO!', 'Essa opção não existe.'])

def menu_alteracao():
  rod_alteracao = True
  opcoes_esperadas = list(range(1, 5 + 1))
  opcoes_esperadas = [str(_) for _ in opcoes_esperadas]

  resposta = None

  while rod_alteracao:
    print()

    menu = [
      'O que você deseja alterar?',
      '  1. Nome',
      '  2. Data de nascimento',
      '  3. Área de pesquisa',
      '  4. Titulação',
      '  5. E-mail'
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