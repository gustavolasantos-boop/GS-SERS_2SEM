"""Cálculos transparentes de consumo, eficiência e geração fotovoltaica.

O módulo usa somente a biblioteca padrão do Python e lê premissas de JSON.
Os valores financeiros são estimativas educacionais, não aconselhamento financeiro.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "data" / "parametros.json"


def load_config(path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    """Carrega parâmetros do projeto; falha com mensagem clara se o JSON for inválido."""
    config_path = Path(path)
    try:
        with config_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Arquivo de parâmetros não encontrado: {config_path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"JSON de parâmetros inválido: {config_path}: {exc}") from exc

    required_sections = {"consumo", "tarifa", "iluminacao_led", "solar_fotovoltaica", "emissoes"}
    missing = required_sections.difference(data)
    if missing:
        raise ValueError(f"Seções obrigatórias ausentes no arquivo de parâmetros: {', '.join(sorted(missing))}")
    return data


def tarifa_por_kwh(config: dict[str, Any]) -> float:
    """Retorna TUSD + TE em R$/kWh usando os valores publicados em R$/MWh."""
    tarifa = config["tarifa"]
    return (float(tarifa["tusd_r_mwh"]) + float(tarifa["te_r_mwh"])) / 1000.0


def custo_energia(kwh: float, tarifa_r_kwh: float) -> float:
    """Custo aproximado da parcela de energia, sem itens adicionais da fatura."""
    if kwh < 0:
        raise ValueError("O consumo em kWh não pode ser negativo.")
    if tarifa_r_kwh < 0:
        raise ValueError("A tarifa por kWh não pode ser negativa.")
    return kwh * tarifa_r_kwh


def calcular_led(config: dict[str, Any]) -> dict[str, float]:
    """Estima energia economizada ao substituir lâmpadas antigas por LEDs."""
    led = config["iluminacao_led"]
    qtd = int(led["quantidade_lampadas"])
    potencia_antiga = float(led["potencia_antiga_w"])
    potencia_led = float(led["potencia_led_w"])
    horas = float(led["horas_uso_por_dia"])
    dias = float(led["dias_mes"])
    preco_led = float(led["preco_unitario_led_estimado_brl"])

    if qtd < 0 or min(potencia_antiga, potencia_led, horas, dias, preco_led) < 0:
        raise ValueError("Os parâmetros das lâmpadas não podem ser negativos.")
    if horas > 24 or dias > 31:
        raise ValueError("Horas por dia devem ser até 24 e dias do mês até 31.")

    economia_kwh_mes = max(0.0, (potencia_antiga - potencia_led) * qtd * horas * dias / 1000.0)
    return {
        "economia_kwh_mes": economia_kwh_mes,
        "economia_kwh_ano": economia_kwh_mes * 12.0,
        "investimento_brl": qtd * preco_led,
    }


def calcular_solar(config: dict[str, Any]) -> dict[str, float]:
    """Estima geração e investimento fotovoltaico com premissas configuráveis."""
    solar = config["solar_fotovoltaica"]
    potencia_kwp = float(solar["potencia_sistema_kwp"])
    geracao_kwh_kwp_mes = float(solar["geracao_mensal_por_kwp_kwh"])
    custo_estimado = float(solar["custo_estimado_1kwp_brl"]) * potencia_kwp
    if potencia_kwp < 0 or geracao_kwh_kwp_mes < 0 or custo_estimado < 0:
        raise ValueError("Os parâmetros fotovoltaicos não podem ser negativos.")
    geracao_mes = potencia_kwp * geracao_kwh_kwp_mes
    return {
        "geracao_kwh_mes": geracao_mes,
        "geracao_kwh_ano": geracao_mes * 12.0,
        "investimento_brl": custo_estimado,
    }


def estimar_emissoes_evitas(kwh_mes: float, config: dict[str, Any]) -> dict[str, float]:
    """Estima emissões médias evitadas em kg CO2eq a partir da energia substituída."""
    if kwh_mes < 0:
        raise ValueError("A energia mensal não pode ser negativa.")
    fator_kg_kwh = float(config["emissoes"]["fator_kg_co2eq_mwh"]) / 1000.0
    kg_mes = kwh_mes * fator_kg_kwh
    return {"kg_co2eq_mes": kg_mes, "kg_co2eq_ano": kg_mes * 12.0}


def comparar_alternativas(config: dict[str, Any]) -> dict[str, Any]:
    """Compara LED e solar para a mesma residência e o mesmo período de referência."""
    consumo_base = float(config["consumo"]["cenario_residencia_kwh_mes"])
    tarifa = tarifa_por_kwh(config)
    base = {
        "consumo_base_kwh_mes": consumo_base,
        "tarifa_estimativa_r_kwh": tarifa,
        "parcela_energia_base_brl_mes": custo_energia(consumo_base, tarifa),
    }

    led = calcular_led(config)
    led["custo_bruto_equivalente_brl_mes"] = led["economia_kwh_mes"] * tarifa
    led["consumo_restante_kwh_mes"] = max(0.0, consumo_base - led["economia_kwh_mes"])
    led["emissoes_evitas"] = estimar_emissoes_evitas(led["economia_kwh_mes"], config)
    led["retorno_simples_teorico_meses"] = (
        led["investimento_brl"] / led["custo_bruto_equivalente_brl_mes"]
        if led["custo_bruto_equivalente_brl_mes"] > 0 else None
    )

    solar = calcular_solar(config)
    solar["custo_bruto_equivalente_brl_mes"] = solar["geracao_kwh_mes"] * tarifa
    solar["consumo_restante_kwh_mes_modelo"] = max(0.0, consumo_base - solar["geracao_kwh_mes"])
    solar["emissoes_evitas"] = estimar_emissoes_evitas(solar["geracao_kwh_mes"], config)
    solar["retorno_simples_teorico_meses"] = (
        solar["investimento_brl"] / solar["custo_bruto_equivalente_brl_mes"]
        if solar["custo_bruto_equivalente_brl_mes"] > 0 else None
    )

    return {"base": base, "led": led, "solar": solar}


def formatar_brl(valor: float | None) -> str:
    """Formata número como moeda brasileira sem depender de locale do sistema."""
    if valor is None:
        return "não calculável"
    formatado = f"{valor:,.2f}"
    formatado = formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {formatado}"
