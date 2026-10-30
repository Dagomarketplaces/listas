# -*- coding: utf-8 -*-
# Gera as páginas de redirecionamento dos QR Codes.
# Os destinos ficam em destinos.csv (caminho;titulo;destino;arquivo_no_drive).
# Para mudar o destino de um QR Code: troque o link no CSV, rode este script e publique.
import csv
import os

BASE = 'https://dagomarketplaces.github.io/listas'
aqui = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(aqui, 'destinos.csv'), encoding='utf-8') as f:
    DESTINOS = {r['caminho']: (r['titulo'], r['destino']) for r in csv.DictReader(f, delimiter=';')}

MODELO = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="refresh" content="0; url={url}">
<title>{titulo} | Dagostino</title>
<script>window.location.replace({url_js});</script>
<style>
  body{{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
       font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#16365C;color:#fff;text-align:center;padding:16px}}
  a{{display:inline-block;margin-top:14px;background:#E07500;color:#fff;padding:12px 20px;border-radius:10px;
     text-decoration:none;font-weight:700}}
</style>
</head>
<body>
  <div>
    <p>Abrindo a <b>{titulo}</b>…</p>
    <a href="{url}">Toque aqui se não abrir sozinho</a>
  </div>
</body>
</html>
'''

for caminho, (titulo, url) in DESTINOS.items():
    pasta = os.path.join(aqui, *caminho.split('/'))
    os.makedirs(pasta, exist_ok=True)
    with open(os.path.join(pasta, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(MODELO.format(titulo=titulo, url=url, url_js='"' + url + '"'))
    print(f'{BASE}/{caminho}/  ->  {url}')
