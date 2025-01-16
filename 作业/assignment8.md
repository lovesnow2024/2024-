# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：

对于一个1，统计上下左右0的数量以及空白的数量，求和即为陆地周长。          30分钟

代码：

```python
n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
directions=[[-1,0],[0,-1],[0,1],[1,0]]
ans=0
for i in range(n):
    for j in range(m):
        if lst[i][j]==0:
            continue
        elif lst[i][j]==1:
            count=0
            for direction in directions:
                if i+direction[0]<0 or i+direction[0]>=n or j+direction[1]<0 or j+direction[1]>=m:
                    count+=1
                else:
                    if lst[i+direction[0]][j+direction[1]]==0:
                        count+=1
                    else:
                        continue
            ans+=count
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-13 155641](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-13 155641.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：

设置方向，碰壁转向。        20分钟

代码：

```python
n=int(input())
matrix=[[0]*n for _ in range(n)]
directions=[[0,1],[1,0],[0,-1],[-1,0]]
count=0
row,col=0,0
for i in range(1,n*n+1):
    matrix[row][col]=i
    row1=row+directions[count][0]
    col1=col+directions[count][1]
    if not (0<=row1<n and 0<=col1<n and matrix[row1][col1]==0):
        count=(count+1)%4
        row1=row+directions[count][0]
        col1=col+directions[count][1]
    row,col=row1,col1
for row in matrix:
    print(' '.join(map(str,row)))
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-11-13 215107](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-13 215107.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：

该问题重点在于计算指定区域的和，本来想进行四重循环强解，果不其然超时了。之后看ai给的先计算了前缀的和再计算，但提交了几次都是WA，且内存两万KB，太大了。无奈看了答案，相比于我的，显然更加巧妙，让垃圾自己堆叠起来，然后取最高。       好几个小时（卡了好久）

代码： 

```python
d=int(input())
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
laji=[[0]*1025 for _ in range(1025)]
ans=[]
for a,b,c in lst:
    for i in range(max(a-d,0),min(a+d+1,1025)):
        for j in range(max(b-d,0),min(b+d+1,1025)):
            laji[i][j]+=c
max_=0
count=0
for k in range(1025):
    for l in range(1025):
        if laji[k][l]>max_:
            max_=laji[k][l]
            count=1
        elif laji[k][l]==max_:
            count+=1
print(count,max_)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-13 164115](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-13 164115.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：

刚开始按自己的思路做，写了一大串，特别长，自以为没问题，却WA了好几次。无奈求ai给个思路，一看到up，down两个计数器，立马就想出来了。哎，为什么没想到呢     20分钟

代码：

```python
def bd(nums):
    if len(nums)<=2:
        return len(set(nums))
    up=down=1
    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]:
            up=down+1
        elif nums[i]<nums[i-1]:
            down=up+1
    return max(up,down)
n=int(input())
nums=list(map(int,input().split()))
print(bd(nums))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-13 223715](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-13 223715.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：

动态规划问题，虽然知道大致步骤，但不同题信息不一样，还是没能把握dp的精髓         30分钟

代码：

```python
n=int(input())
lst=list(map(int,input().split()))
nums=[0]*(max(lst)+1)
for num in lst:
    nums[num]+=1
dp=[0]*(len(nums))
dp[1]=nums[1]*1
for i in range(2,len(nums)):
    dp[i]=max(dp[i-1],dp[i-2]+nums[i]*i)
print(dp[len(nums)-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-13 232813](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-13 232813.png)



### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：

刚开始觉得思路很清晰，从小马开始，打不过就拼掉国王最大的马，平局就不加分。WA了好几次，样例都对。。。没办法，问通义千问，给的答案不如自己的靠谱。没办法，只能看了答案，学习了这个双指针的做法。       2小时

代码：

```python
while True:
    n=int(input())
    if n==0:
        break
    horse1=list(map(int,input().split()))
    horse2=list(map(int,input().split()))
    horse1.sort()
    horse2.sort()
    ans=0
    t_start=0
    t_end=n-1
    k_start=0
    k_end=n-1
    while t_start<=t_end:
        if horse1[t_start]>horse2[k_start]:
            ans+=200
            t_start+= 1
            k_start+= 1
        elif horse1[t_end] >horse2[k_end]:
            ans+=200
            t_end-= 1
            k_end-= 1
        else:
            if horse1[t_start] <horse2[k_end]:
                ans-=200
            t_start+=1
            k_end-=1
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-14 142902](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-14 142902.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

虽然我自己AC不了，但基本思路是有的，题目没有特别难。最后一题同样思路清晰，样例也过了，就是AC不了，很是难受。小岛周长虽然不是补一圈0那个简单的算法，但还是完全靠自己AC的，挺有成就感的（作为代码初学者，我这卑微的成就感）。有进步，可以，继续努力。



