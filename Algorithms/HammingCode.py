def hamming_encode(data):
    r = 1
    while 2**r < len(data) + r + 1:
        r += 1
    
    encoded_data = [0] * (len(data) + r)
    
    j = 0
    for i in range(1, len(encoded_data) + 1):
        if i & (i - 1) != 0:
            encoded_data[i - 1] = int(data[j])
            j += 1
    
    for i in range(r):
        mask = 2**i
        for j in range(1, len(encoded_data) + 1):
            if j & mask == mask:
                encoded_data[j - 1] ^= encoded_data[i]
    
    return encoded_data

def hamming_decode(encoded_data):
    r = 1
    while 2**r < len(encoded_data):
        r += 1
    
    syndrome = [0] * r
    for i in range(r):
        mask = 2**i
        for j in range(len(encoded_data)):
            if j & mask == mask:
                syndrome[i] ^= encoded_data[j]
    
    error_position = sum([2**i * bit for i, bit in enumerate(syndrome)])
    
    if error_position != 0:
        encoded_data[error_position - 1] ^= 1
    
    decoded_data = []
    j = 0
    for i in range(1, len(encoded_data) + 1):
        if i & (i - 1) != 0:
            decoded_data.append(encoded_data[i - 1])
    
    return decoded_data

data = input("Enter binary data: ")

encoded_data = hamming_encode(data)
print("Encoded:", ''.join(map(str, encoded_data)))

decoded_data = hamming_decode(encoded_data)
print("Decoded:", ''.join(map(str, decoded_data)))