---
course: P & S
category:
tags:
  - Maths
  - Probability
latest update: 2026-03-10
status:
---
# Topic：机率与统计 基础


## 1.1几率概论
机率是什么?
	- 对世界了解太少而带来的未知（对A学生，机率是低的，对全知的B而言，机率是100%的）
	- 有些东西是具有随机性的
统计是什么
	如何建立机率模型


## 1.2集合论
P(X) = Y

#### 元素 Element
- a,b,c,d,e...,z
#### 集合Set
A = {a,b,c,d}
B = {h,x,y,z}
#### 子集合Sebset
C = {x,y,z}
C是B的子集合
#### 宇集 Universal Set
S ={a,b,c,d,...,z}
- 所有元素
#### 空集合 Empty Set
$\phi$ = {} 
- 无
#### 交集 Intersection
A $\cap$ B =$\phi$
A $\cap$ C = {x,y,z}
#### 联级 Union
A $\cup$ B = {a,b,c,d,h,x,y,z}
#### 补集 Complement
$A^c$ = {e,f,g,....,z} 
- A集合意外的元素集
#### 差集 Difference
C - B ={h,x,y,z} - {x,y,z} = {h}
#### 不相交 Disjoint
A $\cap$ B =$\phi \rightarrow$ A,B 不相交
#### 互斥 Mutually Exlusive
一群集合中任选两个集合都不相交
$X_1,X_2,X_3....$ 任何两个集合都不相交
#### De Morgan's Law 定理
$(A\cup B)^c=A^c \cap B^c$
	
## 1.3名词定义
#### 实验 Experiment
- 对于不确定结果的实作
1. 步骤 procedures —— 过程 & 规则
2. 模型 model —— 条件
3. 观察 observation —— 结果
#### 样本空间 Sample Space
- 机率实验所有可能的结果的的集合  被称为$\phi 或\Omega$
- 在机率问题中，样本空间就是该问题的宇集
S = [0，1)
#### 事件 Event
- 对实验结果的叙述
- 机率 —— 讲述实验结果符合某事件叙述的机会有多大
- 事件 ---- 结果的集合，既是样本空间的子集

## 公理 （Axioms）
1. 对任何事件A而言，P(A) $\ge$ 0
2. P(S) = 1
3. 事件$A_1,A_2,......$互斥 $\Rightarrow$ P($A_1\cup A_2\cup A_3 \dots$) = P($A_1$) + P($A_2$) + P($A_3$)



交集 = $\cup$
联集 = $\cap$

- P(A) = 1 - P($A^C$)
$\Rightarrow$ A $\cap$ $A^C$ = $\emptyset$ $\Rightarrow$ A, $A^C$ 互斥



- P(A) = P(A-B) + P(A $\cap$ B)
$\Rightarrow$ P(A-B) $\cap$ P(A $\cap$ B) = $\emptyset$
$\Rightarrow$ A = (A-B) $\cup$ (A $\cap$ B) 

- P(A $\cup$ B) = P(A) + P(B) - p(A $\cap$ B)


$C_1$, $C_2$ $\dots$ , $C_n$ 互斥 且 $C_1 \cup C_2 \cup \dots \cup C_n = S$
则对任何事件 $A$ : P(A) = P($A \cap C_1$) + P($A \cap C_2$) + $\dots$  + P($A \cap C_n$)

