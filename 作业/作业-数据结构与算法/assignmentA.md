# Assignment #A: Graph starts

Updated 1830 GMT+8 Apr 22, 2025

2025 spring, Complied by <mark>同学的姓名、院系</mark>

张洺瑜  地球与空间科学学院

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

### M19943:图的拉普拉斯矩阵

OOP, implementation, http://cs101.openjudge.cn/practice/19943/

要求创建Graph, Vertex两个类，建图实现。

思路：

直接挪的课件答案，建图好生麻烦，也是没怎么弄清楚。还是弄两个二维矩阵方便（，还是太菜了。

代码：

```python
class Vertex:
    def __init__(self,key):
        self.key=key
        self.neighbors={}
    def get_neighbor(self,other):
        return self.neighbors.get(other,None)
    def set_neighbor(self,other,weight=0):
        self.neighbors[other]=weight
    def __repr__(self):
        return f"Vertex({self.key})"
    def __str__(self):
        return (
            str(self.key)
            + "connected to:"
            + str([x.key for x in self.neighbors])
        )
    def get_neighbors(self):
        return self.neighbors.keys()
    def get_key(self):
        return self.key
class Graph:
    def __init__(self):
        self.vertices={}
    def set_vertex(self,key):
        self.vertices[key]=Vertex(key)
    def get_vertex(self,key):
        return self.vertices.get(key,None)
    def __contains__(self, key):
        return key in self.vertices
    def add_edge(self,from_vert,to_vert,weight=0):
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert],weight)
    def get_vertices(self):
        return self.vertices.keys()
    def __iter__(self):
        return iter(self.vertices.values())
def construct(n,edges):
    graph=Graph()
    for i in range(n):
        graph.set_vertex(i)
    for edge in edges:
        a,b=edge
        graph.add_edge(a,b)
        graph.add_edge(b,a)
    matrix=[]
    for vertex in graph:
        row=[0]*n
        row[vertex.get_key()]=len(vertex.get_neighbors())
        for neighbor in vertex.get_neighbors():
            row[neighbor.get_key()]=-1
        matrix.append(row)
    return matrix
n,m=map(int,input().split())
edges=[]
for i in range(m):
    a,b=map(int,input().split())
    edges.append((a,b))
matrix=construct(n,edges)
for row in matrix:
    print(' '.join(map(str,row)))


#####
from collections import defaultdict
n,m=map(int,input().split())
dic=defaultdict(int)
A=[[0]*n for _ in range(n)]
L=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    dic[a]+=1
    dic[b]+=1
    A[a][b],A[b][a]=1,1
for i in range(n):
    for j in range(n):
        if i==j:
            L[i][j]=dic[i]-A[i][j]
        else:
            L[i][j]=-A[i][j]
for row in L :
    print(*row)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-24 230031](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-24 230031.png)



### LC78.子集

backtracking, https://leetcode.cn/problems/subsets/

思路：

1. 使用dfs，两个选择，选与不选。
2. 从[]开始，逐渐将元素加入其中，并且将该元素单独弄一个列表加入其中。

代码：

```python
1. class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        def backtrack(i,nums,path):
            ans.append(path[:])
            for j in range(i,len(nums)):
                path.append(nums[j])
                backtrack(j+1,nums,path)
                path.pop()
            return ans
        backtrack(0,nums,path)
        return ans

2.class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back(result,n,count,nums):
            if count==n:
                return 
            mid=[lst[:] for lst in result]
            for k in mid:
                v=k+[nums[count]]
                result.append(v)
            back(result,n,count+1,nums)
        result=[[]]
        n=len(nums)
        back(result,n,0,nums)
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-24 231427](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-24 231427.png)



### LC17.电话号码的字母组合

hash table, backtracking, https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

思路：

dfs直接写就可以解决

代码：

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
        '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits)==0:
            return []
        ans=[]
        def dfs(digits,ans,cur,count):
            if len(cur)==len(digits):
                ans.append(cur[:])
                return
            lst=dic[digits[count]]
            for i in lst:
                dfs(digits,ans,cur+i,count+1) 
        dfs(digits,ans,'',0)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-24 233302](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-24 233302.png)



### M04089:电话号码

trie, http://cs101.openjudge.cn/practice/04089/

思路：

字典树例题，又学到了新知识，将电话号码构建为树，并设置一个标记，当当前号码构建结束时，标记变为true。这样，当之后构建别的电话号码时，如果途中有true标记，或者结束后，该节点仍有子节点，则说明存在前缀现象。

代码：

```python
###字典树
class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,number):
        node=self.root
        for digit in number:
            if digit not in node.children:
                node.children[digit]=TrieNode()
            node=node.children[digit]
            if node.is_end:
                return False
        if node.children:
            return False
        node.is_end=True
        return True
t=int(input())
for _ in range(t):
    n=int(input())
    numbers=[input() for _ in range(n)]
    trie=Trie()
    flag=True
    for number in numbers:
        if not trie.insert(number):
            flag=False
            break
    print('YES' if flag else 'NO')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-26 114853](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-26 114853.png)



### T28046:词梯

bfs, http://cs101.openjudge.cn/practice/28046/

思路：

bfs的思路还是比较好想的，但是我不知道怎么建立那些单词间的关系。只能借鉴群中发的优秀同学的思路了。word[i:]+'_'+word[i+1:]

代码：

```python
from collections import deque,defaultdict
def bfs(start,end,dic):
    queue=deque([(start,[start])])
    visited=set()
    visited.add(start)
    while queue:
        cur_word,cur_path=queue.popleft()
        if cur_word==end:
            return ' '.join(cur_path)
        for k in range(4):
            basis=cur_word[:k]+'_'+cur_word[k+1:]
            for w in dic[basis]:
                if w not in visited:
                    new_path=cur_path+[w]
                    queue.append((w,new_path))
                    visited.add(w)
    return 'NO'
n=int(input())
words=list(input() for _ in range(n))
start,end=input().split()
dic=defaultdict(list)
for word in words:
    for i in range(4):
        basis=word[:i]+'_'+word[i+1:]
        dic[basis].append(word)
print(bfs(start,end,dic))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-26 140818](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-26 140818.png)



### T51.N皇后

backtracking, https://leetcode.cn/problems/n-queens/

思路：

终于是进步了一些，之前面对八皇后还是觉得难的，但这道题也算是较为轻松的解决了。

代码：

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid=[['.']*n for _ in range(n)]
        ans=[]
        visited,visited1,visited2=set(),set(),set()
        def dfs(grid,visited,visited1,visited2,count,ans):
            if count==n:
                result=["".join(row) for row in grid]
                ans.append(result)
                return
            for i in range(n):
                if i not in visited and (i+count) not in visited1  and (i-count)not in visited2:
                    visited.add(i)
                    visited1.add(i+count)
                    visited2.add(i-count)
                    grid[count][i]='Q'
                    dfs(grid,visited,visited1,visited2,count+1,ans)
                    grid[count][i]='.'
                    visited.remove(i)
                    visited1.remove(i+count)
                    visited2.remove(i-count)
        dfs(grid,visited,visited1,visited2,0,ans)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-04-26 144213](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-04-26 144213.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次作业对我来说有些难度。主要是拉普拉斯那道题建两个类着实很复杂。

学会了字典树这一结构，也巩固了bfs

还是在追每日选做，每日一题也是每天都在写。这周末终于能安心参加周赛了，别再忘记就好（







