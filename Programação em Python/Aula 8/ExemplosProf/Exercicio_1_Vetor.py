atividades = ["Programar em python", "criar banco de dados", "almoçar", "continuar a programar"]
print("Agenda Caio")
hora= 9
for info in atividades:
    print(f"No horário de {hora}horas, caio realizará a seguinte atividade:")
    hora=hora+1
    print(info)
