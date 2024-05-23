# Atividade 7
fval = int(input("Insira o primeiro valor:"))
sval = int(input("Qual será o segundo valor?"))
ope = (input("Qual será a operação? Digite seu sinal (+, -, / ou *)"))
if ope == "+":
  res = fval+sval
elif ope == "-":
  res = fval-sval
elif ope == "/":
  res = fval/sval
elif ope == "*":
  res = fval*sval
else:
  ope = -4
print("A operação não foi compreendida" if ope == -4 else f"O resultado é {res}")