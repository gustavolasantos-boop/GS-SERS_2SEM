# Citizen Assist AI — Energia Cidadã

**Trabalho individual — Global Solution 2026.2**  
**Aluno:** Gustavo Lima Andrade Santos  
**RM:** 571709  
**Disciplina:** Soluções em Energias Renováveis e Sustentáveis  
**Data de referência dos dados:** 19/11/2026

## 1. Objetivo

Este projeto implementa, em Python e no terminal, um módulo de orientação energética que pode ser incorporado conceitualmente ao **Citizen Assist AI**. Não é um site e não requer internet, conta externa, API ou biblioteca de terceiros para funcionar.

O assistente ajuda o público a entender estimativas de consumo, comparar uma medida de eficiência energética com uma alternativa renovável e consultar orientações em linguagem acessível. As respostas são baseadas em regras e cálculos determinísticos, para que os resultados sejam rastreáveis.

## 2. Público-alvo e problema

**Público:** famílias em residências urbanas da Região Metropolitana de São Paulo que desejam reduzir a conta de luz, mas não têm necessariamente formação técnica em energia.

**Necessidade:** compreender como uma alteração simples no uso da eletricidade e a geração solar fotovoltaica poderiam reduzir a energia comprada da rede.

**Cenário de referência:** residência com 180 kWh/mês. O valor é um cenário didático arredondado a partir da média residencial nacional de 176 kWh/mês informada para o período de janeiro a dezembro de 2025 pelo Boletim Mensal de Monitoramento do Sistema Elétrico do MME (janeiro de 2026). Não representa um consumidor real.

## 3. Funcionalidades

- Exibição do público-alvo, da necessidade e das premissas do cenário.
- Comparação, para o mesmo domicílio e período mensal/anual, entre:
  - **Eficiência:** troca hipotética de dez lâmpadas incandescentes de 60 W por LEDs de 9 W.
  - **Fonte renovável:** sistema solar fotovoltaico de 1 kWp, com geração mensal ilustrativa configurável.
- Cálculo de kWh economizados/gerados, custo inicial de referência, valor bruto equivalente da energia e emissões médias estimadas evitadas.
- Assistente de perguntas frequentes sobre consumo, tarifa, LEDs, solar, emissões e limitações.
- Referências, dados e ressalvas acessíveis nos arquivos de documentação e no menu do programa.
- Testes automatizados com `unittest`.

## 4. Como executar

Requisito: Python 3.10 ou superior. Não há dependências externas.

### Windows

1. Extraia o ZIP.
2. Abra a pasta `GS_Citizen_Assist_Energia`.
3. Dê dois cliques em `executar_windows.bat`, ou abra o terminal nessa pasta e execute:

```powershell
py main.py
```

### Linux / macOS

No terminal, dentro da pasta do projeto:

```bash
python3 main.py
```

### Executar testes automatizados

No terminal, dentro da pasta do projeto:

```bash
python -m unittest discover -s tests -v
```

No Windows também pode usar `py -m unittest discover -s tests -v`.

## 5. Como usar

No menu principal, selecione:

1. Contexto e público-alvo.
2. Comparação LED x solar fotovoltaica.
3. Orientações práticas.
4. Perguntar ao assistente — tente perguntas como “Como economizar com LED?”, “Qual tarifa foi usada?”, “Quanto consome uma residência?” ou “Essa economia é garantida?”.
5. Fontes, dados e premissas.

As premissas configuráveis estão em `data/parametros.json`. Alterações devem preservar os nomes das chaves para que os cálculos continuem funcionando.

## 6. Justificativas das Recomendações

As recomendações do módulo Energia Cidadã foram definidas considerando o consumo estimado da residência, o investimento inicial, a facilidade de implementação, a economia potencial de energia e os impactos ambientais. O objetivo é apresentar alternativas acessíveis e tecnicamente justificadas, sem tratar estimativas como resultados garantidos.

### 1. Alternativa A — Substituição de lâmpadas antigas por LEDs

**Justificativa econômica:** A substituição de dez lâmpadas incandescentes de 60 W por LEDs de 9 W considera um investimento didático de R$ 80,00, utilizando o preço estimado de R$ 8,00 por lâmpada. Com quatro horas de utilização diária, a redução estimada é de 61,2 kWh por mês, equivalente a aproximadamente R$ 48,31 mensais em energia, utilizando a tarifa simplificada de R$ 0,78938/kWh.

Esse valor representa uma estimativa bruta da energia economizada, e não uma garantia de redução nesse valor na fatura. O resultado real depende do tempo de utilização, da tarifa aplicável e das condições da residência.

**Justificativa de viabilidade:** A medida foi recomendada por apresentar baixo investimento inicial e implementação simples, sem necessidade de obras ou instalação de equipamentos complexos. É especialmente adequada para residências que ainda utilizam lâmpadas incandescentes ou outras lâmpadas de potência elevada. Caso a residência já utilize LEDs eficientes, a economia adicional poderá ser pequena ou inexistente.

**Justificativa ambiental:** A redução do consumo de eletricidade diminui a demanda por energia da rede e pode contribuir para reduzir as emissões associadas à geração elétrica. No cenário estudado, utilizando o fator médio de emissões de 0,0648 kg CO2eq/kWh, a redução estimada corresponde a aproximadamente 3,97 kg CO2eq por mês, ou 47,65 kg CO2eq por ano. Trata-se de uma aproximação que não considera todo o ciclo de vida dos equipamentos. O descarte adequado das lâmpadas substituídas também deve ser considerado.

### 2. Alternativa B — Geração solar fotovoltaica

**Justificativa econômica:** A geração solar foi incluída por representar uma alternativa de fornecimento de energia renovável. No cenário didático, um sistema de 1 kWp possui geração estimada de 100 kWh por mês. Considerando a tarifa simplificada adotada, essa produção corresponde a um valor bruto equivalente de aproximadamente R$ 78,94 mensais.

O investimento de referência utilizado é de R$ 2.910,00, calculado por extrapolação proporcional de uma referência de R$ 2,91/Wp para um sistema residencial de 4 kWp. Esse valor não constitui um orçamento comercial para um sistema de 1 kWp. O retorno financeiro real depende do preço de instalação, da geração efetiva, do consumo simultâneo, das regras de compensação, dos encargos, da manutenção e das condições de financiamento.

**Justificativa de viabilidade:** A solução é indicada para residências com espaço adequado para os módulos, baixa incidência de sombras e condições técnicas favoráveis. Sua implementação exige avaliação do local, orçamento de uma empresa especializada e atendimento às exigências aplicáveis da distribuidora. Por apresentar investimento inicial superior ao da troca de lâmpadas, pode ser mais adequada para moradores que dispõem de recursos para investir no sistema e pretendem utilizá-lo por um período prolongado.

**Justificativa ambiental:** A energia solar fotovoltaica gera eletricidade a partir de uma fonte renovável e pode reduzir a necessidade de eletricidade fornecida pela rede. Aplicando o fator médio de emissões adotado no projeto, a produção estimada de 100 kWh por mês corresponde a aproximadamente 6,48 kg CO2eq por mês, ou 77,76 kg CO2eq por ano, em emissões médias potencialmente evitadas. Essa estimativa é simplificada e não desconta as emissões da fabricação, do transporte, da instalação e do descarte dos equipamentos.

### 3. Comparação e critérios para a recomendação

| Critério | LEDs | Solar fotovoltaica |
|---|---|---|
| Investimento inicial de referência | R$ 80,00 | R$ 2.910,00 |
| Resultado energético estimado | Economia de 61,2 kWh/mês | Geração de 100 kWh/mês |
| Facilidade de implementação | Alta, quando há lâmpadas antigas para substituir | Depende das condições do imóvel e da instalação |
| Necessidade de espaço e obras | Não exige obras | Requer espaço apropriado e instalação técnica |
| Benefício ambiental principal | Redução do consumo elétrico | Geração de eletricidade renovável |
| Principal limitação | A economia depende das lâmpadas substituídas e do uso | Geração e retorno financeiro dependem das condições reais |

Os valores de energia das alternativas não são diretamente equivalentes: a primeira representa consumo evitado, enquanto a segunda representa eletricidade gerada. Da mesma forma, os valores monetários apresentados não correspondem necessariamente à economia líquida na fatura.

A recomendação inicial é priorizar medidas de eficiência energética de baixo custo, como a substituição de lâmpadas antigas por LEDs, quando aplicável. Para residências com condições físicas e financeiras adequadas, a geração solar fotovoltaica pode ser avaliada como uma alternativa complementar. As duas medidas podem ser combinadas, desde que o sistema fotovoltaico seja dimensionado considerando o consumo restante após as medidas de eficiência.

### 4. Limitações das recomendações

Todas as estimativas deste projeto possuem finalidade educacional e dependem das premissas configuradas. Antes de tomar uma decisão real, recomenda-se consultar a fatura de energia, confirmar as tarifas vigentes, verificar o consumo efetivo, obter orçamentos atualizados e utilizar uma simulação solar que considere a localização, a orientação do telhado, a inclinação e o sombreamento.

As referências e os parâmetros utilizados estão documentados nas seções de dados e referências da análise energética. As recomendações do assistente devem ser interpretadas como orientação inicial para apoiar decisões conscientes, e não como garantia de economia financeira ou de redução exata das emissões.


## 7. Estrutura do projeto

```text
GS_Citizen_Assist_Energia/
├── main.py
├── executar_windows.bat
├── executar_unix.sh
├── requirements.txt
├── README.md
├── ENTREGA_template.txt
├── data/
│   └── parametros.json
├── src/
│   ├── __init__.py
│   ├── assistant.py
│   └── energy_calculator.py
├── tests/
│   └── test_energy_calculator.py
└── docs/
    ├── ANALISE_ENERGETICA.md
    ├── TESTES_USABILIDADE.md

```

## 8. Testes

- `tests/test_energy_calculator.py`: testa conversão de tarifa, cálculo LED, geração solar, custo de energia, estimativa de emissões, validação de valores negativos e respostas do assistente.
- `docs/TESTES_USABILIDADE.md`: registra cenários simulados com personas fictícias. Não afirma que pessoas reais participaram.

## 9. Referências

1. **MME — Boletim Mensal de Monitoramento do Sistema Elétrico, janeiro de 2026.** Tabela “Consumo médio mensal por unidade consumidora”; média residencial de 176 kWh/mês para jan–dez/2025.  
   https://www.gov.br/mme/pt-br/assuntos/secretarias/secretaria-nacional-energia-eletrica/publicacoes/boletim-de-monitoramento-do-sistema-eletrico/2026/boletim-mensal-janeiro-2026-vf.pdf

2. **Enel São Paulo — Tarifa de Energia Elétrica.** Tarifas B1 residenciais da Resolução Homologatória ANEEL nº 3.596/2026, vigentes a partir de 04/07/2026: TUSD R$ 472,42/MWh e TE R$ 316,96/MWh.  
   https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html

3. **Greener — Pesquisa Estratégica de Geração Distribuída, 2º semestre de 2026.** Página/figura sobre preços médios de sistemas fotovoltaicos residenciais de 4 kWp; referência de R$ 2,91/Wp em junho de 2026. Usado apenas como referência de mercado, com extrapolação explicitada.  
   https://greenerstorage.blob.core.windows.net/public/estudos/SED_2S_2026.pdf

4. **EPE/MME — Balanço Energético Nacional 2026.** Fator médio de emissões do setor elétrico brasileiro de 64,8 kg CO₂eq/MWh para 2025.  
   https://www.epe.gov.br/pt/imprensa/noticias/epe-publica-o-relatorio-sintese-do-balanco-energetico-nacional-2026

5. **Lei nº 14.300/2022 — Marco Legal da Microgeração e Minigeração Distribuída.** Referência legal para o Sistema de Compensação de Energia Elétrica; a regra aplicável depende das condições da unidade e de sua conexão.  
   https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm

6. **Comissão Europeia — PVGIS.** Ferramenta para estimar produção fotovoltaica mensal/anual a partir da localização, radiação, orientação, inclinação e perdas. Não foi usada para declarar uma produção medida neste cenário; recomenda-se utilizá-la para uma avaliação real.  
   https://re.jrc.ec.europa.eu/pvg_tools/en/

7. **INPE/LABREN — Atlas Brasileiro de Energia Solar, 2ª edição.** Base pública com dados climatológicos de potencial solar no território brasileiro.  
   https://labren.ccst.inpe.br/atlas_2017.html

**Acesso às referências:** 19/11/2026. Valores regulados e preços de mercado mudam; consulte novamente as fontes antes de tomar decisões reais.

## 10. Avisos e limitações

- TUSD + TE não representa todos os itens de uma conta residencial. Tributos, bandeiras, iluminação pública, custo de disponibilidade e condições tarifárias individuais foram excluídos.
- A troca de lâmpadas pressupõe que as dez lâmpadas atuais sejam incandescentes de 60 W, usadas quatro horas por dia. Em uma casa que já usa LEDs, essa economia não se aplica.
- A geração solar de 100 kWh/mês por kWp é uma premissa simplificadora, não uma previsão local. A produção real depende de coordenadas, orientação, inclinação, sombras, sujeira, temperatura, perdas e equipamento.
- O custo de solar em 1 kWp é extrapolado de um benchmark de 4 kWp. Sistemas menores podem ter custo proporcionalmente maior.
- A estimativa monetária solar é o valor bruto equivalente da energia gerada. Ela não modela em detalhe autoconsumo horário, compensação, cobranças de uso da rede, regras legais aplicáveis, manutenção, financiamento ou a tarifa final da unidade.
- O fator de emissões é uma média nacional e não analisa o ciclo de vida de lâmpadas, módulos, inversores ou baterias.
- As recomendações são educativas. Para instalar sistemas elétricos ou fotovoltaicos, obtenha avaliação e orçamento de profissional habilitado.


