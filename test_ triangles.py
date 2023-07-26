# -*- coding:utf-8 -*-
# @Author:Cheng Lei 1037654919@qq.com
# @Time : 2022/6/6 下午5:22
# @FileName: test_ triangles.py
# @Software: PyCharm

#杨辉三角 write by cl
def triangles(max):
    n=0
    lll=[]
    while n<=max:
        ll=[1 for i in range(n+1)]
        for i in range(n+1):
            if i ==0 or i==n:
                ll[i]=1
            else:
                ll[i]=lll[i-1]+lll[i]
        n+=1
        lll=ll
        yield ll
#大神的
def triangles2():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]

n=0
results = []
for t in triangles2():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

