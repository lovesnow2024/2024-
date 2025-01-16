# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：

借鉴（照抄）的群里的思路。直接遍历找到假币，根据一些条件判定

代码：

```python
n=int(input())
for _ in range(n):
    measure=[list(input().split()) for _ in range(3)]
    for f in 'ABCDEFGHIJKL':
        if all((f in i[0] and i[2]=='up') or (f in i[1] and i[2]=='down') or (f not in i[0]+i[1] and i[2]=='even') for i in measure):
            print(f"{f} is the counterfeit coin and it is heavy.")
            break
        if all((f in i[0] and i[2]=='down') or (f in i[1] and i[2]=='up') or (f not in i[0]+i[1] and i[2]=='even') for i in measure):
            print(f"{f} is the counterfeit coin and it is light.")
            break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-18 160312](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-18 160312.png)



### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：

直接从最高的点向下滑。还是不太熟练。

代码：

```python
def dfs(map_,x,y,r,c,record):
    if record[x][y]!=-1:
        return record[x][y]
    directions=[(-1,0),(1,0),(0,1),(0,-1)]
    max_length=1
    for dx, dy in directions:
        nx,ny=dx+x,dy+y
        if 0<=nx<r and 0<=ny<c and map_[nx][ny]<map_[x][y]:
            length=1+dfs(map_,nx,ny,r,c,record)
            max_length=max(max_length,length)
    record[x][y]=max_length
    return max_length
r,c=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(r)]
max_=0
record=[[-1]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        max_=max(max_,dfs(grid,i,j,r,c,record))
print(max_)

```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-12-18 164052](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-18 164052.png)



### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：

乍一看感觉不容易，不过可以让两个点一起走。找到这两个点就行。

代码：

```python
def dfs(grid,n,x1,y1,x2,y2,visited):
    directions=[[-1,0],[1,0],[0,-1],[0,1]]
    visited[x1][y1]=True
    if grid[x1][y1]==9 or grid[x2][y2]==9:
        return True
    for dx,dy in directions:
        nx1,ny1=x1+dx,y1+dy
        nx2,ny2=x2+dx,y2+dy
        if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n and (not visited[nx1][ny1])  and grid[nx1][ny1]!=1 and grid[nx2][ny2]!=1:
            if dfs(grid,n,nx1,ny1,nx2,ny2,visited):
                return True
    visited[x1][y1]=False
    return False
n=int(input())
grid=[list(map(int,input().split())) for _ in range(n)]
ani=[]
for i in range(n):
    for j in range(n):
        if len(ani)==2:
            break
        if grid[i][j]==5:
            ani.append([i,j])
visited=[[False]*n for _ in range(n)]
print('yes' if dfs(grid,n,ani[0][0],ani[0][1],ani[1][0],ani[1][1],visited) else 'no')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-20 163010](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-20 163010.png)



### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：

dp的思路还是不太容易想出来，感觉我的思路总是很混乱，理不清dp中的原理

代码：

```python
m=int(input())
n=int(input())
nums=list(input().split())
dp=[['']*(m+1) for _ in range(n+1)]
nums.sort(key=lambda x:(int(x)/(10**(len(x))-1)))
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=dp[i-1][j]
        if j>=len(nums[i-1]):
            if dp[i-1][j]=='':
                dp[i][j]=nums[i-1]+dp[i-1][j-len(nums[i-1])]
            else:
                dp[i][j]=str(max(int(dp[i-1][j]),int(nums[i-1]+dp[i-1][j-len(nums[i-1])])))
print(dp[n][m])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-19 224756](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-19 224756.png)



### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：

其他都想到了，只是不知道怎么遍历第一行的64种情况。。。还是看的群里群友发的。

代码：

```python
def press(light,x,y):
    directions=[[-1,0],[0,0],[1,0],[0,1],[0,-1]]
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<5 and 0<=ny<6:
            light[nx][ny]^=1
def solve(light):
    for f_row in range(64):
        lights=[row[:] for row in light]
        click=[[0]*6 for _ in range(5)]
        for j in range(6):
            if (f_row >> j)&1:
                click[0][j]=1
                press(lights,0,j)
        for i in range(4):
            for j in range(6):
                if lights[i][j]==1:
                    click[i+1][j]=1
                    press(lights,i+1,j)
        if all(lights[4][j]==0 for j in range(6)):
            for row in click:
                print(*row)
light=[list(map(int,input().split())) for _ in range(5)]
solve(light)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-20 222803](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-20 222803.png)



### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：

本来想直接挨个去掉最小距离，但是又想到最小距离两边的距离可能相等，这样就不知道去除哪块石头了。好多贪心题我都这样想过，遇到这种情况好像就不能简单选择到最优策略了。这是ai帮助写的，我只是看懂了。。。

代码：

```python
def cut_stone(stones,d,m):
    start=-d
    removed=0
    for stone in stones:
        if stone-start<d:
            removed+=1
            if removed>m:
                return False
        else:
            start=stone
    return True
def longest(l,n,m,stones):
    stones=[0]+stones+[l]
    left,right=0,l
    while left<=right:
        mid=left+(right-left)//2
        if cut_stone(stones,mid,m):
            left=mid+1
        else:
            right=mid-1
    return right
l,n,m=map(int,input().split())
stones=[int(input()) for _ in range(n)]
print(longest(l,n,m,stones))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-12-20 222129](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-12-20 222129.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

最后一次作业，感觉还是挺难的。假币和熄灯着实不好想，最后一题的二分查找也不太会。没几天了，争取好好复习一下，把每日选做做完。



