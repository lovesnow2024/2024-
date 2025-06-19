# Assignment #D: 图 & 散列表

Updated 2042 GMT+8 May 20, 2025

2025 spring, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

> **说明：**
>
> 1. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 2. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### M17975: 用二次探查法建立散列表

http://cs101.openjudge.cn/practice/17975/

<mark>需要用这样接收数据。因为输入数据可能分行了，不是题面描述的形式。OJ上面有的题目是给C++设计的，细节考虑不周全。</mark>

```python
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
```



思路：

着实没想到会有相同的数，没考虑到。然后就是数据输入的问题。

代码：

```python
def H(key,x,ans,dic):
    if dic[key] is None or dic[key]==x:
        dic[key]=x
        ans.append(key)
        return False
    return True
import sys
input=sys.stdin.read
data=input().split()
index=0
n=int(data[index])
index+=1
m=int(data[index])
index+=1
nums=[int(i) for i in data[index:index+n]]
dic=[None]*m
ans=[]
for num in nums:
    pos=num%m
    if not H(pos,num,ans,dic):
        continue
    i=1
    while True:
        new_pos=(pos+i**2)%m
        if not H(new_pos,num,ans,dic):
            break
        new_pos=(pos-i**2)%m
        if not H(new_pos,num,ans,dic):
            break
        i+=1
print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-21 220616](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-21 220616.png)



### M01258: Agri-Net

MST, http://cs101.openjudge.cn/practice/01258/

思路：

基本上就是prim算法的模版，直接套用就可以了。刚开始看题干，翻译的有一句说 “一行可能继续到下一行” ，我以为又要在输入上搞我。。。幸好一下就AC了。

代码：

```python
import heapq
def prim(dic,n):
    visited=set()
    start=0
    visited.add(start)
    heap=[]
    for end,value in dic[start]:
        heapq.heappush(heap,(value,start,end))
    res=0
    while heap and len(visited)<n:
        v,s,e=heapq.heappop(heap)
        if e not in visited:
            visited.add(e)
            res+=v
            for neighbor,value in dic[e]:
                if neighbor not in visited:
                    heapq.heappush(heap,(value,e,neighbor))
    return res
while True:
    try:
        n=int(input())
        grid=[list(map(int,input().split())) for _ in range(n)]
        dic={i:[] for i in range(n)}
        for i in range(n):
            for j in range(i+1,n):
                dic[i].append((j,grid[i][j]))
                dic[j].append((i,grid[i][j]))
        print(prim(dic,n))
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-21 222814](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-21 222814.png)



### M3552.网络传送门旅游

bfs, https://leetcode.cn/problems/grid-teleportation-traversal/

思路：

用双端队列，注意传送门使用不加步数，所以得添加到队列左端立刻处理，否则好像会出点问题。传送门使用完后立刻删除。用map储存步数更方便操作。

代码：

```python
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        dic=defaultdict(list)
        n,m=len(matrix),len(matrix[0])
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    dic[matrix[i][j]].append((i,j))
                else:
                    continue
        queue=deque([(0,0)])
        dis=[[float('inf')]*m for _ in range(n)]
        dis[0][0]=0
        while queue:
            x,y=queue.popleft()
            d=dis[x][y]
            if (x,y)==(n-1,m-1):
                return d
            if matrix[x][y] in dic:
                for px,py in dic[matrix[x][y]]:
                    if dis[px][py]>d:
                        dis[px][py]=d
                        queue.appendleft((px,py))
                del dic[matrix[x][y]]
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and matrix[nx][ny]!='#' and d+1<dis[nx][ny]:
                    dis[nx][ny]=d+1
                    queue.append((nx,ny))
        return -1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-21 221032](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-21 221032.png)



### M787.K站中转内最便宜的航班

Bellman Ford, https://leetcode.cn/problems/cheapest-flights-within-k-stops/

思路：

1. Dijkstra，普通写会超时，需要加点剪枝小优化。dist列表，dist [p] [k] = 到达 p 且中转 k 次的最小花费。加上一步判断，如果当前比dist [p] [k]更小，就更新，否则说明已经有更优解。
2. Bellman Ford：本类题特攻，因为这类题有k次的限制。而该方法恰好可以设定循环多少次，所以可以避免无效的多次循环。更高效处理

方法2要比方法1更快。

代码：

```python
###Dijkstra方法

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic=defaultdict(list)
        for s,e,v in flights:
            dic[s].append((e,v))
        heap=[]
        heapq.heappush(heap,(0,src,0))
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        while heap:
            cur_v,cur_p,cur_k=heapq.heappop(heap)
            if cur_p==dst:
                return cur_v
            if cur_k>k:
                    continue
            for next_,v in dic[cur_p]:
                new_v=cur_v+v
                new_k=cur_k+1
                if new_k<=k+1 and new_v<dist[next_][new_k]:
                    dist[next_][new_k]=new_v
                    heapq.heappush(heap,(cur_v+v,next_,cur_k+1))
        return -1
    
###Bellman Ford

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist=[float('inf')]*n
        dist[src]=0
        for _ in range(k+1):
            new_dist=dist.copy()
            flag=False
            for s,e,v in flights:
                if dist[s]+v<new_dist[e]:
                    new_dist[e]=dist[s]+v
                    flag=True
            dist=new_dist
            if not flag:
                break
        return dist[dst] if dist[dst]!=float('inf') else -1


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-21 235924](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-21 235924.png)

![屏幕截图 2025-05-22 000917](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-22 000917.png)

### M03424: Candies

Dijkstra, http://cs101.openjudge.cn/practice/03424/

思路：

感觉比道路要复杂一些，如果没看课件的话，可能想不到用一个diff列表储存最大差值。

代码：

```python
import heapq
from collections import defaultdict
n,m=map(int,input().split())
dic=defaultdict(list)
for _ in range(m):
    a,b,c=map(int,input().split())
    dic[a].append((b,c))
heap=[]
max_candies=[float('inf')]*(n+1)
max_candies[1]=0
heapq.heappush(heap,(0,1))
while heap:
    cur_diff,cur_place=heapq.heappop(heap)
    if cur_place==n:
        break
    if cur_diff>max_candies[cur_place]:
        continue
    for next_,diff in dic[cur_place]:
        if max_candies[next_]>max_candies[cur_place]+diff:
            max_candies[next_]=max_candies[cur_place]+diff
            heapq.heappush(heap,(max_candies[next_],next_))
print(max_candies[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-21 225354](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-21 225354.png)



### M22508:最小奖金方案

topological order, http://cs101.openjudge.cn/practice/22508/

思路：

拓扑排序，Kalm算法（是叫这个吧），把手下败将的数量当做**入度**处理。依次处理入度归零的数据。将**奖金数**作为heap排序的key。每次有入度归零的，奖金加一。

代码：

```python
import heapq
from collections import defaultdict
n,m=map(int,input().split())
dic=defaultdict(set)
defeat=[0]*n
value=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    if a not in dic[b]:
        defeat[a]+=1
    dic[b].add(a)
heap=[]
for i in range(n):
    if defeat[i]==0:
        heapq.heappush(heap,(100,i))
        value[i]=100
while heap:
    cur_value,u=heapq.heappop(heap)
    for x in dic[u]:
        defeat[x]-=1
        if defeat[x]==0:
            value[x]=cur_value+1
            heapq.heappush(heap,(cur_value+1,x))
print(sum(value))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-21 225933](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-21 225933.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次作业几乎全部是模版题，不过感觉自己对于模版还是不太熟悉，不能自己独立做出来，还是需要稍微参考模版。当然，经过这几道题的练习，对这些题型更加熟悉了。每日选做依旧每天跟进。

接下来该认真整理cheatpaper了，还没开始整呢。。。









