# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：

求取公倍数d，则接下来d天定有下一个高峰   15分钟

代码：

```python
count=0
while True:
    p,e,i,d=map(int,input().split())
    v=0
    if p==e==i==d==-1:
        break
    count+=1
    gbs=23*28*33
    for j in range(d+1,d+1+gbs):
        if (j-p)%23==0 and (j-e)%28==0 and (j-i)%33==0:
            v=j
            break
    print(f"Case {count}: the next triple peak occurs in {v-d} days.")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-22 102410](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-22 102410.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：

将武器从小到大排序，价格低的制作，价格高的卖掉   20分钟

代码：

```python
p=int(input())
weapon=list(map(int,input().split()))
weapon.sort()
count1=0
count2=0
ans=[]
j=len(weapon)-1
if p<min(weapon):
    print(0)
else:
    for i in range(len(weapon)):
        if p-weapon[i]>=0:
            p-=weapon[i]
            count1+=1
            ans.append(count1-count2)
        elif p-weapon[i]<0 and j>=i:
            p+=weapon[j]
            j-=1
            count2+=1
            if p>=weapon[i]:
                p-=weapon[i]
                count1+=1
    print(max(ans))
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-10-22 102750](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-22 102750.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：

观察示例很容易得到，只要让时间少的往前就行。难住我的是怎样创建一个序号和输入对应的列表，发现了zip的使用，受教了     10分钟

代码：

```python
n=int(input())
stu_=[[a,int(b)] for a,b in zip(range(1,n+1),input().split()) ]
ans=sorted(stu_,key=lambda x:(x[1],x[0]))
ans1=[]
ans2=0
for i,j in ans:
    ans1.append(i)
for k in range(n-1):
    ans2+=stu_[n-k-2][0]*ans[k][1]
print(' '.join(map(str,ans1)))
print(f"{(ans2/n):.2f}")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-22 123415](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-22 123415.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

来回错了好几次，才发现需要输出n。。。为啥会有输出n的题啊（抓狂），思路很清晰，算出总天数后再转变。建字典挺累人的。   40分钟

代码：

```python
n=int(input())
print(n)
dct={'pop':1,'no':2,'zip':3,'zotz':4,'tzec':5,'xul':6,'yoxkin':7,'mol':8,'chen':9,'yax':10,'zac':11,'ceh':12,'mac':13,'kankin':14,'muan':15,'pax':16,'koyab':17,'cumhu':18,'uayet':19}
year2=0
month2=0
num2=0
dct2={1:'imix',2:'ik',3:'akbal',4:'kan',5:'chicchan',6:'cimi',7:'manik',8:'lamat',9:'muluk',10:'ok',11:'chuen',12:'eb',13:'ben',14:'ix',15:'mem',16:'cib',17:'caban',18:'eznab',19:'canac',20:'ahau'}
for _ in range(n):
    num,month,year=input().split()
    num=int(num.rstrip("."))
    days=int(year)*365+(dct[month]-1)*20+num
    year2=days//260
    num2=(days%260)%13+1
    month2=(days%260)%20+1
    print(f"{num2} {dct2[month2]} {year2}")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-22 135013](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-22 135013.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：

创建三元列表储存每棵树三种状态，从第一棵树开始，分析当前树不砍、向左砍、向右砍时前面已种下的树的数量，逐步遍历每一棵树，使最大的结果向后传递，直到最后求最后一棵树三种状态的最大值。    6小时（通义千问提供大概思路）

代码：

```python
n=int(input())
trees=[list(map(int,input().split())) for _ in range(n)]
nums=[[0,0,0] for _ in range(n+1)]
nums[1][0]=0
nums[1][1]=1
nums[1][2]=1
for i in range(2,n+1):
    w,h=trees[i-1]
    w_1,h_1=trees[i] if i < n else (float('inf'), 0)
    w_2,h_2=trees[i-2]
    nums[i][0]=max(nums[i-1][0],nums[i-1][1],nums[i-1][2])
    if w_2<w-h<=w_2+h_2:
        nums[i][1]=max(nums[i-1][0],nums[i-1][1])+1
    elif w-h>w_2+h_2:
        nums[i][1]=nums[i-1][2]+1
    else:
        nums[i][1]=0
    if w+h<w_1:
        nums[i][2]=max(nums[i-1][0], nums[i-1][1],nums[i-1][2]) + 1
    else:
        nums[i][2]=0
print(max(nums[n][0], nums[n][1], nums[n][2]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-23 194755](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-23 194755.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

将小岛所需雷达位置映射到X轴上（着实没想到），这样果然和进程检测一样。

def的好处之一在于return出现即停止，适合对多种情况返回不同的值，而若是直接写，用print的话，后面代码还是会运行，会导致不小的麻烦。  3小时

代码：

```python
from math import sqrt
def ans(islands,d):
    if d<0:
        return -1
    radars = 1
    ranges = []
    for x, y in islands:
        if y > d:
            return -1
        range_ = sqrt(d ** 2 - y ** 2)
        ranges.append([x - range_, x + range_])
    if not ranges:
        return -1
    ranges.sort(key=lambda x: x[1])
    r = ranges[0][1]
    for start, end in ranges:
        if start > r:
            r = end
            radars += 1
    return radars
count=0
while True:
    count+=1
    n,d=map(int,input().split())
    if n==d==0:
        break
    islands=[list(map(int,input().split())) for _ in range(n)]
    input()
    ans1=ans(islands,d)
    print(f"Case {count}: {ans1}")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-22 224355](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-22 224355.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

作业难度着实提上来了，压力不小。前四道题还可以，都是自己想出来的。但是后两道题还是没有具体思路，借助ai提示思路后才做出来。

更熟悉了**lambda**的用法以及了解了**cmp_to_key**和**restrip**的用法，不虚此行



