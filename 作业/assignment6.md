# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：

怎么说，只能说我太菜了，完全不会。看了答案也不知道怎么递归的，这才第一道题。。。        30分钟

代码：

```python
def hnt(n,a,c,b):
    if n==0:
        return
    hnt(n-1,a,b,c)
    print(f"{a}->{c}")
    hnt(n-1,b,c,a)
n=int(input())
print(2**n-1)
hnt(n,'A','C','B')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

<img src="C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-31 231132.png" alt="屏幕截图 2024-10-31 231132" style="zoom:50%;" />



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：

从头遍历到尾，去除使用过的元素，直到全部数字都使用过      1小时

代码：

```python
#正常版
def generate_permutations(nums, prefix=[]):
    if not nums:
        print(' '.join(map(str, prefix)))
    else:
        for i in range(len(nums)):
            nums1=nums[:i]+nums[i+1:]  #去除使用过的元素
            prefix1=prefix+[nums[i]]
            generate_permutations(nums1,prefix1)

def print_permutations(n):
    nums=[int(a) for a in range(1,n+1)]
    generate_permutations(nums)
n=int(input())
print_permutations(n)

#作弊版
from itertools import permutations
def print_permutations(n):
    numbers=list(range(1,n+1))
    perms=permutations(numbers)
    for perm in perms:
        print(' '.join(map(str, perm)))
n=int(input())
print_permutations(n)
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-11-02 232617](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-02 232617.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：

这应该是很简单的dp问题了，不过我还是没有抓住dp思路。经过这道试题，算是了解了基本思想     2小时

代码：

```python
k=int(input())
missile=list(map(int,input().split()))
dp=[1]*k
for i in range(1,k):
    for j in range(i):
        if missile[j]>=missile[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-02 212053](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-02 212053.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：

新增一个需要dp的变量，着实头疼，无奈看答案。遍历所有重量的背包，把符合的全塞进去，最后输出最大值    2小时

代码：

```python
n,b=map(int,input().split())
value=list(map(int,input().split()))
weight=list(map(int,input().split()))
dp=[[0]*(b+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(b+1):
        if weight[i-1]<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i-1]]+value[i-1])
        else:
            dp[i][j]=dp[i-1][j]
print(max(max(dp)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-02 221532](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-02 221532.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：

在全排列的基础上增加了判断是否符合八皇后的函数，储存在列表里。      2小时

代码：

```python
def safe(prefix):
    num=len(prefix)
    set1=set()
    set2=set()
    for i in range(num):
        if (i-prefix[i]) in set1 or (i+prefix[i]) in set2:
            return False
        set1.add(i - prefix[i])
        set2.add(i + prefix[i])
    return True

def generate_permutations(nums, prefix=[],ans=[]):
    if not nums:
        if safe(prefix):
            ans.append(''.join(map(str,prefix)))

    else:
        for i in range(len(nums)):
            nums1=nums[:i]+nums[i+1:]
            prefix1=prefix+[nums[i]]
            generate_permutations(nums1,prefix1)
    return ans
n=int(input())
nums=list(range(1,9))
ans1=generate_permutations(nums)
for _ in range(n):
    x=int(input())
    print(ans1[x-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：

有了前几道题的训练，还是有点思路的，虽然但是，最后还是看了答案完成最后一步，大体思路已经有了。    30分钟

代码：

```python
n,a,b,c=map(int,input().split())
ls=sorted([a,b,c])
dp=[-1]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for l in ls:
        if i>=l and dp[i-l]!=-1:
            dp[i]=max(dp[i],dp[i-l]+1)
print(dp[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-03 194458](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-11-03 194458.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

dp、递归的出现着实把我难傻了。真的不会。经过这次作业训练，有收获肯定是有那么一点的，但不多。下回再碰到这样的题，估计只会有一些思路，但不知道怎么用代码表现出来。dp像是从底往上算，输出最后的结果。递归像是不断轮回到尽头，再倒放到结果？



