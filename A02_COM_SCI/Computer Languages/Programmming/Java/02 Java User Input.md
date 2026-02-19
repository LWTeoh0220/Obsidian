---
course: Programming
date: 2026-02-20
topic: User Input
tags:
  - Java
  - User_Input
  - Templates
---
# Topic：Java User Input

## 💡 核心概念
#### 固定步骤：
1. import java.util.Scanner;
2. Scanner scanner = new Scanner(System.in);
3. scanner.close();
>- class外面import
>- 代码写在步骤二（开启）和步骤三（关闭）之间

| Variable | Step                |
| :------: | ------------------- |
|   int    | x = scanner.nextInt |
#### 注意事项：
1. 若希望输入时在下一行则用 System.out.**println**();  否则为System.out.print();就可以了
2. 如果是input String，同时String不是第一个input，就要在String的Sout前面放scanner.nextLine();
3. nextInt, nextLine, nextDouble 记得I、L、D、B都要大写



## 💻 程式碼範例
```java
import java.util.Scanner;

public class LearnUserInput {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int age = 0;
        double gpa = 0;

  
        System.out.print("Enter your age: ");
        age = scanner.nextInt();
        scanner.nextLine();

  
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
  

        System.out.print("What is your gpa: ");
        gpa = scanner.nextDouble();

  

        System.out.print("Are you a student (true/false): ");
        boolean isStudent = scanner.nextBoolean();

  

        System.out.println("Hello " + name);
        System.out.println("You are " + age + " years old");
        System.out.println("Your gpa is " + gpa);
        System.out.println(isStudent);


        scanner.close();

    }
}
````

