# Assignment #8: 树为主

Updated 1704 GMT+8 Apr 8, 2025

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

### LC108.将有序数组转换为二叉树

dfs, https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

思路：

利用二分的方法，将列表分为两半，当做左右子树进行同样的操作。

代码：

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left,right):
            if left>right:
                return None
            mid=(left+right+1)//2
            root=TreeNode(nums[mid])
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        return helper(0,len(nums)-1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-10 230218](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-10 230218.png)



### M27928:遍历树

 adjacency list, dfs, http://cs101.openjudge.cn/practice/27928/

思路：

不是太需要构建数，直接用字典更方便。创建一个列表，每到一个节点将自身与子节点排序，在遍历时遇到新的节点（创建集合存储遍历过的节点）进行递归。

代码：

```python
n=int(input())
nums_lst=set()
nodes={}
parent={}
for _ in range(n):
    parts=list(map(int,input().split()))
    value=parts[0]
    child=parts[1:] if len(parts)>1 else []
    nodes[value]=child
    nums_lst.add(value)
    for i in parts[1:]:
        parent[i]=value
root=0
for num in list(nums_lst):
    if num not in parent:
        root=num
        break
visited=set()
result=[]
def print_(node):
    all_nodes=[node]+nodes[node]
    sorted_nodes=sorted(all_nodes)
    for value in sorted_nodes:
        if value !=node and value not in visited:
            if value in nodes:
                print_(value)
        elif value==node and value not in visited:
            visited.add(node)
            result.append(node)
print_(root)
for i in result:
    print(i)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-10 230330](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-10 230330.png)



### LC129.求根节点到叶节点数字之和

dfs, https://leetcode.cn/problems/sum-root-to-leaf-numbers/

思路：

刚做的时候犯了一个错误，误以为只要左右有一个为空节点，就返回。。。太傻了，

代码：

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        def backtrack(root,string):
            nonlocal ans
            if root is None:
                return
            string+=str(root.val)
            if  not root.left and not root.right:
                ans+=int(string)
                string=''
                return 
            backtrack(root.left,string)
            backtrack(root.right,string)
        backtrack(root,'')
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-10 232556](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-10 232556.png)



### M22158:根据二叉树前中序序列建树

tree, http://cs101.openjudge.cn/practice/24729/

思路：

根据前序遍历首位字符是根节点，中序遍历中根节点将左右字数分割这两条可以找到根节点并对两个序列分割为左右字数，再进行递归操作。

代码：

```python
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build_tree(preorder,inorder):
    if not preorder or not inorder:
        return None
    root_val=preorder[0]
    root=TreeNode(root_val)
    mid_index=inorder.index(root_val)
    root.left=build_tree(preorder[1:mid_index+1],inorder[:mid_index])
    root.right=build_tree(preorder[mid_index+1:],inorder[mid_index+1:])
    return root
def postorder(root):
    if root is None:
        return ''
    return postorder(root.left)+postorder(root.right)+root.val
while True:
    try:
        preorder=input()
        inorder=input()
        root = build_tree(preorder, inorder)
        print(postorder(root))
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-10 232100](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-10 232100.png)



### T24729:括号嵌套树

dfs, stack, http://cs101.openjudge.cn/practice/24729/

思路：

没有构建树。首先，前序遍历直接将括号剔除就行。后序遍历也可以用栈来解决。幸亏没有要求中序遍历，不然我就得建树了。

代码：

```python
string=input()
preorder=''
for i in string:
    if i !='(' and i != ')' and i !=',':
        preorder+=i
postorder=''
stack1=[]
stack2=[]
for s in string:
    if s =="(":
        stack2.append(s)
    elif s==')':
        if stack2 and stack1:
            postorder+=stack1.pop()
            stack2.pop()
    elif s==',':
        postorder+=stack1.pop()
    else:
        stack1.append(s)
if stack1:
    postorder+=stack1.pop()
print(preorder)
print(postorder)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-10 231913](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-10 231913.png)



### LC3510.移除最小数对使数组有序II

doubly-linked list + heap, https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/

思路：

直接抄的题解里的答案（灵神的），实在不会做。等期中过去再去好好弄明白。

代码：

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n=len(nums)
        h=[]
        dec=0
        for i,(x,y) in enumerate(pairwise(nums)):
            if x>y:
                dec+=1
            h.append((x+y,i))
        heapify(h)
        lazy=defaultdict(int)
        left=list(range(-1,n))
        right=list(range(1,n+1))
        ans=0
        while dec:
            ans+=1
            while lazy[h[0]]:
                lazy[heappop(h)]-=1
            s,i=heappop(h)
            nxt=right[i]
            if nums[i]>nums[nxt]:
                dec-=1
            pre=left[i]
            if pre>=0:
                if nums[pre]>nums[i]:
                    dec-=1
                if nums[pre]>s:
                    dec+=1
                lazy[(nums[pre]+nums[i],pre)]+=1
                heappush(h,(nums[pre]+s,pre))
            nxt2=right[nxt]
            if nxt2<n:
                if nums[nxt]>nums[nxt2]:
                    dec-=1
                if s>nums[nxt2]:
                    dec+=1
                lazy[(nums[nxt]+nums[nxt2],nxt)]+=1
                heappush(h,(s + nums[nxt2], i))
            nums[i]=s
            l,r=left[nxt],right[nxt]
            right[l]=r
            left[r]=l
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-14 182727](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-14 182727.png)

## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

期中考试整得我心力憔悴，欠了好几天的每日选做只能等之后抓紧补了。
leetcode评论区里说一个月会有几次补记录的机会。。。我前天实在忘记做每日一题了，然后直接回到解放前，哭了。
简单题目没问题，中等题目大部分还行，困难题目直接跪，唉。







