# Cenário base — receita validada

Ponto de partida de **toda** imagem deste ensaio. Testado em 22/09/2026.

## Chamada

`mcp__nanobanana__generate_image`

| Parâmetro | Valor |
|---|---|
| `model_tier` | `pro` ← **obrigatório**, é o que salva o logo |
| `mode` | `generate` |
| `resolution` | `4k` |
| `aspect_ratio` | `16:9` (site/e-mail) · `9:16` (story) |
| `enable_grounding` | `true` |

## Referências (nesta ordem)

1. `fachada/Cenário/Zoom_out_wide_shot_2K_20260922151400.jpeg` — o espaço
2. `marca/simbolo-p-luminoso.png` — o "p" retroiluminado com halo
3. `marca/simbolo-p-solido.png` — a letra limpa, vermelho exato

Quando entrarem os aparelhos, acrescentar **foto inteira + close do logo de cada um**, cada arquivo separado. Até 14 no total.

## Bloco do cenário (copiar sempre)

> O ambiente é idêntico ao da referência: painel de ripas verticais de madeira clara do piso ao teto ocupando o fundo, paredes laterais em cimento queimado cinza-quente com marcas de desempeno, rodapé branco fino, piso de tábuas largas de madeira clara correndo em direção à câmera, e o banco baixo de madeira encostado na base da parede da direita.

## Bloco do logo (copiar sempre — é o que segura a letra)

> O logotipo na parede é a letra "p" minúscula da Pure Pilates, exatamente como nas duas imagens de referência do símbolo: um bojo circular cheio e volumoso, com um furo perfeitamente redondo deslocado para cima e para a direita dentro do bojo, e uma haste vertical reta do lado esquerdo que desce abaixo do bojo e termina num corte reto. A forma é arredondada e larga, de letra minúscula, mais larga que alta. Vermelho vivo #C12030 em acrílico com brilho suave, retroiluminado por luz quente que vaza por trás e desenha um halo dourado nas ripas ao redor. Ele permanece na mesma posição de sempre: centralizado no painel de ripas, um pouco acima da metade da altura da parede, no mesmo tamanho.

## Bloco da luz (copiar sempre)

> Luz: o mesmo sol quente e baixo entrando pela janela à direita da câmera, projetando o retângulo nítido dos caixilhos na parede de cimento e faixas diagonais de luz atravessando as ripas de madeira. As sombras caem para a esquerda, coerentes com a janela.

## Bloco de realismo (copiar sempre)

> Realismo: poros e manchas reais no cimento queimado, veios e emendas entre as tábuas do piso, grão fino da madeira nas ripas, reflexo suave do sol na superfície vermelha do acrílico. Cor quente e suave, acabamento editorial limpo, grão mínimo.

---

## 🔬 O que o teste provou

### 1. Sem o símbolo como referência separada, o logo quebra

`teste-fidelidade-diagonal-v1.png` foi gerado **só com a foto do cenário**. O "p" minúsculo virou um **"P" maiúsculo** de haste alta e o vermelho escureceu pra bordô. Dentro de uma foto larga o logo ocupa poucos pixels, e o modelo reconstrói a letra pelo que ele "acha" que é um P.

`teste-fidelidade-diagonal-v2.png`, com `simbolo-p-luminoso.png` e `simbolo-p-solido.png` como referências 2 e 3 **mais** a descrição da letra em palavras, saiu correto.

**Regra: o close do elemento de marca entra sempre como arquivo próprio.** Vale igual para o logo dos aparelhos.

### 2. `mode: edit` derruba a resolução

| Modo | Saída |
|---|---|
| `edit` (auto, quando só há 1 referência) | 1408×768 — ignorou o `4k` |
| `generate` | 5504×3072 ✅ |

Sempre passar `mode: "generate"` explicitamente.

### 3. O modelo resiste a mudar muito de ângulo

Pedi diagonal a três quartos; veio um plano quase frontal, só um pouco mais aberto. A âncora da referência é forte — ótimo pra fidelidade, ruim pra variedade. Para ângulos realmente diferentes, descrever a **nova posição da câmera em relação ao que aparece no quadro** (o que entra, o que sai, que parede fica de frente), não só nomear o ângulo.
