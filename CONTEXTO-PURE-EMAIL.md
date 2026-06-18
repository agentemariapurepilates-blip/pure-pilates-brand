# Contexto — E-mails HTML Pure Pilates (handoff de sessão)

> Documento de continuidade. Salvo em **15/06/2026**. Use isto pra retomar de onde paramos ao reabrir o Claude Code.

## O que estamos fazendo
Criando e-mails HTML para a Pure Pilates, começando pela unidade de negócios **estúdios**.
Primeiro e-mail: **"Indique um amigo / Indique Pilates"** (programa de indicação) → arquivo [indique-um-amigo.html](indique-um-amigo.html).

## Fluxo de trabalho estabelecido
- Sempre puxar os guias da marca via MCP `pure-pilates`: ferramentas **`layout`** e **`copy`** (e `ti`) ANTES de produzir.
- Salvar aprendizados com `salvar_layout` / `salvar_copy` / `salvar_ti` (requer login gh da Maria).

## Decisões finais de design (e-mail estúdios)
| Item | Valor | Por quê |
|---|---|---|
| Fundo | creme claro `#F6EFE2` sólido | tint claro do laranja; é o tom dos posts de estúdio; leve/sutil |
| Estrutura | **SEM card branco** — conteúdo direto no creme | mais imersivo, colado nos posts de estúdio |
| Vermelho | `#C12030` | vermelho oficial da marca (NÃO `#c10230`, que era erro do template original) |
| Laranja | `#DB9828` | substituiu os dourados `#c9a96e`/`#d4a853` (dourado é PROIBIDO na paleta) |
| Texto | `#231F20` | cinza escuro Pure |
| Fonte | `'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif` | Montserrat só renderiza em Apple Mail/iOS; Gmail/Outlook caem no Arial |
| Forma dos cards | `border-radius:70px 70px 0 70px` | assinatura Pure = 3 cantos redondos + 1 canto reto |
| Forma do hero | `border-radius:140px 140px 140px 0` | idem (canto reto embaixo-esquerda) |

## Regras técnicas de e-mail (aprendidas nesta sessão)
- **NÃO renderizam em Gmail/Outlook**: web fonts (Montserrat), SVG inline, `radial-gradient`, `background-image` com gradiente. → sempre usar fallback/cor sólida.
- **Renderiza em 100% dos clientes**: cor sólida (`background-color`). `border-radius` funciona em Gmail/Apple; Outlook ignora e mostra cantos quadrados (degrada, não quebra).
- Layout 100% em `<table role="presentation">` + estilos inline. Repetir `font-family` em cada `h1/h2/p` (Outlook não herda do body).
- Montserrat fica como progressive enhancement via `<link>` Google Fonts no `<head>`.

## Salvo no MCP (guia `layout`)
- **`padrao-de-email-html`** — padrão geral de e-mail HTML (estrutura, tokens, fonte).
- **`formas-permitidas`** — catálogo de formas (pétala, círculo, pílula, arco, etc.) + regra da forma-assinatura (3 redondos + 1 reto, raio generoso ~70px).
- **`modelo-email-estudios`** — este modelo, específico da unidade estúdios.

## Arquivos locais (pasta "Editor html")
- `indique-um-amigo.html` — e-mail concreto (exemplo final, aprovado).
- `modelo-email-estudios.html` — modelo reutilizável (com placeholders) pra unidade estúdios.
- `CONTEXTO-PURE-EMAIL.md` — este arquivo.

## Pendências / próximos passos
1. **Enviar e-mail de teste via Gmail** — a integração Gmail não tinha conectado nesta sessão; você reconectou e vai reabrir o Claude Code pras ferramentas carregarem. Ao reabrir, é só pedir *"manda o e-mail de teste"* que eu disparo pra **agentemaria.purepilates@gmail.com**.
2. **Testar renderização** — PutsMail (putsmail.com) pra enviar teste real; Litmus / Email on Acid pra preview em 90+ clientes; can-i-email.com pra checar suporte de CSS; mail-tester.com pra nota de spam.
3. Avaliar se vamos criar modelos pra outras unidades de negócio além de estúdios.
