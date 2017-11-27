if __name__ == '__main__':
    m=3
    a=[.4,.3,.3]
    b=[1,0,0]
    c=[0,1,1]
    sum1=0
    sum2=0
    for i in range(m):
        sum1+=(a[i]*b[i])
    for j in range(m):
        sum2+=(a[j]*c[j])
    k=max(sum1,sum2)
    if(k==sum1):
        print "The result of bayes optimal classifier which is positive is ",sum1
    else:
        print "The result of bayes optimal classifier which is negative is ",sum2
