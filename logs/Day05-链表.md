
# 📅 Day05 - 2025/04/15 - 链表

## 今日完成题目（共3题）

| 题号 | 题目 | 是否独立完成 | 难度 | 标签 |
|------|------|----------------|------|------|
| [24](https://leetcode.cn/problems/swap-nodes-in-pairs/description/) |Swap two pairs | ❌ | Medium | Linkedlist, 迭代|
| [138](https://leetcode.cn/problems/copy-list-with-random-pointer/description/) |Copy List with Random Pointers| ❌ |  Medium | Linkedlist, hashmap|
| [148](https://leetcode.cn/problems/sort-list/description/) |Sort list| ❌ | Medium | Linkedlist, 快慢指针，merge sort|
| [146](https://leetcode.cn/problems/lru-cache/description/) |LRU Cache| ❌ | Medium | Linkedlist, hashmap, doubly linked list|


---

## 解题总结

- 节点交换的核心代码模板
- 1. 浅拷贝（shallow copy）
只复制最外层的对象，内部的引用不变。所以原对象和拷贝对象的子对象是共享的。

“内部引用”，指的是容器（如 list/dict/set/class）中包含的元素，如果这些元素是可变对象（如 list/dict），那么浅拷贝只复制外层容器，这些元素本身的引用仍然是指向原来的对象。

- 2. 深拷贝（deep copy）
递归复制所有子对象，完全独立的副本。原对象和拷贝对象互不影响。

- 3.链表排序中的一些技巧：
快慢指针找链表中点，经典技巧

合并两个有序链表：类似 21 题

递归归并排序，链表排序的标准写法

切断链表要注意（slow.next = None）



---


