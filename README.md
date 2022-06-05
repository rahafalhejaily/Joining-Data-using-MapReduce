# Joining Data using MapReduce
### Assignment: Joining Data
In this assignment, you are given a Python mapper and reducer to perform the Join Data.

Part 1
=======
**Step 1** : Make the Python scripts for the mapper and reducer executable. Execute the following commands:
```
chmod +x join1_mapper.py && chmod +x join1_reducer.py
```

**Step 2**: Test the program in serial execution my executing the following command: 

```
cat join1_File*.txt | ./join1_mapper.py | sort | ./join1_reducer.py
```
The output of the command:
```
Apr-04 able 13 991
Dec-15 able 100 991
Jan-01 able 5 991
Feb-02 about 3 11
Mar-03 about 8 11
Feb-22 actor 3 22
Feb-23 burger 5 15
Mar-08 burger 2 15

```


**Step 3** : Run the following commands to put the data files `join1_FileA.txt` and `join1_FileB.txt` into the Hadoop Distributed File System. 

Create a folder called "assign2"

```
hdfs dfs -mkdir /user/cloudera/assign2
```

Put the first file in
```
hdfs dfs -put ~/map-reduce-join-exercise/join1_FileA.txt /user/cloudera/assign2/
```

Now the second one
```
hdfs dfs -put ~/map-reduce-join-exercise/join1_FileB.txt /user/cloudera/assign2/
```

**Step 4** : Run the map-reduce job using the following command :

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/cloudera/assign2 -output /user/cloudera/output_join  -mapper /home/cloudera/join1_mapper.py -reducer /home/cloudera/join1_reducer.py
```
The output of the command , It should be similar to the the output of step 2.

Part 2
=======

**Step 1** : Create the data files using `make_join2data.py` with different arguments. This is included in the shell script `make_data.sh` which can be run by invoking the command:
```
sh make_data.sh
```
**Step 2**: Use HDFS commands to copy the 6 files created in step 1 into one HDFS directory:
Create a folder called "join_input"
```
hdfs dfs -mkdir /user/cloudera/join_input
```
Put the all file in
```
hdfs dfs -put /home/cloudera/join2_genchan* /user/cloudera/join_input
```
```
hdfs dfs -put /home/cloudera/join2_gennum* /user/cloudera/join_input/
```
**Step 3**: Make the Python scripts for the mapper and reducer executable. Execute the following commands:
```
chmod +x join2_mapper.py && chmod +x join2_reducer.py
```
**Step 4**: Test the program in serial execution my executing the following command:
```
cat join2_gen*.txt  | ./join2_mapper.py | sort | ./join2_reducer.py
```
The output of the command:
```
('Almost_Games', 49237)
('Almost_News', 46592)
('Almost_Show', 50202)
('Baked_Games', 51604)
('Baked_News', 47211)
('Cold_News', 47924)
('Cold_Sports', 52005)
('Dumb_Show', 53824)
('Dumb_Talking', 103894)
('Hot_Games', 50228)
('Hot_Show', 54378)
('Hourly_Cooking', 54208)
('Hourly_Show', 48283)
('Hourly_Talking', 108163)
('Loud_Games', 49482)
('Loud_Show', 50820)
('PostModern_Games', 50644)
('PostModern_News', 50021)
('Surreal_News', 50420)
('Surreal_Sports', 46834)

```
**Step 5** : Run the map-reduce job using the following command :
```
hadoop  jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/cloudera/join_input  -output /user/cloudera/join_output  -mapper /home/cloudera/join2_mapper.py -reducer /home/cloudera/join2_reducer.py -numReduceTasks 1
```
The output of the command , It should be similar to the the output of step 4.
