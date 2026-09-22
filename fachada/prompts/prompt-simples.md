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

## ⚠️ A pose não fecha por palavras

Descrever a geometria em prosa levou a pose de ruim para quase certa (v8 → v9), mas **a perna de baixo continua flutuando sem apoio**. O modelo entende a curva do tronco e erra o contato com o assento.

O que resolve: **passar a foto da pose como terceira referência**. Palavra descreve intenção; imagem trava geometria. A foto precisa estar em `fachada/` como arquivo — imagem colada no chat não chega ao gerador.
