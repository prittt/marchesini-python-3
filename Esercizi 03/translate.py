def translate_v1(s: str, from_lst: str, to_lst: str) -> str:
    transtable = str.maketrans(from_lst, to_lst)
    return s.translate(transtable)

def translate_v2(s: str, from_lst: str, to_lst: str) -> str:
    if len(from_lst) != len(to_lst):
        return s
    
    # for old, new in zip(from_lst, to_lst):
    #     s.replace(old, new)

    for i in range(len(from_lst)):
        s = s.replace(from_lst[i], to_lst[i])
    return s


if __name__ == "__main__":
    print(translate_v1("ciao", "abdc", "wxzy"))
    print(translate_v2("ciao", "abdc", "wxzy"))