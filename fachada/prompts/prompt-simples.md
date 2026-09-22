# O prompt que funcionou — versão curta

Depois de sete tentativas com prompts de 800 palavras, **o curto ganhou**. Prompt longo compete consigo mesmo: cada bloco que eu acrescentava para travar uma coisa fazia outra escapar (a modelo trocava de pessoa, a pose se desfazia, o enquadramento fechava).

## Referências — duas, só

1. `fachada/Cenário/WhatsApp Image 2026-09-22 at 10.22.47 (1).jpeg` — a Wunda Chair
2. `fachada/Cenário/Captura de Tela 2026-09-22 às 15.53.38.png` — o painel ripado com o "p"

## Parâmetros

`model_tier: "pro"` · `mode: "generate"` · `resolution: "4k"` · `aspect_ratio: "16:9"` · `enable_grounding: true`

`negative_prompt`: `pele suada, pele de porcelana, pele lisa demais, filtro de beleza, aparência de render 3D`

## O prompt

> Uma fotografia editorial de uma mulher praticando na Wunda Chair da foto anexada, num estúdio de paredes bege bem claras, levemente alaranjadas.
>
> Numa das paredes há o painel de ripas verticais da foto anexada, com o "p" vermelho retroiluminado — o painel ocupa só um trecho da parede, não a parede inteira. O resto é a parede bege clara lisa.
>
> O aparelho é exatamente o da foto anexada, com os mesmos logotipos pretos na lateral de madeira.
>
> A modelo: morena de pele marrom médio, cabelo preto cacheado volumoso e solto na altura dos ombros, corpo atlético. Top regata preto e legging preta de cintura alta, descalça.
>
> A pose é o alongamento lateral da sereia na cadeira. Ela está sentada de lado sobre o assento, com o peso apoiado num quadril só. As duas pernas ficam juntas, uma encostada na outra, e apoiadas em cima do próprio assento: estendidas para o lado com os joelhos levemente flexionados, as canelas descansando sobre o estofado e só os pés passando um pouco da borda. Nenhuma perna fica solta no ar. A mão de baixo desce à frente da cadeira e segura a barra de madeira do pedal lá embaixo, com o braço esticado sustentando o peso do tronco. A partir desse apoio o corpo desenha uma curva longa em C aberta para cima: a cintura do lado de apoio se fecha, as costelas do lado de cima se abrem, e o outro braço sobe num arco por cima da cabeça, com a mão ultrapassando a linha da cabeça. A cabeça se inclina para trás e o olhar acompanha a mão levantada. Expressão serena, sem sorrir.
>
> A luz: sol quente da tarde entrando de lado e batendo raspante numa das paredes, desenhando sombras nítidas. Ele raspa o rosto e o corpo dela de lado e deixa o outro lado na sombra.
>
> Pele seca e fosca, com poros visíveis e tom desigual. Cabelo com frizz e fios soltos pegando o sol.
>
> 50mm, corpo inteiro e aparelho inteiro dentro do quadro. Sem retoque, grão fino.

## Para trocar de peça

Trocar só o parágrafo da pose e o da luz. O resto fica.

## Os logotipos miúdos: resolver fora do modelo

O modelo erra "pure" (sai "Pure" com P maiúsculo) e embola a figurinha. Não fecha por prompt — é o ponto de ruptura dele com tipografia pequena.

`fachada/geradas/fachada-modelo-painel-v6-logo-real.png` prova o caminho: o logotipo oficial recomposto por cima, em multiply, com o veio da madeira atravessando a gravação. O script está em `scratchpad/comp4.py` da sessão; a ideia é apagar a área com madeira ladrilhada e aplicar a arte oficial mascarada por luminância.

## A pose: imagem trava, palavra só aproxima

Trajetória: v8 (pernas boiando no ar) → v9 (prosa com geometria de contato: quase certa, perna de baixo ainda solta) → **v10 (foto da pose como referência: fechou)**.

Referência da pose: `fachada/Pose/pose-referencia-sereia.png`, passada como **primeira** das três entradas.

A descrição escrita continua no prompt junto com a imagem — as duas somadas. A leitura que funcionou nomeia os apoios, não a intenção:

- sentada de lado no assento, peso num quadril só
- perna de cima dobrada, canela inteira deitada sobre o estofado, dedos passando a borda
- perna de baixo descendo por fora da lateral do assento, joelho quase reto
- mão de baixo segurando **por cima a barra de madeira do pedal**, braço quase esticado sustentando o tronco
- tronco em curva de C: cintura do lado do apoio fecha, costelas de cima abrem
- braço de cima em arco acima e à frente da cabeça, mão aberta, palma para baixo
- cabeça para trás, queixo levantado, olhar além da mão

**O que ainda escapa:** o modelo troca a mão de apoio da barra do pedal para a própria perna. É o último ponto de contato a travar.

## Ganho colateral da v10

Foi a primeira em que o **aparelho inteiro** coube no quadro — "MetaLife", "Pure Pilates" e "Linha infinity" visíveis, com a plataforma no chão. Com a pose travada por imagem, o modelo parou de gastar decisão no corpo e resolveu melhor o enquadramento.
