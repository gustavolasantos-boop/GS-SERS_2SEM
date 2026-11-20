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

## 6. Resultado da comparação — cenário-base

Com as premissas entregues:

- **Tarifa de referência:** R$ 0,78938/kWh (TUSD + TE da classe B1 residencial convencional da Enel São Paulo; não é o total da fatura).
- **LED:** economia calculada de 61,2 kWh/mês, ou 734,4 kWh/ano. O custo de R$ 80,00 para dez LEDs é uma premissa de exercício, não uma cotação verificada.
- **Solar:** geração estimada de 100 kWh/mês para 1 kWp. O custo de referência de R$ 2.910,00 é uma extrapolação linear de um valor médio de R$ 2,91/Wp divulgado para sistemas residenciais de 4 kWp em junho de 2026; não equivale a um orçamento de sistema de 1 kWp.

O programa também mostra o valor bruto equivalente da energia e as emissões médias evitadas estimadas. Esses valores não são garantias de economia, retorno financeiro ou benefício ambiental real. Leia `docs/ANALISE_ENERGETICA.md`.

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
    └── ROTEIRO_VIDEO.md
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

## 11. Entrega acadêmica

O enunciado solicita repositório GitHub, vídeo técnico não listado de até 3 minutos e um arquivo `.txt` contendo nome/RM, link do repositório e link do vídeo. O arquivo `ENTREGA_template.txt` serve como modelo; complete os dois links depois de publicar os materiais. O ZIP deste projeto não substitui a exigência de publicação ou o formato final indicado pelo professor.
