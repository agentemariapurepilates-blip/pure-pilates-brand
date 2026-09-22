# Fachada — Ensaio Fotográfico

Ensaio construído **a partir do cenário real** enviado pela Maria. As variações mudam luz, ângulo e enquadramento — **nunca** o cenário, os aparelhos ou o logotipo.

## 🔒 A regra do ensaio

> Os aparelhos precisam ser **exatamente os mesmos**: mesmo modelo, mesmas cores, mesmo estofado, **mesmo logotipo na mesma posição**.

Isso não se resolve descrevendo no prompt. Resolve-se **mandando referência de tudo** e rodando no tier certo.

## 📁 Estrutura

| Pasta | O que vai aqui |
|---|---|
| [referencias/cenario/](referencias/cenario/) | Fotos do espaço real — 2 a 3 ângulos |
| [referencias/aparelhos/](referencias/aparelhos/) | Cada aparelho: **foto inteira + close do logo** |
| [referencias/logo/](referencias/logo/) | Close do logo aplicado (posição exata na peça) |
| [prompts/](prompts/) | Prompt de cada cena, com modelo, tier e seed |
| [geradas/](geradas/) | Saídas brutas |
| [aprovadas/](aprovadas/) | Seleção final, já tratada |

**Padrão de nome:** `fachada-<cena>-<versao>.png` — ex.: `fachada-diagonal-manha-v3.png`

## 📥 O que subir (e por quê)

O Nano Banana Pro aceita **até 14 referências**, cada uma em resolução cheia.

| # | Arquivo | Por que é obrigatório |
|---|---|---|
| 1–3 | Cenário, 2–3 ângulos | Trava parede, piso, janela e proporção do espaço |
| 4+ | **Cada aparelho inteiro** | Carrega silhueta, estrutura, cor e estofado |
| 4+ | **Close do logo em cada aparelho** | Sem o close, o logo vira mancha no downsampling |

### ❌ Nunca juntar referências numa colagem

Aprendizado validado (ensaio Pelourinho, jul/2026): juntar duas peças numa imagem lado a lado fez cada uma ocupar metade do quadro e **destruiu o logo pequeno**. Resolução é o recurso escasso — cada referência vai inteira, num arquivo só dela.

### ⚙️ Rota técnica obrigatória

| Rota | Logo |
|---|---|
| Higgsfield → `nano_banana_pro` | ❌ vira mancha (roda o `nano_banana_2` por baixo) |
| **MCP `nanobanana` → `model_tier: "pro"`** | ✅ nítido e legível |

Peça com logo, marca ou texto **sempre** pelo MCP `nanobanana` no tier `pro`. Com `enable_grounding: true` e `resolution: "4k"`.

## 🎬 As variações

Definidas de verdade só depois de ver o cenário. O eixo é sempre **o mesmo espaço, os mesmos aparelhos** — muda:

- **Luz** — meio da manhã pela janela · fim de tarde raspante · noturna com o logo aceso
- **Ângulo** — frontal · diagonal 3/4 · baixo valorizando o pé-direito · detalhe do aparelho
- **Distância** — plano geral do espaço · plano médio com um aparelho · close de textura
- **Formato** — 16:9 (site/e-mail) e 9:16 (story) da mesma cena
- **Ocupação** — vazio (institucional) · com aluna em movimento

## 🎨 Direção de arte

- **Cores:** vermelho Pure `#C12030` como único acento · creme, off-white, madeira clara · cinza escuro `#231F20`.
- **Luz-assinatura:** sol direcional quente **de lado**, forte o bastante pra desenhar sombra legível. Sempre pedir a luz **e onde a sombra cai** — sol sem sombra é o que denuncia IA.
- **Acabamento:** editorial polido, alta chave, cor quente e suave, grão mínimo. Nada de torto, flash ou borrão — isso destrói a marca.
- **Composição:** sujeito de um lado, espaço negativo do outro pra copy. Câmera na altura do peito.

## ✅ Checklist antes de aprovar

- [ ] Aparelho é **o mesmo** — silhueta, cor, estofado
- [ ] **Logo na mesma posição** e legível em miniatura (reduza a 20% e leia)
- [ ] Vermelho batendo com `#C12030` (sem virar laranja ou rosa)
- [ ] Sombra coerente com a fonte de luz declarada
- [ ] Verticais retas, horizonte nivelado
- [ ] Versão 16:9 **e** 9:16 da mesma cena
- [ ] Área livre para headline
- [ ] Renomeado no padrão e movido para `aprovadas/`

> ℹ️ Imagens do Gemini carregam **SynthID**, marca d'água invisível de IA. Não impede o uso, mas é detectável — vale saber em peça de marca.
