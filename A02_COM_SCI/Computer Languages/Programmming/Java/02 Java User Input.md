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

