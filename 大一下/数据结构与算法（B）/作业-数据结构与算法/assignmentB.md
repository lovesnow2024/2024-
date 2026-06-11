# Assignment #B: 图为主

Updated 2223 GMT+8 Apr 29, 2025

2025 spring, Complied by <mark>同学的姓名、院系</mark>

张洺瑜  地球与空间科学学院

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

### E07218:献给阿尔吉侬的花束

bfs, http://cs101.openjudge.cn/practice/07218/

思路：

寻常的迷宫bfs题。

代码：

```python
from collections import deque
def bfs(grid,start,end,r,c):
    queue=deque([(start[0],start[1],0)])
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    visited=set()
    visited.add(tuple(start))
    while queue:
        x,y,time=queue.popleft()
        if [x,y]==end:
            return time
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c and (nx,ny) not in visited and grid[nx][ny]!='#':
                visited.add((nx,ny))
                queue.append((nx,ny,time+1))
    return 'oop!'
t=int(input())
for _ in range(t):
    r,c=map(int,input().split())
    grid=[list(input()) for _ in range(r)]
    flag1,flag2=False,False
    start,end=[0,0],[0,0]
    for i in range(r):
        row=grid[i]
        if 'S' in row:
            start[0],start[1]=i,row.index('S')
            flag1=True
        elif 'E' in row:
            end[0],end[1]=i,row.index('E')
            flag2=True
        if flag1 and flag2:
            break
    print(bfs(grid,start,end,r,c))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-30 215825](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-30 215825.png)



### M3532.针对图的路径存在性查询I

disjoint set, https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/

思路：

还以为要建类，用完整的并查集做法。其实由于数组单调，所以只需要比较相邻两个数就可以将他们分成不同的组，用每个组的首位作记录，比较节点的记录值是否一致。

代码：

```python
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        lst=[0]*len(nums)
        tmp=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>maxDiff:
                tmp=i
            lst[i]=tmp
        ans=[False]*len(queries)
        for j,(x,y) in enumerate(queries):
            if lst[x]==lst[y]:
                ans[j]=True
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-30 220939](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-30 220939.png)



### M22528:厚道的调分方法

binary search, http://cs101.openjudge.cn/practice/22528/

思路：

我以为是要从数组里找一个临界值，然后不会找浮点数。看了答案才知道是直接二分查找b。我第一次也是这么想的，但是感觉数太大了（

代码：

```python
def check(b,nums):
    a=b/1e9
    count=0
    target=0.6*len(nums)
    for num in nums:
        new_scores=a*num +1.1**(a*num)
        if new_scores>=85:
            count+=1
            if count>=target:
                return True
    return False
nums=list(map(float,input().split()))
left,right=1,10**9
ans=0
while left<=right:
    mid=(left+right)//2
    if check(mid,nums):
        right=mid-1
        ans=mid
    else:
        left=mid+1
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-01 205834](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-01 205834.png)



### Msy382: 有向图判环 

dfs, https://sunnywhy.com/sfbj/10/3/382

思路：

用字典构建有向图，套用dfs模版就行了。

代码：

```python
from collections import defaultdict
def dfs(dic,num,visited,path,count):
    if path==num and count!=0:
        return True
    for next_ in dic[path]:
        if next_ not in visited:
            visited.add(next_)
            if dfs(dic,num,visited,next_,count+1):
                return True
            visited.remove(next_)
    return False
n,m=map(int,input().split())
dic=defaultdict(list)
nums=set()
for _ in range(m):
    u,v=map(int,input().split())
    dic[u].append(v)
    nums.add(u)
    nums.add(v)
flag='No'
for num in nums:
    visited=set()
    if dfs(dic,num,visited,num,0):
        flag='Yes'
        break
print(flag)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-01 204354](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-01 204354.png)



### M05443:兔子与樱花

Dijkstra, http://cs101.openjudge.cn/practice/05443/

思路：

用字典构建地图，然后利用堆结构每次选取当前总路径最短的进行下一次操作。注意记录路径，然后在到终点时再变为要求的结果。

代码：

```python
import heapq
from collections import defaultdict
def path(dic,start,end):
    if start==end:
        return start
    heap=[]
    heapq.heappush(heap,(0,start,[]))
    visited=set()
    while heap:
        sum_dist,cur_place,path=heapq.heappop(heap)
        if cur_place in visited:
            continue
        visited.add(cur_place)
        if cur_place==end:
            result=path[0][0]
            for part in path:
                result+=f'->({part[1]})->{part[2]}'
            return result
        for place,dist in dic[cur_place]:
            if place not in visited:
                new_path=path[:]
                new_path.append((cur_place,dist,place))
                heapq.heappush(heap,(sum_dist+dist,place,new_path))
    return 'no'
p=int(input())
places=[input() for _ in range(p)]
dic=defaultdict(list)
q=int(input())
for _ in range(q):
    a,b,dist=input().split()
    dic[a].append((b,int(dist)))
    dic[b].append((a, int(dist)))
r=int(input())
for _ in range(r):
    start,end=input().split()
    print(path(dic,start,end))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-01 133150](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-01 133150.png)



### T28050: 骑士周游

dfs, http://cs101.openjudge.cn/practice/28050/

思路：

固定步数的bfs，但是问题在于超时，所以需要每走一步，将下一步能做的选择统计数量，选择最少的那个。

代码：

```python
def dfs(grid,count,x,y,n):
    if count==0:
        return True
    directions=[(1,2),(1,-2),(-1,2),(-1,-2),(2,-1),(2,1),(-2,1),(-2,-1)]
    next_moves=[]
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and not grid[nx][ny]:
            moves=sum((0<=nx+ddx<n and 0<=ny+ddy<n and not grid[nx+ddx][ny+ddy]) for ddx,ddy in directions)
            next_moves.append((moves,nx,ny))
    next_moves.sort()
    for _,nx,ny in next_moves:
        grid[nx][ny]=True
        if dfs(grid,count-1,nx,ny,n):
            return True
        grid[nx][ny]=False
    return False
n=int(input())
x,y=map(int,input().split())
grid=[[False]*n for _ in range(n)]
grid[x][y]=True
print('success' if dfs(grid,n*n-1,x,y,n) else 'fail')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-01 094301](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-01 094301.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次作业大多数是bfs、dfs做法，我对这些还是挺熟的，所以做起来还算是轻松。又用了一遍dijkstra算法，也是又巩固了一下。
每日选做一定要跟上，五一回家多做点题。









