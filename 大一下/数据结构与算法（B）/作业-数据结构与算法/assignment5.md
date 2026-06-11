# Assignment #5: 链表、栈、队列和归并排序

Updated 1348 GMT+8 Mar 17, 2025

2025 spring, Complied by <mark>同学的姓名、院系</mark>

张洺瑜   地球与空间科学学院

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

### LC21.合并两个有序链表

linked list, https://leetcode.cn/problems/merge-two-sorted-lists/

思路：

判断l1和l2的节点大小，将较小的那个接到结果链表的后面。最后将剩余的节点全部接到后面。

代码：

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre=ListNode(-1)
        prev=pre
        while list1 and list2:
            if list1.val<=list2.val:
                prev.next=list1
                list1=list1.next
            else:
                prev.next=list2
                list2=list2.next
            prev=prev.next
        prev.next = list1 if list1 is not None else list2
        return pre.next
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-18 223818](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-18 223818.png)



### LC234.回文链表

linked list, https://leetcode.cn/problems/palindrome-linked-list/

<mark>请用快慢指针实现。</mark>

利用快慢指针，将链表分为两半。然后比较两边的链表是否相等。

代码：

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针
        if not head or not head.next:
            return True
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev,cur=None,slow
        while cur:
            next_=cur.next
            cur.next=prev
            prev=cur
            cur=next_
        left,right=prev,head
        while left:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-18 224133](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-18 224133.png)



### LC1472.设计浏览器历史记录

doubly-lined list, https://leetcode.cn/problems/design-browser-history/

<mark>请用双链表实现。</mark>

ok，又长知识了，对于链表更加熟悉了。
创建一个双向链表，直接进行操作。总感觉这道题的visit的实现非常适合链表的特性。

代码：

```python
class Node:
    def __init__(self,val):
        self.val=val
        self.pre=None
        self.next=None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur=Node(homepage)

    def visit(self, url: str) -> None:
        new=Node(url)
        self.cur.next=new
        new.pre=self.cur
        self.cur=new
    def back(self, steps: int) -> str:
        while self.cur.pre is not None and steps!=0:
            self.cur=self.cur.pre
            steps-=1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next is not None and steps!=0:
            self.cur=self.cur.next
            steps-=1
        return self.cur.val
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-19 144413](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-19 144413.png)



### 24591: 中序表达式转后序表达式

stack, http://cs101.openjudge.cn/practice/24591/

思路：

遇到数字，添加到输出栈；遇到左括号，添加到运算符栈；遇到运算符，根据栈顶运算符的优先级大小进行不同的操作；遇到右括号，则将栈顶元素不断压入输出栈中，直到遇到左括号，将左括号弹出。

代码：

```python
n=int(input())
for _ in range(n):
    string=list(input())
    num=''
    stack,ans=[],[]
    lst=['+','-','*','/']
    for i in string:
        if i.isdigit() or i=='.':
            num+=i
        else:
            if num!='':
                ans.append(num)
            num=''
            if i=='(':
                stack.append(i)
            elif i==')':
                while stack and stack[-1]!='(':
                    ans.append(stack.pop())
                stack.pop()
            elif i=='+' or i=='-':
                while stack and stack[-1] in lst:
                    ans.append(stack.pop())
                stack.append(i)
            elif i=='*' or i=='/':
                while stack and stack[-1] in lst:
                    if stack[-1]=='*' or stack[-1]=='/':
                        ans.append(stack.pop())
                    else:
                        break
                stack.append(i)
    if num!='':
        ans.append(num)
    while stack:
        ans.append(stack.pop())
    print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-17 221410](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-17 221410.png)



### 03253: 约瑟夫问题No.2

queue, http://cs101.openjudge.cn/practice/03253/

<mark>请用队列实现。</mark>

神奇，头一次知道deque的rotate用法，之前是一点都没有接触到（或许是我忘了也说不定？），太适合解这种问题了。

代码：

```python
from collections import deque
def rotate_(n,p,m):
    if n==0:return
    queue=deque(range(1,n+1))
    queue.rotate(-p+1)
    ans=[]
    while queue:
        queue.rotate(-m+1)
        ans.append(queue.popleft())
    print(','.join(map(str,ans)))

while True:
    n,p,m=map(int,input().split())
    if n==p==m==0:
        break
    rotate_(n,p,m)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-19 140808](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-19 140808.png)



### 20018: 蚂蚁王国的越野跑

merge sort, http://cs101.openjudge.cn/practice/20018/

思路：

先是直接用的归并排序，之前也做过归排的题。之后看见群里用的bisect，二分查找方法，感觉代码非常简洁，思路简单直接。
不过还是归并排序运行更快一些。

代码：

```python
### 归并排序
def merge_sort(lst,count):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left=merge_sort(lst[:mid],count)
    right=merge_sort(lst[mid:],count)
    return merge(left,right,count)
def merge(left,right,count):
    sorted_arr=[]
    i=j=0
    while i<len(left) and j< len(right):
        if left[i]>=right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
            count[0]+=len(left)-i
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
n=int(input())
speeds=[int(input()) for _ in range(n)]
count=[0]
merge_sort(speeds,count)
print(count[0])

### bisect

import bisect
n=int(input())
ans=0
sort_=[]
for _ in range(n):
    speed=int(input())
    idx=bisect.bisect_left(sort_,speed)
    ans+=idx
    sort_.insert(idx,speed)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-19 202643](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-19 202643.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次学到了不少，双向链表、快慢指针、还有deque中的rotate用法，还巩固了归并排序。不过还是有很多亟待提高的地方。。。leetcode周赛我也参加了几次，除了几周前有一次靠宿舍里的数学大佬答对了3个题，这几次大多是1道题，偶尔是两道（取决于中等题的难度）。。。还是要多加练习，加油！









