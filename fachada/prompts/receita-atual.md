# Receita atual — modelo no painel ripado

Validada na v6 (22/09/2026). Substitui `cenario-base.md`, que foi montado sobre o `Zoom_out`, e esse arquivo era um **render**, não o estúdio real.

## Referências — só duas

1. `fachada/Cenário/WhatsApp Image 2026-09-22 at 10.22.47 (1).jpeg` — a Wunda Chair
2. `fachada/Cenário/Captura de Tela 2026-09-22 às 15.53.38.png` — **o painel ripado real com o "p"**

Menos é mais: com 5–7 referências o modelo misturava fontes (o lockup vermelho `logo-pure-pilates.png` contaminava a serigrafia preta do aparelho). Com duas, ele obedece.

## Parâmetros

`model_tier: "pro"` · `mode: "generate"` · `resolution: "4k"` · `aspect_ratio: "16:9"` · `enable_grounding: true`

## O painel real ≠ o render

| | Render `Zoom_out` | **Painel real** |
|---|---|---|
| Ripas | madeira mel, quente | claras, acinzentadas/amendoadas |
| Retroiluminação | halo dourado quente | **branca e fria** |
| O "p" | vetor chapado | acrílico vermelho profundo, **com reflexo especular** |

## As quatro travas que funcionaram

**1. "Exatamente o anexado".** Dizer que o aparelho é o da foto anexada e que "nada no aparelho muda", listando os três logotipos pelo nome, posição e tamanho pequeno.

**2. Luz lateral dura com sombra nomeada.** É o que mata a pele plástica:
> sol natural entrando de lado, baixo e duro, pela esquerda da câmera. Ele acende a lateral esquerda do rosto e deixa o lado direito na sombra, com uma linha de transição nítida atravessando a bochecha, o pescoço e o ombro. A sombra do corpo é projetada nítida sobre as ripas do painel atrás.

**3. Pele seca e fosca (decisão da Maria: sem suor).** Contraria o guia da marca, que trata o suor como o detalhe que mais vende realismo — mas a marca manda. A textura passa a vir de outro lugar:
> seca e fosca, acabamento mate. Poros bem visíveis no rosto inteiro. Tom desigual, vermelhidão leve nas maçãs e asas do nariz. Pequenos brilhos secos e irregulares só nos pontos altos do osso. Buço e pelos finos captando a luz raspante nas bordas. Linhas finas no canto dos olhos. Poros e pelos finos também nos braços e pernas.

`negative_prompt`: `pele suada, brilho de suor, pele molhada, gotas de suor, pele de porcelana, pele aerografada, pele lisa demais, aparência de cera, filtro de beleza, aparência de render 3D, CGI, luz de estúdio difusa`

**4. Enquadramento declarado por elemento.** Nomear o que tem de caber inteiro, um por um, e quanto do quadro cada um ocupa. "Plano aberto" sozinho não basta — o modelo fecha.

## ⚠️ O que ainda não resolvi

- **A base do aparelho corta.** "Linha infinity" e a plataforma de madeira ficam fora do quadro. Da v5 para a v6 melhorou, mas não fechou.
- **As pernas se separam.** Peço "pernas estendidas juntas" e elas saem abertas, com a da frente longa demais.
- **Tipografia miúda erra** ("insinity", "incinity"). Para peça final, o caminho seguro é recompor os logotipos reais em cima — a imagem tem 5504 px de largura, sobra resolução para isso.

## Descartado pelo caminho

- **`mode: "edit"`** — ignora o `4k` e devolve 1408×768.
- **"iPhone 17 Pro Max em modo retrato"** — não borrou o fundo (o que era bom) mas veio junto com pele lisa: processamento de celular suaviza pele.
- **`subsurface scattering`** — a internet recomenda, o guia da marca proíbe: dá cara de render 3D.
