import math
from operator import itemgetter
if __name__ == '__main__':
    lst=[]
    k=1
    lst.append([7,7,'Bad'])
    lst.append([7,4,'Bad'])
    lst.append([3,4,'Good'])
    lst.append([1,4,'Good'])
    dist=[]
    test=[3,7]
    for i in lst:
        dist.append(math.sqrt(math.pow(test[0]-i[0],2)+math.pow(test[1]-i[1],2)))
    for i in range(4):
        lst[i].append(dist[i])
    print lst
    new_lst=sorted(lst, key=itemgetter(3))
    print new_lst
    final=[]
    c1=0
    c2=0
    for i in range(k):
        final.append(new_lst[i][2])
        if final[i]=="Good":
            c1+=1
        else:
            c2+=1
    print final,c1,c2
    if c1>c2:
        print "The test is Good."
    elif c1<c2:
        print "The test is Bad."
    else:
        print "More training data required!!can't classify now."
