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
#### double:
| 公式     | -2000.12345 —负数 | 2000.12345 —正数 | 解释       |
| ------ | --------------- | -------------- | -------- |
| %.2f   | -2000.12        | 2000.12        | 小数后两位    |
| %, .2f | -2,000.12       | 2,000.12       | 每百位加`,`号 |
| %(.2f  | (2000.12)       | 2000.12        | 负数()     |
| % .2f  | -2000.12        | ` 2000.12`     | 正数空一格    |

#### int:
| 数字   | 公式 1 | 结果 1 | 公式 2 | 结果 2 |
| ---- | ---- | ---- | ---- | ---- |
| 1    | %04d | 0001 | %-4d | 1    |
| 23   | %04d | 0023 | %-4d | 23   |
| 456  | %04d | 0456 | %-4d | 456  |
| 7890 | %04d | 7890 | %-4d | 7890 |




## 💻 程式碼範例
```java
public class HelloWorld {
    public static void main(String []args) {
       System.out.println("Hello World");
    }
}
````
