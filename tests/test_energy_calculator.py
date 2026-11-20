"""Testes automatizados com unittest (sem dependências de terceiros)."""
import unittest

from src.assistant import responder
from src.energy_calculator import (
    calcular_led,
    calcular_solar,
    comparar_alternativas,
    custo_energia,
    estimar_emissoes_evitas,
    load_config,
    tarifa_por_kwh,
)


class EnergyCalculatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_config()

    def test_tarifa_convertida_de_mwh_para_kwh(self):
        self.assertAlmostEqual(tarifa_por_kwh(self.config), 0.78938, places=5)

    def test_economia_led_no_cenario_base(self):
        resultado = calcular_led(self.config)
        self.assertAlmostEqual(resultado["economia_kwh_mes"], 61.2, places=2)
        self.assertAlmostEqual(resultado["economia_kwh_ano"], 734.4, places=2)
        self.assertAlmostEqual(resultado["investimento_brl"], 80.0, places=2)

    def test_geracao_solar_no_cenario_base(self):
        resultado = calcular_solar(self.config)
        self.assertAlmostEqual(resultado["geracao_kwh_mes"], 100.0, places=2)
        self.assertAlmostEqual(resultado["investimento_brl"], 2910.0, places=2)

    def test_custo_energia(self):
        self.assertAlmostEqual(custo_energia(180, 0.78938), 142.0884, places=4)

    def test_emissoes_e_positiva_e_anualizada(self):
        resultado = estimar_emissoes_evitas(100, self.config)
        self.assertAlmostEqual(resultado["kg_co2eq_mes"], 6.48, places=2)
        self.assertAlmostEqual(resultado["kg_co2eq_ano"], 77.76, places=2)

    def test_consumo_negativo_gera_erro(self):
        with self.assertRaises(ValueError):
            custo_energia(-1, 0.8)

    def test_comparacao_contem_as_duas_alternativas(self):
        resultado = comparar_alternativas(self.config)
        self.assertIn("led", resultado)
        self.assertIn("solar", resultado)
        self.assertGreater(resultado["solar"]["geracao_kwh_mes"], 0)

    def test_assistente_responde_sobre_led(self):
        resposta = responder("Como posso economizar com lâmpadas LED?", self.config)
        self.assertIn("61.2 kWh/mês", resposta)

    def test_assistente_explica_limites(self):
        resposta = responder("Essa economia é garantida?", self.config)
        self.assertIn("estimativas", resposta.casefold())


if __name__ == "__main__":
    unittest.main(verbosity=2)
