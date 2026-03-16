---
course: Data Structure
category:
tags:
latest update: 2026-03-16
status: 🧠Understanding / 🧪Testing / 🚀Mastered
---

# Topic：Array

## Static Array 传统阵列
优点1： 记忆体连续摆放，大幅提升效率
优点2：取资料的过程只需要O(1) —— 只需要知道位址就可以瞬间获取
缺点1：固定大小，因此：
	numpy没有append
	numpy没有insert/delete 
#### 空间局限性
当读取一个Array时，CPU会把附近Array打包到CPU Cache(S-RAM)  —— 对应 优点1