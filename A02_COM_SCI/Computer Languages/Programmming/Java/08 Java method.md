---
course: Programming
date: 2026-02-24
topic: method
tags:
  - method
  - overloaded_methods
  - variable_scope
---
# Topic：Java method

## 💡 核心概念
#### 静态方法（Static Methods）

回传值（Return Value）的类型

| 程式                     | 表示           |
| ---------------------- | ------------ |
| static void xxx(){}    | 不回传数据        |
| static String xxx(){}  | 回传文字Str      |
| static double xxx(){}  | 回传浮点数double  |
| static boolean xxx(){} | 回传布林值boolean |
(String xxx, double xxx, boolean xxx)

#### 方法重载 (Method Overloading)
- 方法名相同
- 参数列表（patameters）不同
- 返回值可以不同
> 重复相同的参数列表会判定为“重复定义”（Duplicate Method），导致编译失败

the three dimension:

| 变化                                           | 解释   |
| -------------------------------------------- | ---- |
| add(int a) vs add(int a, int b)              | 数量不同 |
| add(int a) vs add(double a)                  | 类型不同 |
| add(int a, double b) vs add(double a, int b) | 顺序不同 |

#### 變數範圍 (Scope)


## 💻 程式碼範例
```java
package Notes;
import java.util.Scanner;
public class LearnMethod {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

  
        System.out.print("Enter your first name: ");
        String first = sc.nextLine();

        System.out.print("Enter your last name: ");
        String last = sc.nextLine();

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

  
        yourInfo(first,last, age);
        
        double number = 5;
        System.out.println(square(number));
        
        System.out.println(getFullName(first, last));

  
        if(ageCheck(age)){
            System.out.println("You are an adult");
        }
        else{
            System.out.println("You are not an adult");
        }
        sc.close();
    }

  

    static void yourInfo(String first, String last, int age){
        System.out.printf("Your name is %s %s\n", first, last);
        System.out.printf("Your age is %d\n", age);
    }

    static double square(double number){
        return number * number;
    }
  
  
  // Method Overload
    static String getFullName(String first){
        return first + " ";
    }
    static String getFullName(String first, String last){
        return first + " " + last;
    }

    static boolean ageCheck(int agee){
        if(agee >= 18){
            return true;
        }
        else{
            return false;
        }
    }
}
````
