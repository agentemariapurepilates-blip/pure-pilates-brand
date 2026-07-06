# Proposta de novo site — Pure Pilates

Landing page de proposta para o redesign de **purepilates.com.br**, construída sobre o sistema visual aprovado da marca (vermelho `#C12030`, laranja `#DB9828`, creme `#F6EFE2`, formas-assinatura e Montserrat). Estrutura inspirada na do Wellhub, adaptada à Pure.

- Arquivo: [`pure-pilates-lp.html`](pure-pilates-lp.html) — **documento único e autossuficiente** (fontes Montserrat, logo e símbolo P todos embutidos em base64).
- Só tema claro. Seções: hero, como funciona, app (vídeo), benefícios, Studio Pilates (aparelhos), Pure Pass, depoimentos, unidades (casca — puxa a localização do aluno), franquia, CTA e rodapé.

## Como visualizar

Abra num servidor local (recomendado — assim a Montserrat carrega e o **vídeo do app** dá play):

```bash
cd site
python3 -m http.server 8137
# abra http://127.0.0.1:8137/pure-pilates-lp.html
```

> Abrir por **duplo-clique** (`file://`) funciona, mas o vídeo do YouTube retorna "Erro 153" (o YouTube exige origem `http`). No site hospedado de verdade o vídeo funciona normalmente.

## Observações

- Valores (ex.: R$199) e endereços das unidades são **ilustrativos** — confirmar antes de publicar.
- Assets da marca originais em [`../marca/`](../marca/).
