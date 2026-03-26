---
course: P & S
category:
tags:
latest update: 2026-03-10
status:
---
# Topic：随机变数、CDF、PMF、机率分布

## 4.1 随机变数 (Random Variable) —— RV
#### 什么是 R.V. —— 数字化
- 把实验结果(outcome)数字化的表示方式

#### 目的 —— 推导更数学、简明

#### 本质 —— 一个函数
函数 X of abcd = 0 
$\Rightarrow X(abcd) =0$
$\Rightarrow X: S \rightarrow R$

#### 表示方法 —— X、Y
通常用大写字母X、Y、Z表示随机变量，用小写字母x、y、z表示其可能的取值

### 随机变数的种类
#### 1. 离散随机变数 Discrete R.V.
if X(Pass) = 0, X(Fail) = 1,X(Zero) = 2,X(Hundred)=3,....
$\Rightarrow X=0,X=1,X=2,X=3,....$
#### 离散RV的值是 
	1. 有限
	2. 可数无穷


### 2. 连续随机变数 Continuous R.V.
#### 连续R.V.的值是
	1.无穷多
	2.不可数


### 无穷多
![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
对于无穷多的两个集合，两者的数量一样多
![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
	標準是看能否建立**一對一的對應關係**（雙射）
	集合 A：所有正整數${1,2,3,4,5,6,......}$
	集合 B：$10^5,10^{10},10^{15},......$
- $1 \leftrightarrow 10^5$
- $2 \leftrightarrow 10^{10}$
- $3 \leftrightarrow 10^{15}$
-  $\dots$
![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
- $n \leftrightarrow 10^{5n}$
![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

 

## 4.2 累积分布函数 (Cumulative Distribution Function) —— CDF
#### 对于一个随即变数X，我们定义CDF为函数：
$$F_X(x) \overset{def}{=} P(X \le x)$$
	隨機變數小於或等於某個值的累積機率
	事件範圍 = (-无限,X] 
	定義域 (Domain) = (-无限, 无限）
	對應域Range = [0,1]

$P(a < X \le b)$
$F_X(b) - F_X(a)$

$P(a \le X \le b)$
$F_X(b) - F_X(a) + P(X=a)$

$P(a < X < b)$
$F_X(b) - F_X(a) - P(X=b)$

$P(a \le X < b)$
$F_X(b) - F_X(a) - P(X=b) + P(X=a)$

$F_X$为CDF（RV的函数）
x = 变数

Eg:
当Range = (0,1)
$F_X(0.5) = P(X \le 0.5) =\frac{1}{2}$
$P(3 < X \le 5) = P(-\infty < X \le 5) - P(-\infty < X \le 3)$
		    $= P(X \le 5)-P(X\le 3)$
		    $=F_X(5) -F_X(3)$


## 4.3 机率质量函数 PMF



## 4.4 离散机率分布 I



## 4.4 离散机率分布 II
