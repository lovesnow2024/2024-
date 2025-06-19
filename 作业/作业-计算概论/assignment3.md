# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==（请改为同学的姓名、院系）==

张洺瑜  地球与空间科学学院

**说明：**

1）Oct⽉考： AC6==（请改为同学的通过数）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。                           **成绩**：<u>AC4</u>

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：

利用ASCII表对字母进行解码，大写，小写分别解码     5分钟

代码

```python
k=int(input())
s=list(input())
for i in range(len(s)):
    if ord(s[i])>=ord('a'):

        s[i]=chr((ord(s[i])-ord('a')-k)%26+ord('a'))
    else:
        s[i]=chr((ord(s[i])-ord('A')-k)%26+ord('A'))
print(''.join(s))

```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-10-11 155844](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-11 155844.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：

很简单的题，固定的两位数，直接求和即可    2分钟

代码

```python
m,n=input().split()
a=int(m[0])*10+int(m[1])
b=int(n[0])*10+int(n[1])
print(a+b)

```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-10-11 160145](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-11 160145.png)



### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：

根据题意创建列表，进行循环求和，之后再检验最后一位对应情况    7分钟

代码

```python
n=int(input())
for _ in range(n):
    num=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    yz=['1','0','X','9','8','7','6','5','4','3','2']
    sf=list(input())
    ans=0
    for i in range(len(num)):
        ans+=num[i]*int(sf[i])
    y=ans%11
    if y<=10:
        if sf[17]==yz[y]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-10-11 160352](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-11 160352.png)



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：

之前做过一样的题，简单，只需注意用除法时将类型改为整数，否则是浮点数类型   3分钟

代码

```python
n=int(input())
while n!=1:
    if n%2==0:
        a=int(n/2)
        print(f"{n}/2={a}")
        n=a
    else:
        b=n*3+1
        print(f"{n}*3+1={b}")
        n=b
else:
    print('End')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-10-11 160616](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-11 160616.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：

我是一步步判断的，十分加十分的繁琐，之后找ai给了优化的答案，豁然开朗，将数字与字母对应起来，确实之后计算要方便得多        如果算上考试时间，得有2小时（泪目），几乎一直在做这道题

##### 代码

```python
# 
def lm(n):
    num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    zm=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    ans=''
    i=0
    while n>0:
        for _ in range(n//num[i]):
            ans+=zm[i]
            n-=num[i]
        i+=1
    return ans
def sz(m):
    dct={'M':1000,'C':100,'D':500,'X':10,'L':50,'V':5,'I':1}
    ans=0
    for i in range(len(m)):
        if i>0 and dct[m[i]]>dct[m[i-1]]:
            ans+=dct[m[i]]-2*dct[m[i-1]]
        else:
            ans+=dct[m[i]]
    return ans
s=input()
if s.isdigit():
    print(lm(int(s)))
else:
    print(sz(s))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-10-11 160806](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-10-11 160806.png)



### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：

实在不会，不看答案根本无从下手，有一点思路，但不知道怎么做

代码

```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

前四道题很简单，但后两道便开始吃力了，前一道还好，但用了一堆if终于把自己弄懵了，错了也不知道错在哪，最终也没搞出来，后一道基本不会。不过还是学到了很多，了解了之前一直觉得复杂的字典的用法，还有isdigit()这个判断是否是整数的用法，以及更方便的数据类型deque、解包操作符的用法。

可以说已有很大的进步，但还是不足，之后需要加大投入时间了。









