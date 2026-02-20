---
course: Programming
date: 2026-02-20
topic:
tags:
  - Java
  - arithmetic
  - math
  - Random
---
# Topic：Java Maths

## 💡 核心概念
#### arithmetic:
- 可使用 `+=` / `-=` / `*=` / `%=`
- x++ 是  `x += 1` ,  x-- 是 `x -= 1` 

#### Math:
- **Mathematical Constants** ： PI /  E / TAU

|     数字      |         公式         |
| :---------: | :----------------: |
|    power    |  Math.pow(数字, 次数)  |
|  absolute   |    Math.abs(数字)    |
| square root |   Math.sqrt(数字)    |
|    四舍五入     |   Math.round(数字)   |
|    向上取整     |   Math.ceil(数字)    |
|    向下取整     |   Math.floor(数字)   |
|   maximum   | Math.max(n.1, n.2) |
|   minimum   | Math.min(n.1, n.2) |

#### Random:
##### 前置作业：
1. import java.util.Random;
2. Random random = new Random();

|       数字        |            公式             |
| :-------------: | :-----------------------: |
|     两数间的int     | random.nextInt(最小数，最大数+1) |
|    0-1之间的随机数    |   random.nextDouble();    |
| 随机返回 true/false |   random.nextBoolean();   |
## 💻 程式碼範例
```java
package Notes;
import java.util.Random;

public class LearnMaths {
    public static void main(String[] args) {
    
        /* arithmetic */
        double x = 10;
        double y = 3;

  
        x += y;
        System.out.println(x);
        x++;
        System.out.println(x);

  
        x -= y;
        System.out.println(x);
        x--;
        System.out.println(x);

  
  
        x *= y;
        System.out.println(x);

        x /= y;
        System.out.println(x);

        x %= y;
        System.out.println(x);

  

        /* Math */
        System.out.println(Math.PI);
        System.out.println(Math.E);
        System.out.println(Math.TAU);

  
        double result;
        
        result = Math.pow(2,5);
        System.out.println(result);

        result = Math.abs(-5);
        System.out.println(result);

        result = Math.sqrt(9);
        System.out.println(result);

        result = Math.round(3.14);
        System.out.println(result);

        result = Math.ceil(3.14);
        System.out.println(result);

        result = Math.floor(3.99);
        System.out.println(result);

        result = Math.max(5,15);
        System.out.println(result);

        result = Math.min(5,15);  
        System.out.println(result);

  

        /* Random numbers */
        Random random = new Random();

        int number1;
        double number2;
        boolean number3;

        number1 = random.nextInt(1,6);
        System.out.println(number1);

        number2 = random.nextDouble();
        System.out.println(number2);

        number3 = random.nextBoolean();
        System.out.println(number3);

    }
}
````
