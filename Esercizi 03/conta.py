def conta_parole_v1(s: str) -> int:
    return len(s.split())

def conta_parole_v2(s: str) -> int:
    cnt = 0
    in_word = False
    for c in s:
        if not c.isspace() and not in_word:
            in_word = True
            cnt += 1
        if c.isspace(): 
            in_word = False
    return cnt

print(conta_parole_v1("  Questa e' una stringa lunga 45 caratteri.  "))
print(conta_parole_v1("1 2 3 a b c"))
print(conta_parole_v1("! @?$ ciao,prova"))

print(conta_parole_v2("  Questa e' una stringa lunga 45 caratteri.  "))
print(conta_parole_v2("1 2 3 a b c"))
print(conta_parole_v2("! @?$ ciao,prova"))


