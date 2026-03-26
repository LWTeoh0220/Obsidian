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
#### 对于一个随机变数X，我们定义CDF为函数：
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


### 离散随机变数的CDF
当 $x \in [0, 1)$ 时， $F_X(x) = 0$
当 $x \in [1, 2)$ 时， $F_X(x) = \frac{1}{n}$
当 $x \in [2, 3)$ 时， $F_X(x) = \frac{2}{n}$
$\dots$
当 $x \in [n, +\infty)$ 时， $F_X(x) = 1$

因此  $F_X(X^+)=F_X(x)$
	 $F_X(X^-)=F_X(x)-P(X=x)$
### 连续随机变数的CDF
当 $x \in [0, 1)$ 时，
$F_X(-0.1) = P(X \le -0.1)=0$
$F_X(0.1) = P(0 \le X \le 0.1)=0.1$
$F_X(0.5) = P(0 \le X \le 0.5)=0.5$
$F_X(1) = P(0 \le X \le 1)=1$
$F_X(1.7) = P(0 \le X \le 1.7)=1$

因此  $F_X(x^-)=F_X(x)=F_X(x^+)$


## 4.3 机率质量函数(Probability Mass Funtion) PMF
对任意整数值的**离散随机变数**X，我们定义PMF为函数
$$p_X(x) \overset{def}{=} P(X \le x)$$
#### 条件：
- 非负性：所有可能的x机率必须大于或等于0
- 单位和性质：所有可能结果的机率综合必须精确等于1

#### PMF $\Rightarrow$ CDF
$$F_X(x) =\sum\limits_{n=-\infty}^{[x]}p_X(x)$$

#### CDF $\Rightarrow$ PMF
$$P_X(x)=F_X(x^+)-F_X(x^-)$$


### 机率分布 Probability Distribution
- 任何一个PMF/PDF都是一种机率分布



## 4.4 离散机率分布 I
### Bernoulli机率分布
- 一次实验两种结果
X ~ Bernoulli(p) 【另一个结果为 (1-p)】

1. PMF
$$p_X(x) = \begin{cases} 
p & ,x = 1, \\ 
1-p & ,x = 0, \\ 
0 & ,\text{otherwise}. 
\end{cases}
$$

2. CDF
$$F_X(x) =\sum\limits_{n=-\infty}^{[x]}p_X(x)$$
$$F_X(x) = \begin{cases} 
0 & ,x <0, \\ 
1-p & ,0\le x<1, \\ 
1 & ,x\ge 1. 
\end{cases}
$$


Eg:
	成功率为0.6作一次实验，X表成功次数
	X ~ Bernoulli(0.6)

### Binomial 机率分布
- 多次实验两种结果
- 若实验成功率为p作n次实验，X表成功次数
X ~ BIN(n,p)
1. PMF
$p_X(x)$
$=P(X=x$
= $\dbinom{n}{x}p^x(1-p)^{n-x}$

2. CDF
$$\begin{aligned}
F_X(x) =\sum\limits_{n=-\infty}^{[x]}p_X(x)\\
&=\sum\limits_{m=-\infty}^{[x]}\dbinom{n}{m}p^m(1-p)^{n-m}
\end{aligned}$$


Eg:
	成功率为0.6作10次实验，X表成功次数
	X ~ Bernoulli(10,0.6)
	= p(X=8)
	= $\dbinom{10}{8}0.6^8(1-0.6)^{10-8}$
## 4.4 离散机率分布 II
