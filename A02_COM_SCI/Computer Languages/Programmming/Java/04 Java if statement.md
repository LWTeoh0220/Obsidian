---
course: Programming
date: 2026-02-20
topic: if statement
tags:
  - if_statement
  - ternary_operator
  - enhanced_switch
latest update: 02/21/2026
---
# Topic：Java if statement

## 💡 核心概念
#### 1. if......else if......else : 
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

#### 2. ternary operator :
**variable = (condition) ? ifTrue : ifFalse;**



#### 3. enhanced switch : 
![][X_ASSETS/Java_Learning_001.png]



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
        
          
   
        /* Enhanced switch */
        scanner.nextLine();
        System.out.print("Enter a day: ");
        String day = scanner.nextLine();

  

        /*
        switch(day){
            case "Monday" -> System.out.println("It is a weekday");
            case "Tuesday" -> System.out.println("It is a weekday");
            case "Wednesday" -> System.out.println("It is a weekday");
            case "Thursday" -> System.out.println("It is a weekday");
            case "Friday" -> System.out.println("It is a weekday");
            case "Saturday" -> System.out.println("It is a weekend");
            case "Sunday" -> System.out.println("It is a weekend");
            default -> System.out.printf("%s is not a day", day);
        }
         */

        switch(day){
            case "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ->
                System.out.println("It is a weekday");
            case "Saturday", "Sunday" ->
                System.out.println("It is a weekend");
            default -> System.out.println(day + "is not a day");
        }
        
        
		scanner.close();
    }
}
````
