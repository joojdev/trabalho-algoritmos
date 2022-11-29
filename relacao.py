import utilidades
import lib

relacao_txt = 'relacao.txt'

armazenamento_relacao = {}

if utilidades.existe_arquivo(relacao_txt):
  with open(relacao_txt, 'r') as arquivo:
    lista_linhas = arquivo.readlines()
    lista_linhas = ''.join(lista_linhas)
    lista_linhas = lista_linhas.split('\n')
    lista_linhas = [_.split(';') for _ in lista_linhas]

    for dados in lista_linhas:
      professor = dados.pop(0)
      disciplina = dados.pop(0)
      ano = dados.pop(0)
      semestre = dados.pop(0)
      curso = dados.pop()

      pacote = [professor, disciplina, ano, semestre, dados, curso]
      chave = f'{professor} {disciplina} {ano} {semestre}'
      armazenamento_relacao[chave] = pacote
    
    arquivo.close()

def lista_dados(dados):
  lista = [
    f'Professor: {dados[0]}',
    f'Disciplina: {dados[1]}',
    f'Ano: {dados[2]}',
    f'Semestre: {dados[3]}',
    'Dias com horário:'
  ]

  for dia in dados[4]:
    lista.append(f' {dia}')

  lista.append(f'Curso: {dados[5]}')
  
  return lista

def submenu_professores_disciplinas():
  rod_professores_disciplinas = True

  while rod_professores_disciplinas:
    print()

    menu = [
      'Submenu de Professores - Disciplinas:',
      '  1. Listar todos',
      '  2. Listar relação professor - disciplina',
      '  3. Incluir professor em uma disciplina',
      '  4. Alterar dados',
      '  5. Excluir',
      '  6. Voltar'
    ]

    utilidades.imprime_caixa(menu)

    print()

    entrada = input(' > ')

    if (entrada == '1'):
      utilidades.limpa_tela()
      lista_relacao = list(armazenamento_relacao.items())

      for (chave, dados) in lista_relacao:
        print()
        utilidades.imprime_caixa(lista_dados(dados))
    elif (entrada == '2'):
      utilidades.limpa_tela()
      print()

      professor = input('  Digite o registro funcional do professor: ')
      disciplina = input('  Digite a sigla da disciplina: ')
      ano = input('  Digite o ano: ')
      semestre = input('  Digite o semestre: ')

      relacao = lib.buscar_coisa(armazenamento_relacao, f'{professor} {disciplina.upper()} {ano} {semestre}')

      utilidades.limpa_tela()

      if not relacao:
        utilidades.imprime_caixa(['ATENÇÃO!', 'Não existe nenhuma relação com estas informações.'])
      else:
        utilidades.imprime_caixa(lista_dados(relacao))
    elif (entrada == '3'):
      utilidades.limpa_tela()
      print()
      professor = input('  Digite o registro funcional do professor: ')
      disciplina = input('  Digite a sigla da disciplina: ')
      ano = input('  Digite o ano: ')
      semestre = input('  Digite o semestre: ')
      print()
      curso = input('  Digite o nome do curso: ')
      print()
      lista_dias = []
      pegando_input = True
      
      while pegando_input:
        dia = input('  Digite o dia e o horário das aulas ("fim" para terminar): ')


        if dia.lower() == 'fim':
          pegando_input = False
        else:
          lista_dias.append(dia)

      disciplina = disciplina.upper()
      chave = f'{professor} {disciplina} {ano} {semestre}'
      pacote = [professor, disciplina, ano, semestre, lista_dias, curso]
      armazenamento_relacao[chave] = pacote
    elif (entrada == '4'):
      utilidades.limpa_tela()
      professor = input('  Digite o registro funcional do professor: ')
      disciplina = input('  Digite a sigla da disciplina: ')
      ano = input('  Digite o ano: ')
      semestre = input('  Digite o semestre: ')

      chave = f'{professor} {disciplina.upper()} {ano} {semestre}'

      if chave not in armazenamento_relacao:
        utilidades.limpa_tela()
        utilidades.imprime_caixa(['ATENÇÃO!', 'Não existe nenhuma relação com essas informações.'])
      else:
        posicao = menu_alteracao()
        valor_antigo = armazenamento_relacao[chave][posicao]
        if posicao == 4:
          lista_dias = []
          pegando_input = True
      
          while pegando_input:
            dia = input('  Digite o dia e o horário das aulas ("fim" para terminar): ')

            if dia.lower() == 'fim':
              pegando_input = False
            else:
              lista_dias.append(dia)
          
          utilidades.limpa_tela()
          utilidades.imprime_caixa(['ATENÇÃO!', '  Você tem certeza que quer mudar esta informação? (S/N)', f'   Valor antigo: {", ".join(valor_antigo)}', f'   Valor novo: {", ".join(lista_dias)}'])

          print()

          opcao = input(' > ')

          utilidades.limpa_tela()

          if opcao.lower() == 's':
            sucesso = lib.alterar_coisa(armazenamento_relacao, chave, posicao, lista_dias)

            if sucesso:
              utilidades.imprime_caixa(['Dados alterados com sucesso!'])
            else:
              utilidades.imprime_caixa(['Houve um problema!'])
          else:
            utilidades.imprime_caixa(['Operação cancelada!'])
        else:
          utilidades.limpa_tela()
          valor_novo = input('  Digite o valor novo: ')
          dados = armazenamento_relacao[chave][::]

          utilidades.imprime_caixa(['ATENÇÃO!', '  Você tem certeza que quer mudar esta informação? (S/N)', f'   Valor antigo: {valor_antigo}', f'   Valor novo: {valor_novo}'])

          print()

          opcao = input(' > ')

          utilidades.limpa_tela()

          if opcao.lower() == 's':
            dados[posicao] = valor_novo
            dados[1] = dados[1].upper()
            [professor, disciplina, ano, semestre] = dados

            chave_nova = f'{professor} {disciplina} {ano} {semestre}'

            armazenamento_relacao[chave_nova] = dados

            lib.deletar_coisa(armazenamento_relacao, chave)
            
            utilidades.imprime_caixa(['Dados alterados com sucesso!'])
          else:
            utilidades.imprime_caixa(['Operação cancelada!'])
    elif (entrada == '5'):
      utilidades.limpa_tela()
      professor = input('  Digite o registro funcional do professor: ')
      disciplina = input('  Digite a sigla da disciplina: ')
      ano = input('  Digite o ano: ')
      semestre = input('  Digite o semestre: ')
      
      chave = f'{professor} {disciplina.upper()} {ano} {semestre}'

      if chave not in armazenamento_relacao:
        utilidades.limpa_tela()
        utilidades.imprime_caixa(['ATENÇÃO!', 'Não existe nenhuma relação com essas informações.'])
      else:
        print()

        utilidades.imprime_caixa(['ATENÇÃO!', 'Você tem certeza que quer deletar esta relação? (S/N)'])

        print()

        opcao = input(' > ')

        utilidades.limpa_tela()

        if opcao.lower() == 's':
          sucesso = lib.deletar_coisa(armazenamento_relacao, chave)

          if sucesso:
            utilidades.imprime_caixa(['Relação removida com sucesso!'])
          else:
            utilidades.imprime_caixa(['Houve um problema!'])
        else:
          utilidades.imprime_caixa(['Operação cancelada!'])
    elif (entrada == '6'):
      lista_linhas = []

      for dados in list(armazenamento_relacao.values()):
        dados = dados[::]
        dados[4] = ';'.join(dados[4])
        dados_formatados = ';'.join(dados)
        
        lista_linhas.append(dados_formatados)

      with open(relacao_txt, 'w') as arquivo:
        for indice in range(len(lista_linhas)):
          arquivo.write(lista_linhas[indice])
          
          if indice != len(lista_linhas) - 1:
            arquivo.write('\n')

      rod_professores_disciplinas = False
      utilidades.limpa_tela()
    else:
      utilidades.imprime_caixa(['ATENÇÃO!', 'Essa opção não existe.'])

def menu_alteracao():
  rod_alteracao = True
  opcoes_esperadas = list(range(1, 6 + 1))
  opcoes_esperadas = [str(_) for _ in opcoes_esperadas]

  reposta = None

  while rod_alteracao:
    print()

    menu = [
      'O que você deseja alterar?',
      '  1. Registro funcional do professor',
      '  2. Sigla da disciplina',
      '  3. Ano',
      '  4. Semestre',
      '  5. Dias com horário',
      '  6. Nome do curso'
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