from faker import Faker

fake = Faker('pt_BR')

def salva_arquivo(qnt_nomes: int):
    with open("nomes.txt", "w", encoding="utf-8") as arquivo: #Cria arquivo.txt, w indica que é write (escrita) e encoding indica o formato
        for _ in range(qnt_nomes):
            nome = fake.name()
            arquivo.write(nome + "\n")

def hash_inicial(nome: str, tamanho_tabela: int):
    letra_inicial = nome[0].upper()
    codigo_ascii = ord(letra_inicial)
    return (codigo_ascii + 13) % tamanho_tabela

def le_arquivo():
    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        nomes = [linha for linha in arquivo]
    
    print(nomes[:10]) # Lê só as 10 primeiras linhas
    return nomes

# Outra versão da linha 18
'''
nomes = []
for linha in arquivo:
    nomes.append(linha)
'''

if __name__ == "__main__":
    # salva_arquivo(20000)

    tabela = {}
    for i in range(26):
        tabela[i] = []

    nomes = le_arquivo()
    for nome in nomes:
        hash_code = hash_inicial(nome, 26)
        tabela[hash_code].append(nome)
    
    for categoria in tabela:
        print(f"Categoria: {categoria} - {(len(categoria) / 100) * "*"}\n")