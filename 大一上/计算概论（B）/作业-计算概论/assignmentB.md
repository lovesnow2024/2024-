# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

**说明：**

1）⽉考： AC1<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：

不断求两数之差取最大，后一个数大于前一个数就继续，小于的话就移动前一个数。        10分钟

代码：

```python
prices=list(map(int,input().split()))
s=0
current=0
max_=0
for i in range(1,len(prices)):
    if prices[i]>=prices[s]:
        current=prices[i]-prices[s]
        max_ = max(max_, current)
    elif prices[i]<prices[s]:
        s=i
print(max_)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-06 202145](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-06 202145.png)



### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：

借鉴的群里同学给的思路，当时是想到要让最大值和平均值比较，不过，没做出来。

代码：

```python
n,k=map(int,input().split())
times=list(map(int,input().split()))
while len(times)>=1 and k>=1:
    average = sum(times) / k
    max_=max(times)
    if max_<=average:
        print(f"{average:.3f}")
        break
    else:
        times.pop(times.index(max_))
        k-=1
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-12-06 202123](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-06 202123.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：

抄的群里大佬的，真想不到。

代码：

```python
values=list(map(int,input().split(',')))
n=len(values)
dp=[[0]*2 for _ in range(n)]
dp[0][0]=values[0]
ans=values[0]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][0]+values[i],values[i])
    dp[i][1]=max(dp[i-1][1]+values[i],dp[i-1][0])
    ans=max(ans,dp[i][0],dp[i][1])
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-06 211519](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-06 211519.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：

抄的群里发的同学的，不，大佬的。dfs的题啊，我没想到。光看着那输入就觉得麻烦得要死。

代码：

```python
n,m=map(int,input().split())
values=[list(input().split()) for _ in range(n)]
sale=[list(input().split()) for _ in range(m)]
ans=float('inf')
def dfs(values,sale,items=0,total=0,store=[0]*m):
    global ans
    if items==n:
        sale_ans=0
        for i in range(m):
            store_=0
            for s in sale[i]:
                a,b=map(int,s.split('-'))
                if store[i]>=a:
                    store_=max(store_,b)
            sale_ans+=store_
        ans=min(ans,total-sale_ans-(total//300)*50)
        return
    for k in values[items]:
        num,p=map(int,k.split(':'))
        store[num-1]+=p
        dfs(values,sale,items+1, total+p, store)
        store[num-1]-=p
dfs(values,sale)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-07 120437](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-07 120437.png)



### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：

现找第一个岛，让它全变为2。然后一步一步扩展，直到到第二座岛。dfs、bfs交叉使用。

代码：

```python
n=int(input())
lst=[list(map(int,input())) for _ in range(n)]
m=len(lst[0])
from collections import deque
def dfs(x, y, queue, grid,n,m):
    if not check(x,y,n,m) or grid[x][y] != 1:
        return
    grid[x][y] = 2
    queue.append((x, y))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx,ny=x+dx,y+dy
        dfs(nx, ny, queue, grid,n,m)
def check(x,y,n,m):
    return 0 <= x < n and 0 <= y <m
def shortest_bridge(grid,n,m):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    queue = deque()
    island = False
    for i in range(n):
        if island:
            break
        for j in range(m):
            if grid[i][j] == 1:
                dfs(i, j, queue, grid,n,m)
                island = True
                break
    steps = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if check(nx, ny,n,m) and grid[nx][ny] != 2:
                    if grid[nx][ny] == 1:
                        return steps
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
        steps +=1
print(shortest_bridge(lst,n,m))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-07 102924](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-07 102924.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：

只要知道按乘积排列，一切都会好起来的。

代码：

```python
n=int(input())
a,b=map(int,input().split())
nums=[list(map(int,input().split())) for _ in range(n)]
nums0=sorted(nums,key=lambda x:(x[1]*x[0]))
ans=0
current=a
for i in range(n):
    if i>0:
        current*=nums0[i-1][0]
    coins=current//nums0[i][1]
    ans=max(ans,coins)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-07 111154](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-07 111154.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

第一道题10分钟就想出来了，然后。。。就没有然后了。土豪购物看了半天不知道怎么写，然后去看了两岛这个题，写不出来。炸鸡排和国王游戏也看了一眼，知道应该有规律，但是已经心态炸了，只能眼巴巴看着时间到头。难绷。。。期末加油啊！！！！



