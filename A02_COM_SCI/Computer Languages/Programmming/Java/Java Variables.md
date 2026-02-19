---
course: Programming
date: 2026-02-20
topic: Variables
tags:
  - Java
  - Variables
---
# Topic：Java Variables

## 💡 核心概念
- 主要的 Variable 分成
 Primitive：
	 1. Int
	 2. Double
	 3. Char
	 4. Boolean
	
 Reference：
	1. String
	2. Array
	3. Object


## 💻 程式碼範例
```java
public class Learn2{

    public static void main(String []args){

        /* int */
        int age = 20;
        System.out.println(age);

        /* double */
        double gpa = 4.0;
        System.out.println("My GPA is " + gpa);

        /* char */
        char grade = 'A';
        System.out.println("The grade is " + grade);
  
        /* boolean */
        boolean isStudent = true;
        System.out.println(isStudent);
  
  
        /* String */
        String name = "LWTeoh";
        System.out.println("My name is " + name + ", " + age + " years old");

    }

}
````
## Output
> 20
> My GPA is 4.0
> The grade is A
> true
> My name is LWTeoh, 20 years old