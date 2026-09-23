"""
Aplica o logotipo oficial da Pure Pilates por cima do que o modelo gerou.

Por que existe: o gerador erra tipografia miuda de forma consistente — sai
"Pure" com P maiusculo em vez de "pure", e a figurinha da pessoa ajoelhada
vira um borrao. Quatro rodadas de prompt nao resolveram; esta e a correcao
confiavel.

Como usar:
  1. Recorte a area do logo na imagem gerada e olhe, para medir a caixa:
     ffmpeg -i gerada.png -vf "crop=700:350:2400:2580,scale=iw*2:ih*2" medir.png
  2. Ajuste BASE, OUT e as coordenadas X0/Y0/X1/Y1 abaixo.
  3. Ajuste SY0/SY1 para uma faixa de madeira limpa da MESMA tabua, usada
     para apagar o logo errado.
  4. python aplicar-logo-real.py

Requer Pillow. O PNG do logo tem alfa sujo (fundo branco opaco), por isso a
mascara sai da luminancia e nao do canal alfa.
"""

from PIL import Image, ImageChops, ImageFilter

BASE = "/Users/renatalouzada/Desktop/VS Code/Editor html/fachada/geradas/fachada-cadillac-suspensao-v20.png"
LOGO = "/Users/renatalouzada/Desktop/VS Code/Editor html/marca/logo-pure-pilates.png"
OUT  = "/Users/renatalouzada/Desktop/VS Code/Editor html/fachada/geradas/fachada-cadillac-suspensao-v20-logo-real.png"

base = Image.open(BASE).convert("RGB")
X0, Y0, X1, Y1 = 2580, 2694, 2827, 2790
W, H = X1 - X0, Y1 - Y0
PAD = 18
ex0, ey0, ex1, ey1 = X0 - PAD, Y0 - PAD, X1 + PAD, Y1 + PAD
ew, eh = ex1 - ex0, ey1 - ey0

# apagar o logo gerado com madeira limpa de baixo, ladrilhada e espelhada
SY0, SY1 = 2800, 2845
strip = base.crop((ex0, SY0, ex1, SY1))
patch = Image.new("RGB", (ew, eh)); y = 0; flip = False
while y < eh:
    patch.paste(strip.transpose(Image.FLIP_TOP_BOTTOM) if flip else strip, (0, y))
    y += strip.height; flip = not flip
patch = patch.filter(ImageFilter.GaussianBlur(0.4))
feather = Image.new("L", (ew, eh), 0)
feather.paste(255, (PAD, PAD, ew - PAD, eh - PAD))
feather = feather.filter(ImageFilter.GaussianBlur(PAD * 0.9))
base.paste(patch, (ex0, ey0), feather)

# arte oficial, mascara por luminancia sobre branco
raw = Image.open(LOGO).convert("RGBA")
flat = Image.alpha_composite(Image.new("RGBA", raw.size, (255,)*4), raw).convert("RGB")
mask = flat.convert("L").point(lambda v: 255 if v < 200 else 0)
mask = mask.crop(mask.getbbox())

ar = mask.width / mask.height
tw, th = W, round(W / ar)
if th > H: th, tw = H, round(H * ar)
mask = mask.resize((tw, th), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.35))
px, py = X0 + (W - tw) // 2, Y0 + (H - th) // 2

region = base.crop((px, py, px + tw, py + th))
dark = ImageChops.multiply(region, Image.new("RGB", region.size, (40, 33, 31)))
region.paste(dark, (0, 0), mask)
base.paste(region, (px, py))
base.save(OUT)
print("ok", px, py, tw, th)
