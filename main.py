"""Ponto de entrada do Citizen Assist AI — módulo Energia Cidadã."""
from __future__ import annotations

from src.assistant import responder, resumo_comparacao
from src.energy_calculator import comparar_alternativas, formatar_brl, load_config, tarifa_por_kwh


def mostrar_cabecalho(config: dict) -> None:
    print("=" * 66)
    print(" CITIZEN ASSIST AI | ENERGIA CIDADÃ")
    print(" Orientações acessíveis sobre eficiência e energia renovável")
    print(f" Projeto individual: {config['projeto']['autor']} | RM {config['projeto']['rm']}")
    print("=" * 66)


def mostrar_contexto(config: dict) -> None:
    print("\nPÚBLICO E CONTEXTO\n")
    print(config["publico_alvo"])
    print(f"\nNecessidade: {config['necessidade']}")
    print(f"Consumo de referência usado: {config['consumo']['cenario_residencia_kwh_mes']:.0f} kWh/mês.")
    print(f"Média residencial pública de referência: {config['consumo']['media_residencial_brasil_kwh_mes']:.0f} kWh/mês.")
    print("Os números descrevem um cenário didático; não representam a casa de um usuário específico.")


def mostrar_recomendacoes(config: dict) -> None:
    print("\nRECOMENDAÇÕES PRÁTICAS\n")
    print("1. Confira os últimos 12 meses de consumo na fatura ou no app da distribuidora.")
    print("2. Troque lâmpadas incandescentes por LED de fluxo luminoso equivalente, se ainda existirem.")
    print("3. Reduza o tempo de uso de equipamentos e evite deixá-los ligados sem necessidade.")
    print("4. Antes de instalar painéis solares, avalie sombra, estrutura do telhado e orçamento completo.")
    print("5. Compare a tarifa total da fatura, os encargos e as regras de compensação vigentes.")
    print("6. Consulte as referências listadas no README.md e no documento de análise energética.")


def menu_perguntas(config: dict) -> None:
    print("\nASSISTENTE DE ENERGIA — digite sua pergunta. Digite 'voltar' para sair.")
    while True:
        pergunta = input("\nVocê: ").strip()
        if pergunta.casefold() in {"voltar", "sair", "0"}:
            break
        print(f"\nAssistente: {responder(pergunta, config)}")


def mostrar_resumo(config: dict) -> None:
    print("\n" + resumo_comparacao(config))
    input("\nPressione Enter para voltar ao menu...")


def mostrar_ajuda(config: dict) -> None:
    print("\nREFERÊNCIAS RÁPIDAS\n")
    print(f"Tarifa usada: {formatar_brl(tarifa_por_kwh(config))}/kWh (TUSD + TE, sem itens adicionais da fatura).")
    print("Fontes e limitações completas: README.md e docs/ANALISE_ENERGETICA.md.")
    print("Premissas que podem ser editadas: data/parametros.json.")
    input("\nPressione Enter para voltar ao menu...")


def main() -> None:
    try:
        config = load_config()
    except (FileNotFoundError, ValueError) as erro:
        print(f"Erro ao carregar o projeto: {erro}")
        raise SystemExit(1) from erro

    mostrar_cabecalho(config)
    opcoes = {
        "1": ("Contexto e público-alvo", lambda: mostrar_contexto(config)),
        "2": ("Comparar alternativas (LED x solar fotovoltaica)", lambda: mostrar_resumo(config)),
        "3": ("Orientações práticas", lambda: mostrar_recomendacoes(config)),
        "4": ("Perguntar ao assistente", lambda: menu_perguntas(config)),
        "5": ("Fontes, dados e premissas", lambda: mostrar_ajuda(config)),
    }
    while True:
        print("\nMENU PRINCIPAL")
        for numero, (titulo, _) in opcoes.items():
            print(f"{numero}. {titulo}")
        print("0. Encerrar")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "0":
            print("Obrigado por usar o Energia Cidadã. Consulte README.md para referências e limitações.")
            break
        acao = opcoes.get(escolha)
        if acao is None:
            print("Opção inválida. Digite um número entre 0 e 5.")
            continue
        acao[1]()


if __name__ == "__main__":
    main()
