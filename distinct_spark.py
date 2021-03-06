from pyspark import SparkContext
import re

# remove any non-words and split lines into separate words
# finally, convert all words to lowercase
def splitter(line):
        line = re.sub(r'^\W+|\W+$', '', line)
	return map(str.lower, re.split(r'\W+', line))

#using mapreduce concept to count the distinct number of words
if __name__ == '__main__':
        sc = SparkContext("local", "distinct_wordcount")
	text = sc.textFile('pg2701.txt')#read file
	words = text.flatMap(splitter)#splitter function on every line
        words_mapped = words.map(lambda x: (x,1))#playing map part
	counts = words_mapped.reduceByKey(lambda x,y:1)#playing reduce part and then count
	c = counts.count()
	print(c)
