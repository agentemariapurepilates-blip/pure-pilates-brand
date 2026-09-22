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
> A pose: sentada de lado sobre o assento, as pernas estendidas juntas ao longo dele, uma das mãos segurando a barra do pedal lá embaixo, o outro braço subindo num arco longo acima da cabeça, a cabeça inclinada para cima acompanhando a mão. Expressão serena, sem sorrir.
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
