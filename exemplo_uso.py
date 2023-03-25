import solver


def main():
    solver.ALGORITMO = 1
    arq_instancia = "Testes/inst_teste.csv"
    solver.resolve_instancia(arq_instancia, "arq_solucao1.csv")
    solver.ALGORITMO = 2
    solver.resolve_instancia(arq_instancia, "arq_solucao2.csv")
    solver.ALGORITMO = 3
    solver.resolve_instancia(arq_instancia, "arq_solucao3.csv")


if __name__ == "__main__":
    main()
