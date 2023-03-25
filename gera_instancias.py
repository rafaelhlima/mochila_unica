import random as rnd
import os

# Os métodos neste arquivo são usados para gerar instâncias aleatórias para o problema
# da mochila única, usando apenas valores inteiros.

# Peso mínimo e máximo usado na geração da instância
PESO_MIN, PESO_MAX = 20, 60
# Unidade multiplicadora de valor/peso para definir o valor do item
VALOR_PESO_MIN, VALOR_PESO_MAX = 10, 20
# Capacidade da mochila
CAPACIDADE_MIN, CAPACIDADE_MAX = 300, 600


# Gera uma instância do problema da mochila com a quantidade de itens informada
# Os itens são identificados com códigos iniciando em zero
# Se um nome de arquivo for especificado, os dados gerados são salvos em formato CSV
# Os dados gerados são retornados em uma lista de tuplas
def gera_instancia(qtd_itens, arq_instancia=None):
    # Armazena todos os dados da instância gerada
    dados_inst = list()
    # Gera a capacidade da mochila
    capac_mochila = rnd.randint(CAPACIDADE_MIN, CAPACIDADE_MAX)
    # Gera o peso e o valor de todos os itens da instância
    for i in range(qtd_itens):
        peso_item = rnd.randint(PESO_MIN, PESO_MAX)
        valor_peso_item = rnd.uniform(VALOR_PESO_MIN, VALOR_PESO_MAX)
        valor_item = int(peso_item * valor_peso_item)
        dados_item = (i, peso_item, valor_item)
        dados_inst.append(dados_item)
    # Salva os dados no arquivo de instância
    if arq_instancia is not None:
        with open(arq_instancia, "w+", encoding="utf8") as f:
            f.write(f"QTD_ITENS;{qtd_itens}\n")
            f.write(f"CAPACIDADE;{capac_mochila}\n")
            f.write("ITEM;PESO;VALOR\n")
            for item in dados_inst:
                f.write(f"{item[0]};{item[1]};{item[2]}\n")
    # Retorna os dados gerados
    return dados_inst, capac_mochila


# Gera várias instâncias usando as configurações de tamanho e quantidade de repetição por configuração
def gera_varias_instancias(pasta_instancias, configuracoes, qtd_por_config):
    prefixo_instancia = "inst_{:02d}_n{}.csv"
    cont_inst = 1
    for qtd_itens in configuracoes:
        for _ in range(qtd_por_config):
            arq_instancia = prefixo_instancia.format(cont_inst, qtd_itens)
            arq_instancia = os.path.join(pasta_instancias, arq_instancia)
            dados_gerados, capac_gerada = gera_instancia(qtd_itens, arq_instancia)
            # Verifica se o peso de todos os itens é superior ao tamanho da mochila
            # Caso contrário, imprime um aviso de que a instância é trivial
            peso_total = 0
            for item in dados_gerados:
                peso_total += item[1]
            if peso_total <= capac_gerada:
                print(f"AVISO: Instância {arq_instancia} tem peso total dos itens inferior à capacidade da mochila")
            else:
                print(f"OK: Instancia {arq_instancia} (Peso total = {peso_total}; Capacidade = {capac_gerada})")
            cont_inst += 1


def main():
    # Chama a geração de 20 instâncias (4 repetições por tamanho)
    tamanhos = [30, 50, 100, 150, 200]
    repeticoes = 4
    gera_varias_instancias("Instancias", tamanhos, repeticoes)


if __name__ == "__main__":
    main()
