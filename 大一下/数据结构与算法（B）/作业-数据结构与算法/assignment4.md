# Assignment #4: 位操作、栈、链表、堆和NN

Updated 1203 GMT+8 Mar 10, 2025

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

### 136.只出现一次的数字

bit manipulation, https://leetcode.cn/problems/single-number/



<mark>请用位操作来实现，并且只使用常量额外空间。</mark>

好吧，对位运算太不熟悉了，两个相同的数的异或运算是0，巧妙。

代码：

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            result^=i
        return result
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-11 224625](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-11 224625.png)



### 20140:今日化学论文

stack, http://cs101.openjudge.cn/practice/20140/



思路：

与之前的字符串解码是一类题，只是要改变将数字推入栈中的时机，因为数字在"["的后面。

代码：

```python
string=input()
stack=[]
ans=''
cur=0
for i in string:
    if i=='[':
        if cur:
            stack.append(cur)
        stack.append(ans)
        ans=''
        cur=0
    elif i.isdigit():
        cur=cur*10+int(i)
    elif i==']':
        num=stack.pop()
        a=stack.pop()
        ans=a+ans*num
    else:
        if cur:
            stack.append(cur)
            cur=0
        ans+=i
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-11 224949](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-11 224949.png)



### 160.相交链表

linked list, https://leetcode.cn/problems/intersection-of-two-linked-lists/



思路：

看了一下题解感觉思路很简单，将链表接在另一个链表尾部，如此得到的两个列表必定在同一位置有相同的值，即为相交点。

代码：

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        while a!=b:
            a=a.next if a else headB
            b=b.next if b else headA
        return a
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-11 230618](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-11 230618.png)



### 206.反转链表

linked list, https://leetcode.cn/problems/reverse-linked-list/



思路：

通过双指针实现反转链表。考虑遍历链表，并在访问各节点时修改 next 引用指向

代码：

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current=head
        while current:
            next_=current.next
            current.next=prev
            prev=current
            current=next_
        return prev
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-12 211949](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-12 211949.png)



### 3478.选出和最大的K个元素

heap, https://leetcode.cn/problems/choose-k-elements-with-maximum-sum/



思路：

周赛看到这个直接把我心态搞炸了，我就AC了一个题。
重要一步就是将nums1、nums2、索引进行捆绑排序，然后对于遍历a，对于相同的nums1中的数，它的ans肯定一样。然后用堆结构记录最大的k个nums2的值，并用s记录ans。

代码：

```python
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        a = sorted((x, y, i) for i, (x, y) in enumerate(zip(nums1, nums2)))
        n = len(a)
        ans = [0] * n
        h = []
        s = i = 0
        while i < n:
            start = i
            x = a[start][0]
            while i < n and a[i][0] == x:
                ans[a[i][2]] = s
                i += 1
            for j in range(start, i):
                y = a[j][1]
                s += y
                heappush(h, y)
                if len(h) > k:
                    s -= heappop(h)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2025-03-11 230335](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-11 230335.png)



### Q6.交互可视化neural network

https://developers.google.com/machine-learning/crash-course/neural-networks/interactive-exercises

**Your task:** configure a neural network that can separate the orange dots from the blue dots in the diagram, achieving a loss of less than 0.2 on both the training and test data.

**Instructions:**

In the interactive widget:

1. Modify the neural network hyperparameters by experimenting with some of the following config settings:
   - Add or remove hidden layers by clicking the **+** and **-** buttons to the left of the **HIDDEN LAYERS** heading in the network diagram.
   - Add or remove neurons from a hidden layer by clicking the **+** and **-** buttons above a hidden-layer column.
   - Change the learning rate by choosing a new value from the **Learning rate** drop-down above the diagram.
   - Change the activation function by choosing a new value from the **Activation** drop-down above the diagram.
2. Click the Play button above the diagram to train the neural network model using the specified parameters.
3. Observe the visualization of the model fitting the data as training progresses, as well as the **Test loss** and **Training loss** values in the **Output** section.
4. If the model does not achieve loss below 0.2 on the test and training data, click reset, and repeat steps 1–3 with a different set of configuration settings. Repeat this process until you achieve the preferred results.

给出满足约束条件的<mark>截图</mark>，并说明学习到的概念和原理。

![屏幕截图 2025-03-12 215522](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2025-03-12 215522.png)

其实不是很能理解这些都代表什么，怎么影响最后结果的。说直白点就是，刚接触很茫然。之后会再去那个页面学习其他内容。。。

简单了解了一下正则化的概念，是一种用于防止模型过拟合的技术。

## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次作业基本是链表里基础的题，热题100里已经做过，正好复习一下。每日选做依然跟进，然后再找几道其他的题。之后会针对薄弱点，比如一直不熟的递归和动规，去leetcode的专题模块学习。









