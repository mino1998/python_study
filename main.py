photo=[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
name=["may", "kein", "kain", "radi"]
yearning=[5, 10, 1, 3]


def solution(name, yearning, photo):
    result=[]
    for i in photo:
        dataSum=0
        for j in name:
            if j in i:
                dataSum+=yearning[name.index(j)]
        result.append(dataSum)
    return result
