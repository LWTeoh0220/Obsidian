---
course: P & S
category:
tags:
latest update: 2026-03-10
status:
---
# Topic：数数概率 Count Probability


#### Fundamental Principle of Counting
某实验有n种不同结果，另一种实验有m种结果。
	 操作此两实验将有nm种不同结果
	
#### 判断条件
1. Distinguishable 可区分吗？
2. With/Without Replacement 是否可放回？
3. Order matters or not 顺序是否有差异？




若有n异物，从中依序取出k物，共有多少种结果？
##### Permutation 排列
n * (n-1) * (n-2) * ... * (x-(k-1)) = $\dfrac{n!}{(n-k)!}$
##### Choose with Replacements
n* n * n ...... * n = $n^k$
##### Combination
$\dfrac{n(n-1)(n-2)\dots (n-(k-1))}{k!}$ = $\dfrac{n!}{(n-k)!k!}$

> 1/k! : k没有区别
> 
 $\dbinom{n}{r}$ : binomial coefficients 二项式系数
 来自二项式定理 $(x+y)^n = \sum_{k=0}^{n}\dbinom{n}{r}x^ky^{n-k}$
> n choose r


##### Multinomial 多项组合
10次，4次为A，3次为B，2次为C，1次为
$\dbinom{10}{4}\dbinom{6}{3}\dbinom{3}{2}\dbinom{1}{1}$ = 