---
type: Template
status: 🧠Understanding / 🧪Testing / 🚀Mastered
topic: 未命名
tags:
  - Templates
---
# 🧩 模型/算法：未命名


## 📌 定義與公式

a = `np.array([[1,2,3],[3,4,5]])`
b = `np.array([[1,2,3],[4,5,6],[7,8,9]])`

| Code                     | 用途        | 备注                                                     |
| ------------------------ | --------- | ------------------------------------------------------ |
| `name = np.array([])`    | 创建数组      |                                                        |
| `name[]`                 | 切片        | `a[0][1], b[:2][2]`                                    |
| `name.ndim`              | 维度        | `a = 2,b = 2`                                          |
| `name.shape`             | 每个维度的元素数量 | `len(name.shape) == name.ndim`, `a = (2,3), b = (3,3)` |
| `name.size`              | 总元素数      | `a = 6, b = 9`                                         |
|                          |           |                                                        |
| `np.zeros(1d,2d,3d)`     | 充满0的数组    | `np.zeros(4) -> array([0.,0.,0.,0.])`                  |
| `np.ones(1d,2d,3d)`      | 充满1的数组    | `np.ones(4) -> array([1.,1.,1.,1.])`                   |
| `np.empty(1d,2d,3d)`     | 随机数字      | `np.zeros(4) -> array([.,.,.,.])`                      |
| `np.arange(起始，终值+1, 增值)` | 元素范围的数组   |                                                        |
| `np.linspace()`          |           |                                                        |


## 🤖 代碼實現 (Python/Java/C++)
```python
# 優化算法實現