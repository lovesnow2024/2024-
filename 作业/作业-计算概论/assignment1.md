# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==同学的名字 院系==

张洺瑜 地球与空间科学学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：分为能被四整除的以及不是整百的及3200倍数的，是整百且能被400整除以及不是3200倍数的，其他的。        

用时：10分钟



##### 代码

```python
# 
a=int(input())
if ((a%4==0 and a%100!=0) or a%400==0) and a%3200!=0:
    print('Y')
else:
    print('N')
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240913180005942](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240913180005942.png)



### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：腿数不可能是奇数，所以先除去奇数，剩下的偶数分为可被四整除的和不可被四整除的。全为鸡时数量最多。数量最少时，能被四整除的直接除以四，算作全为兔子；不能被四整除的，整除四再加一。

用时：5分钟



##### 代码

```python
#
a=int(input())
if a%2!=0:
    print('0'+' '+'0')
else:
    if a%4==0:
        b=a/2
        c=a/4
    else:
        b=a/2
        c=a//4+1
    print(int(c),int(b))

```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-09-13 175842](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-13 175842.png)

### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：先考虑一边的奇偶，在考虑另一边的奇偶

用时：3分钟



##### 代码

```python
# 
a=input().split()
m,n=int(a[0]),int(a[1])
if m%2==0:
    print(m//2*n)
else:
    v=n//2
    print(m//2*n+v)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-13 205301](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-13 205301.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：两边整除向上取

用时：5分钟



##### 代码

```python
#
w=input().split()
n,m,a=int(w[0]),int(w[1]),int(w[2])
i=(m-0.0001)//a+1
j=(n-0.0001)//a+1
print(int(i+j))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-13 212116](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-13 212116.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：先将两列字符串变为小写，再用比较运算符直接进行比较

用时：10分钟



##### 代码

```python
# 
m=input().lower()
n=input().lower()
if m<n:
    print(-1)
elif m>n:
    print(1)
else:
    print(0)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-13 214206](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-13 214206.png)



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：将满足条件的结果放入列表当中，统计列表当中字符的数量

用时：6分钟



##### 代码

```python
# 
n=int(input())
num=[]
for i in range(n):
    a=input().split()
    s1,s2,s3=int(a[0]),int(a[1]),int(a[2])
    s=s1+s2+s3
    if s>=2:
        num.append(i)
print(len(num))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-13 215953](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-09-13 215953.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

作为一个代码小白，一个没怎么玩过电脑的初学者，Python让我感受到了计算机的魅力。这些练习题的确很基础，也让我学到了不少新的保留字。我对编程愈来愈感兴趣，我会更努力的学习，也得好好练习自己的盲打技能。

但对于难题，还是毫无头绪，有一种无力感。希望通过努力能够有所收获。



