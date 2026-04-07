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

#### 目的 
1. **量化抽象事件**：透過隨機變數，我們可以把它們變成數字（例如：1 或 0），這樣電腦和數學公式才能處理。
2. **進行數學運算**：一旦變成數字，我們就可以計算**平均值**（期望值）、**變異數**（風險）或機率分佈。你無法對「正面」求平均，但可以對「1」求平均。
3. **簡化複雜問題**：它讓我們能用一個簡單的代號（如$X$）代表背後複雜的隨機過程。例如，"$X>10$"可以代表「今天的股市漲幅超過 100 點」，而不必每次都描述整個市場。
**將「機率」轉化為「代數」**

#### 本质 —— 一个函数
把“实验结果”（文字叙述、发生的事件）映射到“实数”（数值）上
函数 X of abcd = 0 
$\Rightarrow X(abcd) =0$
$\Rightarrow X: S \rightarrow R$
$\Rightarrow X(s) = r$
- $s$ ：代表一个可能的**结果**（比如：掷出一点、醉汉往前走）。
- $X$：代表**规则**（函数）。
- $r$ (或你的 $y$)：代表最后得出的**数字**。


**隨機變數**常以**大寫的英文字母**表示, 而它的**觀察值**則以對應的**小寫字母**表示
隨機變數X取值x : $X=x$

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
$P(X=x_i) =p_i, i =1,2,3,\dots,n$
	$p_1+p_2+$
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
即，累积到`[x]`为止的所有机率之和
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
$=P(X=x)$
= $\dbinom{n}{x}p^x(1-p)^{n-x}$

2. CDF
$$\begin{aligned}
F_X(x) &=\sum\limits_{n=-\infty}^{[x]}p_X(x)\\
&=\sum\limits_{m=-\infty}^{[x]}\dbinom{n}{m}p^m(1-p)^{n-m}
\end{aligned}$$


Eg:
	成功率为0.6作10次实验，X表成功次数
	X ~ Bernoulli(10,0.6)
	= p(X=8)
	= $\dbinom{10}{8}0.6^8(1-0.6)^{10-8}$

### Uniform机率分布
- 1次实验，n种结果，结果机率均等
如果X等于a, a+1..., b
X ~ UNIF(x,p)
![[Pasted image 20260327003633.png]]

为什么需要机率分布
	事物背后的机率模型是未知的
	可以经由相似的分布，模拟该事务的运作


### Geometric 机率分布

具有失意性

若试验成功过机率为p，试到成功为止，做了X次尝试
![[Pasted image 20260327203455.png]]


### Pascal机率分布

若实验成功机率为p，试到第k次成功为止共作了X次
![[Pasted image 20260327204316.png]]

### Poisson 机率分布
![[Pasted image 20260327204907.png]]
![[Pasted image 20260327205017.png]]z


