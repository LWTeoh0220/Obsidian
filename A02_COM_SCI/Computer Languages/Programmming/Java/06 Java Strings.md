---
course: Programming
date: 2026-02-21
topic:
tags:
  - Java
  - String
  - SubString
---
# Topic：Java Strings

## 💡 核心概念

| 表示                  | 公式                           |
| ------------------- | ---------------------------- |
| 输出index数量           | x.length();                  |
| 依据index找元素          | x.charAt();                  |
| 依据元素找最前index        | x.indexOf("元素");             |
| 依据元素找最后index        | x.lastIndexOf("元素");         |
|                     |                              |
| 所有元素小写              | x.toLowerCase();             |
| 所有元素大写              | x.toUpperCase();             |
| 去除前后空白格             | x.trim();                    |
|                     |                              |
| 替换元素                | x.replace("元素1", "元素2“);     |
| 确认是否为空 true/false   | x.isEmpty();                 |
| 确认是否包含元素 true/false | x.contains("元素");            |
| 确认是否完全等于            | x.equals("String");          |
| 确认是否等于（忽略大小写）       | x.equalsIgnoreCase("String); |
|                     |                              |
| SubString           |                              |
| index 0 到 10        | x.substring(10)              |
|                     | x.substring()                |

## 💻 程式碼範例
```java
package Notes;

public class LearnString {
    public static void main(String[] args) {
    
        /* String mathod */
        String name = " LWTeoh L ";
       
        int length = name.length();
        char letter = name.charAt(0);
        int index = name.indexOf("L");
        int lastIndex = name.lastIndexOf("L");

        System.out.println(length);
        System.out.println(letter);
        System.out.println(index);
        System.out.println(lastIndex);

  
        name = name.toLowerCase();
        System.out.println(name);

        name = name.toUpperCase();
        System.out.println(name);

        name = name.trim();
        System.out.println(name);

  
        name = name.replace("L", "G");
        System.out.println(name);
        
        System.out.println(name.isEmpty());
        System.out.println("".isEmpty());

        System.out.println(name.contains(" "));
        System.out.println(name.contains("L"));

  

        System.out.println(name.equals("LWTEOH L"));
        System.out.println(name.equals("GWTEOH G"));
        System.out.println(name.equalsIgnoreCase("gwteoh g"));

  

        /* SubString mathod */
        String email = "t114ab0049@ntut.org.tw";
        
        String studentID = email.substring(0,10);
        String domain1 = email.substring(10);
        String domain2 = email.substring(email.indexOf("@") +1 );

        System.out.println(studentID);
        System.out.println(domain1);
        System.out.println(domain2);
    }
}
````
