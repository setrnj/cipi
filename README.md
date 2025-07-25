# Spark大规模文本词频统计

## 项目简介
本项目基于 Apache Spark，实现对大规模文本文件（支持中英文）的高效词频统计，适用于大数据分析、文本挖掘等场景。

## 功能特点
- 支持大规模文本分布式词频统计
- 兼容中文、英文及特殊符号
- 兼容 Python 2/3，支持 Spark 单机与集群运行
- 结果输出至终端或文件，可灵活扩展

## 环境依赖
- Python 3.6 及以上（推荐）
- Apache Spark 2.3 及以上
- Hadoop（可选，推荐用于大规模数据）

## 安装与运行

1. 克隆仓库
   ```bash
   git clone https://github.com/yourname/wordcount-spark-demo.git
   cd wordcount-spark-demo
   ```

2. 准备数据  
   将待统计的文本文件命名为 `input.txt` 放在项目根目录。

3. 运行脚本  
   ```bash
   export PYSPARK_PYTHON=python3
   spark-submit wordcount.py
   ```

## 使用示例

文本样例（input.txt）：
```
你们有你们的黎巴嫩，我有我的黎巴嫩。
我的心重负着累累果实
你们有你们的黎巴嫩，我有我的黎巴嫩
```

运行结果：
```
你们有你们的黎巴嫩，我有我的黎巴嫩。: 3
我的心重负着累累果实: 2
...
```

![运行截图](./image.png)
## 项目目录结构

```
wordcount-spark-demo/
│
├── wordcount.py        # 主程序
├── input.txt           # 示例输入文本
├── README.md           # 项目说明文档
└── screenshot.png      # 运行示例截图
```

## 技术实现与亮点

- 使用 Apache Spark 的 RDD 机制，实现分布式高性能统计
- 针对中文/英文混合文本的分词与编码问题做了适配
- 支持灵活扩展，后续可用于情感分析、关键词提取等

## 常见问题

- **编码错误**：请确保使用 Python3 并设置 `export PYSPARK_PYTHON=python3`
- **找不到文件**：请检查输入文件路径和名称

## License

MIT

## 联系方式

如有建议或问题，欢迎提 issue 或联系邮箱 a0635886@qq.com

