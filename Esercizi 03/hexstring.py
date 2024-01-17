def hexstring2vec(s: str) -> list[int]:
    hex_list = []
    for i in range(0, 16, 2):
        if i < len(s):
            hex_str = s[i:i+2]
            hex_val = int(hex_str, 16)
        else:
            hex_val = 0
        hex_list.append(hex_val)
    return hex_list

print(hexstring2vec("12AB34CD56EF7890"))
print(hexstring2vec("12ab34cd56ef7890"))
print(hexstring2vec("35AF"))
print(hexstring2vec("0A0a0B0bcCdD"))
print(hexstring2vec(""))
