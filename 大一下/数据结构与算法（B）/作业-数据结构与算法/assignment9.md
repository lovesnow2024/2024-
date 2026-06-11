# Assignment #9: Huffman, BST & Heap

Updated 1834 GMT+8 Apr 15, 2025

2025 spring, Complied by <mark>同学的姓名、院系</mark>

张洺瑜 地球与空间科学学院

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

### LC222.完全二叉树的节点个数

dfs, https://leetcode.cn/problems/count-complete-tree-nodes/

思路：

dfs做法确实较为简单

代码：

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            return 1+left+right
        return dfs(root)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-17 193407](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-17 193407.png)



### LC103.二叉树的锯齿形层序遍历

bfs, https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

思路：

层序遍历的稍稍进阶版，增加一个flag使遍历的顺序发生变化。关键是deque的双端插入、删除的支持。

代码：

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[[root.val]]
        queue=deque([root])
        flag=0
        while queue:
            result=[]
            if flag%2==1:
                for _ in range(len(queue)):
                    node=queue.popleft()
                    if node.left:
                        result.append(node.left.val)
                        queue.append(node.left)
                    if node.right:
                        result.append(node.right.val)
                        queue.append(node.right)
            else:
                for _ in range(len(queue)):
                    node=queue.pop()
                    if node.right:
                        result.append(node.right.val)
                        queue.appendleft(node.right)
                    if node.left:
                        result.append(node.left.val)
                        queue.appendleft(node.left)
            if result:
                ans.append(result)
            flag+=1
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-17 195902](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-17 195902.png)



### M04080:Huffman编码树

greedy, http://cs101.openjudge.cn/practice/04080/

思路：

想到用堆了，但没有想到这么用。取出最小的两个数，它们就是最下面的叶子，然后将他们的和加入堆中，不断循环。用取出的次数来模拟路径的长度。

代码：

```python
import heapq
n=int(input())
node_values=list(map(int,input().split()))
heapq.heapify(node_values)
ans=0
while len(node_values)>1:
    a=heapq.heappop(node_values)
    b=heapq.heappop(node_values)
    sum_=a+b
    ans+=sum_
    heapq.heappush(node_values,sum_)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-17 202237](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-17 202237.png)



### M05455: 二叉搜索树的层次遍历

http://cs101.openjudge.cn/practice/05455/

思路：

分为两个步骤，一个是建树，另一个是层序遍历。后一个之前做过，所以关键就在于建树。搜索树的建立相当于构建有序列表。想象一下，一个数从二叉树根处下落，不断根据自身大小与节点值的比较选择向下走的方向，直到遇到一个空节点，然后在这里“落座”。

代码：

```python
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build_tree(root,value):
    if root is None:
        return TreeNode(value)
    if value<root.val:
        root.left=build_tree(root.left,value)
    elif value>root.val:
        root.right=build_tree(root.right,value)
    return root
def level_order(root):
    if not root:
        return []
    result=[]
    queue=deque([root])
    while queue:
        size=len(queue)
        for _ in range(size):
            node=queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
nums=list(map(int,input().split()))
root=None
seen=set()
for num in nums:
    if num not in seen:
        seen.add(num)
        root=build_tree(root,num)
result=level_order(root)
print(*result)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-17 202741](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-17 202741.png)



### M04078: 实现堆结构

手搓实现，http://cs101.openjudge.cn/practice/04078/

类似的题目是 晴问9.7: 向下调整构建大顶堆，https://sunnywhy.com/sfbj/9/7

思路：

通过二分插入实现。

代码：

```python
#二分插入
import bisect
n=int(input())
lst=[]
for _ in range(n):
    measure=list(map(int,input().split()))
    if measure[0]==1:
        bisect.insort_left(lst,measure[1])
    else:
        print(lst.pop(0))
#手搓二分插入
def bisect_insert(lst,target):
    low,high=0,len(lst)
    while low<high:
        mid=(low+high)//2
        if lst[mid]<target:
            low=mid+1
        else:
            high=mid
    return low
n=int(input())
lst=[]
for _ in range(n):
    measure=list(map(int,input().split()))
    flag=measure[0]
    if flag==1:
        target=measure[1]
        idx=bisect_insert(lst,target)
        lst.insert(idx,target)
    else:
        print(lst.pop(0))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-17 210905](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-17 210905.png)

![屏幕截图 2025-04-17 210832](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-17 210832.png)

### T22161: 哈夫曼编码树

greedy, http://cs101.openjudge.cn/practice/22161/

思路：

不会，困难题还是太难为我了。头一次用def __ lt __制定比较规则。

代码：

```python
from collections import defaultdict
import heapq
class HuffmanNode:
    def __init__(self,chars,freq,left=None,right=None):
        self.chars=chars
        self.freq=freq
        self.left=left
        self.right=right
    def __lt__(self, other):
        if self.freq!=other.freq:
            return self.freq<other.freq
        return min(self.chars)<min(other.chars)
def build_huffman_tree(char_freq):
    heap=[]
    for char,freq in char_freq.items():
        heapq.heappush(heap,HuffmanNode({char},freq))
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        merged_chars=left.chars.union(right.chars)
        merged_freq=left.freq+right.freq
        merged_node=HuffmanNode(merged_chars,merged_freq,left,right)
        heapq.heappush(heap,merged_node)
    return heap[0] if heap else None
def build_codebook(root):
    codebook = {}
    def traverse(node, code):
        if not node.left and not node.right:
            char = min(node.chars)
            codebook[char] = code
            return
        if node.left:
            traverse(node.left, code + '0')
        if node.right:
            traverse(node.right, code + '1')
    traverse(root, '')
    return codebook


def build_decodebook(root):
    decodebook = {}
    def traverse(node, code):
        if not node.left and not node.right:
            char = min(node.chars)
            decodebook[code] = char
            return
        if node.left:
            traverse(node.left, code + '0')
        if node.right:
            traverse(node.right, code + '1')
    traverse(root, '')
    return decodebook

def encode(string,codebook):
    return ''.join(codebook[char] for char in string)


def decode(bits,decodebook):
    current = ''
    result = []
    for bit in bits:
        current += bit
        if current in decodebook:
            result.append(decodebook[current])
            current = ''
    return ''.join(result)

n=int(input())
dic=defaultdict(int)
for _ in range(n):
    parts=list(input().split())
    dic[parts[0]]=int(parts[1])
root = build_huffman_tree(dic)
codebook = build_codebook(root)
decodebook = build_decodebook(root)
while True:
    try:
        string=input()
        if string.isdigit():
            print(decode(string, decodebook))
        else:
            print(encode(string, codebook))
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-17 225312](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-17 225312.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

前五道题依旧还可以，不过Huffman着实没想到这么做。

最后一道困难题依旧太难为我了，实在不会做。

期中考试结束了，接下来要把之前的每日选做全部补回来。









