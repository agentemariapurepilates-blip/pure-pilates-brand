# Proposta de novo site — Pure Pilates

Landing page de proposta para o redesign de **purepilates.com.br**, construída sobre o sistema visual aprovado da marca (vermelho `#C12030`, laranja `#DB9828`, creme `#F6EFE2`, formas-assinatura e Montserrat). Estrutura inspirada na do Wellhub, adaptada à Pure.

- Arquivo: [`pure-pilates-lp.html`](pure-pilates-lp.html) — **documento único e autossuficiente** (fontes Montserrat, logo e símbolo P todos embutidos em base64). Sem build, sem dependências: CSS e JS puros.
- Só tema claro. Ordem das seções: hero, como funciona, **app**, **unidades**, benefícios, Studio Pilates (aparelhos), Pure Pass, depoimentos, franquia, CTA e rodapé.

## Seção do app

- O vídeo do YouTube toca dentro de um **celular renderizado em 3D** (moldura, espessura, botões laterais, reflexo de vidro e sombra de contato — tudo CSS).
- O aparelho fica **deitado** de propósito: o vídeo é 16:9 e a tela tem 16:9 exato, então ele preenche sem corte. Se um dia existir um vídeo **vertical** (9:16) do app, dá para virar o celular em pé sem perder imagem.
- Ele **gira conforme a rolagem** (−26° a +13° em Y, com inclinação em X e paralaxe), via um listener de scroll com `requestAnimationFrame`.
- Abaixo do texto, um **dock de redes sociais**: o ícone cresce conforme o mouse se aproxima, com física de mola (48 → 84 px). Reimplementação em JS puro do padrão do dock do macOS.
- Ícones alternam vermelho (símbolo branco) e bege `#E2D0B4` (símbolo vermelho). O símbolo branco sobre o bege foi testado e **reprovado**: contraste de 1,51:1, contra o mínimo de 3:1 da WCAG.

## Seção de unidades

- Dados **reais**, puxados da API que o site oficial usa: `POST /Unidades/ObterUnidades?pagina=1&latitude=…&longitude=…` (retorna `distance`, `img`, `address`, `whatsappLink`, `url`).
- Fotos reais dos estúdios em [`assets/unidades/`](assets/unidades/), baixadas de `purepilates.com.br/Content/img/unidades/`.
- Cada card: foto, distância em km, endereço, telefone, WhatsApp e os botões *Agende uma aula experimental* e *Mais detalhes* (apontam para as páginas reais de cada unidade).
- **A rede não publica telefone fixo por unidade** — conferi 120 unidades na API e o campo `phone` vem vazio em todas. O número exibido é o do WhatsApp do estúdio, usado nas duas ações.
- As distâncias estão **fixas no HTML** (calculadas a partir da Av. Paulista). Para virar "perto de *você*" de verdade, a página precisa pedir a geolocalização do visitante e chamar a API.

## Como visualizar

Abra num servidor local (recomendado — assim a Montserrat carrega e o **vídeo do app** dá play):

```bash
cd site
python3 -m http.server 8137
# abra http://127.0.0.1:8137/pure-pilates-lp.html
```

> Abrir por **duplo-clique** (`file://`) funciona, mas o vídeo do YouTube retorna "Erro 153" (o YouTube exige origem `http`). No site hospedado de verdade o vídeo funciona normalmente.

## Observações

- Os endereços e fotos das unidades agora são **reais** (vindos da API oficial); os valores do Pure Pass seguem a confirmar antes de publicar.
- Links das redes sociais foram tirados do rodapé de purepilates.com.br — **confirmar com o marketing**. O TikTok (`@purepilatesbr`) existe e ficou de fora do dock.
- Assets da marca originais em [`../marca/`](../marca/).
