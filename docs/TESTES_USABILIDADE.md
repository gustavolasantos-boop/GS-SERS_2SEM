# Registro de testes e ajustes de usabilidade

**Projeto:** Citizen Assist AI — Energia Cidadã  
**Responsável:** Gustavo Lima Andrade Santos — RM 571709  
**Tipo de validação:** testes automatizados e cenários de usabilidade simulados  


## 1. Testes automatizados executáveis

Arquivo: `tests/test_energy_calculator.py`  
Comando: `python -m unittest discover -s tests -v`

Os testes verificam a conversão de tarifa, a economia de iluminação, a geração solar, o custo simplificado, as emissões estimadas, a validação de entrada negativa e a presença de respostas do assistente. Execução feita no ambiente de desenvolvimento em 19/11/2026: **9 testes aprovados, 0 falhas (`OK`)**. A versão do Python usada está registrada no arquivo `VERSAO_PYTHON_TESTES.txt` no pacote.

## 2. Cenários de diferentes usuarios

| ID | Persona fictícia e tarefa | Resultado esperado | Observação simulada / risco identificado | Ajuste implementado |
|---|---|---|---|---|
| U01 | Pessoa sem conhecimento técnico pergunta como reduzir a conta | Recebe ações concretas e uma distinção entre eficiência e geração | “Não sei o que significa kWh.” | O assistente usa exemplos de casa e o README explica o contexto e as unidades. |
| U02 | Morador pergunta quanto economizaria trocando lâmpadas | Vê a fórmula, a economia mensal e as premissas | “A economia só vale se eu tiver lâmpadas antigas.” | A resposta alerta que o cálculo não se aplica a uma casa que já usa LED. |
| U03 | Família compara LED e painel solar | Vê investimento, energia, custos e limitações das duas opções | “R$ por kWh parece o valor total da conta.” | A tela e os documentos avisam que TUSD + TE é só uma parcela, sem diversos itens da fatura. |
| U04 | Pessoa interessada em solar pergunta se a geração é garantida | Recebe explicação de telhado, sombras, variação e consulta a fontes técnicas | “O sistema sempre gera 100 kWh por mês?” | A geração é rotulada como premissa didática configurável; PVGIS e INPE são indicados para estimativa local. |
| U05 | Usuário digita uma opção inexistente ou pergunta algo não coberto | Programa informa a opção válida / temas suportados | Risco de interpretar ausência de resposta como dado real | Menu valida opções; assistente oferece temas e não inventa informação específica. |

## 3. Resultado da revisão simulada

A revisão concluiu que o assistente precisa mostrar, junto dos números, as condições que os geraram. Foram mantidos os seguintes avisos na solução: tarifa simplificada não equivale à conta final; LED depende das lâmpadas existentes; geração solar é variável; custo do sistema de 1 kWp é uma extrapolação; cálculo de emissões não representa ciclo de vida; nenhuma economia ou prazo de retorno é garantido.


