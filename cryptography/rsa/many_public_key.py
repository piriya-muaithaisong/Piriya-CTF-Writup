from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

os.chdir("/home/kali/Downloads/keys_and_messages")
with open('21.pem') as f:
    key = RSA.importKey(f.read())
keys = []

for file in os.listdir():
    if file.endswith(".pem") and file != '21.pem': 
        keys.append(file)

print(keys)
n = key.n
e = key.e
p = 1
for i in keys:
    with open(i) as f:
        compare_key = RSA.importKey(f.read())
    if GCD(compare_key.n,n) != 1 :
        print("Found :",i)
        p = GCD(compare_key.n,n)
        print("P = ",p)
        break

q = n//p
assert p*q == n

ct = "c62d91677825632cb8ac9d2fbee7490fca70b3f067bd8d811fa446a21001de7943cacafc429b2513d3f20c3224d212ca2937a4a4ea10792a1c498b791e978e4b050b525576bc68421e40d9f420c0b8a07778daf69edf2095bf48222896bb2d6581288ce7a2e7aec15a88a440ff1a1e48beb56f68b4f860d1f64a6ec8cafed90846b7d893bc482df69c8478d5a0d6fc2d043cdd97178740a9eb59d2576b5136200c8ea77e648c88e6c5104ca5d0c6add2fc2c8569ce909f8461e7fa3d901fe67eaeff656399d4751fedba9973e246427e0c7a217f5bdc3edcb5033f17b5ef53419e340355a809eb46f48f538e880abd6f72212b02d3dbf2c4f633a503e648d1a835c4574b23e329e1c51078ea7cbb7533e771899498d4a5760bc0799b7e046f268f098fe0b57de47cd70ccf01ad3c9daec5027f306141bfe7a6c0bd29ee6caf94c7433c25e34ee974005e2360337cb6b3cec5eaf5d31d19f01435f4cdcaa455a18e78dee078395b8ad14b9c3a0d817dc1e3109c7b8af35ab3a5950bf47d5e621f9373ef421540052aac307ecea91f9c29c14bfd81b41d4c5a9b34a8ec2fa1ae06c3d881f39286c3d8dbb1849602fecc27bb135f7dd443e2598d247d1182d350b04be1ac0a734cb0e852a36902d88066ac375a35e279b126e413a97aaa35a0ba933f7b8d574c298332ce428c181464b240709a414af1b77103441b6ccfd0790eccea5926844054903c83f4cb415d600a6b7bc771c9e7a86394a2b427ebe8edec08b8095f561827716898e11caf6f0fe562af8a69f7b6469f0e86bdcc32f429f10821c763b34307efc5b2ae7fd524a07e5d0b762c096f025a3f240fb7bd3554582dcce32c175867d93970b0422e17870ec58f2a305545a3d284b3abb2d21a45ad8fd5faed0dc66312a5aa2f994606a51cd6682acd48ea3fb883f0611e1e5c2fb4047b5c80815ba5d3bcfefaf121bfde4d5c91ee27bb899ef0d29fa5c6dc4223ac2bfcff0217d08579a13e9b02dc97aa2622df62eeaaa38bb3bd087cdd209f03e8926a951e90eaa0f678a252a067ac66402a4c85865931689ed3b33f9f6de0c499f140ef508dfba6007a607a271dcbec18a61f7488bba34d143f93bc259310ffbf23f3391734d8d8811a4be8abf6382e55c2ccbfd80b1559d907fd8d46e0431cdbcd8fdb06d57973437f7b8ff5efc5a53c80d552e8fe622971f7376eeea35f4df9b32ada93e531a52b63ba13f6b7bf61ab337d6d93feb0e8c8a309dfa7e5f50e8cf9655b73ae64822b50db5312f35f4718b0668305065ea283ddf8f0a4e8f486ee9d119ebc584be1837b3d959a25ace208ffac2fb703390a72d3027b64fdd1955b513c0403f09232efa1794a277e0be3f4f9f3a6fd23c6e52101e723cef5db7a2a18a107cd522379adb40c5ed36b26cdf53a1000d7d576f1157b42aac3d3ee011275"
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

private_key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(private_key)
decrypted = cipher.decrypt(bytes.fromhex(ct))

#pt = pow(ct, d, n)
#decrypted = long_to_bytes(pt)
print(decrypted)