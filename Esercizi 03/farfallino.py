def farfallino_encode_v1(s: str) -> str:
    return s.replace("a", "afa").replace("e", "efe").replace("i", "ifi").replace("o", "ofo").replace("u","ufu").replace("y","yfy")


def farfallino_encode_v2(s: str) -> str:
    
    # for i in range(len(s)):
    #     s[i]

    out = ""
    for c in s:
        if c == "a":
            out += "afa"
        elif c == "e":
            out += "efe"
        elif c == "i":
            out += "ifi"
        elif c == "o":
            out += "ofo"
        elif c == "u":
            out += "ufu"
        else:
            out += c

    return out


def farfallino_encode_v3(s: str) -> str:
    
    # for i in range(len(s)):
    #     s[i]

    out = ""
    for c in s:
        match c:
            case "a":
                out += "afa"
            case "e":
                out += "efe"
            case "i":
                out += "ifi"
            case "o":
                out += "ofo"
            case "u":
                out += "ufu"
            case _:
                out += c

    return out


def farfallino_encode_v4(s: str) -> str:
    
    # for c in ["a", "e", "i", "o", "u"]:
    #     s = s.replace(c, c + "f" + c)

    s = s.lower()
    for c in "aeiou":
        s = s.replace(c, c + "f" + c)

    return s











# def farfallino_encode_v2(s: str) -> str:
#     replace_dict = {
#         "a": "afa",
#         "e": "efe",
#         "i": "ifi",
#         "o": "ofo",
#         "u": "ufu",
#         "y": "yfy",
#     }
#     encoded_str = s
#     for k, v in replace_dict.items():
#         encoded_str = encoded_str.replace(k, v)
#     return encoded_str


if __name__ == "__main__":
    s = "ciaociao"
    print(farfallino_encode_v1(s))
    print(farfallino_encode_v2(s))
    print(farfallino_encode_v3(s))
    print(farfallino_encode_v4(s))


