import utilidades
from professores import submenu_professores
from disciplinas import submenu_disciplinas
from relacao import submenu_professores_disciplinas

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
    utilidades.limpa_tela()
    submenu_professores()
  elif (entrada == '2'):
    utilidades.limpa_tela()
    submenu_disciplinas()
  elif (entrada == '3'):
    utilidades.limpa_tela()
    submenu_professores_disciplinas()
  elif (entrada == '4'):
    utilidades.limpa_tela()
    relatorio()
  elif (entrada == '5'):
    rodando = False
  else:
    utilidades.limpa_tela()
    utilidades.imprime_caixa(['ATENÇÃO!', 'Essa opção não existe.'])