import utilidades
import relacao
import professores
import disciplinas

def submenu_relatorio():
  print()
  ano = input('  Digite o ano: ')
  semestre = input('  Digite o semestre: ')
  
  lista_relacoes = []

  for rel in list(relacao.armazenamento_relacao.values()):
    if rel[2] == ano and rel[3] == semestre:
      lista_relacoes.append(rel)

  if len(lista_relacoes) == 0:
    utilidades.imprime_caixa(['Não existe aulas neste ano e semestre.'])
  else:
    for rel in lista_relacoes:
      caixa = [
        f'Registro Funcional: {rel[0]}',
        f'Nome do Professor: {professores.armazenamento_professores[rel[0]][0]}',
        f'Sigla da Disciplina: {rel[1]}',
        f'Nome da Disciplina: {disciplinas.armazenamento_disciplinas[rel[1]][0]}',
        f'Ano: {rel[2]}',
        f'Semestre: {rel[3]}',
        'Dias com horário:'
      ]

      for dia in rel[4]:
        caixa.append(f' {dia}')

      caixa.append(f'Curso: {rel[5]}')

      utilidades.imprime_caixa(caixa)