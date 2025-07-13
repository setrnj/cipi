# coding=utf-8
from pyspark import SparkContext

sc = SparkContext("local", "WordCount")

# 读取文本文件
lines = sc.textFile("input.txt")

# 分词、转小写、计数
words = lines.flatMap(lambda line: line.split()) \
    .map(lambda word: word.lower()) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

# 排序并输出前20高频词
top_words = words.sortBy(lambda x: x[1], ascending=False).take(20)
for word, count in top_words:
	print("{}: {}".format(word, count))
