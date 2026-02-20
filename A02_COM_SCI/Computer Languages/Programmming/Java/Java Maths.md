---
course:
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
-  x++ 是  `x += 1`  x-- 是 `x -= 1` 

#### math:
- **Mathematical Constants** ： PI /  E / TAU
- 

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
