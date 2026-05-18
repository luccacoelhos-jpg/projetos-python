numero = int(input("Tabuada de qual número?"))

print(f"--- Tabuada de {numero} ---")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")