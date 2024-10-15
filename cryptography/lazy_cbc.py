# chosen cipher text attack
ct = "AA"*16 + "00"*16 + "AA"*16
print(ct)

#251a2330bf20258def017839b450c9251f7bb3fc8a067fac30e1071cf9295fbec9e4677db72944e8fd57fcf5d7ea9de3
pt = "251a2330bf20258def017839b450c9251f7bb3fc8a067fac30e1071cf9295fbec9e4677db72944e8fd57fcf5d7ea9de3"
def split_text_by_len(text, lenght):
    return [ text[i:i+lenght] for i in range(0, len(text), lenght) ]

a = split_text_by_len(pt,32)
print(a)
# then xor block 1 and 3