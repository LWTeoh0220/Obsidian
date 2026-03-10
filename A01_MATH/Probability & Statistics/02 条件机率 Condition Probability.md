---
course: P & S
category:
tags:
  - Maths
  - Probability
latest update: 2026-03-10
status:
---
# Topic：条件机率 Condition Probability


P($X | Y$  ) 
$X$：所关心之事件
$Y$  : 条件（观察到的，已发生的事件）

若某实验结果$o_i$ 与某条件$Y$ 不相交，则
P($o_i$ | $Y$ ) = 0


P($o_i | Y$) = $\frac{P(o_i)}{P(o_i) + P(o_2) + \dots + P(o_n)}$ = $\frac{P(o_i)}{Y}$

考虑事件 X = {$o_1,o_2,q_1,q_2$}，已知事件Y = {$o_1,o_2,o_3$}发生，则
P(X|Y) = P($o_1 | Y$) + P($o_2 | Y$) = $\frac{P(o_1)}{P(Y)}$ + $\frac{P(o_2)}{P(Y)}$ = $\frac{P({o_1,o_2})}{P(Y)}$ = $\frac{P(X \cap Y)}{P(Y)}$

#### P($X|Y$) = $\frac{P(X \cap Y)}{P(Y)}$ 

>key words:
 "condition on", "Suppose", "if", "Assuming", "given that"


#### 条件机率性质
1. 性质一 ： P(X|Y) = $\frac{P(X \cap Y) \ge 0}{P(Y) \ge 0}$ $\ge 0$
2. 性质二： P(Y|Y) = $\frac{P(Y \cap Y)}{P(Y)}$ = 1
3. 性质三： A，B互斥，则P($A \cup B|Y$) = $\frac{P(A)}{P(Y)} + \frac{P(B)}{P(Y)}$ = P(A|Y) + P(B|Y)


---
## Total Probability 定理

P(A) = P(A|$C_1$)P($C_1$) + P(A|$C_2$)P($C_2$) + $\dots$  + P(A|$C_n$)P($C_n$)

