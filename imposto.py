def SomaImposto(Imposto, Custo):
    return (1 + Imposto/100)*Custo
a = float(input("Digite o imposto: "))
b = float(input("Digite o custo: "))

print("Valor com imposto:", SomaImposto(a,b))