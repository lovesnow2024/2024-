# Assignment #C: 202505114 Mock Exam

Updated 1518 GMT+8 May 14, 2025

2025 spring, Complied by <mark>同学的姓名、院系</mark>

张洺瑜  地球与空间科学学院

> **说明：**
>
> 1. **⽉考**：AC0（缺考）<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
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

### E06364: 牛的选举

http://cs101.openjudge.cn/practice/06364/

思路：

简单排序，不过感觉还是慢了，肯定还能更快。

代码：

```python
n,k=map(int,input().split())
lst=[]
for i in range(1,n+1):
    a,b=map(int,input().split())
    lst.append([i,a,b])
lst.sort(key=lambda x:x[1],reverse=True)
result=[]
for j in range(k):
    idx,a,b=lst[j]
    result.append([idx,b])
result.sort(key=lambda x:x[1])
print(result[-1][0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-14 211330](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-14 211330.png)



### M04077: 出栈序列统计

http://cs101.openjudge.cn/practice/04077/

思路：

直接回溯。如果还有没加的数，就加入；如果可以出栈，就输出。

代码：

```python
def backtrack(count,stack,cur,ans,n):
    if count==n:
        ans[0]+=1
        return
    if cur<=n:
        backtrack(count,stack+[cur],cur+1,ans,n)
    if stack:
        backtrack(count+1,stack[:-1],cur,ans,n)
n=int(input())
ans=[0]
backtrack(0,[],1,ans,n)
print(ans[0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-14 212544](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-14 212544.png)



### M05343:用队列对扑克牌排序

http://cs101.openjudge.cn/practice/05343/

思路：

犹豫半天，不敢下手，怕直接模拟太慢了，又没有别的办法。好吧，这样也是做出来了。

代码：

```python
n=int(input())
cards=list(input().split())
lst=[[] for _ in range(9)]
for s in cards:
    x,y=s[0],int(s[1])
    lst[y-1].append(s)
lst2=[[] for _ in range(4)]
for l in lst:
    if l:
        for st in l:
            x,y=st[0],st[1]
            lst2[ord(x)-ord('A')].append(st)
for i in range(1,10):
    print(f"Queue{i}:{' '.join(lst[i-1])}")
for j in range(4):
    print(f"Queue{chr(j+ord('A'))}:{' '.join(lst2[j])}")
result=[]
for row in lst2:
    result.extend(row)
print(' '.join(result))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-14 215432](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-14 215432.png)



### M04084: 拓扑排序

http://cs101.openjudge.cn/practice/04084/

思路：

之前做过两道这样的题，还算是比较熟悉。不过我可能很难去想到是否有重复边。。。

代码：

```python
from collections import defaultdict
import heapq
v,a=map(int,input().split())
dic=defaultdict(set)
in_degree=[0]*(v+1)
for _ in range(a):
    x,y=map(int,input().split())
    if y not in dic[x]:
        in_degree[y]+=1
    dic[x].add(y)
heap=[]
for i in range(1,v+1):
    if in_degree[i]==0:
        heapq.heappush(heap,i)
result=[]
while heap:
    u=heapq.heappop(heap)
    result.append(f"v{u}")
    for x in dic[u]:
        in_degree[x]-=1
        if in_degree[x]==0:
            heapq.heappush(heap,x)
print(*result)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-15 091917](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-15 091917.png)



### M07735:道路

Dijkstra, http://cs101.openjudge.cn/practice/07735/

思路：

做了几道dijkstra后果然熟练了很多，这道题也是轻松拿下。

代码：

```python
from collections import defaultdict
import heapq
k=int(input())
n=int(input())
r=int(input())
dic=defaultdict(list)
for _ in range(r):
    s,d,l,t=map(int,input().split())
    dic[s].append([d,l,t])
ans=-1
heap=[]
heapq.heappush(heap,(0,1,0))
while heapq:
    cur_length,cur_place,cur_money=heapq.heappop(heap)
    if cur_place==n and cur_money<=k:
        ans=cur_length
        break
    for d,l,t in dic[cur_place]:
        if cur_money+t>k:
            continue
        heapq.heappush(heap,(cur_length+l,d,cur_money+t))
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-15 093251](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-15 093251.png)



### T24637:宝藏二叉树

dp, http://cs101.openjudge.cn/practice/24637/

思路：

树状dp。呵呵，对于dp一向是敬而远之，总是不知道怎么表示转移方程。这道dp的思路还算不是太复杂。

代码：

```python
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def dfs(node):
    if not node:
        return (0,0)
    left=dfs(node.left)
    right=dfs(node.right)
    case1=node.val+left[0]+right[0]
    case2=max(left)+max(right)
    return (case2,case1)
n=int(input())
values=list(map(int,input().split()))
root=TreeNode(values[0])
queue=deque([root])
lst=deque(values[1:])
while queue:
    node=queue.popleft()
    if lst:
        node.left=TreeNode(lst.popleft())
        queue.append(node.left)
    if lst:
        node.right=TreeNode(lst.popleft())
        queue.append(node.right)
    if not lst:
        break
print(max(dfs(root)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-05-15 095707](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-05-15 095707.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

缺考了，应该是能AC5的。如果拓扑排序那道题没有重复边的话，概率能冲进AC6。咱也不期待期末能AK了，只希望能AC5就心满意足了。再多练习点，尤其是dp。









