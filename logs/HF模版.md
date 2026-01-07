📝 LeetCode 笔记模板 

题目： [No.1 Two Sum] (附链接)

核心考点： HashMap (Time: O(1) / Space: O(N))

我的初级解法 (Bad): 暴力双循环 O(N²)。（记录为什么这个解法在面试中会被拒）

Hedge Fund 思维 (Solid):

Idea: “以空间换时间”。遍历数组时，回头看一眼 target - current_value 是否已经在字典里。

Corner Case: 只有 2 个数怎么办？找不到怎么办？

Pythonic Snippet (背诵版): (贴上不超过 15 行的精简代码，用 Python Type Hinting)

底层原理 (Why): 为什么 Dict 查找是 O(1)？（见 Part 1）
