# my dumb solution without using the vulnerable pad function

import os,json

# 2^128 collision protection!
BLOCK_SIZE = 32

# Nothing up my sleeve numbers (ref: Dual_EC_DRBG P-256 coordinates)
W = [0x6b17d1f2, 0xe12c4247, 0xf8bce6e5, 0x63a440f2, 0x77037d81, 0x2deb33a0, 0xf4a13945, 0xd898c296]
X = [0x4fe342e2, 0xfe1a7f9b, 0x8ee7eb4a, 0x7c0f9e16, 0x2bce3357, 0x6b315ece, 0xcbb64068, 0x37bf51f5]
Y = [0xc97445f4, 0x5cdef9f0, 0xd3e05e1e, 0x585fc297, 0x235b82b5, 0xbe8ff3ef, 0xca67c598, 0x52018192]
Z = [0xb28ef557, 0xba31dfcb, 0xdd21ac46, 0xe2a91e3c, 0x304f44cb, 0x87058ada, 0x2cb81515, 0x1e610046]

# Lets work with bytes instead!
W_bytes = b''.join([x.to_bytes(4,'big') for x in W])
X_bytes = b''.join([x.to_bytes(4,'big') for x in X])
Y_bytes = b''.join([x.to_bytes(4,'big') for x in Y])
Z_bytes = b''.join([x.to_bytes(4,'big') for x in Z])
print(Z_bytes.hex())

def pad(data):
    padding_len = (BLOCK_SIZE - len(data)) % BLOCK_SIZE
    return data + bytes([padding_len]*padding_len)

def blocks(data):
    return [data[i:(i+BLOCK_SIZE)] for i in range(0,len(data),BLOCK_SIZE)]

def xor(a,b):
    return bytes([x^y for x,y in zip(a,b)])

def rotate_left(data, x):
    x = x % BLOCK_SIZE
    return data[x:] + data[:x]

def rotate_right(data, x):
    x = x % BLOCK_SIZE
    return  data[-x:] + data[:-x]

def scramble_block(block):
    for _ in range(40):
        #print("inline = ",block)
        block = xor(W_bytes, block)
        #print(" XOR W = ", block)
        block = rotate_left(block, 6)
        #print(" rotate_left = ", block)
        block = xor(X_bytes, block)
        #print(" XOR X = ", block)
        block = rotate_right(block, 17)
        #print(" rotate_right = ", block)
    return block

def cryptohash(msg):
    initial_state = xor(Y_bytes, Z_bytes)
    #print("init = ",initial_state.hex())
    msg_padded = pad(msg)
    #print(" msg_padded = ", msg_padded.hex())
    msg_blocks = blocks(msg_padded)
    #print(" msg_blocks = ", msg_blocks)
    for i,b in enumerate(msg_blocks):
        mix_in = scramble_block(b)
        print(" mix_in = ", mix_in)

        for _ in range(i):
            mix_in = rotate_right(mix_in, i+11)
            mix_in = xor(mix_in, X_bytes)
            mix_in = rotate_left(mix_in, i+6)
        initial_state = xor(initial_state,mix_in)
    return initial_state.hex()



def cryptohash(msg):
    # hash with one block is invulnerable
    # if block one: hash = mix_in1 ^ initial_state
    # if block two: hash = mix_in1 ^ initial_state ^ f(mix_in2)
    initial_state = xor(Y_bytes, Z_bytes)
    msg_padded = pad(msg)
    msg_blocks = blocks(msg_padded)
    for i,b in enumerate(msg_blocks):
        mix_in = scramble_block(b)
        for _ in range(i):             # If there is only one block, then there will be no loop, because i = 0. Looks vulnerable
            mix_in = rotate_right(mix_in, i+11)
            mix_in = xor(mix_in, X_bytes)
            mix_in = rotate_left(mix_in, i+6)
        initial_state = xor(initial_state,mix_in)
    return initial_state.hex()


def reverse_scramble_block(block):
    for _ in range(40):
        block = rotate_left(block, 17)
        block = xor(X_bytes, block)
        block = rotate_right(block, 6)
        block = xor(W_bytes, block)
    return block

def solve():
    initial_state = xor(Y_bytes, Z_bytes)
    b = os.urandom(32)
    scr = scramble_block(b)

    i=1
    mix_in2 = os.urandom(32)
    mix_in1 = xor(scr, mix_in2)

    mix_in2 = rotate_right(mix_in2, i+6)
    mix_in2 = xor(mix_in2, X_bytes)
    mix_in2 = rotate_left(mix_in2, i+11)

    b2 = reverse_scramble_block(mix_in1)
    b3 = reverse_scramble_block(mix_in2)

    assert cryptohash(b2+b3) == cryptohash(b)
    return json.dumps({"m1":(b2+b3).hex(), "m2":b.hex()})

print(solve())