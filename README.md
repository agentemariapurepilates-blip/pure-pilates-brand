# Pure Pilates — Templates de E-mail HTML

Biblioteca de e-mails marketing/institucionais em HTML da **Pure Pilates**, alinhada aos guias oficiais da marca (cores, tipografia e formas). Todos os templates são *email-safe*: layout em tabelas, estilos inline, `bgcolor` nos blocos coloridos (o Gmail remove `background-color` do CSS) e formas via `border-radius` + fonte web-safe com Montserrat como reforço.

## 🎨 Tokens da marca

| Token | HEX | Uso |
|---|---|---|
| Vermelho Pure | `#C12030` | Cor principal — hero, headings, CTAs, selos |
| Laranja | `#DB9828` | Acento secundário — divisórias, prazos, badges |
| Cinza escuro Pure | `#231F20` | Corpo de texto |
| Branco | `#FFFFFF` | Superfícies / texto sobre fundo escuro |
| Fonte | `'Montserrat', Arial, 'Helvetica Neue', Helvetica, sans-serif` | Montserrat só renderiza em Apple Mail/iOS; demais clientes caem no Arial |

## 📧 Templates de e-mail — [`emails/`](emails/)

| Arquivo | Descrição |
|---|---|
| [email-atualizacao-senha-pure-pilates.html](emails/email-atualizacao-senha-pure-pilates.html) | Aviso de atualização de senha preventiva (LGPD) — formas vazadas + preenchidas |
| [atualizacao-senha.html](emails/atualizacao-senha.html) | Versão anterior do aviso de senha |
| [cupom-50-desconto.html](emails/cupom-50-desconto.html) | Cupom de 50% de desconto |
| [indique-um-amigo.html](emails/indique-um-amigo.html) | Programa Indique Pilates |
| [modelo-email-estudios.html](emails/modelo-email-estudios.html) | Modelo base da unidade Estúdios (fundo creme, sem card branco) |

## 🔶 Biblioteca de formas da marca — [`formas/`](formas/)

Formas da linguagem visual Pure (cantos arredondados + 1 canto reto, pétala, "D", banner). Cada forma em versão **cheia**, **contorno vermelho** e **contorno branco**.

| Recurso | Descrição |
|---|---|
| [formas-pure-pilates.html](formas/formas-pure-pilates.html) | Índice visual de todas as formas |
| [forma-1-banner-ponta-direita.html](formas/forma-1-banner-ponta-direita.html) | Banner + rabinho (`border-radius: 80px 140px 140px 0`) |
| [forma-2-canto-superior-esquerdo.html](formas/forma-2-canto-superior-esquerdo.html) | Canto único (`160px 0 0 0`) |
| [forma-3-folha-petala.html](formas/forma-3-folha-petala.html) | Pétala — forma assinatura (`50% 50% 0 50%`) |
| [forma-4-d-arco-direito.html](formas/forma-4-d-arco-direito.html) | "D" / meia-pílula (`0 130px 130px 0`) |
| [formas/png/](formas/png/) | PNG transparente 4× para arrastar no Canva |
| [formas/svg/](formas/svg/) | Vetor recolorível |

## 📄 Documentação — [`docs/`](docs/)

- [CONTEXTO-PURE-EMAIL.md](docs/CONTEXTO-PURE-EMAIL.md) — contexto e padrões de construção dos e-mails

## ⚙️ Cuidados técnicos (renderização)

- `bgcolor` em **todo** bloco colorido (Gmail remove `background-color` do CSS inline).
- Contornos (formas vazadas) via `border` — o Gmail mantém bordas.
- Formas com `border-radius` degradam para retângulo no Outlook desktop, sem quebrar.
- Repetir `font-family` em cada `h1`/`h2`/`p` (o Outlook não herda do `<body>`).
- Avaliar sempre pelo e-mail **recebido** na caixa de entrada, não pelo rascunho do Gmail (que achata o layout).
