# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：

只要a==b或a//b>=2，行动方必赢。所以用一个计数器表示此时的行动方。    

代码：

```python
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    a,b=max(a,b),min(a,b)
    count=0
    while a!=b and a//b<2:
        count+=1
        a,b=b,a-b
    flag=count%2
    if flag==0:
        print('win')
    else:
        print('lose')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-11 225213](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-11 225213.png)



### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：

我这是没什么技术含量的，就是一层层死算。

代码：

```python
n=int(input())
onion=[list(map(int,input().split())) for _ in range(n)]
d=n//2-1
ans=[]
for i in range(d+1):
    e=n-i-1
    current=0
    for j in range(i,e+1):
        current+=onion[i][j]
        current+=onion[e][j]
    for k in range(i+1,e):
        current+=onion[k][i]
        current+=onion[k][e]
    ans.append(current)
if n%2==1:
    ans.append(onion[n//2][n//2])
print(max(ans))
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-12-12 104254](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-12 104254.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：

乍一看我以为直接从大到小排就行了。。。哈哈，太傻了。

从头遍历，小于零就扔掉最小的药水。第一次用堆其实。

代码：

```python
import heapq
n=int(input())
potions=list(map(int,input().split()))
start=0
count=0
min_heap=[]
for i in range(n):
    start+=potions[i]
    if potions[i]<0:
        heapq.heappush(min_heap,potions[i])
    if start<0:
        start-=heapq.heappop(min_heap)
    else:
        count+=1
print(count)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-12 110459](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-12 110459.png)



### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：

leecode上有个一样的题，之前是做过的。所以这道题完全理解。

代码：

```python
stack=[]
min_stack=[]
while True:
    try:
        act=input()
        if act=="pop":
            if stack:
                p=stack.pop()
                if p==min_stack[-1]:
                    min_stack.pop()
        elif act=="min":
            if min_stack:
                print(min_stack[-1])
        else:
            _,a=act.split()
            stack.append(int(a))
            if min_stack:
                if int(a)<=min_stack[-1]:
                    min_stack.append(int(a))
            else:
                min_stack.append(int(a))
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-12 112049](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-12 112049.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：

头一次接触dijkstra，很不熟练。这道题也是看了答案再做的。用堆好像更简单一些。

代码：

```python
import heapq
def energy_(map_,x1,y1,x2,y2,m,n):
    if map_[x1][y1]=='#' or map_[x2][y2]=='#':
        return 'NO'
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    visited=[[False]*n for _ in range(m)]
    energy_queue=[(0,x1,y1)]
    while energy_queue:
        energy,x,y=heapq.heappop(energy_queue)
        if x==x2 and y==y2:
            return energy
        if visited[x][y]:
            continue
        visited[x][y]=True
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and (not visited[nx][ny]):
                if map_[nx][ny]!='#':
                    delta_height=abs(int(map_[nx][ny])-int(map_[x][y]))
                    next_e=delta_height+energy
                    heapq.heappush(energy_queue,(next_e,nx,ny))
    return 'NO'
m,n,p=map(int,input().split())
map_=[list(input().split()) for _ in range(m)]
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    print(energy_(map_,x1,y1,x2,y2,m,n))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-12 132201](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-12 132201.png)



### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：

真的没想到对visited加这样的时间维度。写出来之后不出所料有WA了，究其原因竟是没有加上能够踩上终点的条件，导致一直输出oop。太粗心了。很搞心态

代码：

```python
from collections import deque
def bfs(x1,y1,x2,y2,grid,r,c,k):
    directions=[[-1,0],[1,0],[0,1],[0,-1]]
    visited=set()
    queue=deque([(x1,y1,0)])
    while queue:
        x,y,time=queue.popleft()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c and (nx,ny,(time+1)%k) not  in visited:
                if nx==x2 and ny==y2:
                    return time+1
                elif grid[nx][ny]!='#' or (time+1)%k==0:
                    queue.append((nx,ny,time+1))
                    visited.add((nx,ny,(time+1)%k))
    return 'Oop!'
t=int(input())
for _ in range(t):
    r,c,k=map(int,input().split())
    grid=[list(input()) for _ in range(r)]
    x1,y1,x2,y2=0,0,0,0
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='S':
                x1,y1=i,j
            elif grid[i][j]=='E':
                x2,y2=i,j
    print(bfs(x1, y1, x2, y2, grid,r,c,k))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-12 170746](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-12 170746.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

总体难度比月考小很多了。多亏这次作业，让我去学了堆的用法。

前四道题大致上可以自己做出来，当然这是给了题目类型的情况下。后两道还是不熟练，而且有些新东西没接触过根本不会做。需要多刷题了。leecode有在写，争取机考前刷完大部分题。

每日选做好久没做了，偶尔做的也是之前发的题，所以作业完成的偏晚。每日选做也得跟上了。



