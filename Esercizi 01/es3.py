
# # Primo modo
# i = 1
# mcd = 1
# while i <= m and i <= n:
#     if m % i == 0 and n % i == 0:
#         mcd = i
#     i += 1

# # Secondo modo
# i = min(m, n)
# mcd = 1
# while i > 1:
#     if m % i == 0 and n % i == 0:
#         mcd = i
#         break
#     i -= 1
def gcd(m,n):
    mcd = 1
    for i in range(min(m, n), 0, -1):
        if m % i == 0 and n % i == 0:
            mcd = i
            break
    return mcd


# Terzo modo
# (a,b) -> (b, a % b)
# (15,6) -> (6, 3) -> (3, 0)
# (6, 15) -> (15, 6)
# a = m
# b = n
# while b > 0:
#     a, b = b, a % b
# mcd = a

print('Dammi due numeri interi m e n')
m = int(input('m: '))  # 594437
n = int(input('n: '))  # 588253
mcd = gcd(m,n)

print('Il M.C.D. tra ', m, 'e', n, 'è', mcd)
