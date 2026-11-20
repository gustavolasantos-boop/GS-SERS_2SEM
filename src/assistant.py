"""Assistente de orientações de energia, baseado em regras e sem serviços externos."""
from __future__ import annotations

from typing import Any

from .energy_calculator import comparar_alternativas, formatar_brl, tarifa_por_kwh


def resumo_comparacao(config: dict[str, Any]) -> str:
    resultado = comparar_alternativas(config)
    base, led, solar = resultado["base"], resultado["led"], resultado["solar"]
    return (
        "COMPARAÇÃO PARA A RESIDÊNCIA DE REFERÊNCIA\n"
        f"Consumo considerado: {base['consumo_base_kwh_mes']:.1f} kWh/mês.\n"
        f"Tarifa de referência (TUSD + TE): R$ {base['tarifa_estimativa_r_kwh']:.5f}/kWh.\n"
        f"Parcela estimada de energia antes das medidas: {formatar_brl(base['parcela_energia_base_brl_mes'])}/mês.\n\n"
        "1) EFICIÊNCIA — substituição de lâmpadas\n"
        f"Economia estimada: {led['economia_kwh_mes']:.1f} kWh/mês; "
        f"{led['economia_kwh_ano']:.1f} kWh/ano.\n"
        f"Investimento de referência: {formatar_brl(led['investimento_brl'])}.\n"
        f"Valor bruto equivalente da energia: {formatar_brl(led['custo_bruto_equivalente_brl_mes'])}/mês.\n"
        f"Emissões médias evitadas estimadas: {led['emissoes_evitas']['kg_co2eq_ano']:.1f} kg CO2eq/ano.\n\n"
        "2) FONTE RENOVÁVEL — sistema fotovoltaico\n"
        f"Geração estimada: {solar['geracao_kwh_mes']:.1f} kWh/mês; "
        f"{solar['geracao_kwh_ano']:.1f} kWh/ano.\n"
        f"Investimento de referência: {formatar_brl(solar['investimento_brl'])}.\n"
        f"Valor bruto equivalente da energia: {formatar_brl(solar['custo_bruto_equivalente_brl_mes'])}/mês.\n"
        f"Emissões médias evitadas estimadas: {solar['emissoes_evitas']['kg_co2eq_ano']:.1f} kg CO2eq/ano.\n\n"
        "IMPORTANTE: valores brutos teóricos, não promessa de economia nem previsão de fatura. "
        "O cálculo não inclui impostos, bandeiras, iluminação pública, cobrança mínima, regras de compensação, "
        "manutenção, financiamento nem diferenças entre autoconsumo e energia injetada. "
        "As premissas estão em data/parametros.json e podem ser alteradas."
    )


def responder(pergunta: str, config: dict[str, Any]) -> str:
    """Responde às perguntas frequentes com orientações simples e referenciadas."""
    texto = pergunta.casefold().strip()
    if not texto:
        return "Digite uma pergunta para receber uma orientação."

    if any(p in texto for p in ("compar", "solar", "fotovolta", "placa", "painel")):
        return resumo_comparacao(config)
    if any(p in texto for p in ("tarifa", "preço", "preco", "conta", "fatura", "quanto custa")):
        tarifa = tarifa_por_kwh(config)
        origem = config["tarifa"]["origem"]
        return (
            f"A tarifa usada no cenário é de R$ {tarifa:.5f}/kWh, calculada pela soma de TUSD e TE "
            "da classe B1 residencial convencional da Enel São Paulo. Esse valor não é o total da conta: "
            "impostos, bandeira, iluminação pública e custo de disponibilidade não estão incluídos.\n"
            f"Origem: {origem} Consulte a seção Referências no README para o link oficial."
        )
    if any(p in texto for p in ("led", "lâmpada", "lampada", "iluminação", "iluminacao", "economizar")):
        return (
            "A troca de lâmpadas só economiza a diferença entre as potências quando a lâmpada está acesa. "
            "No cenário didático, 10 lâmpadas de 60 W por 4 horas/dia são trocadas por LEDs de 9 W: "
            f"a economia estimada é de {comparar_alternativas(config)['led']['economia_kwh_mes']:.1f} kWh/mês. "
            "Se a residência já usa LED, esse resultado não se aplica. Apague luzes em ambientes vazios e escolha "
            "LEDs com fluxo luminoso adequado; descarte lâmpadas corretamente."
        )
    if any(p in texto for p in ("consumo", "kwh", "quilowatt")):
        c = config["consumo"]
        return (
            f"A referência nacional informada no conjunto de dados é {c['media_residencial_brasil_kwh_mes']:.0f} kWh/mês. "
            f"O cenário desta demonstração usa {c['cenario_residencia_kwh_mes']:.0f} kWh/mês; é uma hipótese arredondada, "
            "não o consumo real de uma pessoa. Compare sempre com o histórico da sua própria fatura.\n"
            f"Fonte e período: {c['origem']}"
        )
    if any(p in texto for p in ("emiss", "carbono", "co2", "ambiente", "sustent")):
        e = config["emissoes"]
        return (
            f"O modelo usa um fator médio de {e['fator_kg_co2eq_mwh']:.1f} kg CO2eq/MWh para estimar emissões associadas "
            "à eletricidade da rede substituída. Isso é uma aproximação da média do sistema elétrico, não uma análise "
            "do ciclo de vida nem uma redução garantida.\n"
            f"Fonte: {e['origem']}"
        )
    if any(p in texto for p in ("limita", "garant", "preciso", "confi", "real", "telhado", "sombra")):
        return (
            "Os resultados são estimativas educacionais. Para um orçamento real, confira o histórico de consumo, "
            "a tarifa vigente da distribuidora, impostos e encargos. Para fotovoltaica, verifique telhado, sombras, "
            "orientação, estrutura, perdas, orçamento instalado e regras de compensação aplicáveis. Use PVGIS ou o Atlas "
            "Brasileiro de Energia Solar do INPE para estudar o potencial local e solicite avaliação de profissional habilitado."
        )
    return (
        "Posso ajudar com: consumo médio, lâmpadas LED, tarifa da energia, comparação entre eficiência e solar, "
        "emissões estimadas e limitações dos cálculos. Faça uma pergunta usando um desses temas."
    )
