import os
from operator import itemgetter

# Este arquivo implementa 3 algoritmos para o problema da mochila
# Algoritmo 1: Insere primeiro na mochila os itens de maior valor
# Algoritmo 2: Insere primeiro na mochila os itens de menor peso
# Algoritmo 3: Insere primeiro na mochila os itens de maior valor/peso


# Lê os dados de uma única instância e retorna uma lista de listas com as informações
# dos itens e a capacidade da mochila na instância
def le_dados_instancia(arq_instancia):
    with open(arq_instancia, "r", encoding="utf8") as f:
        linhas = f.readlines()
        # Lê a quantidade de itens e a capacidade
        v_linha = linhas[0].strip().split(";")
        qtd_itens = int(v_linha[1])
        v_linha = linhas[1].strip().split(";")
        capacidade = int(v_linha[1])
        # Apaga os valores já lidos
        del linhas[:3]
        # Lê os dados de todos os itens
        dados_instancia = list()
        for i in range(qtd_itens):
            v_linha = linhas[i].strip().split(";")
            id_item = int(v_linha[0])
            peso_item = int(v_linha[1])
            valor_item = int(v_linha[2])
            dados_instancia.append([id_item, peso_item, valor_item])
    # Retorna os dados lidos
    return dados_instancia, capacidade


# Implementa o Algoritmo 1, que coloca na mochila primeiro os itens de maior valor
def algoritmo_maior_valor(dados_inst, capacidade):
    # Armazena os itens que estão na mochila
    solucao = list()
    # Cria uma cópia dos dados da instância (para não estragar o original)
    dados = [linha[:] for linha in dados_inst]
    # Ordena de forma decrescente com relação ao valor
    dados.sort(key=itemgetter(2), reverse=True)
    # Coloca os itens na mochila
    capac_usada = 0
    valor_total = 0
    for item in dados:
        id_item = item[0]
        peso_item = item[1]
        valor_item = item[2]
        # Se couber na mochila, então coloca na mochila
        if capac_usada + peso_item <= capacidade:
            solucao.append(id_item)
            capac_usada += peso_item
            valor_total += valor_item
    # Retorna a solução, o valor total e o peso total da mochila
    return solucao, valor_total, capac_usada


# Implementa o Algoritmo 2, que coloca na mochila primeiro os itens de menor peso
def algoritmo_menor_peso(dados_inst, capacidade):
    # Armazena os itens que estão na mochila
    solucao = list()
    # Cria uma cópia dos dados da instância (para não estragar o original)
    dados = [linha[:] for linha in dados_inst]
    # Ordena de forma crescente com relação ao peso
    dados.sort(key=itemgetter(1))
    # Coloca os itens na mochila
    capac_usada = 0
    valor_total = 0
    for item in dados:
        id_item = item[0]
        peso_item = item[1]
        valor_item = item[2]
        # Se couber na mochila, então coloca na mochila
        if capac_usada + peso_item <= capacidade:
            solucao.append(id_item)
            capac_usada += peso_item
            valor_total += valor_item
    # Retorna a solução, o valor total e o peso total da mochila
    return solucao, valor_total, capac_usada


# Implementa o Algoritmo 3, que coloca na mochila primeiro os itens de maior valor/peso
# Para cada item, calcula-se a relação valor/peso (quanto o item vale por unidade de peso)
def algoritmo_maior_valor_peso(dados_inst, capacidade):
    # Armazena os itens que estão na mochila
    solucao = list()
    # Cria uma cópia dos dados da instância (para não estragar o original)
    dados = [linha[:] for linha in dados_inst]
    # Cria a coluna valor/peso
    for item in dados:
        peso = item[1]
        valor = item[2]
        valor_peso = valor / peso
        item.append(valor_peso)
    # Ordena de forma decrescente com relação ao valor
    dados.sort(key=itemgetter(3), reverse=True)
    # Coloca os itens na mochila
    capac_usada = 0
    valor_total = 0
    for item in dados:
        id_item = item[0]
        peso_item = item[1]
        valor_item = item[2]
        # Se couber na mochila, então coloca na mochila
        if capac_usada + peso_item <= capacidade:
            solucao.append(id_item)
            capac_usada += peso_item
            valor_total += valor_item
    # Retorna a solução, o valor total e o peso total da mochila
    return solucao, valor_total, capac_usada


# Salva uma solução em um arquivo CSV
def salva_solucao(arq_solucao, solucao, valor, peso):
    with open(arq_solucao, "w+", encoding="utf8") as f:
        f.write(f"VALOR_TOTAL;{valor}\n")
        f.write(f"PESO_TOTAL;{peso}\n")
        f.write("ITENS")
        for item in solucao:
            f.write(f";{item}")


# Este método lê resolve uma única instância do arquivo arq_instancia
# e salva a solução encontrada no arquivo arq_solucao
def resolve_instancia(arq_instancia, arq_solucao):
    dados, capacidade = le_dados_instancia(arq_instancia)
    solucao, valor, peso = algoritmo_maior_valor(dados, capacidade)
    salva_solucao(arq_solucao, solucao, valor, peso)


# Resolve todas as instâncias em uma pasta informada (pasta_instancias)
# e salva as soluções na pasta pasta_solucoes
# IMPORTANTE: Ambas as pastas devem existir previamente
def resolve_todas_instancias(pasta_instancias, pasta_solucoes):
    # Lista de arquivos de instância
    instancias = os.listdir(pasta_instancias)
    instancias.sort()
    # Processa todas as instâncias
    for instancia in instancias:
        arq_instancia = os.path.join(pasta_instancias, instancia)
        arq_solucao = os.path.join(pasta_solucoes, instancia)
        resolve_instancia(arq_instancia, arq_solucao)


def main():
    resolve_todas_instancias("Instancias", "Solucoes")


if __name__ == "__main__":
    main()
