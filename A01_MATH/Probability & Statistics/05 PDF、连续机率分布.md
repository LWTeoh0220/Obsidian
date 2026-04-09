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
$PMF:p_X(a) = p = 0$。连续RV每点发生机率为0，因此找PMF无意义

连续的东西用密度，机率密度：
$PDF:f_X(x) = \lim\limits_{\Delta x\to 0}\frac{P(x\le X\le x+ \Delta x)}{\Delta x}$
$= \lim\limits_{\Delta \to0}\frac{F_X(x+\Delta x) - F_X(x)}{\Delta x}$
$= F'_X(x)$

$CDF F_X(x) \rightarrow PDF f_X(x)$—— $\frac{d}{dx}$
$PDF f_X(x)\rightarrow  CDF F_X(x)$—— $\int_{-\infty}^x$

$P(a < X \le b) = F_X(b) -F_X(a)$
$=\int_{-\infty}^bf_X(x)dx-\int_{-\infty}^af_X(x)dx$
$=\int_a^bf_X(x)dx$

PDF为CDF的微分
- $f_X(x) =F'_X(x)$ 
- $F_X(x) =\int_a^bf_X(x)dx$ 
- $\int_{-\infty}^{\infty}f_X(x) = 1$
- $f_X(x) \ge 0$
PDF可以大于1


## 5-2 连续机率分布

#### Uniform 机率分布
在一個指定的範圍內（從a到b），每一個點發生的機會（機率密度）完全一樣
![[Pasted image 20260408165355.png]]


#### Exponential 机率分布
- 具有失意性(memoryless) —— 已经发生的事情不会影响未来的概率
- 与期望值相关
- 描述任意连续两个随机事件的间隔时间或等候时间
![[Pasted image 20260408170212.png]]

$\lambda$速率参数(rate parameter)：单位时间（或单位距离）内事件发生的平均次数
【**平均发生次數 /单位時間** : 1/t】



#### Erlang机率分布
用来modal一件有多个关卡事情的总时间，而每个关卡所需时间都是随机的

![[Pasted image 20260408170447.png]]
![[Pasted image 20260408170519.png]]

当n为1，Erlang将变成Exponential
每一个关卡是独立的Exponential lambda随机变数的整合




#### Normal 机率分布（常态分布）/ Gaussian高斯机率分布
常被用作 很多随机量的总和

X ~ Gaussian($\mu,\sigma$)
X ~ N($\mu,\sigma^2$)

PDF:
$f_X(x) =\dfrac{1}{\sqrt{2\pi\sigma}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

PDF是一个对称的钟形，对称于$\mu$，宽窄取决于$\sigma$
$\sigma$ 大则宽，小则窄


CDF:
积分算不出来，很难算



#####  Standard Normal Distribution 标准常态分布 （特殊的值）
Z ~ N(0,1)
PDF:
$F_Z(z) =\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}$

CDF:
$\Phi(z) = \int_{-\infty}^Z \frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}} du$
![[Pasted image 20260408224849.png]]![[Pasted image 20260408225256.png]

![[Pasted image 20260408225708.png]]



![[Pasted image 20260408225804.png]]![[Pasted image 20260408230018.png]]

