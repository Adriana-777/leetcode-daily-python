
# 📅 Day04 - 2025/04/14 - 链表

## 今日完成题目（共3题）

| 题号 | 题目 | 是否独立完成 | 难度 | 标签 |
|------|------|----------------|------|------|
| [141](https://leetcode.cn/problems/linked-list-cycle/description/) | LinkedList Cycle | ❌ | Easy | Linkedlist, Hash, 快慢指针 |
| [21](https://leetcode.cn/problems/merge-two-sorted-lists/description/) |merge two sorted lists| ❌ | Easy | Linkedlist, 递归, 迭代|
| [2](https://leetcode.cn/problems/add-two-numbers/description/) |Add two numbers| ❌ | Medium | Linkedlist, |


---

## 解题总结

- 学习了快慢指针，即Floyd's Cycle-Finding Algorithm/龟兔赛跑算法，注意边界条件和循环终止条件避免空指针和fast指针越界
- 合并链表，反转链表首先想到用递归
- 遍历链表 l1 代码（模版，需背）
    while l1:  # 从链表头节点开始向后遍历，直到遇到空节点
        print(l1.val)  # 当前节点值
        l1 = l1.next  # 准备遍历下一个节点
  
- carry % 10	取余，得当前位的值	写入当前位的结果	 12 % 10 = 2
  carry // 10	整除，得进位值	计算下一次的进位	   12 // 10 = 1
   % 10：得到 个位数字，用于填充当前位。
   // 10：得到 十位数字，用于下一次进位。
   这对操作广泛用于 大数加法、乘法、字符串数字运算 等场景。


---

## 明日计划

- 字符串练习题（344、387、242）
- 复习 Python 字符串 API
