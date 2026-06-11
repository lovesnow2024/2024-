# Assignment #3: 惊蛰 Mock Exam

Updated 1641 GMT+8 Mar 5, 2025

2025 spring, Complied by <mark>同学的姓名、院系</mark>

张洺瑜  地球与空间科学学院

> **说明：**
>
> 1. **惊蛰⽉考**：AC0（缺考）<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
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

### E04015: 邮箱验证

strings, http://cs101.openjudge.cn/practice/04015



思路：

直接按条件一一验证即可

代码：

```python
def check(mail):
    if mail.count('@')>1 or mail.count('@')==0:
        return False
    if mail[0]=='@' or mail[0]=='.' or mail[-1]=='@' or mail[-1]=='.':
        return False
    idx=mail.index('@')
    if mail[idx+1]=='.' or mail[idx-1]=='.' or '..' in mail:
        return False
    if '.' not in mail[idx+1:]:
        return False
    return True
while True:
    try:
        mail=list(input())
        print('YES' if check(mail) else 'NO')
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-06 175713](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-06 175713.png)



### M02039: 反反复复

implementation, http://cs101.openjudge.cn/practice/02039/



思路：

转换为列表，然后再输出原始信息

代码：

```python
m=int(input())
string=list(input())
n=len(string)//m
grid=[]
for i in range(n):
    v=string[m*i:m*(i+1)]
    if i%2==1:
        v.reverse()
    grid.append(v)
ans=''
for l in range(m):
    for k in range(n):
        ans+=grid[k][l]
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-06 205419](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-06 205419.png)



### M02092: Grandpa is Famous

implementation, http://cs101.openjudge.cn/practice/02092/



思路：

利用字典统计出现次数，之后转为二元列表进行排序，再输出第二梯队的序号。

代码：

```python
from collections import defaultdict
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    dic=defaultdict(int)
    for _ in range(n):
        lst=list(map(int,input().split()))
        for i in lst:
            if i in dic:dic[i]+=1
            else:dic[i]=1
    ans=[]
    for k in dic:
        ans.append([k,dic[k]])
    ans.sort(key=lambda x:(x[1],-x[0]),reverse=True)
    num=ans[1][1]
    result=[]
    for a,b in ans[1:]:
        if b==num:
            result.append(a)
        else:
            break
    print(' '.join(map(str,result)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-06 210812](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-06 210812.png)



### M04133: 垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/



思路：

印象深刻的题，直接建立1025*1025的矩阵填垃圾，再遍历统计最值

代码：

```python
d=int(input())
n=int(input())
litter=[list(map(int,input().split())) for _ in range(n)]
grid=[[0]*1025  for _ in range(1025)]
for a,b,c in litter:
    for k in range(max(a-d,0),min(a+d+1,1025)):
        for l in range(max(b-d,0),min(b+d+1,1025)):
            grid[k][l]+=c
max_=-1
count=1
for i in range(1025):
    for j in range(1025):
        if grid[i][j]>max_:
            count=1
            max_=grid[i][j]
        elif grid[i][j]==max_:
            count+=1
print(count,max_)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-06 211950](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-06 211950.png)



### T02488: A Knight's Journey

backtracking, http://cs101.openjudge.cn/practice/02488/



思路：

缺考了，但是如果参加的话，估计就AC5。。。这道题肯定花完我剩下的时间

正常的dfs题。我改了两遍，超时，然后发现全部遍历找路径时间太长了，于是我直接以最小字典序的标准遍历，就是‘A1'–>'A2'–>'A3'….，找到一条直接跳出所有循环，然后就WA了。。。发现directions的顺序也有说法，字典序小的在前面，依旧是只找一条路径，这才AC。。。

代码：

```python
def dfs(grid,x,y,p,q,visited,ans,count,path):
    directions=[(-1,-2),(1,-2),(-2,-1),(2,-1),(-2,1),(2,1),(-1,2),(1,2)]
    if count==0:
        ans.append(''.join(path))
        return True
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<p and 0<=ny<q and (nx,ny) not in visited:
            visited.add((nx, ny))
            path.append(grid[nx][ny])
            if dfs(grid,nx,ny,p,q,visited,ans,count-1,path):
                return True
            path.pop()
            visited.remove((nx,ny))
    return False
n=int(input())
for v in range(n):
    p,q=map(int,input().split())
    grid=[['0']*q for _ in range(p)]
    for i in range(p):
        for j in range(q):
            a=i+1
            b=chr(ord('A')+j)
            grid[i][j]=b+str(a)
    ans=[]
    flag=False
    for y in range(q):
        for x in range(p):
            path=[grid[x][y]]
            visited=set()
            visited.add((x,y))
            count=p*q-1
            if dfs(grid,x,y,p,q,visited, ans, count, path):
                flag=True
                break
        if flag:
            break

    print(f'Scenario #{v+1}:')
    print(ans[0] if ans else 'impossible')
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-06 234410](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-06 234410.png)



### T06648: Sequence

heap, http://cs101.openjudge.cn/practice/06648/



思路：

着实想不到，我的想法一开始就到列上了，因为很明显，每行排序后的第一个数相加一定是最小和，然后用堆结构。。。deepseek给的一直MLE，让它改，它说可以限制堆中元素数量不超过n，但是它仅仅这么说，输出的代码没有这么改。

代码：

```python
import heapq
t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    lst1=sorted(map(int,input().split()))
    for _ in range(m-1):
        lst2=sorted(map(int,input().split()))
        heap=[(lst1[i]+lst2[0],i,0) for i in range(n)]
        heapq.heapify(heap)
        result=[]
        for _ in range(n):
            cur,i,j=heapq.heappop(heap)
            result.append(cur)
            if j+1<n:
                heapq.heappush(heap,(lst1[i]+lst2[j+1],i,j+1))
        lst1=result
    print(*lst1)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted")==

![屏幕截图 2025-03-07 153537](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-07 153537.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

感觉比之前计概的时候进步太多了，dfs题基本上能够自己把模版写出来，不过像倒数第二题这种有限制的，我还是花了好久。还有，最后一题是真想不到。。。debug能力确实欠缺，来个WA就炸了

任务还有好多啊，最近一直跟着每日选做和leecode上的每日一题，但100热题、寒假选做都还差着一半多点，抓紧时间吧。



