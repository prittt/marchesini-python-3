import statistics

def media_v1(a : list):
    sum = 0
    for i in range(len(a)):
        sum +=a[i]
    return sum/len(a)


def media_v2(a):
    return sum(a)/len(a)


def media_v3(a):
    return statistics.mean(a)


def media_v4(a : list):
    sum = 0
    for e in a:
        sum += e
    return sum/len(a)


def varianza_v1(a : list):
    m = media_v3(a)
    var = 0
    for i in range(len(a)):
        var += (m - a[i])**2
    return var/len(a)


def varianza_v2(a : list):
    m = media_v3(a)
    var = 0
    for e in a:
        var += (m - e)**2
    return var/len(a)

def varianza_v3(a : list):
    return statistics.pvariance(a)

a = [10, 10, 11, 11, 12, 12]
print(media_v1(a))
print(media_v2(a))
print(media_v3(a))
print(media_v4(a))
print(varianza_v1(a))
print(varianza_v2(a))
print(varianza_v3(a))