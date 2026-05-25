# --- Multiplas funções - Exercício controle de qualidade ---
def cabecalho():
    print("\n" + "=" *30)
    print("Sistema de qualidade")
def verificar_status(peso):
    if peso >= 50 and peso <=100:
       return "Aprovada"
    else:
       return "Reprovada"
cabecalho()
peso_item = float(input("Digite o peso do item em gramas:"))
status = verificar_status(peso_item)
print(f"Resultado da inspeção:{status}")
print("=" * 30)