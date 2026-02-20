---
course: Programming
date: 2026-02-20
topic:
tags:
  - Java
  - Printf
---
# Topic：Java Printf

## 💡 核心概念
- System.out.printf("%s is %d years old \n", name, age)


| Variable | 公式                         | key word |
| :------: | -------------------------- | -------- |
|  String  | printf(" ......%s\n", x ); | %s       |
|   char   | printf(" ......%c\n", x ); | %c       |
|   int    | printf(" ......%d\n", x ); | %d       |
|  double  | printf(" ......%f\n", x ); | %f       |
| boolean  | printf(" ......%b\n", x ); | %b       |
##### double（- 2000.12345）:
| 公式  | -2000.12345 | 2000.12345 |
| --- | ----------- | ---------- |
|     |             |            |
%.2f  ------>  -2000.12
%, .2f ------> -2,000.12
%(.2f -------> (2000.12)
%  .2f -------->-2000.12



## 💻 程式碼範例
```java
public class HelloWorld {
    public static void main(String []args) {
       System.out.println("Hello World");
    }
}
````
