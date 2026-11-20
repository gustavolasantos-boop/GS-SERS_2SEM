# Análise energética — Citizen Assist AI / Energia Cidadã

**Autor:** Gustavo Lima Andrade Santos — **RM:** 571709  
**Data de referência:** 19/11/2026

## 1. Contexto

O público escolhido é formado por famílias em residências urbanas da Região Metropolitana de São Paulo que querem compreender o consumo e reduzir o custo de energia. Esse grupo pode precisar de recomendações práticas e explicações sem jargão. A solução usa uma interface de terminal que funciona localmente e não solicita dados pessoais.

A necessidade energética estudada é reduzir a eletricidade comprada da rede em uma residência hipotética. Duas alternativas são comparadas para o mesmo consumo-base e o mesmo período de referência: (A) eficiência na iluminação com LEDs e (B) fornecimento por solar fotovoltaica.

## 2. Dados, unidades e premissas

| Parâmetro | Valor usado | Tipo e origem |
|---|---:|---|
| Consumo médio residencial nacional | 176 kWh/mês | Dado publicado pelo MME, média de jan–dez/2025 conforme boletim de janeiro de 2026 |
| Consumo de cenário | 180 kWh/mês | Estimativa didática arredondada a partir dos 176 kWh/mês; não é dado de usuário |
| TUSD residencial B1 | R$ 472,42/MWh | Enel São Paulo, valores vigentes a partir de 04/07/2026 |
| TE residencial B1 | R$ 316,96/MWh | Enel São Paulo, valores vigentes a partir de 04/07/2026 |
| Tarifa energética usada nos cálculos | R$ 0,78938/kWh | Soma de TUSD + TE dividida por 1.000; exclui itens adicionais da fatura |
| Lâmpadas antigas | 10 × 60 W | Premissa hipotética (incandescentes) |
| Lâmpadas novas | 10 × 9 W | Premissa hipotética (LEDs de iluminação comparável) |
| Tempo de uso de cada lâmpada | 4 horas/dia; 30 dias/mês | Premissa hipotética |
| Preço por LED | R$ 8,00 | Estimativa didática, não cotação de mercado |
| Sistema fotovoltaico | 1 kWp | Potência do cenário de simulação |
| Geração fotovoltaica | 100 kWh/mês por kWp | Premissa didática configurável; requer estudo local para projeto real |
| Referência de preço fotovoltaico | R$ 2,91/Wp para sistema de 4 kWp | Pesquisa Greener, junho de 2026; custo de 1 kWp calculado por extrapolação linear |
| Fator médio de emissões | 64,8 kg CO₂eq/MWh | EPE/MME, BEN 2026, eletricidade gerada no Brasil em 2025 |

## 3. Fórmulas

### 3.1 Tarifa simplificada

\[
T = \frac{472{,}42 + 316{,}96}{1000} = 0{,}78938\;\text{R\$/kWh}
\]

### 3.2 Consumo-base

\[
C_{base}=180\;\text{kWh/mês}
\]

Parcela energética teórica antes das medidas:

\[
180\times 0{,}78938 = R\$\;142{,}09/\text{mês}
\]

Não é o valor total da fatura; a conta real pode conter impostos, bandeiras, contribuição de iluminação pública, custo de disponibilidade e outros itens.

### 3.3 Alternativa A — troca de lâmpadas por LED

Energia economizada:

\[
E_{LED}=\frac{(P_{antiga}-P_{LED})\times N\times h\times d}{1000}
\]

\[
E_{LED}=\frac{(60-9)\times10\times4\times30}{1000}=61{,}2\;\text{kWh/mês}
\]

Em um ano, se o padrão de uso se mantiver:

\[
61{,}2\times12=734{,}4\;\text{kWh/ano}
\]

Investimento premissado:

\[
10\times R\$\;8{,}00=R\$\;80{,}00
\]

Valor bruto equivalente da energia economizada:

\[
61{,}2\times R\$\;0{,}78938\approx R\$\;48{,}31/\text{mês}
\]

A economia depende de haver lâmpadas antigas para substituir, do uso efetivo e de equivalência adequada de iluminação.

### 3.4 Alternativa B — geração solar fotovoltaica

A premissa de produção do exercício é 100 kWh por mês para cada kWp instalado.

\[
E_{FV}=1\;\text{kWp}\times100\;\text{kWh/(kWp\cdot mês)}=100\;\text{kWh/mês}
\]

Produção anualizada:

\[
100\times12=1.200\;\text{kWh/ano}
\]

O custo publicado pela Greener foi de R$ 2,91/Wp para sistemas residenciais de referência de 4 kWp, em junho de 2026. A simulação usa uma extrapolação proporcional:

\[
1.000\;\text{Wp}\times R\$\;2{,}91/\text{Wp}=R\$\;2.910{,}00
\]

O cálculo é somente uma referência didática: um sistema comercial de 1 kWp pode ter custo por Wp maior, e o preço real precisa de cotação completa.

Valor bruto equivalente da produção:

\[
100\times R\$\;0{,}78938=R\$\;78{,}94/\text{mês}
\]

Esse valor representa apenas energia gerada multiplicada pela tarifa de referência. Não é uma estimativa de economia líquida nem inclui o regime específico de compensação, consumo simultâneo, encargos, custo mínimo, tributos, manutenção ou financiamento.

## 4. Comparação para a mesma residência

| Critério | Alternativa A: LEDs | Alternativa B: solar fotovoltaica |
|---|---|---|
| Tipo | Redução de demanda / eficiência | Geração renovável |
| Energia estimada | 61,2 kWh/mês economizados | 100 kWh/mês gerados para 1 kWp |
| Energia anualizada | 734,4 kWh/ano | 1.200 kWh/ano |
| Investimento inicial usado | R$ 80,00 (premissa) | R$ 2.910,00 (extrapolação linear de referência de 4 kWp) |
| Valor bruto equivalente mensal | R$ 48,31 | R$ 78,94 |
| Viabilidade | Fácil e barata se houver lâmpadas incandescentes; sem obra | Exige telhado apropriado, pouco sombreamento, orçamento, instalador habilitado e trâmites com distribuidora |
| Impacto ambiental | Menor consumo da rede; descarte correto das lâmpadas | Produção renovável; considerar materiais, fabricação, manutenção e descarte ao fim da vida útil |
| Principal limitação | A economia não existe se a casa já usa LEDs | Geração e economia líquida variam; não é possível garantir produção ou retorno sem estudo e orçamento |

As alternativas atendem à mesma necessidade geral de reduzir a energia comprada da rede no domicílio de referência, mas não entregam a mesma quantidade de kWh. LED é a ação de menor investimento e mais simples; solar pode gerar mais energia, mas tem investimento e requisitos técnicos maiores. As duas medidas também podem ser combinadas, desde que o sistema solar seja dimensionado a partir do consumo remanescente.

## 5. Estimativa ambiental

O fator de emissões usado é 64,8 kg CO₂eq/MWh, equivalente a 0,0648 kg CO₂eq/kWh.

- LEDs: \(61{,}2\times0{,}0648\approx3{,}97\) kg CO₂eq/mês ou 47,65 kg CO₂eq/ano.
- Solar: \(100\times0{,}0648=6{,}48\) kg CO₂eq/mês ou 77,76 kg CO₂eq/ano.

É uma aproximação baseada no fator médio do sistema elétrico. Não inclui emissões de fabricação, transporte e descarte dos equipamentos, nem prova uma redução marginal exata.

## 6. Integração com o assistente

O arquivo `src/assistant.py` conecta os cálculos às respostas. O assistente pode:

- apresentar a comparação e as premissas;
- explicar a tarifa usada e o motivo de ela não equivaler ao total da fatura;
- explicar a economia de LED e avisar que o resultado não se aplica a uma casa que já usa LED;
- explicar o fator de emissão e as incertezas;
- recomendar avaliação local e orçamento profissional para solar.

A funcionalidade é determinística e funciona sem uma API de IA, o que favorece reprodutibilidade, funcionamento offline e facilidade de avaliar os cálculos. É o módulo de energia a ser integrado ao fluxo maior do Citizen Assist AI.

## 7. Referências verificáveis

- MME, Boletim Mensal de Monitoramento do Sistema Elétrico, jan./2026: https://www.gov.br/mme/pt-br/assuntos/secretarias/secretaria-nacional-energia-eletrica/publicacoes/boletim-de-monitoramento-do-sistema-eletrico/2026/boletim-mensal-janeiro-2026-vf.pdf
- Enel São Paulo, Tarifa de Energia Elétrica: https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html
- Greener, Pesquisa Estratégica de Geração Distribuída, 2º semestre de 2026: https://greenerstorage.blob.core.windows.net/public/estudos/SED_2S_2026.pdf
- EPE/MME, Relatório Síntese do Balanço Energético Nacional 2026: https://www.epe.gov.br/pt/imprensa/noticias/epe-publica-o-relatorio-sintese-do-balanco-energetico-nacional-2026
- Lei nº 14.300/2022: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm
- Comissão Europeia, PVGIS: https://re.jrc.ec.europa.eu/pvg_tools/en/
- INPE/LABREN, Atlas Brasileiro de Energia Solar, 2ª ed.: https://labren.ccst.inpe.br/atlas_2017.html

## 8. Limitações e atualização

Os resultados são estimativas. Para decisão real, confirme tarifa e regras regulatórias vigentes, colete consumo mensal real, use um simulador solar com localização e condições de telhado, solicite orçamentos instalados e considere tributos, encargos, financiamento e manutenção. Todas as premissas editáveis estão em `data/parametros.json`.
