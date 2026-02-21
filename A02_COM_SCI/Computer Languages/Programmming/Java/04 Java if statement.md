---
course: Programming
date: 2026-02-20
topic: if statement
tags:
  - if_statement
  - ternary_operator
---
# Topic：Java if statement

## 💡 核心概念
- 公式： 
if( 条件){
内容....
内容....
}
else if(条件){
内容...
内容...
}
else{
内容...
内容...
}




## 💻 程式碼範例
```java
package Notes;
import java.util.Scanner;
public class LearnIfStatement {
    public static void main(String[] args) {
    
        Scanner scanner = new Scanner(System.in);

        int age;
        String name;

  
        System.out.print("Enter your name: ");
        name = scanner.nextLine();

        System.out.print("Enter your age: ");
        age = scanner.nextInt();


        if(name.isEmpty()){
            System.out.println("You didn't enter your name?");
        }
        else{
            System.out.println("Hello " + name);
        }


        if(age >= 60){
            System.out.println("You are a senior");
        }
        else if(age >= 18){
            System.out.println("You are an adult");
        }
        else if(age < 0){
            System.out.println("You are a baby");
        }
        else if(age == 0){
            System.out.println("You haven't been born yet");
        }
        else{
            System.out.println("You are a child");
        }
        
        
          

        /* ternary operator  */
        // variable = (condition) ? ifTrue : ifFalse;

        int score = 55;

        String passOrFail = (score >= 60) ? "Pass" : "Fail";
        System.out.println(passOrFail);
        
        
		scanner.close();
    }
}
````
