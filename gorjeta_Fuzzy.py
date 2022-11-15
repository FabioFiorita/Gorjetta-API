import numpy as np
import skfuzzy as fuzzy
import skfuzzy.control as control
import matplotlib.pyplot as plt

def gorjeta(serv, qual):
    universo = np.arange(0, 11)

    qualidade = control.Antecedent(universe=universo, label="qualidade")
    servico = control.Antecedent(universe=universo, label="servico")

    # Criando função de pertinência triangular -> trimf, trapezoidal -> trapmf
    qualidade["ruim"] = fuzzy.trapmf(qualidade.universe, [0, 0, 2, 5])
    qualidade["bom"] = fuzzy.trimf(qualidade.universe, [3, 5, 7])
    qualidade["excelente"] = fuzzy.trapmf(qualidade.universe, [5, 8, 10, 10])

    servico["ruim"] = fuzzy.trapmf(servico.universe, [0, 0, 2, 5])
    servico["bom"] = fuzzy.trimf(servico.universe, [3, 5, 7])
    servico["excelente"] = fuzzy.trapmf(servico.universe, [5, 8, 10, 10])
    # qualidade.view()
    # servico.view()

    universo_gorjeta = np.arange(0, 21)

    gorjeta = control.Consequent(universe=universo_gorjeta, label="gorjeta")

    gorjeta["pequena"] = fuzzy.trapmf(gorjeta.universe, [0, 0, 5, 8])
    gorjeta["razoável"] = fuzzy.trimf(gorjeta.universe, [5, 10, 15])
    gorjeta["generosa"] = fuzzy.trapmf(gorjeta.universe, [10, 15, 20, 20])

    regra1 = control.Rule(servico["ruim"] | qualidade["ruim"], gorjeta["pequena"])
    regra2 = control.Rule(servico["bom"], gorjeta["razoável"])
    regra3 = control.Rule(servico["excelente"] | qualidade["excelente"], gorjeta["generosa"])

    # Adicionando regras ao controle
    gorjeta_controle = control.ControlSystem([regra1, regra2, regra3])

    # Criando sistema com o controle de gorjeta
    sistema = control.ControlSystemSimulation(gorjeta_controle)

    sistema.input["qualidade"] = qual  # 1
    sistema.input["servico"] = serv  # 2

    # Executando o sistema
    sistema.compute()

    # print(sistema.output['gorjeta'])

    # gorjeta.view(sim=sistema)

    return (sistema.output['gorjeta'])