---
course:
date: 2026-02-22
topic: Loops
tags:
  - While_loops
  - For_loops
  - logical_operators
  - nested_loops
---
# Topic：Java Loops and logical operators

## 💡 核心概念
#### Nested Loops
| 符号  | 公式   |
| --- | ---- |
| or  | \|\| |
| and | &&   |
| not | !    |

#### While / Do While
| 符号         | 公式                                                             | 解释                                                     |
| ---------- | -------------------------------------------------------------- | ------------------------------------------------------ |
| While      | while(condition){<br>      step......<br>	  step......<br>};   | 先判断条件，再执行循环<br>条件为假，则跳过循环<br>                          |
| Do...While | do{<br>      step......<br>	  step......<br>}while(condition); | 先执行一次循环体<br>然后再检查条件是否为真<br>无论条件是否满足<br>循环体**至少会被执行一次** |

#### For
**for(nutralization;condition;step){
      step......
      step......
}**

## 💻 程式碼範例
```java
package Notes;
import java.nio.channels.Pipe.SourceChannel;
import java.rmi.server.SocketSecurityException;
import java.util.Scanner;

public class LearnLoopsAndLogicalOp {
    public static void main(String[] args) {
    
        Scanner scanner = new Scanner(System.in);
        
        String name = "";
        String response = "";

  
        /* while loops */
        
        // || = or       
        while(name.isEmpty() || name.equals("name") || name.equals(" ")){
            System.out.print("Enter your name: ");
            name = scanner.nextLine();
        }

        // ! = not
        while(!response.equals("Q")){
            System.out.print("Press Q to quit");
            response = scanner.nextLine();
        }


        int age = 0;
        // && = and
        // do...while == run the code inside do...while one time first, after that run the condition of while
        do{
            if(age>150){
                System.out.println("Your age must not higher that 150...... ");
            }
            else{
                System.out.println("Your age can't be nagative");
            }
            System.out.print("Please enter your age: ");
            age = scanner.nextInt();
        }while(age < 0 || age > 150);

  

        System.out.printf("You are %d years old\n", age);

  
        // for(nutralization;condition;step){}
        System.out.print("Start number: ");
        int start = scanner.nextInt();
        System.out.print("Ending number: ");
        int end = scanner.nextInt();
        System.out.printf("Which number you want to skip between %d to %d: ", start, end);
        int skip = scanner.nextInt();

        for(int i = start; i <= end; i++){
            if(i == skip){
                continue;
            }
            System.out.println(i);
        }

  

        // nested loops
        for(int i = 1; i <=3; i++){
            for(int j = 1; j<=10; j++){
                System.out.print(j+10*(i-1) + " ");
            }
            System.out.println();
        }
        
        scanner.close();
    }
}
````
