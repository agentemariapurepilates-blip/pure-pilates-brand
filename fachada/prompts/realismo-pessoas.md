# Como gerar pessoas que não parecem IA

Pesquisa feita em 22/09/2026 + o que já estava validado no histórico de produção da Pure. Fontes no fim.

## A causa raiz (por que o default é pele plástica)

Dois vieses somados, que explicam por que "pedir mais qualidade" piora:

1. **Os modelos treinam em moda e e-commerce retocados.** O entendimento default de "pele boa" é, na prática, "pele com filtro".
2. **Os avaliadores humanos premiaram pele lisa** durante o treino. Existe um viés sistemático pró-suavização mesmo quando o material de origem tinha textura.

> Conclusão prática: realismo não é algo que você pede — é algo contra o que você **empurra ativamente**.

---

## 1. O vilão é a LUZ, não o prompt ⭐

O achado que mais muda resultado, e o que a pesquisa e o nosso próprio teste de jul/2026 dizem igual:

| Luz | Efeito na pele |
|---|---|
| Softbox frontal, difusa, suave, chapada | **Apaga a textura.** Devolve porcelana por mais que você peça poro |
| **Sol duro e raspante de lado** | **Revela** cada poro e o relevo do rosto |

> *"Even perfect skin text cannot save flat, unrealistic lighting."*

O cenário da fachada já tem a luz certa: sol baixo entrando pela janela da direita, raspando. **Usar isso a favor** — posicionar a modelo de modo que o sol raspe o rosto dela de lado.

## 2. Trocar palavra de qualidade por fato óptico

Adjetivo de qualidade puxa o modelo para o cluster de arte digital polida. Especificação fotográfica puxa para fotografia de verdade.

| ❌ Cortar | ✅ Usar |
|---|---|
| 8K, 4K, UHD | 50mm, f/5.6 |
| ultra realista, hyperreal | sem retoque |
| masterpiece, premiado | grão fino de filme |
| CGI, render, octane, unreal engine | fotografia editorial sem retoque |
| pele perfeita, impecável, radiante | poros, linhas finas, variação de tom |

**A âncora que funciona:** começar com `Uma fotografia editorial sem retoque de…`

## 3. Bloco de imperfeição dedicado (colar em todo prompt de pessoa)

> Poros visíveis no rosto inteiro — testa, nariz, maçãs e queixo — com variação de tom ao longo da pele, leve rubor nas maçãs e no nariz, leve oleosidade natural na zona T pegando o sol, buço fino captando a luz de lado. Linhas finas de expressão no canto dos olhos e na testa aparecem com o esforço. Brilho de suor real na testa, no pescoço, no colo e ao longo do braço, desenhando o relevo do músculo. Assimetria natural: ombros em alturas levemente diferentes, sobrancelhas não idênticas. Catchlight nítido da janela nos dois olhos. Textura natural dos lábios com linhas finas.

## 4. Cabelo cacheado — o erro é a uniformidade

Sem instrução, saem anéis perfeitos e idênticos, que é a assinatura da IA. O que resolve:

> Fios individuais visíveis, cachos de tamanhos desiguais, frizz real com fios rebeldes soltos escapando ao redor da cabeça e pegando o sol de lado como um contorno brilhante, alguns fios grudados na têmpora pelo suor.

O contorno brilhante do frizz contra a luz raspante é o detalhe que mais vende a foto.

## 5. Câmera

`50mm, f/5.6` para corpo inteiro com a sala legível. **Não** usar profundidade de campo rasa/bokeh quando o cenário precisa aparecer — no nosso caso o ripado, o logo e o aparelho são o ponto.

`85mm` só em retrato fechado.

---

## ⚠️ Dois conflitos com o guia da marca — a marca vence

| A internet diz | O guia Pure diz | O que fazemos |
|---|---|---|
| Use `subsurface scattering` | Cortar — é vocabulário de CG e dá cara de render 3D | **Não usar** |
| Use negative prompt ("no plastic skin, waxy") | Nunca escrever negativas no prompt (o Gemini piora) | **Prosa 100% positiva** + a proibição no parâmetro `negative_prompt`, separado do texto |

`negative_prompt` validado:
`pele de porcelana, pele aerografada, aparência de cera, filtro de beleza, pele lisa demais, aparência de render 3D, CGI`

---

## ✅ Resultado do primeiro teste (`fachada-modelo-cadeira-serena-v1.png`)

**Funcionou:** poros visíveis na maçã e na testa, variação de tom, linha nasolabial, linhas finas no canto do olho, rubor perto do nariz, suor no pescoço e no colo com o sol desenhando o relevo do pescoço, tendões marcados, catchlight nos olhos, assimetria real. **O cabelo saiu excelente** — cachos desiguais, fios individuais, frizz com contorno brilhante contra o sol.

**A corrigir:** a modelo saiu aparentando mais idade do que o briefing sugere (o briefing não fixou idade — vale cravar), o tom de pele veio mais claro que "marrom médio", o cabelo mais longo que "altura dos ombros", e — o mais importante — **o corpo dela tapa o logo "p" da parede**. Tipografia miúda do aparelho ainda erra ("insinity" em vez de "infinity").

---

## Fontes

- [Make AI Images Look Real: Fix Plastic Skin (2026) — Quest Studio](https://queststudio.io/blog/make-it-look-real-prompt-rules)
- [How to Fix Plastic Skin in AI Portraits — Oakgen](https://oakgen.ai/blog/fix-plastic-skin-ai-portraits)
- [Add hyper-realistic skin texture with AI — Claid](https://claid.ai/blog/article/fix-ai-skin-texture)
- [How to fix AI-generated skin to look realistic — Morphic](https://morphic.com/resources/how-to/fix-ai-generated-skin-realistic)
- [Realistic Skin Texture & Lighting in AI Portraits — Sozee](https://sozee.ai/resources/realistic-skin-texture-ai-portraits/)
- [Nano Banana Prompt Guide — Leonardo.Ai](https://leonardo.ai/news/nano-banana-prompt-guide)
- [Gemini 3 Pro Image / Nano Banana Pro — Google DeepMind](https://deepmind.google/models/gemini-image/pro/)
