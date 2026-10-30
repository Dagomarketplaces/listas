# -*- coding: utf-8 -*-
# Gera as páginas de redirecionamento dos QR Codes.
# Para mudar o destino de um QR Code: troque o link em DESTINOS, rode este script e publique.
import os

BASE = 'https://dagomarketplaces.github.io/listas'

# caminho do QR Code -> (título, link de destino)
DESTINOS = {
    'invictus/nivel-2-premium': (
        'Lista Nível 2 – Colégio Invictus – Premium',
        # TESTE DRIVE - VERSAO 1.pdf (pasta de testes no Google Drive)
        'https://drive.google.com/file/d/1RJkP8qg3PA5hj9gZkjpIWC2JIL8pAhO9/view'),
    'invictus/nivel-2-economica': (
        'Lista Nível 2 – Colégio Invictus – Econômica',
        BASE + '/testes/orcamento-teste-nivel-2-economica.pdf'),
}

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

aqui = os.path.dirname(os.path.abspath(__file__))
for caminho, (titulo, url) in DESTINOS.items():
    pasta = os.path.join(aqui, *caminho.split('/'))
    os.makedirs(pasta, exist_ok=True)
    with open(os.path.join(pasta, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(MODELO.format(titulo=titulo, url=url, url_js='"' + url + '"'))
    print(f'{BASE}/{caminho}/  ->  {url}')
