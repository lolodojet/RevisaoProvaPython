# Exercicio 1
numeros = [1, 2, 3]
numeros.append([4, 5])
print(numeros)
# Resposta: Vai printar 1, 2, 3 e [4, 5]

# Exercicio 2
#   print(numeros[4])  #DEIXEI COMENTADO PQ TAVA DANDO ERRO NO RESTO DO CÓDIGO
# Respostas: Vai dar erro porque o elemento/index não existe

# Exercicio 3 - Resposta: Listas são mutáveis e Tuplas são imutáveis

# Exercício 4 
tupla = (10, 20, 30)
print(tupla[1])
# Resposta: Vai printar 20

# Exercício 5
dicionario_notas = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carlos": 9.0 
}
# Resposta: print(notas["Carlos"]) Implementando o print chamando pela chave que é "Carlos"


# Exercicio 6
cidades = {
    "RS": ["Gravata", "Pelotas", "Erechim"],
    "SC": ["Joinville", "Jaraguá", "Toledo"],
    "PR": ["Curitiba", "Toledo", "Maringá"]
}
print(cidades)

# Exercicio 7
print(cidades["SC"])

# Exercicio 8
nomes = []
i = 0
while i < 5:
    nomeNovo = input("Adicione o nome de 5 pessoas: ")
    i += 1
    nomes.append(nomeNovo)
print(nomes)

tupla = tuple(nomes)
print(tupla)

# Exercicio 9
MenuNomes = []
def adicionar_nomes (lista, nome):
    lista.append(nome)

def remover_nomes (lista, nome):
    lista.remove(nome)
    
def alterar_nome (lista, novo_nome, indice):
    if 0 <= indice < len(MenuNomes):
        lista[indice] = novo_nome
    else:
        print("Indice inválido!")
         
def mostrar_nomes (lista):
    for nome in lista:
        print(nome)
        
while True:
    
    print("=== Menu ===")
    print('1 - Adicionar nomes')
    print('2 - Remover nomes')
    print('3 - Alterar nomes')
    print('4 - Mostrar nomes')
    print('5 - Sair')
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        while True:
            nome = input("Digite os nomes que deseja adicionar e diga -> sair <- para encerrar!: ")
            if nome == "sair":
                break
            elif nome.strip() == "":
                print("Você não pode colocar um numero vazio")
                   
            adicionar_nomes(MenuNomes, nome)
            print(f"O contato {nome} foi adicionado!")
            
    elif escolha == '2':
        nome = input("Diga o nome que quer remover: ")
        remover_nomes(MenuNomes, nome)
        print(f"O nome {nome} foi removido!")
        
    elif escolha == '3':
        if MenuNomes:
            for i, nome in enumerate (MenuNomes):
                print(f"{i}: {nome}")

            indice = int(input("Digite o indice do nome que quer alterar: "))
            novo_nome = input("Digite o novo nome: ")
            alterar_nome(MenuNomes, novo_nome, indice)
            print(f"o nome {novo_nome} foi adicionado!")

        else:
            print("Não tem nenhum nome na lista")
        
    elif escolha == '4':
        if not MenuNomes:
            print("Nao tem nenhum nome na lista")
        else:
            mostrar_nomes(MenuNomes)
    elif escolha == '5':
        print("Saindo...")
        break