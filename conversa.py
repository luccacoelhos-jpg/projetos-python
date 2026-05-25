# --- Ferramenta de conversão dólar x real ---
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("Conversor dolar x real")
preco = float(input("Digite o preço do produto em dolar"))
resultado = converter(preco)
print(f"O valor em reais é:{resultado:.2f}")