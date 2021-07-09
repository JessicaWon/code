# 练习
```
本仓库只为自己练习使用，无任何其他用途
```
## 查找
### 二分查找
```
二分查找根号n还不错
这个地方需要注意一点，就是最好设置一个n，每次n = n*2.0
如果大了，那就old_item - old_item/n
如果小了，那就old_item + old_item/n
慢慢的缩小距离

另外精度需要考虑一定的位数，就可以通过保留上次计算的结果，如果和上次一样，那么就可以退出了，如果不同，那么就可以赋值给这个保留计算结果的变量
```
## 排序
### 堆排序
```
堆排序中比较重要的一点是从最后一个非叶子节点开始往前，一般是index = n/2-1
然后需要注意的是，排序完一次后需要头尾互相换，这里的尾巴一定一定是新的tail，而不是老的tail!!!
```
### 快排
```
主要的问题是选取最后一个节点为base，从前往后扫描，遇到比"base"大的数值，那么就把这个数值将最后一个数值覆盖掉，然后循环结束break
然后再从后往前扫描，遇到比"base"小的值，将前面的index对应的值覆盖掉
当head 和tail相交时候，将base填进去
前面两个是两个循环，因为要来回扫描多遍，所以还需要一个head < tail的判断来进行死循环


然后，分成前后两个数组，再次重复上述的动作，也就是需要递归

那，什么时候停止递归呢？就是当head == tail的时候, 也就是传递进去的头尾是一样的时候就停止了
```
### topk问题
```
可以使用python中的特殊技能：分片来实现插入时候造成的数据过多
比如说可以通过array = array[:k]这样来实现
```

## 队列的实现
```
这里的话队列的实现在python中可以使用array.insert(0, item)来实现先进先出的功能
```
## 栈的实现
```
可以通过使用array.append(item), array.pop() 来实现栈

```
