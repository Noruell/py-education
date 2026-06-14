from Education.additional_projects.text_encryptor.alphabets import ALPHABETS_DICT

CHIPHER_METHODS = {1: "Цезарь", 
                   2: "Атбаш", 
                   3: "Переворот строки", 
                   4: "XOR"}

# Шифр Цезаря
def caesar(text, shift, alphabets, language):
    encoded = []
    normal = alphabets[language]['normal']
    for char in text:
        if char not in normal:
            encoded.append(char)
            continue
        old_index = normal.index(char)
        new_index = (old_index + shift) % len(normal)
        encoded.append(normal[new_index])
    return ''.join(encoded)

# Шифр Атбаш
def atbash(text, alphabets, language):
    encoded = []
    normal = alphabets[language]['normal']
    revers = alphabets[language]['revers']
    atbash_dict = dict(zip(normal, revers))
    for char in text:
        if char not in normal:
            encoded.append(char)
            continue
        new_char = atbash_dict.get(char)
        encoded.append(new_char)
    return ''.join(encoded)

# Шифр Переворот строки
def flip(text):
    return text[::-1]

# Шифр XOR
def xor_encrypt(text, key): 
    encoded = []
    key_code = ord(key)
    for char in text:
        result = ord(char) ^ key_code
        encoded.append(result)
    return encoded

def xor_decrypt(encoded, key):
    decrypted = [chr(code ^ ord(key)) for code in encoded]
    return ''.join(decrypted)


if __name__ == "__main__":
    result = caesar("привет, андрей", 3, ALPHABETS_DICT, 'русский')
    print(f"{result}\n")

    result1 = atbash("привет, андрей", ALPHABETS_DICT, 'русский')
    print(f"{result1}\n")

    result2 = flip("привет")
    print(f"{result2}\n")

    result3 = xor_encrypt("привет, Андрей", "а")
    print(f"{result3}\n")

    result4 = xor_decrypt(result3, "а")
    print(f"{result4}")
  
