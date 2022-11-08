import utilidades

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
      
    elif (entrada == '3'):
      pass
    elif (entrada == '4'):
      pass
    elif (entrada == '5'):
      pass
    elif (entrada == '6'):
      rod_professores_disciplinas = False
    else:
      utilidades.imprime_caixa(['ATENÇÃO!', 'Essa opção não existe.'])