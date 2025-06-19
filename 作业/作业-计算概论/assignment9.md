# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：

对每个点进行dfs，然后取出最大值     30分钟

代码：

```python
def dfs(x,y,lst):
    if x<0 or y<0 or x>len(lst)-1 or y> len(lst[0])-1 or lst[x][y]!='W':
        return 0
    lst[x][y]='.'
    area=1
    directions=[[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,1],[1,0]]
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        area+=dfs(nx,ny,lst)
    return area
def max_(n,m,lst):
    max_ans=0
    for i in range(n):
        for j in range(m):
            if lst[i][j]=='W':
                area=dfs(i,j,lst)
                max_ans=max(area,max_ans)
    return max_ans
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    lst=[list(input()) for _ in range(n)]
    print(max_(n,m,lst))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-21 125845](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-21 125845.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：

第一次自己做bfs题，不够熟练，对模板不太了解     30分钟

代码：

```python
from collections import deque
def bfs(m,n,map_):
    directions=[[-1,0],[0,1],[0,-1],[1,0]]
    start=[0,0]
    queue=deque([start])
    visited=[[False]*n for _ in range(m)]
    visited[0][0]=True
    steps=0
    while queue:
        current=len(queue)
        for _ in range(current):
            x,y=queue.popleft()
            if map_[x][y]==1:
                return steps
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and  (not visited[nx][ny]) and map_[nx][ny]!=2:
                    queue.append([nx,ny])
                    visited[nx][ny]=True
        steps+=1
    return 'NO'
m,n=map(int,input().split())
map_=[list(map(int,input().split())) for _ in range(m)]
ans=bfs(m,n,map_)
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-11-21 142805](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-21 142805.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：

普通的dfs题，直套模板     20分钟

代码：

```python
def check(n,m,nx,ny,lst):
    if nx<0 or nx>=n or ny<0 or ny>=m or lst[nx][ny]:
        return False
    else:
        return True
def dfs(n,m,x,y,lst,count,ans):
    if count==0:
        ans[0]+=1
        return
    lst[x][y]=True
    count-=1
    directions=[[-2,-1],[-2,1],[-1,2],[-1,-2],[1,2],[1,-2],[2,1],[2,-1]]
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if check(n,m,nx,ny,lst):
            dfs(n,m,nx,ny,lst,count,ans)
    lst[x][y]=False
    count+=1
t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    lst = [[False] * m for _ in range(n)]
    count=n*m-1
    ans=[0]
    dfs(n,m,x,y,lst,count,ans)
    print(ans[0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-21 164843](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-21 164843.png)



### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：

套模板的同时记录路径，对我来说已经不简单了，通义千问给了个错误答案，和我的差不多。有问题，但死活看不出来，急死我了。       3小时

代码：

```python
def check(n, m, nx, ny, visited):
    if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
        return False
    else:
        return True

def dfs(n, m, x, y, current_sum):
    global max_sum,best_path
    if x == n - 1 and y == m - 1:
        if current_sum > max_sum:
            max_sum= current_sum
            best_path[:] = path[:]
        return
    visited[x][y] = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if check(n, m, nx, ny, visited):
            next_sum = current_sum+ matrix[nx][ny]
            path.append((nx, ny))
            dfs(n, m, nx, ny, next_sum)
            path.pop()
    visited[x][y] = False

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_sum = float('-inf')
best_path = []
path=[(0,0)]
visited = [[False] * m for _ in range(n)]
dfs(n, m, 0, 0,matrix[0][0])
for i,j in best_path:
    print(i + 1, j + 1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-21 230931](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-21 230931.png)





### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：

其实是个数学题      5分钟

代码：

```python
m,n=map(int,input().split())
map_=[[0]+[1]*(n-1)]
for _ in range(m-1):
    k=[1]+[-1]*(n-1)
    map_.append(k)
for i in range(1,m):
    for j in range(1,n):
        map_[i][j]=map_[i-1][j]+map_[i][j-1]
print(map_[m-1][n-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-21 233247](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-21 233247.png)



### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：

为什么我看了模板还不会，哎，又借助的外力完善的，自己只做了一半多      4小时

代码：

```python
from math import sqrt
def check(n):
    if n<=0:
        return False
    else:
        return int(sqrt(n))**2==n
def dfs(a,x0,n,ans,count):
    if x0==n:
        if sum(ans)==n:
            count[0]+=1
        return
    for i in range(x0+1,n+1):
        current=a[x0:i]
        if int(current)!=0 and check(int(current)):
            ans.append(i-x0)
            dfs(a,i,n,ans,count)
            ans.pop()
a=input()
n=len(a)
count=[0]
ans=[]
dfs(a,0,n,ans,count)
print('Yes' if count[0]!=0 else 'No')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-23 193122](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-23 193122.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

dfs、bfs都是模板题，我不否认。是我实力不够，没法看着模板做出来，稍微变一变就不会了，这种应对变化的能力太欠缺了。大部分最后一步还是靠ai完善。像我这种只能靠ai才能AC大部分题的。。。实在有些焦虑（流泪）。当然，我会继续努力跟上的。能不能跟上就是另一回事（滑稽）



