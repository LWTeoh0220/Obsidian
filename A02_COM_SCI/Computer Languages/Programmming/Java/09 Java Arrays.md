---
course: Programming
date: 2026-03-22
topic: Arrays
tags:
  - Search
  - Variables
---
# Topic：Java Arrays

## 💡 核心概念
-

## 💻 程式碼範例
```java
package Notes;
import java.util.Arrays;
import java.util.Scanner;

public class N09Array {
    public static void main(String[] args) {

        String[] fruits = {"apple", "orange", "banana", "coconut"};
        System.out.println(fruits[0]);

  
        // 修改单一元素
        fruits[0] = "pineapple";
        System.out.println(fruits[0]);

  
        // 获取数组长度 len()
        int numOfFruits = fruits.length;
        System.out.println(numOfFruits);

  
        //output each elements （way 1)
        for(int i = 0; i<fruits.length; i++){
            System.out.println(fruits[i]);
        }

  
  
        // 顺序排序
        Arrays.sort(fruits);
        //output each elements (way 2)
        for(String fruit : fruits){
            System.out.println(fruit);
        }

  

        // 让数组的每个元素都变成Pineapple
        Arrays.fill(fruits, "Pineapple");
        for(String fruit : fruits){
            System.out.println(fruit);
        }

  
  

        Scanner scanner = new Scanner(System.in);


        System.out.print("What of food do you want: ");
        // set the length of Array
        int size = scanner.nextInt();
        String[] foods = new String[size];

  
        scanner.nextLine();
        // enter user input into an array
        for(int i = 0; i < foods.length; i++){
            System.out.print("Enter a food: ");
            foods[i] = scanner.nextLine();
        }
        for(String food: foods){
            System.out.print(food + " ")
        }

  
  
  
  
        // Search array
        int[] numbers = {1,9,2,8,3,5,4};
        System.out.print("Enter a number to search: ");
        int target = scanner.nextInt();
  

        for(int i = 0; i < numbers.length; i++){
            if(numbers[i] == target){
                System.out.println("Found " + target + " at index " + i);
                break;
            }
        }

  
        boolean isfound = false;

        for(int i = 0; i < numbers.length; i++){
            if(numbers[i] == target){
                isfound = true;
                break;

            }
        }

        if(!isfound){
            System.out.println("Element not found");
        }

  
  

        // variable arguments  varargs
        System.out.println(add(1,2,3,4,5));

  

        // 2-D array

        String[] frt = {"apple", "orange", "banana"};
        String[] vegetables = {"carrot", "broccoli", "spinach"};
        String[] meets = {"chicken", "beef", "pork"};

  
  
        String[][] all = {{"apple", "orange", "banana"},
                          {"carrot", "broccoli", "spinach"},
                          {"chicken", "beef", "pork"}};
        all[0][0] = "pineapple";

        String[][] groceries = {frt, vegetables, meets};

  

        for(String[] fd : groceries){
            for(String food : fd){p
                System.out.print(food + " ");
            }
            System.out.println();
        }

        scanner.close();

  

    }

    // varargs
    static int add(int... numbers){
        int sum = 0;
        for(int number : numbers){
            sum += number;
        }
        return sum;

    }

    // varargs
    static double average(double... numbers){
        double sum = 0;
        if(numbers.length == 0){
            return 0;
        }
        for(double number : numbers){
            sum += number;
        }
        return sum / numbers.length;
    }

  
  

}
````
