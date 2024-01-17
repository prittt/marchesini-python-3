import re

def rimuovi_singoli_spazi_v1(s: str) -> str:
    result = ""
    for i in range(len(s)):
        if s[i] != " " or (i > 0 and s[i-1] == " ") or (i < len(s)-1 and s[i+1] == " "):
            result += s[i]
    return result


def rimuovi_singoli_spazi_v2(s: str) -> str:
    return re.sub(r'(?<!\s)\s(?!\s)', "", s)


def rimuovi_singoli_spazi_v3(s: str) -> str:
    return re.sub(r'(\b|^)\s(\b|$)', "", s)


old_print = print

def print(*args):
    # old_print("|", *args, "|", sep="", **kargs)
    old_print("|", end="")
    old_print(*args, end = "")
    old_print("|")

# list = [1, 2, 3]
# s = set((1, 2, 3, 2, 1))
# a = list(s)
# print(s, a, list)

print(rimuovi_singoli_spazi_v1(" a b c "))
print(rimuovi_singoli_spazi_v1("  a  b  c  "))
print(rimuovi_singoli_spazi_v1("  abc   def ghi   jkl    mno pqr  s "))

print(rimuovi_singoli_spazi_v2(" a b c "))
print(rimuovi_singoli_spazi_v2("  a  b  c  "))
print(rimuovi_singoli_spazi_v2("  abc   def ghi   jkl    mno pqr  s "))

print(rimuovi_singoli_spazi_v3(" a b c "))
print(rimuovi_singoli_spazi_v3("  a  b  c  "))
print(rimuovi_singoli_spazi_v3("  abc   def ghi   jkl    mno pqr  s "))
