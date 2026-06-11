# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

**说明：**

1）⽉考： AC3<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：

本以为是自动按着输入顺序排的，但是WA了几次，加上按index排序才正确      30分钟

代码：

```python
n = int(input())
lst = [input().split() for _ in range(n)]
lst1 = []
for _ in range(n):
    if int(lst[_][1]) >= 60:
        lst1.append(lst[_])
lst2 = [k for k in lst if k not in lst1]
lst1 = sorted(lst1, key=lambda x: (-int(x[1]),lst.index(x) ))
for a, b in lst1:
    print(a)
for i, j in lst2:
    print(i)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-07 220320](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-07 220320.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：

先将矩阵还原，将结果算出后，再将矩阵转换。考试时有点紧张，没看清怎么转换的矩阵，一直不明白元素值是什么。。。      25分钟

代码：

```python
n,m1,m2=map(int,input().split())
x=[list(map(int,input().split())) for _ in range(m1)]
y=[list(map(int,input().split())) for _ in range(m2)]
lst1=[[0]*n for _ in range(n)]
lst2=[[0]*n for _ in range(n)]
ans=[]
for a,b,c in x:
    lst1[a][b]=c
for a1,b1,c1 in y:
    lst2[a1][b1]=c1
for i in range(n):
    for j in range(n):
        count=0
        for x in range(n):
            count+=lst1[i][x]*lst2[x][j]
        if count!=0:
            ans.append([i,j,count])
for row in ans:
    print(' '.join(map(str,row)))
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-11-07 223455](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-07 223455.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

依旧是排序题，需要注意同时只能使用m个技能，这是一个难点       40分钟

代码：

```python
nc = int(input())
for _ in range(nc):
    n, m, b = map(int, input().split())
    jn = [list(map(int, input().split())) for i in range(n)]
    jn1 = sorted(jn, key=lambda x: (x[0], -x[1]))
    count = 1
    c = m
    for i in range(n):
        if jn1[i][0] > count:
            count = jn1[i][0]
            c = m
        if c > 0 and jn1[i][0] == count:
            b -= jn1[i][1]
            c -= 1
        if b <= 0:
            print(count)
            break
    if b > 0:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-07 220736](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-07 220736.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：

经典dp问题，按照之前的套路做了一下，很套路化    30分钟

代码：

```python
n,m=map(int,input().split())
moneys=list(map(int,input().split()))
dp=[float('inf')]*(m+1)
dp[0]=0
for i in range(1,m+1):
    for money in moneys:
        if i>=money:
            dp[i]=min(dp[i],dp[i-money]+1)
print(dp[m] if dp[m]!=float('inf') else -1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-07 221048](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-07 221048.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：

难点在于如623千，623是一个整体，不能先让6*100，所以需要有个current来储存        40分钟

代码：

```python
strings=list(input().split())
dct1={'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19}
dct2={'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}
dct3={'hundred':100, 'thousand':1000, 'million':1000000}
if strings[0]=='negative':
    strings.pop(0)
    flag=True
else:
    flag=False
ans=0
current=0
for i in strings:
    if i in dct1:
        current+=dct1[i]
    elif i in dct2:
        current+=dct2[i]
    elif i == 'hundred':
        current*=100
    elif i in dct3:
        ans+=current*dct3[i]
        current=0
ans+=current
if flag:
    print(-ans)
else:
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-08 134145](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-08 134145.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：

进程检测一样的题，直接按截止时间排序求解     20分钟

代码：

```python
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x: (x[1],x[0]))
count=0
dead=-1
for start,end in lst:
    if start>dead:
        count+=1
        dead=end
print(count)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-08 141642](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-08 141642.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这回考试没有那么难，但因为我这些天懈怠了好久，已经很不熟练了。况且我发现我的思路不够灵活，看到题只想按题干说的一步一步解，很麻烦。打字速度也很慢，严重影响时间。期中结束后是时候捡起来了。



