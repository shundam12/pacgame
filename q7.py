# 必要に応じライブラリをインストール
# pip install pycryptodome
# pip install gmpy2


from Crypto.Util.number import long_to_bytes
import gmpy2


l_msg2 = 5551661899064132363908509758865182357480521146105392604076612717916430960884482861361367317238290344986976632536184531388072054445751666241
l_msg, _ = gmpy2.iroot(l_msg2, 2)
msg = long_to_bytes(int(l_msg))
print(msg.decode())