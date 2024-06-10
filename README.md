# Cloud-Hadoop

We used the Austen, Shelley, and Bronte texts. 

```
hdfs dfs -rm -r /user/sandbox/words
mapred streaming \
  -input /user/sandbox/books \
  -output /user/sandbox/words \
  -mapper mapper.py \
  -reducer reducer.py \
  -file scripts2/mapper.py \
  -file scripts2/reducer.py
```
