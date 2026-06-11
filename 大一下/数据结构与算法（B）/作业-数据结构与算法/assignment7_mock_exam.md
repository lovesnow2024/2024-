# Assignment #7: 20250402 Mock Exam

Updated 1624 GMT+8 Apr 2, 2025

2025 spring, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

> **说明：**
>
> 1. **⽉考**：AC0（未参与）<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
> 2. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E05344:最后的最后

http://cs101.openjudge.cn/practice/05344/



思路：

约瑟夫问题，用双端队列的rotate解决。

代码：

```python
from collections import deque
n,k=map(int,input().split())
person=list(range(1,n+1))
persons=deque(person)
result=[]
while len(persons)>1:
    persons.rotate(-k+1)
    result.append(persons.popleft())
print(*result)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-02 194918](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-02 194918.png)



### M02774: 木材加工

binary search, http://cs101.openjudge.cn/practice/02774/



思路：

二分查找，能做出来，说明我的确有进步了。

代码：

```python
def check(lengths,k,mid,n):
    count=0
    for i in range(n):
        cur=lengths[i]
        while cur>=mid:
            cur-=mid
            count+=1
            if count>=k:
                return True
    return False
n,k=map(int,input().split())
lengths=[int(input()) for _ in range(n)]
if sum(lengths)<k:
    print(0)
else:
    ans=0
    left,right=1,max(lengths)
    while left<=right:
        mid=(left+right)//2
        if check(lengths,k,mid,n):
            ans=mid
            left=mid+1
        else:
            right=mid-1
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-02 201046](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-02 201046.png)



### M07161:森林的带度数层次序列存储

tree, http://cs101.openjudge.cn/practice/07161/



思路：

先建树再输出后序遍历。练了很多树的题，这道题思路不是很难。但一遇到错误我就慌了，十分难受。

代码：

```python
from collections import deque
class TreeNode:
    def __init__(self,val,n):
        self.val=val
        self.children=[None]*n
def build_tree(lsts0,root):
    queue=deque([root])
    while queue:
        node=queue.popleft()
        for i in range(len(node.children)):
            if lsts0:
                val,idx=lsts0.popleft()
                new_node=TreeNode(val,idx)
                node.children[i]=new_node
                queue.append(new_node)
            else:
                return
def postorder(root):
    if not root:
        return []
    result=[]
    for child in root.children:
        result.extend(postorder(child))
    result.append(root.val)
    return result
n=int(input())
ans=[]
for _ in range(n):
    lst=list(input().split())
    lsts=[]
    for i in range(len(lst)//2):
        lsts.append((lst[i*2],int(lst[i*2+1])))
    lsts0=deque(lsts)
    a,b=lsts0.popleft()
    root=TreeNode(a,b)
    build_tree(lsts0,root)
    ans.append(postorder(root))
result=[item for row in ans for item in row]
print(' '.join(result))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-02 213143](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-02 213143.png)



### M18156:寻找离目标数最近的两数之和

two pointers, http://cs101.openjudge.cn/practice/18156/



思路：

双指针，先对列表排序，然后从两端向中间不断靠近。

代码：

```python
def find(s,i,j,t):
    ans=[]
    while i<j:
        current=s[i]+s[j]
        if current>t:
            ans.append([current, abs(t - current)])
            j-=1
        elif s[i]+s[j]==t:
            ans=[[t,0]]
            return ans
        else:
            ans.append([current,abs(t-current)])
            i+=1
    return ans
t=int(input())
s=list(map(int,input().split()))
s.sort()
i,j=0,len(s)-1
ans0=find(s,i,j,t)
ans1=sorted(ans0,key=lambda x:(x[1],x[0]))
print(ans1[0][0])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-02 203817](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-02 203817.png)



### M18159:个位为 1 的质数个数

sieve, http://cs101.openjudge.cn/practice/18159/



思路：

直接弄出2到10001之间的所有质数。考场上肯定写不下来，筛法早就忘光了。。。然后是范围处理有些问题，导致RE（这可比WA更让人难受）。。。

代码：

```python
def prime():
    nums=[True]*10002
    nums[0]=nums[1]=False
    p=2
    while p**2<=10001:
        if nums[p]:
            for i in range(p**2,10002,p):
                nums[i]=False
        p+=1
    primes=[j for j in range(11,10002) if nums[j] and j%10==1]
    return primes
t=int(input())
lst=prime()
for i in range(t):
    n = int(input())
    print(f"Case{i+1}:")
    count=0
    ans=[]
    for num in lst:
        if num<n:
            ans.append(num)
        else:
            break
    if ans:
        print(*ans)
    else:
        print('NULL')


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-02 213426](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-02 213426.png)



### M28127:北大夺冠

hash table, http://cs101.openjudge.cn/practice/28127/



思路：

就喜欢这种简单粗暴的题，dic [name] =  [  set(题目编号)  ,  n ]，直接排序

代码：

```python
m=int(input())
dic={}
for _ in range(m):
    name,question,state=input().split(',')
    if name not in dic:
        dic[name]=[set(),0]
        if state=='yes':
            dic[name][0].add(question)
        dic[name][1]+=1
    else:
        if state=='yes':
            dic[name][0].add(question)
        dic[name][1]+=1
result=[]
for i in dic:
    a=len(dic[i][0])
    b=dic[i][1]
    result.append([i,a,b])
result.sort(key=lambda x:(-x[1],x[2],x[0]))
for i in range(min(len(result),12)):
    print(i+1,result[i][0],result[i][1],result[i][2])
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2025-04-02 214855](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-02 214855.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

题目最难的是中等题，但我最多能AC5，筛法实在是忘干净了。通过这些题，我发现我处理细节的能力不足，导致很多问题出在循环条件等小问题上，还是要多加练习。如果没有提示，我是真的很难第一时间想出来用什么。虽然‘木材加工’是十分明显的二分查找，但我并没有第一时间想到。









