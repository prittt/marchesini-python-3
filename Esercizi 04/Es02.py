from Es01 import dict_invert

def dict_invert_inplace(d: dict) -> None:

    # new_d = {}
    # for k, v in d.items():
    #     new_d[v] = k
    new_d = dict_invert(d)
    
    # keys = list(d.keys())
    # for k in keys:
    #     del d[k]
    d.clear()

    # for k, v in new_d.items():
    #     d[k] = v
    d.update(new_d)


def main():
    mydict = { 'Theodore': 10,
            'Mathew': 11,
            'Roxanne': 9,}
    dict_invert_inplace(mydict)
    print(mydict)

if __name__ == "__main__":
    main()