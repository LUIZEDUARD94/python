def converta(hora, minuto):
    if 0 < hora <= 12 and 0 < minuto < 60:
        print(f"{hora}:{minuto} AM")
    elif 12 < hora < 24 and 0 < minuto < 60:
        print(f"{hora - 12}:{minuto} PM")
    else:
        print("Valor inválido")


while True:
    hora = int(input("Hora: "))
    if hora == 999:
        break
    minuto = int(input("Minuto: "))
    converta(hora,minuto)
    print("="*20)