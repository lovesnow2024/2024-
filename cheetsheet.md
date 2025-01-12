### 1.求下一个排列

```python
def next_(num0):
    i=len(num0)-2
    while i>=0 and num0[i]>=num0[i+1]:
        i-=1
    if i>=0:
        j=len(num0)-1
        while num0[j]<=num0[i]:
            j-=1
        num0[i],num0[j]=num0[j],num0[i]
    num0[i+1:]=reversed(num0[i+1:])
    return num0
```

### 二分查找

```Python
def quicksort(arr):
    if len(arr) <= 1:  # 基准情况
        return arr
    else:
        pivot = arr[0]  # 选择第一个元素作为基准
        less = [x for x in arr[1:] if x <= pivot]  # 小于等于基准的元素
        greater = [x for x in arr[1:] if x > pivot]  # 大于基准的元素
        return quicksort(less) + [pivot] + quicksort(greater)  # 递归排序并合并结果
```

### 2.Dijkstra算法（走山路为例）

```python
import heapq
def energy_(map_,x1,y1,x2,y2,m,n):
    if map_[x1][y1]=='#' or map_[x2][y2]=='#':
        return 'NO'
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    visited=[[False]*n for _ in range(m)]
    energy_queue=[(0,x1,y1)]
    while energy_queue:
        energy,x,y=heapq.heappop(energy_queue)
        if x==x2 and y==y2:
            return energy
        if visited[x][y]:
            continue
        visited[x][y]=True
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and (not visited[nx][ny]):
                if map_[nx][ny]!='#':
                    delta_height=abs(int(map_[nx][ny])-int(map_[x][y]))
                    next_e=delta_height+energy
                    heapq.heappush(energy_queue,(next_e,nx,ny))
    return 'NO'
m,n,p=map(int,input().split())
map_=[list(input().split()) for _ in range(m)]
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    print(energy_(map_,x1,y1,x2,y2,m,n))
```

### 3.动态规划

> #### 放苹果

```python
t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for k in range(n + 1):
        dp[0][k] = 1
    for l in range(m+1):
        dp[l][1]=1
    for i in range(1,m+1):
        for j in range(2,n+1):
            if j>i:
                dp[i][j]=dp[i][i]
            else:
                dp[i][j]=dp[i][j-1]+dp[i-j][j]
    print(dp[m][n])
```

> #### 零钱兑换

```python
n,m=map(int,input().split())
moneys=list(map(int,input().split()))
dp=[float('inf')]*(m+1)
dp[0]=0
for i in range(1,m+1):
    for money in moneys:
        if i>=money:
            dp[i]=min(dp[i],dp[i-money]+1)
print(dp[m] if dp[m]!=float('inf') else -1)
```

> #### 公共子序列

```python
z1,z2=input().split()
dp=[[0]*(len(z2)+1) for _ in range(len(z1)+1)]
for i in range(1,len(z1)+1):
    for j in range(1,len(z2)+1):
         if z1[i-1]==z2[j-1]:
             dp[i][j]=dp[i-1][j-1]+1
         else:
             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[len(z1)][len(z2)])
```

> #### 土豪购物

```python
values=list(map(int,input().split(',')))
n=len(values)
dp=[[0]*2 for _ in range(n)]
dp[0][0]=values[0]
ans=values[0]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][0]+values[i],values[i])
    dp[i][1]=max(dp[i-1][1]+values[i],dp[i-1][0])
    ans=max(ans,dp[i][0],dp[i][1])
print(ans)
```

> #### 最大摆动子序列

```python
def max_len(n,nums):
	if n==1:
		return 1
	else:
		up=1
        down=1
		for i in range(1,n):
			if nums[i]>nums[i-1]:
				up=down+1
			elif nums[i]<nums[i-1]:
				down=up+1
	return max(up,down)
n=int(input())
nums=list(map(int,input().split()))
print(max_len(n,nums))
```

> #### 拦截导弹

```python
k=int(input())
tunnel=list(map(int,input().split()))
dp=[1]*k
for i in range(1,k):
    for j in range(i):
        if tunnel[j]>=tunnel[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
```

### 4.河中跳房子/好斗的牛

```python
def cut_stone(places,d,m):
    start=-d
    removed=0
    for place in places:
        if place-start<d:
            removed+=1
            if removed>m:
                return False
        else:
            start=place
    return True
def longest(n,c,places):
    left,right=0,places[n-1]-places[0]  #最短距离与最远距离
    while left<=right:
        mid=left+(right-left)//2
        if cut_stone(places,mid,n-c):
            left=mid+1
        else:
            right=mid-1
    return right
n,c=map(int,input().split())
places=[int(input()) for _ in range(n)]
places.sort()
print(longest(n,c,places))
```

### 5.哈希表

```python
def window(s):
    left=0
    max_=0
    dic={}
    for right in range(len(s)):
        if s[right] in dic:
            left=max(left,dic[s[right]]+1)
        dic[s[right]]=right
        current=right-left+1
        max_=max(max_,current)
    return max_
s=input()
print(window(s))
```

```python
if strs==[""]:
	return [[""]]
dic={}
for string in strs:
    c="".join(sorted(string))
    if c in dic:
        dic[c].append(string)
    else:
        dic[c]=[string]
return [k for k in dic.values()]
```

### 6.广度优先搜索

> #### 寻宝

```python
from collections import deque
def bfs(m,n,map_):
    directions=[[-1,0],[0,1],[0,-1],[1,0]]
    start=[0,0]
    queue=deque([start])
    visited=[[False]*n for _ in range(m)]
    visited[0][0]=True
    steps=0
    while queue:
        current=len(queue)
        for _ in range(current):
            x,y=queue.popleft()
            if map_[x][y]==1:
                return steps
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and  (not visited[nx][ny]) and map_[nx][ny]!=2:
                    queue.append([nx,ny])
                    visited[nx][ny]=True
        steps+=1
    return 'NO'
m,n=map(int,input().split())
map_=[list(map(int,input().split())) for _ in range(m)]
ans=bfs(m,n,map_)
print(ans)
```

> #### 变换的迷宫

```
from collections import deque
def bfs(x, y):
	visited = {(0, x, y)}
	dx = [0, 0, 1, -1]
	dy = [1, -1, 0, 0]
	queue = deque([(0, x, y)])
	while queue:
		time, x, y = queue.popleft()
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			temp = (time + 1) % k
			if 0 <= nx < r and 0 <= ny < c and (temp, nx, ny) not in visited:
				cur = maze[nx][ny]
				if cur == 'E':
					return time + 1
				elif cur != '#' or temp == 0:
					queue.append((time + 1, nx, ny))
					visited.add((temp, nx, ny))
	return 'Oop!'
t = int(input())
for _ in range(t):
	r, c, k = map(int, input().split())
	maze = [list(input()) for _ in range(r)]
	for i in range(r):
		for j in range(c):
			if maze[i][j] == 'S':
				print(bfs(i, j))
```

### 7.归并排序（排序的逆序数）

```python
def merge_sorted(left,right):
    result=[]
    i=j=count=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            count+=len(left)-i
    result+=left[i:]
    result+=right[j:]
    return result,count
def sort(arr):
    if len(arr)<=1:
        return arr,0
    else:
        mid=len(arr)//2
        left,x=sort(arr[:mid])
        right,y=sort(arr[mid:])
        merged,z=merge_sorted(left,right)
        return merged,x+y+z
_,ans=sort(lst)
print(ans)
```

### 8.堆的应用

```python
import heapq
n=int(input())
potions=list(map(int,input().split()))
start=0
count=0
min_heap=[]
for i in range(n):
    start+=potions[i]
    if potions[i]<0:
        heapq.heappush(min_heap,potions[i])
    if start<0:
        start-=heapq.heappop(min_heap)
    else:
        count+=1
print(count)
```

### 9.栈的应用

> #### 字符串解码

```python
s=input()
stack=[]
current=0
string=""
for i in range(len(s)):
    if s[i].isdigit():
        current=current*10 + int(s[i])
    elif s[i]=='[':
        stack.append(current)
        stack.append(string)
        string=""
        current=0
    elif s[i]=="]":
        a=stack.pop()
        num=stack.pop()
        string=a+string*num
    else:
        string+=s[i]
print(string)
```

> #### 括号匹配

```python
def is_valid_parentheses(s)
	stack = []
	# 括号映射
	parentheses_map = {')': '(', '}': '{', ']': '['}
	for char in s:
		if char in parentheses_map.values():
			stack.append(char)
		elif char in parentheses_map.keys():
			if not stack or stack.pop() != parentheses_map[char]:
				return False
	return not stack
# 测试
print(is_valid_parentheses("()[]{}")) # 输出: True
```

### 10.深度优先搜索

> #### 滑雪

```python
def dfs(map_,x,y,r,c,record):
    if record[x][y]!=-1:
        return record[x][y]
    directions=[(-1,0),(1,0),(0,1),(0,-1)]
    max_length=1
    for dx, dy in directions:
        nx,ny=dx+x,dy+y
        if 0<=nx<r and 0<=ny<c and map_[nx][ny]<map_[x][y]:
            length=1+dfs(map_,nx,ny,r,c,record)
            max_length=max(max_length,length)
    record[x][y]=max_length
    return max_length
r,c=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(r)]
max_=0
record=[[-1]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        max_=max(max_,dfs(grid,i,j,r,c,record))
print(max_)
```

> #### 螃蟹采蘑菇

```python
def dfs(grid,n,x1,y1,x2,y2,visited):
    directions=[[-1,0],[1,0],[0,-1],[0,1]]
    visited[x1][y1]=True
    if grid[x1][y1]==9 or grid[x2][y2]==9:
        return True
    for dx,dy in directions:
        nx1,ny1=x1+dx,y1+dy
        nx2,ny2=x2+dx,y2+dy
        if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n and (not visited[nx1][ny1])  and grid[nx1][ny1]!=1 and grid[nx2][ny2]!=1:
            if dfs(grid,n,nx1,ny1,nx2,ny2,visited):
                return True
    visited[x1][y1]=False
    return False
n=int(input())
grid=[list(map(int,input().split())) for _ in range(n)]
ani=[]
for i in range(n):
    for j in range(n):
        if len(ani)==2:
            break
        if grid[i][j]==5:
            ani.append([i,j])
visited=[[False]*n for _ in range(n)]
print('yes' if dfs(grid,n,ani[0][0],ani[0][1],ani[1][0],ani[1][1],visited) else 'no')
```

> #### 迷宫可行路径数

```python
def check(n,m,x,y,map_):
    if x<0 or x>=n or y<0 or y>=m or map_[x][y]==1:
        return False
    else:
        return True
def dfs(n,m,x,y,map_,ans):
    directions=[[-1,0],[1,0],[0,1],[0,-1]]
    if x==n-1 and y==m-1:
        ans[0]+=1
        return
    middle=map_[x][y]
    map_[x][y]=1
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if check(n,m,nx,ny,map_):
            dfs(n,m,nx,ny,map_,ans)
    map_[x][y]=middle
n,m=map(int,input().split())
map_=[list(map(int,input().split())) for _ in range(n)]
x,y=0,0
ans=[0]
dfs(n,m,x,y,map_,ans)
print(ans[0])
```

> #### 受到祝福的平方

```python
from math import sqrt
def check(n):
    if n<=0:
        return False
    else:
        return int(sqrt(n))**2==n
def dfs(a,x0,n,ans,count):
    if x0==n:
        if sum(ans)==n:
            count[0]+=1
        return
    for i in range(x0+1,n+1):
        current=a[x0:i]
        if int(current)!=0 and check(int(current)):
            ans.append(i-x0)
            dfs(a,i,n,ans,count)
            ans.pop()
a=input()
n=len(a)
count=[0]
ans=[]
dfs(a,0,n,ans,count)
print('Yes' if count[0]!=0 else 'No')
```

> #### 矩阵最大权值路径

```python
# 读取输入
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
# 定义方向
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 右、下、左、上
visited = [[False] * m for _ in range(n)] # 标记访问
max_path = []
max_sum = -float('inf') # 最大权值初始化为负无穷
# 深度优先搜索
def dfs(x, y, current_path, current_sum):
	global max_path, max_sum
	# 到达终点，更新结果
	if (x, y) == (n - 1, m - 1):
		if current_sum > max_sum:
			max_sum = current_sum
			max_path = current_path[:]
		return #return 后面没有值，表示函数直接结束并返回 None，退出递归调用，回溯的关键。
	# 遍历四个方向
	for dx, dy in directions:
		nx, ny = x + dx, y + dy
		# 检查边界和是否访问过
		if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
			# 标记访问
			visited[nx][ny] = True
			current_path.append((nx, ny))
			# 递归搜索
			dfs(nx, ny, current_path, current_sum + maze[nx][ny])
			# 回溯
			current_path.pop()
			visited[nx][ny] = False
# 初始化起点
visited[0][0] = True
dfs(0, 0, [(0, 0)], maze[0][0])
# 输出结果
for x, y in max_path:
	print(x + 1, y + 1)
```

### 11.滑动窗口

> #### 滑动窗口的最大值

```python
from collections import  deque
n,k=map(int,input().split())
nums=list(map(int,input().split()))
window=deque()
max_=[]
for i,num in enumerate(nums):
    if window and window[0]<=i-k:
        window.popleft()
    while window and nums[window[-1]]<num:
        window.pop()
    window.append(i)
    if i>=k-1:
        max_.append(nums[window[0]])
print(*max_)
```

> #### 完美的爱

```python
from collections import defaultdict
n=int(input())
values=list(map(int,input().split()))
target=520
delta_value=[x-target for x in values]
p_sum=0
max_=0
sum_indices=defaultdict(list)
sum_indices[0].append(-1)
for i,value in enumerate(delta_value):
    p_sum+=value
    if p_sum in sum_indices:
        # 如果当前前缀和之前出现过，说明存在一个子数组其元素平均值为target_average
        length=i-sum_indices[p_sum][0]
        max_=max(max_,length)
    sum_indices[p_sum].append(i)
max_value=max_*target if max_>0 else 0
print(max_value)
```

### 12.贪心

> #### Woodcutters

```python
n=int(input())
trees=[list(map(int,input().split())) for _ in range(n)]
nums=[[0,0,0] for _ in range(n+1)]
nums[1][0]=0
nums[1][1]=1
nums[1][2]=1
for i in range(2,n+1):
    w,h=trees[i-1]
    w_1,h_1=trees[i] if i < n else (float('inf'), 0)
    w_2,h_2=trees[i-2]
    nums[i][0]=max(nums[i-1][0],nums[i-1][1],nums[i-1][2])
    if w_2<w-h<=w_2+h_2:
        nums[i][1]=max(nums[i-1][0],nums[i-1][1])+1
    elif w-h>w_2+h_2:
        nums[i][1]=nums[i-1][2]+1
    else:
        nums[i][1]=0
    if w+h<w_1:
        nums[i][2]=max(nums[i-1][0], nums[i-1][1],nums[i-1][2]) + 1
    else:
        nums[i][2]=0
print(max(nums[n][0], nums[n][1], nums[n][2]))
```

> #### 垃圾炸弹

```python
d=int(input())
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
laji=[[0]*1025 for _ in range(1025)]
ans=[]
for a,b,c in lst:
    for i in range(max(a-d,0),min(a+d+1,1025)):
        for j in range(max(b-d,0),min(b+d+1,1025)):
            laji[i][j]+=c
max_=0
count=0
for k in range(1025):
    for l in range(1025):
        if laji[k][l]>max_:
            max_=laji[k][l]
            count=1
        elif laji[k][l]==max_:
            count+=1
print(count,max_)
```

### 13.欧拉筛

```python
def euler_sieve(n):
    is_prime = [True] * (n + 1)  # 初始化布尔数组，假设所有数都是质数
    primes = []  # 存储找到的质数
    for i in range(2, n + 1):  # 从2开始遍历到n
        if is_prime[i]:  # 如果i是质数
            primes.append(i)  # 将i加入质数列表

        for p in primes:  # 遍历已找到的质数
            if i * p > n:  # 如果i * p超过了n，停止标记
                break
            is_prime[i * p] = False  # 标记i * p为合数
            if i % p == 0:  # 关键条件：如果i能被p整除
                break  # 停止标记，避免重复标记

    return primes  # 返回所有质数
```

### 埃氏筛

```python
def sieve_of_eratosthenes(n):
	# 创建一个布尔列表，初始化为 True，表示所有数字都假设为素数
	primes = [True] * (n + 1)
	primes[0] = primes[1] = False # 0 和 1 不是素数
	# 从 2 开始，处理每个数字
	for i in range(2, int(n**0.5) + 1):
		if primes[i]: # 如果 i 是素数
			# 将 i 的所有倍数标记为非素数
			for j in range(i * i, n + 1, i):
				primes[j] = False
	# 返回所有素数
	return [x for x in range(2, n + 1) if primes[x]]
```

### 14.快速幂

1. 如果指数 n 为0，则任何数（除了0）的0次幂都是1。
2. 如果指数 n 为奇数，则可以表示成 a^(n-1) * a 的形式，其中 (n-1) 是偶数。
3. 如果指数 n 为偶数，则可以表示成 (a^2)^(n/2) 的形式，这样就可以递归地进行计算。

下面是一个使用 Python 实现的快速幂函数示例：

```python
def fast_power(base, exponent):
    result = 1
    while exponent > 0:
        # 如果当前指数是奇数，那么我们需要把基数乘到结果上
        if exponent % 2 == 1:
            result *= base
        # 将基数平方
        base *= base
        # 将指数除以2
        exponent //= 2
    return result
```

这是一个模意义下的快速幂实现：

```python
def fast_power_mod(base, exponent, mod):
    result = 1
    base = base % mod  # 更新基数，避免其过大
    while exponent > 0:
        if exponent % 2 == 1:  # 如果指数是奇数
            result = (result * base) % mod
        exponent = exponent >> 1  # 右移一位，等同于除以2
        base = (base * base) % mod
    return result
```

### 16.Counter

1. **创建 `Counter` 对象**：
   - 可以通过传入一个可迭代对象（如列表、元组、字符串等）来创建 `Counter` 对象。
   - 也可以通过关键字参数来创建。

```python
from collections import Counter

# 通过列表创建
counter = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(counter)  # 输出: Counter({'a': 3, 'b': 2, 'c': 1})

# 通过字符串创建
counter = Counter('abracadabra')
print(counter)  # 输出: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# 通过关键字参数创建
counter = Counter(a=3, b=2, c=1)
print(counter)  # 输出: Counter({'a': 3, 'b': 2, 'c': 1})
```

2. **访问元素的计数**：可以像普通字典一样访问元素的计数。

```python
counter = Counter('abracadabra')
print(counter['a'])  # 输出: 5
print(counter['z'])  # 输出: 0 （未出现的元素计数为 0）
```

3. **更新计数**：使用 `update` 方法可以增加计数。

```python
counter = Counter('abracadabra')
counter.update('aaa')
print(counter)  # 输出: Counter({'a': 8, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

4. **减去计数**：使用 `subtract` 方法可以减少计数。

```python
counter = Counter('abracadabra')
counter.subtract('aaa')
print(counter)  # 输出: Counter({'a': 2, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

5. **最常见的元素**：使用 `most_common` 方法可以获取最常见的元素及其计数。

```python
counter = Counter('abracadabra')
print(counter.most_common(3))  # 输出: [('a', 5), ('b', 2), ('r', 2)]
```

6. **元素的总和**：使用 `sum` 函数可以计算所有元素的总计数。

```python
counter = Counter('abracadabra')
total_count = sum(counter.values())
print(total_count)  # 输出: 11
```

7. **删除元素**：可以使用 `del` 语句删除某个元素。

```python
counter = Counter('abracadabra')
del counter['a']
print(counter)  # 输出: Counter({'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

8. **清空计数器**：使用 `clear` 方法可以清空计数器。

```python
counter = Counter('abracadabra')
counter.clear()
print(counter)  # 输出: Counter()
```

## 17.函数

```python
enumerate, collections.deque, collections.heapq, isdigit(), popleft(), pop(), index(), push(), reverse=True, key=lambda x:x[0], abs, math.ceil(), math.floor(), math.gcd(), math.sqrt(), 
pow(x,y)-x**y, round(), f"{num:0xd}", f"{num:.xf}", map(), print(*ans), print(a,end=''), print(''.join(l)), max, min, range, sum, len, chr(num), ord(word), append, add, lst.insert(index,x)-在index处后插入x, lst.reserve(反转)
dic.items(), dic.keys(), dic.values(), split(), strip(chars), lstrip(left), rstrip(right), str.replace(old,news),  itertools.permutations(arr,2)
```

```python
import heapq
heapq.heapify(list)
heapq.heappop(list)
heapq.heappush(list,a)
heapq.heappushpop(list,a)
```

```python
from collections import deque
append(x) ：将元素 x 添加到右端。
appendleft(x) ：将元素 x 添加到左端。
pop() ：从右端弹出元素。
popleft() ：从左端弹出元素。
extend(iterable) ：在右端添加多个元素。
extendleft(iterable):在左端添加多个元素（注意，它是逆序添加的）
```

```python
1. 入栈 (Push): 使用 append() 方法将元素压入栈。
2. 出栈 (Pop): 使用 pop() 方法将栈顶元素弹出。
3. 栈顶元素 (Peek): 使用索引 [-1] 访问栈顶元素。
4. 检查栈是否为空: 使用 if not stack 来判断栈是否为空。
```

#### 浅拷贝与深拷贝问题

```python
浅拷贝：
import copy
shallow_copy = copy.copy(original)
深拷贝：
import copy
deep_copy = copy.deepcopy(original)
```

### 多行输入

```python
while True:
    try:
        ---
    except EOFError:
        break
```

### 浮点数

```python
f"{value:.nf}"、f"Percentage: {percentage:.2%}"、f"Scientific notation: {large_number:.2e}"
```

### 字典的使用

```python
#创建字典
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
#通过键来搜索值
法一：print(my_dict['name']) # 输出：Alice
法二：print(my_dict.get('name')) # 输出：Alice
print(my_dict.get('address', 'Not Found'))
#通过值来搜索键
找到所有的键：
法一：keys = [key for key, value in my_dict.items() if value == search_value]
法二：keys = list(filter(lambda key: my_dict[key] == search_value, my_dict))
#找到第一个符合条件的键：
key = next((key for key, value in my_dict.items() if value == search_value), None)
#添加或更新元素（键值对）：
my_dict['age'] = 26 # 更新
my_dict['country'] = 'USA' # 添加
#向字典中某一个键下添加元素：
my_dict = {'key1': [1, 2, 3], 'key2': [4, 5]}
my_dict['key1'].append(4)
#删除键值对
法一：del my_dict['city'] # 删除 'city' 键值对
法二：age = my_dict.pop('age')
print(age) # 输出：26
```

### 集合的使用

```python
# 创建集合
my_set = {1, 2, 3, 4, 5}
another_set = set([3, 4, 5, 6, 7])
#注意：set() 用来创建集合时，它接受一个可迭代对象（如列表、元组、字符串等），因而这里set() 会自动从列表中提取元素并创建集合，而不能直接set(3, 4, 5, 6, 7)，因为set()括号里只可以有一个参数，而{}则不同。
# 添加元素
my_set.add(6)
# 删除元素（不存在元素可抛出错误）
my_set.remove(2)
# 删除不存在的元素，不会抛出错误
my_set.discard(10)
```

### lambda函数的使用

```python
#在字典排序中：
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
#按值升序排序，注意sorted得到的是一个列表!
#如果想要降序并转化为字典格式如下：
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
与map结合：
# 对列表中的每个元素进行平方操作
squared_numbers = list(map(lambda x: x ** 2, numbers))
```

### 18.区间问题

**按照右端点排序**：

（1）不相交区间数目最大

（2）区间选点问题（给出一堆区间，取**尽量少**的点，使得每个区间内**至少有一个点**）——尽量选择当前区间最右边的点，同不相交区间数目最大

(3)区间覆盖问题：给出一堆区间和一个目标区间，问最少选择多少区间可以**覆盖**掉题中给出的这段目标区间。

**按照左端点排序**：

（1）区间合并（左端点由小到大排序，维护前面区间右端点ed）

（2）区间分组问题：从**前往后**依次枚举每个区间，判断当前区间能否被放到某个现有组里面。

### 19.回溯

回溯的**基本步骤**如下：

1. **选择**：在当前状态下选择一个可行的选项。

2. **探索**：基于选择，递归地进入下一层状态，继续进行选择。

3. **撤销选择**：如果当前选择不再满足问题的约束，或者搜索到问题的边界，就回溯，撤销当前的选择，返回上一步，尝试其他的选择。

> #### 八皇后问题：给出一个数b，要求输出第b个串。串的比较是这样的：皇后串x置于皇后串y之前，当且仅当将x视为整数时比y小。

```python
list1 = []
def queen(s):
	if len(s) == 8:
		list1.append(s)
		return
	for i in range(1, 9):
		if all(str(i) != s[j] and abs(len(s) - j) != abs(i - int(s[j])) for j in range(len(s))):
			queen(s + str(i))
queen('')
samples = int(input())
for k in range(samples):
	print(list1[int(input()) - 1])
```

> #### 全排列问题

```python
#正常版
def generate_permutations(nums, prefix=[]):
    if not nums:
        print(' '.join(map(str, prefix)))
    else:
        for i in range(len(nums)):
            nums1=nums[:i]+nums[i+1:]  #去除使用过的元素
            prefix1=prefix+[nums[i]]
            generate_permutations(nums1,prefix1)

def print_permutations(n):
    nums=[int(a) for a in range(1,n+1)]
    generate_permutations(nums)
n=int(input())
print_permutations(n)
#作弊版
from itertools import permutations
def print_permutations(n):
    numbers=list(range(1,n+1))
    perms=permutations(numbers)
    for perm in perms:
        print(' '.join(map(str, perm)))
n=int(input())
print_permutations(n)
```

### 20.排序

（1） sorted() **返回一个新的排序后的列表**，原始的可迭代对象不被修改。可以作用于任何可迭代对象，包括列表、元组、字典等。支持自定义排序规则（通过 key 参数）。用于需要保持原始数据不变的情况，或需要排序结果为列表的场景。

```python
#如按长度排序：（字典中的用法见上一条）
words = ["banana", "apple", "pear", "cherry"]
sorted_words = sorted(words, key=len)
#对列表中的数组按照数组的第一个数字排序：
sorted_dist=sorted(dist,key=lambda x:x[0])
```

（2） .sort() 是 **列表对象的方法**，只能对 **列表** 进行排序，原地修改列表，即 排序会直接修改原列表，返回值为 None 。适用于不需要保留原列表的情况，或者希望节省内存的场景。

```python
#冒泡排序
for i in range(n):
	for j in range(n-1-i):
		if l[j] + l[j+1] > l[j+1] + l[j]:
			l[j],l[j+1] = l[j+1],l[j]
```

### 21.bisect函数

```python
from bisect import bisect  #lo、hi为索引范围，默认为整个序列
bisect_left(lst, x, lo=0, hi=len(lst))   #取索引
bisect_right(lst, x, lo=0, hi=len(lst)) 或 bisect(lst, x, lo=0, hi=len(lst))
bisect.insort_left(lst, x, lo=0, hi=len(lst))  #插入
insort_right(lst, x, lo=0, hi=len(lst)) 或 insort(lst, x, lo=0, hi=len(lst))
e.g.：
lst=[9,8,7,6,5,4,3,2,1]
print(bisect(lst,10,lo=0,hi=len(lst)))  #输出10，因为需要在所有小于x的数之后，所以索引为1的后面。
lst=[1,2,3,4,4,5,6,7,8,9]
print(bisect(lst,4,lo=0,hi=len(lst)))  #输出5，索引为最后一个4之后
```

