"""
Verifica se a base da URL concorda com o padrão correto.

Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URL inválidas:
    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.coexistent/cambio
"""
# https://www.bytebank.com.br/cambio
import re

url = "www.bytebank.com.br/cambio"
padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")
