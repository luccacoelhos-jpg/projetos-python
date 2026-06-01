# --- Aluno 1: Formato do nome do filme. ---
def formatar(nome):
    return nome.upper()
# --- Aluno 2: Verificação de acesso. ---
def verificador(idade):
    if idade >=18:
      return "autorizado"
    else:
      return "Não autorizado"
# --- Aluno 3: Mensagem de retorno. ---
def gerar_mensagem(status):
   if status == "autorizada":
      return "Tenha uma ótima sessão."
   else:
      return "Sinto muito, idade não autorizada."
   # --- Aluno 4: Integrador do projeto. ---
   nome_filme = input("Digite o nome do filme:")
   idade_filme = int(input("Digite sua idade:"))
   filme = formatar(nome_filme)
   status_final = verificação(idade_filme)
   mensagem = gerar_mensagem(status_final)
   print(f"\n filme:{filme}")
   print(f"Status:{status_final}")
   print(f"Aviso:{mensagem}")