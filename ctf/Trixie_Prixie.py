import numpy as np
import base64
import sympy

def is_invertible_mod(matrix, mod):
    sym_mat = sympy.Matrix(matrix.tolist())
    try:
        _ = sym_mat.inv_mod(mod)
        return True
    except:
        return False

def generate_valid_matrix(mod=256, size=4):
    while True:
        mat = np.random.randint(0, 256, size=(size, size))
        if is_invertible_mod(mat, mod) and is_invertible_mod(np.rot90(mat), mod):
            return mat

def encrypt_message(message, key, block_size=4):
    message_bytes = [ord(c) for c in message]
    while len(message_bytes) % block_size != 0:
        message_bytes.append(0)
    encrypted = []
    for i in range(0, len(message_bytes), block_size):
        block = np.array(message_bytes[i:i+block_size])
        enc_bloa
