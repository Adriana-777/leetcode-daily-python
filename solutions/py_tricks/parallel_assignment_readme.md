# Python 平行赋值技巧大全

> 本文档收录了 Python 中最常用、最实用的平行赋值（Parallel Assignment）技巧，适合刷题、开发、数据处理等高频场景。

---

## 📌 技巧目录

1. [基础平行赋值](#1-基础平行赋值)
2. [变量交换](#2-变量交换)
3. [列表解包](#3-列表解包)
4. [星号 * 拆包](#4-星号--拆包)
5. [链表反转技巧](#5-链表反转技巧)
6. [斐波那契数列构建](#6-斐波那契数列构建)
7. [函数返回值解包](#7-函数返回值解包)
8. [zip + 解包](#8-zip--解包)
9. [嵌套结构解包](#9-嵌套结构解包)
10. [条件判断 + 平行赋值](#10-条件判断--平行赋值)
11. [配合 enumerate 遍历](#11-配合-enumerate-遍历)

---

## 1. 基础平行赋值
```python
a, b = 1, 2
```

## 2. 变量交换
```python
a, b = b, a
```
不再需要使用 `tmp` 中间变量。

## 3. 列表解包
```python
a, b, c = [1, 2, 3]
```

## 4. 星号 * 拆包
```python
head, *body, tail = [1, 2, 3, 4, 5]
# head = 1, body = [2,3,4], tail = 5
```
用于提取首尾，适合字符串、栈/队列模拟。

## 5. 链表反转技巧
```python
cur.next, pre, cur = pre, cur, cur.next
```
应用于链表反转（高频刷题场景）。

## 6. 斐波那契数列构建
```python
x, y = 0, 1
for _ in range(10):
    x, y = y, x + y
```

## 7. 函数返回值解包
```python
def divide(x, y):
    return x // y, x % y

q, r = divide(10, 3)
```

## 8. zip + 解包
```python
pairs = [(1, 2), (3, 4)]
a_list, b_list = zip(*pairs)
# a_list = (1, 3), b_list = (2, 4)
```

## 9. 嵌套结构解包
```python
(a, (b, c)) = (1, (2, 3))
```

## 10. 条件判断 + 平行赋值
```python
x, y = (1, 0) if flag else (0, 1)
```

## 11. 配合 enumerate 遍历
```python
for i, val in enumerate([4, 5, 6]):
    print(i, val)
```

