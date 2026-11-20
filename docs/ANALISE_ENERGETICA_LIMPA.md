# Análise Energética - Citizen Assist AI | Energia Cidadã

**Autor:** Gustavo Lima Andrade Santos  
**RM:** 571709  
**Data de referência:** 19/11/2026

---

## Sumário

1. Contexto
2. Dados, unidades e premissas
3. Fórmulas e cálculos
   - 3.1. Tarifa simplificada
   - 3.2. Consumo-base
   - 3.3. Alternativa A - LEDs
   - 3.4. Alternativa B - Solar fotovoltaica
4. Comparação das alternativas
5. Estimativa ambiental
6. Integração com o assistente
7. Referências verificáveis
8. Limitações e atualização

---

## 1. Contexto

O público escolhido é formado por **famílias em residências urbanas da Região Metropolitana de São Paulo** que querem compreender o consumo e reduzir o custo de energia. Esse grupo pode precisar de recomendações práticas e explicações sem jargão. A solução usa uma interface de terminal que funciona localmente e não solicita dados pessoais.

A necessidade energética estudada é reduzir a eletricidade comprada da rede em uma residência hipotética. Duas alternativas são comparadas para o mesmo consumo-base e o mesmo período de referência:

- **Alternativa A - Eficiência energética:** troca de lâmpadas antigas por LEDs.
- **Alternativa B - Fonte renovável:** geração de energia solar fotovoltaica.

## 2. Dados, unidades e premissas

Os valores abaixo combinam dados publicados e premissas didáticas. As estimativas não representam o consumo ou a instalação de uma pessoa específica.

| Parâmetro | Valor usado | Tipo e origem |
|---|---:|---|
| Consumo médio residencial nacional | 176 kWh/mês | Dado publicado pelo MME; média de jan.-dez./2025 conforme boletim de janeiro de 2026 |
| Consumo do cenário | 180 kWh/mês | Estimativa didática arredondada a partir dos 176 kWh/mês; não é dado de usuário |
| TUSD residencial B1 | R$ 472,42/MWh | Enel São Paulo; valores vigentes a partir de 04/07/2026 |
| TE residencial B1 | R$ 316,96/MWh | Enel São Paulo; valores vigentes a partir de 04/07/2026 |
| Tarifa usada nos cálculos | R$ 0,78938/kWh | Soma de TUSD + TE dividida por 1.000; exclui itens adicionais da fatura |
| Lâmpadas antigas | 10 x 60 W | Premissa hipotética: lâmpadas incandescentes |
| Lâmpadas novas | 10 x 9 W | Premissa hipotética: LEDs com iluminação comparável |
| Tempo de uso por lâmpada | 4 horas/dia; 30 dias/mês | Premissa hipotética |
| Preço por LED | R$ 8,00 | Estimativa didática; não é cotação de mercado |
| Sistema fotovoltaico | 1 kWp | Potência usada no cenário de simulação |
| Geração fotovoltaica | 100 kWh/mês por kWp | Premissa didática configurável; requer estudo local para um projeto real |
| Referência de preço fotovoltaico | R$ 2,91/Wp para sistema de 4 kWp | Pesquisa Greener, junho de 2026; custo para 1 kWp calculado por extrapolação linear |
| Fator médio de emissões | 64,8 kg CO2eq/MWh | EPE/MME, BEN 2026; eletricidade gerada no Brasil em 2025 |

> **Importante:** TUSD + TE é uma tarifa simplificada para os cálculos deste exercício. Ela não representa o valor total de uma fatura residencial.

## 3. Fórmulas e cálculos

### 3.1. Tarifa simplificada

A tarifa de referência é calculada pela soma da TUSD e da TE, convertida de reais por megawatt-hora para reais por quilowatt-hora:

```text
T = (472,42 + 316,96) / 1000 = 0,78938 R$/kWh
```

### 3.2. Consumo-base

O cenário utiliza um consumo estimado de 180 kWh por mês:

```text
C_base = 180 kWh/mês
```

A parcela energética teórica antes das medidas é:

```text
180 x 0,78938 = R$ 142,09/mês
```

Esse cálculo **não representa o valor total da fatura**. A conta real pode incluir impostos, bandeiras tarifárias, contribuição de iluminação pública, custo de disponibilidade e outros itens.

### 3.3. Alternativa A - troca de lâmpadas por LED

A economia mensal de energia é estimada pela diferença de potência entre as lâmpadas, multiplicada pela quantidade de lâmpadas e pelo tempo de uso:

```text
E_LED = ((P_antiga - P_LED) x N x h x d) / 1000
```

Aplicando as premissas do cenário:

```text
E_LED = ((60 - 9) x 10 x 4 x 30) / 1000 = 61,2 kWh/mês
```

Se o padrão de uso se mantiver durante um ano:

```text
61,2 x 12 = 734,4 kWh/ano
```

**Investimento estimado para a troca:**

```text
10 x R$ 8,00 = R$ 80,00
```

**Valor bruto equivalente da energia economizada:**

```text
61,2 x R$ 0,78938 = aproximadamente R$ 48,31/mês
```

A economia depende da existência de lâmpadas antigas para substituir, do uso efetivo e da escolha de LEDs com equivalência adequada de iluminação. Se a residência já utiliza LEDs, essa economia não se aplica.

### 3.4. Alternativa B - geração solar fotovoltaica

A premissa da simulação é uma geração de 100 kWh por mês para cada kWp instalado.

```text
E_FV = 1 kWp x 100 kWh/(kWp x mês) = 100 kWh/mês
```

**Produção anualizada:**

```text
100 x 12 = 1.200 kWh/ano
```

A referência de preço publicada pela Greener foi de R$ 2,91/Wp para sistemas residenciais de referência de 4 kWp, em junho de 2026. A simulação extrapola esse valor proporcionalmente para 1 kWp:

```text
1.000 Wp x R$ 2,91/Wp = R$ 2.910,00
```

Esse valor é apenas uma referência didática. Um sistema comercial de 1 kWp pode ter custo por Wp maior; o preço real exige orçamento completo.

**Valor bruto equivalente da produção:**

```text
100 x R$ 0,78938 = R$ 78,94/mês
```

Esse valor representa a energia estimada gerada multiplicada pela tarifa de referência. **Não é uma estimativa de economia líquida.** O cálculo não inclui o regime específico de compensação, consumo simultâneo, encargos, custo mínimo, tributos, manutenção ou financiamento.

## 4. Comparação para a mesma residência

| Critério | Alternativa A - LEDs | Alternativa B - Solar fotovoltaica |
|---|---|---|
| Tipo | Redução de demanda / eficiência | Geração renovável |
| Energia estimada | 61,2 kWh/mês economizados | 100 kWh/mês gerados para 1 kWp |
| Energia anualizada | 734,4 kWh/ano | 1.200 kWh/ano |
| Investimento inicial usado | R$ 80,00 (premissa) | R$ 2.910,00 (extrapolação linear da referência de 4 kWp) |
| Valor bruto equivalente mensal | R$ 48,31 | R$ 78,94 |
| Viabilidade | Simples e de baixo custo se houver lâmpadas incandescentes; não exige obra | Exige telhado apropriado, pouco sombreamento, orçamento, instalador habilitado e trâmites com a distribuidora |
| Impacto ambiental | Reduz o consumo da rede; é necessário descartar corretamente as lâmpadas | Gera energia renovável; devem ser considerados materiais, fabricação, manutenção e descarte ao fim da vida útil |
| Principal limitação | A economia não ocorre se a casa já usa LEDs | Geração e economia líquida variam; não é possível garantir produção ou retorno sem estudo e orçamento |

As duas alternativas atendem à necessidade geral de reduzir a energia comprada da rede no domicílio de referência, mas **não entregam a mesma quantidade de kWh**. A troca por LEDs exige menor investimento inicial e é mais simples. A energia solar pode gerar mais energia no cenário estimado, mas requer maior investimento e avaliação técnica.

As medidas também podem ser combinadas, desde que o sistema solar seja dimensionado considerando o consumo remanescente.

## 5. Estimativa ambiental

O fator de emissões usado é de 64,8 kg CO2eq/MWh, equivalente a 0,0648 kg CO2eq/kWh.

- **LEDs:** 61,2 x 0,0648 = aproximadamente 3,97 kg CO2eq/mês, ou 47,65 kg CO2eq/ano.
- **Solar:** 100 x 0,0648 = 6,48 kg CO2eq/mês, ou 77,76 kg CO2eq/ano.

Esses valores são aproximações baseadas no fator médio do sistema elétrico. Não incluem emissões de fabricação, transporte e descarte dos equipamentos, nem demonstram uma redução marginal exata.

## 6. Integração com o assistente

O arquivo `src/assistant.py` conecta os cálculos às respostas. O assistente pode:

- apresentar a comparação entre as alternativas e as respectivas premissas;
- explicar a tarifa usada e por que ela não equivale ao total da fatura;
- explicar a economia estimada com LEDs e alertar que o resultado não se aplica a residências que já usam LED;
- explicar o fator de emissão e as incertezas da estimativa ambiental;
- recomendar avaliação local e orçamento profissional para a instalação de um sistema solar.

A funcionalidade é determinística e funciona sem uma API de IA, favorecendo a reprodutibilidade, o uso offline e a verificação dos cálculos. O módulo representa a contribuição de energia a ser integrada ao fluxo maior do **Citizen Assist AI**.

## 7. Referências verificáveis

1. **MME - Boletim Mensal de Monitoramento do Sistema Elétrico, janeiro de 2026.** Média residencial de 176 kWh/mês para o período de janeiro a dezembro de 2025.  
   <https://www.gov.br/mme/pt-br/assuntos/secretarias/secretaria-nacional-energia-eletrica/publicacoes/boletim-de-monitoramento-do-sistema-eletrico/2026/boletim-mensal-janeiro-2026-vf.pdf>

2. **Enel São Paulo - Tarifa de Energia Elétrica.**  
   <https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html>

3. **Greener - Pesquisa Estratégica de Geração Distribuída, segundo semestre de 2026.** Referência de preço para sistemas fotovoltaicos residenciais.  
   <https://greenerstorage.blob.core.windows.net/public/estudos/SED_2S_2026.pdf>

4. **EPE/MME - Relatório Síntese do Balanço Energético Nacional 2026.**  
   <https://www.epe.gov.br/pt/imprensa/noticias/epe-publica-o-relatorio-sintese-do-balanco-energetico-nacional-2026>

5. **Lei número 14.300/2022 - Marco Legal da Microgeração e Minigeração Distribuída.**  
   <https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm>

6. **Comissão Europeia - PVGIS.** Ferramenta para estimar a produção fotovoltaica a partir de localização, radiação, orientação, inclinação e perdas. Não foi usada para declarar uma produção medida neste cenário; recomenda-se para uma avaliação real.  
   <https://re.jrc.ec.europa.eu/pvg_tools/en/>

7. **INPE/LABREN - Atlas Brasileiro de Energia Solar, segunda edição.**  
   <https://labren.ccst.inpe.br/atlas_2017.html>

## 8. Limitações e atualização

Os resultados são estimativas para fins educacionais. Antes de tomar uma decisão real:

- confirme a tarifa e as regras regulatórias vigentes;
- consulte o consumo mensal real da residência;
- utilize um simulador solar que considere localização e condições do telhado;
- solicite orçamentos com instalação e avalie tributos, encargos, financiamento e manutenção.

Todas as premissas editáveis do projeto estão em `data/parametros.json`. Tarifas e preços de mercado podem mudar; consulte novamente as fontes antes de usar os valores em uma decisão real.
