# Assignment #6: 回溯、树、双向链表和哈希表

Updated 1526 GMT+8 Mar 22, 2025

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

### LC46.全排列

backtracking, https://leetcode.cn/problems/permutations/

思路：

回溯算法，探索所有的可能，如果不满足要求，则会回溯到上一步。探索完所有的可能解。

代码：

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,ans,path=[]):
            if not nums:
                ans.append(path[:])
            else:
                for i in range(len(nums)):
                    nums0=nums[:i]+nums[i+1:]
                    path0=path+[nums[i]]
                    backtrack(nums0,ans,path0)
       	ans=[]
        backtrack(nums,ans)
        return ans
   
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-22 165615](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-22 165615.png)



### LC79: 单词搜索

backtracking, https://leetcode.cn/problems/word-search/

思路：

不同于全排列，这道题第一眼想到的是dfs，也是回溯的一种。这道题完全靠自己写下来的，虽然运行时间上只打败了百分之十的人。。。

代码：

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,visited,x,y,count):
            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            if count==len(word):
                return True
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and ((nx,ny) not in visited) and board[nx][ny]==word[count]:
                    visited.add((nx,ny))
                    if dfs(board,visited,nx,ny,count+1):
                        return True
                    visited.remove((nx,ny))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    visited=set()
                    visited.add((i,j))
                    if dfs(board,visited,i,j,1):
                        return True
        return False

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-22 172409](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-22 172409.png)



### LC94.二叉树的中序遍历

dfs, https://leetcode.cn/problems/binary-tree-inorder-traversal/

思路：

回溯解决，主要要了解中序遍历的定义。

代码：

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-24 170251](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-24 170251.png)



### LC102.二叉树的层序遍历

bfs, https://leetcode.cn/problems/binary-tree-level-order-traversal/

思路：

bfs的做法，如同树形迷宫。每一层结束后将这一层的节点放入结果列表中，继续遍历下一层节点。一层一层往下走。

代码：

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        result,queue=[],deque([root])
        while queue:
            cur=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(cur)
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-24 171348](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-24 171348.png)



### LC131.分割回文串

dp, backtracking, https://leetcode.cn/problems/palindrome-partitioning/

思路：

回溯+枚举字符串；回溯加dp处理。动态规划我是真的不熟悉。。。

代码：

```python
###backtracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        path=[]
        n=len(s)
        def dfs(i,path):
            if i==n:
                ans.append(path[:])
                return
            for j in range(i,n):
                tmp=s[i:j+1]
                if tmp==tmp[::-1]:
                    path.append(tmp)
                    dfs(j+1,path)
                    path.pop()
        dfs(0,path)
        return ans

    
###动态规划+backtracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        result=[]
        for i in range(n):
            dp[i][i]=True
        for l in range(2,n+1):   ###这里的双重循环也算是处理回文问题的模版dp代码了吧
            for i in range(n-l+1):
                j=i+l-1
                if s[i]==s[j]:
                    if l==2:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
        def backtrack(start, path):
            if start == n:
                result.append(path[:])
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()
        backtrack(0,[])
        return result

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-22 181317](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-22 181317.png)



### LC146.LRU缓存

hash table, doubly-linked list, https://leetcode.cn/problems/lru-cache/

思路：

用的双向链表，不过对这些节点的指向改变着实有些懵，接下来会再去搞懂这道题，并看看其他的做法。

代码：

```python
class DNode:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.cache={}
        self.head=DNode()
        self.tail=DNode()
        self.head.next=self.tail
        self.tail.prev=self.head
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.move_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.move_head(node)
        else:
            node=DNode(key,value)
            self.cache[key]=node
            self.add_head(node)
            self.size+=1
            if self.size>self.capacity:
                removed=self.remove_tail()
                del self.cache[removed.key]
                self.size-=1
    def add_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def removed_node(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def move_head(self,node):
        self.removed_node(node)
        self.add_head(node)
    def remove_tail(self):
        node=self.tail.prev
        self.removed_node(node)
        return node
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-24 184245](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-24 184245.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

对于新结构：树、链表，还是太不熟悉了，加上指针指向就感觉好绕，有时候根本不知道现在这个节点指向哪，值是多少。好晕的感觉。

前几天的每日选做有两道困难的bfs和dfs题，还是高看自己了，并不能完整的写下来。Robots那个在于不能按平常的“一步”思考，而是把“一秒”看成“一步”，这样才能保证输出是最少秒。2048那道题思路并不难，难点在于如何生成操作后的新列表，比较繁琐。

做到现在，浑浑噩噩的，我也不知道有没有进步，应该是有那么一些进步的，却并不多。最后到底能不能AC5以上呢，好难受。









