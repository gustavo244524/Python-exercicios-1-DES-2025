#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.
Dia_02 = int(ia_01 = int(input("Dias para atividade 01"))
Dinput("Dias para atividade 02" ))
Dia_03 = int(input("Dias para atividade 03"))

if Dia_01 < 0 or Dia_02 < 0 or Dia_03 < 0:
    print("erro numero negativo")

else:
    soma = Dia_01 + Dia_02 + Dia_03
    primt(f"tempo total do projeto:{soma} dias ")