# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==同学的姓名、院系==

张洺瑜  地球与空间科学学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：

不用建立矩阵，重点只是一的位置，只需找出1的具体坐标，可以直接算出步骤数

3分钟

##### 代码

```python
# 
for i in range(5):
    j=list(input().split())
    if '1' in j:
        a=j.index('1')
        print(abs(i-2)+abs(a-2))

```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-09-24 225939](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-24 225939.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：

这题思路非常简单，但如果这么简单的用循环加1就超时了(悲)，所以要用数学的思维找出其中规律，           用时：5分钟(包括看答案)

##### 代码

```python
# 
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a%b==0:
        print(0)
    else:
        print(b-a%b)
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-09-25 153031](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-25 153031.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：

乍一看没什么思路，其实只需要依次对元素分情况分析，将事件和人员数分别储存于参数中。

7分钟（主要是思考）

##### 代码

```python
# 
n=int(input())
v=map(int,input().split())
result=0
police=0
for i in v:
    if i<0 and police==0:
        result+=1
    elif i>0:
        police+=i
    else:
        police-=1
print(result)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-25 163424](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-25 163424.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：

建立一个列表，将所有树以True的方式存入，之后将区域内的树全改为False，最后输出树的值

4分钟

##### 代码

```python
# 
v=input().split()
L,M=int(v[0]),int(v[1])
tree=[True]*(L+1)
for i in range(M):
    s=input().split()
    start,end=int(s[0]),int(s[1])
    for e in range(start,end+1):
        tree[e]=False
print(sum(tree))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-24 173520](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-24 173520.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：

建立一个列表，将水仙花数依次放入，之后再依次输出，注意最后一个数后无空格，可分情况对待。					5分钟

##### 代码

```python
# 
a,b=map(int,input().split())
c=[]
for i in range(a,b+1):
    k=i//100
    j=(i-k*100)//10
    l=i%10
    if i==k**3+j**3+l**3:
        c.append(i)
if len(c)==0:
    print('NO')
else:
    for r in range(len(c)):
        if r<len(c)-1:
            print(c[r],end=' ')
        else:
            print(c[r])
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-24 173059](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-24 173059.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：

刚开始看让人无从下手，没有一点思路，借助人工智能给出思路后豁然开朗，只需要得知所有骑手中用时最短的时间即可。但这样还有问题，需要将提前出发的骑手略去，因为主角不会在起点跟着他们出发。          15分钟多

##### 代码

```python
# 
import math
def arrive_time(n,vt):
    time=[]
    for v,t in vt:
        distance=4.5
        ti=distance/v*3600+t
        time.append(ti)
    charley=math.ceil(min(time))
    return charley

while True:
    n=int(input())
    vt=[]
    if n==0:
        break
    for i in range(n):
        v,t=map(int,input().split(  ))
        if t<0:
            continue
        vt.append((v,t))
    print(arrive_time(n,vt))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-25 181830](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-25 181830.png)

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

感觉自身实力还是不够强，有些用法不能够灵活使用。越到后面可能更需要找出题目的本质，而非根据题目描述死算，就如这次的Ride to school以及Divisibility problem。

这回的题目不少是看答案才找到正确思路的，实在难受



