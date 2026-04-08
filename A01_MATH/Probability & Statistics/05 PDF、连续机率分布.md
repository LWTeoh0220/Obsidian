---
course: P & S
category:
tags:
latest update: 2026-04-08
status: 🧠Understanding / 🧪Testing / 🚀Mastered
---
# Topic：PDF、连续机率分布

## 5-1 机率密度函数 PDF(Probability Density Function)

机率分布不均等，对于**连续的随机变数**，我们用PDF了解某个数字发生的机率大小

- 范围内（样本空间）具有无限个数字，因此
$PMF:p_X(a) = p = 0$。a为任意数，因此找PMF无意义

连续的东西用密度，机率密度：
$PDF:f_X(x) = \lim\limits_{\Delta x\to 0}\frac{P(x\le X\le x+ \Delta x)}{\Delta x}$
$= \lim\limits_{\Delta \to0}\frac{F_X(x+\Delta x) - F_X(x)}{\Delta x}$
$= F'_X(x)$

$CDF F_X(x) \rightarrow PDF f_X(x)$—— $\frac{d}{dx}$
$PDF f_X(x)\rightarrow  CDF F_X(x)$—— $\int_{-\infty}^x$

$P(a < X \le b) = F_X(b) -F_X(a)$
$\int_{-\infty}^bf_X(x)dx-\int_{-\infty}^af_X(x)dx$
$\int_a^bf_X(x)dx$



## 5-2 连续机率分布