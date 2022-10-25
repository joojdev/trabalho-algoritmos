import utilidades
from professores import submenu_professores
from disciplinas import submenu_disciplinas

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
      pass
    elif (entrada == '2'):
      pass
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

def relatorio():
  pass

rodando = True

while rodando:
  print()

  menu = [
    'Menu de Opções:',
    '  1. Submenu de Professores',
    '  2. Submenu de Disciplinas',
    '  3. Submenu de Professores - Disciplinas',
    '  4. Relatório',
    '  5. Sair'
  ]

  utilidades.imprime_caixa(menu)

  print()

  entrada = input(' > ')

  if (entrada == '1'):
    submenu_professores()
  elif (entrada == '2'):
    submenu_disciplinas()
  elif (entrada == '3'):
    submenu_professores_disciplinas()
  elif (entrada == '4'):
    relatorio()
  elif (entrada == '5'):
    rodando = False
  else:
    utilidades.imprime_caixa(['ATENÇÃO!', 'Essa opção não existe.'])