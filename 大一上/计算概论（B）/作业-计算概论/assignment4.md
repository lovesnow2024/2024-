# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院111

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：

将价值为负数的电视放入一个列表中排序，取前m项或是负数电视的数量，求和   5分钟

代码

```python
# 
n,m=map(int,input().split())
value=list(map(int,input().split()))
value2=[value[i] for i in range(n) if value[i]<0]
value2.sort()
ans=0
for i in range(min(m,len(value2))):
    ans-=value2[i]
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-16 150649](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-16 150649.png)



### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：

关键一步就是将列表排序，没什么难度   3分钟

代码

```python
n=int(input())
money=list(map(int,input().split()))
money.sort(reverse=True)
count=0
money1=0
ans=sum(money)
for i in range(n):
    if money1<=ans:
        count+=1
        money1+=money[i]
        ans-=money[i]
    else:
        break
print(count)

```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-10-18 193559](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-18 193559.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：

每一行最小值相加或每一列最小值相加，取两者中更小的    20分钟（思考）

代码

```python
n=int(input())
for _ in range(n):
    m=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    min_b=min(b)
    sum_ans3=sum(x+min_b for x in a)
    min_a=min(a)
    sum_ans4 = sum(y + min_a for y in b)
    print(min(sum_ans3, sum_ans4))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-18 210325](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-18 210325.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：

分组凑整     7分钟

代码

```python
from math import ceil
n=int(input())
num=list(map(int,input().split()))
a=num.count(1)
b=num.count(2)
c=num.count(3)
ans=num.count(4)
if a<=c:
    ans+=c+ceil(b/2)
else:
    ans+=c
    if b%2==0:
        ans+=int(b/2)+ceil((a-c)/4)
    else:
        if a-c>=2:
            ans+=ceil(b/2)+ceil((a-c-2)/4)
        else:
            ans+=ceil(b/2)
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-18 215053](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-18 215053.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：

想了半天，怎么也是超时，我也试了试埃氏筛法，可能是由于我不理解，将范围弄宽了，也超时了，思考了一整天，还是去看了答案，找到了这个同样用埃筛的学长答案，终于是理解了埃筛的具体步骤。学长用%1==0来判断整数的方法也是我没有想到的   1.5天

代码

```python
n=int(input())
lst=[int(a) for a in input().split()]
l=[1]*(10**6)
l[0]=0
for i in range(1,10**3):
    if l[i]==1:
        for j in range(2*i+1,10**6,i+1):
            l[j]=0
for k in range(n):
    a=lst[k]
    if a**0.5%1==0:
        b=int(a**0.5)
        if l[b-1]==1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-19 155918](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-19 155918.png)



### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：

知道要排序，但不知道怎么成功排序（有8987、898这样的数字干扰），直到看到群里数院大佬的解法，醍醐灌顶啊，深感钦佩，佩服佩服     2小时

代码

```python
n=int(input())
v=[[a,int(a)/(10**len(a)-1)] for a in input().split()]
v1=sorted(v,key=lambda x:x[1])
ans=[num for num,i in v1]
min_num=''.join(ans)
max_num=''.join(ans[::-1])
print(max_num,min_num)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-10-19 154526](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-19 154526.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

前四道题目中规中矩，后两道难，尤其是前一道，不知已经超时多少次了

芯片那个题本以为是每行和每列都要有，真的是没一点思路，不过好在题目并非如此

我还是不喜欢英文题目，英文不好的我看的太难受，还总担心会不会漏掉什么，而翻译有时候不尽人意，哎

前段时间着实懈怠得很，拖欠了太多，后面加把劲跟上



