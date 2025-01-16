# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：

想复杂了，没有立刻想到中学就已经知道的方法。第一次用洛谷，测试点就是测试数据吗，真的只有这几个吗？       10分钟

代码：

```python
n=int(input())
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-27 122243](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-27 122243.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：

与上一道题思路类似，只不过在这里多一步循环。别的不谈，狄贵同学简直是概念神，太厉害了！

10分钟

代码：

```python
n=int(input())
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2,n+1):
    for j in range(i):
        dp[i]+=dp[j]
print(dp[n])
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-11-27 123146](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-27 123146.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：

emm，我是在前两个题基础上想出来的思路，可以当做另一种数楼梯：一次跨1步或是k步。不过我的代码超时了，ai加了一个求取前缀和的操作就AC了，这么有效的吗？      30分钟

代码：

```python
t,k=map(int,input().split())
mod=10**9+7
max_b=10**5
dp=[0]*(max_b+1)
dp[0]=1
for j in range(1,max_b+1):
    if j<k:
        dp[j]=1
    else:
        dp[j]=(dp[j-1]+dp[j-k])%mod
prefix_sum = [0] * (max_b + 1)
for i in range(1, max_b + 1):
    prefix_sum[i] = (prefix_sum[i - 1] + dp[i]) % mod
for _ in range(t):
    a,b=map(int,input().split())
    ans=(prefix_sum[b] - prefix_sum[a - 1])%mod
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-27 155811](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-27 155811.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：

从头遍历至尾，在每个节点运用双指针技术进行双向扩展，不断更新最大的子串的信息。        1小时

代码：

```python
def longestPalindrome(self, s: str) -> str:
        def expand(s,left,right):
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1
        n=len(s)
        if n==0:
            return 0
        start,end=0,0
        for i in range(n):
            len1=expand(s,i,i)
            len2=expand(s,i,i+1)
            len0=max(len1,len2)
            if len0>end-start:
                start=i-(len0-1)//2
                end=i+len0//2
        return s[start:end+1] 
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-27 202429](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-27 202429.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：

RE好久，然后改了输入的方式；还是RE了好久，就向答案代码转变；然后是该死的WA，最后将答案基本照抄了过来，才AC的。应该大概率是输入的问题，哭死了，感觉虚度光阴。。。               3天

代码：

```python
import sys
from collections import deque
input = sys.stdin.read
def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n
def bfs(sx,sy,sh,m,n,h,water_height):
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue=deque([(sx,sy,sh)])
    water_height[sx][sy] = sh
    while queue:
        x,y,height=queue.popleft()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if is_valid(nx, ny, m, n) and h[nx][ny]<height:
                if water_height[nx][ny]<height:
                    water_height[nx][ny]=height
                    queue.append((nx,ny,height))
def main():
    data = input().split()
    k = int(data[0])
    idx=1
    result=[]
    for _ in range(k):
        m, n =map(int, data[idx:idx + 2])
        idx+=2
        h = []
        for i in range(m):
            h.append(list(map(int, data[idx:idx + n])))
            idx += n
        water_height = [[0] * n for _ in range(m)]
        i, j = map(int, data[idx:idx + 2])
        idx+=2
        i,j=i-1,j-1
        p=int(data[idx])
        idx+=1
        for _ in range(p):
            x,y=map(int,data[idx:idx+2])
            idx+=2
            x,y=x-1,y-1
            if h[x][y]<=h[i][j]:
                continue
            bfs(x,y,h[x][y],m,n,h,water_height)

        result.append("Yes" if water_height[i][j] > 0 else "No")
    sys.stdout.write('\n'.join(result) +'\n')
if __name__=="__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-30 001845](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-30 001845.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：

思路容易，但是挺恶心的。

1. 求线段数，而不是步数
2. x,y给的是反的，离谱

我做了好久，好不容易不再RE了，又开始WA了。我照着答案不断修改，一直改，还是不行。花了我一个半小时，我的代码已经彻底不再是我的了（这也是我很排斥答案，而喜欢用AI的原因），最后才发现输出少了个冒号。。。天哪，无言以对，这算什么。。。为什么不能让我知道我哪里出错了（红温）         若干个小时

代码：

```python
from collections import deque
def bfs(start,end,lst,h,w):
    visited=set()
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    ans=[]
    queue=deque([start])
    while queue:
        x, y,steps,direction = queue.popleft()
        if (x, y) == end:
            ans.append(steps)
            break
        for i,(dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            if 0 <= nx < h+2 and 0 <= ny < w+2 and ((nx, ny, i) not in visited):
                new_direction = i
                new_steps=steps if new_direction ==direction else steps+1
                if (nx,ny)==end:
                    ans.append(new_steps)
                    continue
                if lst[nx][ny]!='X':
                    visited.add((nx,ny,i))
                    queue.append((nx,ny,new_steps,new_direction))

    if len(ans)==0:
        return -1
    else:
        return min(ans)
count=1
while True:
    w,h=map(int,input().split())
    if w==h==0:
        break
    lst= [' ' * (w + 2)] + [' ' + input() + ' ' for _ in range(h)] + [' ' * (w + 2)]
    print(f"Board #{count}:")
    count0=1
    while True:
        x3,y3,x0,y0=map(int,input().split())
        if x3==x0==y3==y0==0:
            break
        y1,x1,y2,x2=x3,y3,x0,y0
        start = (x1, y1, 0, -1)
        end=(x2,y2)
        v=bfs(start,end,lst,h,w)
        if v==-1:
            print(f"Pair {count0}: impossible.")
        else:
            print(f"Pair {count0}: {v} segments.")
        count0+=1
    print()
    count += 1
```



代码运行截图 <mark>（至少包含有"Accepted"）![屏幕截图 2024-11-30 180807](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-30 180807.png)</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

正如大家所言，前两题很简单。。第三题我也能独立想出来，第四题是看AI给的思路才去写的。后两个题，挺好的挺好的，锻炼耐心、毅力、细节。很好的题，下次不要再让我看见了。



