# photo=[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
# name=["may", "kein", "kain", "radi"]
# yearning=[5, 10, 1, 3]
#
#
# def solution(name, yearning, photo):
#     result=[]
#     for i in photo:
#         dataSum=0
#         for j in name:
#             if j in i:
#                 dataSum+=yearning[name.index(j)]
#         result.append(dataSum)
#     return result
import numpy as np

import numpy as np

def solution(food):
    answer=[]
    if((len(food)<=9 and len(food)>=2)):
        for i in range(1,len(food)):
            data=str(i)
            answer.extend(data*(food[i]//2))
        answer_inverse=answer[::-1]
        water='0'
        answer=''.join(map(str,answer))
        answer=answer+water
        answer_inverse=''.join(map(str,answer_inverse))
        answer=answer+answer_inverse
        return answer
food=[1, 3, 4, 6,4,5,8,10]
print(solution(food))