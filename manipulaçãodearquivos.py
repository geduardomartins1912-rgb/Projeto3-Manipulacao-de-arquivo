# Atividade 1
with open("frutas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Maçã\n")
    arquivo.write("Banana\n")
    arquivo.write("Laranja\n")

print("Arquivo 'frutas.txt' criado com sucesso!")
# Atividade 2
with open("frutas.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo 'frutas.txt':")
    print(conteudo)
# Atividade 3
with open("frutas.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Uva\n")
    arquivo.write("Abacaxi\n")

print("Novas frutas sucesso!")
# Atividade 4
try:
    with open("arquivo_inexistente.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado. Criando um novo arquivo...")
    with open("arquivo_inexistente.txt", "w", encoding="utf-8") as novo_arquivo:
        novo_arquivo.write("Arquivo criado automaticamente.\n")
    print("certo certo!")
# Atividade 5
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")

    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}, Email: {email}\n")

    print("Usuário cadastrado com sucesso!")













