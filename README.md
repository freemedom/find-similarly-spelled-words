# find-similarly-spelled-words
Find similarly spelled words
查找相似拼写写法的单词

```
查找类似拼写的单词，请输入要查找的单词：disposal

<function similar at 0x000001908B8A6B80>
按相似度排序的前10个结果：
disposal: 1.0
dispose: 0.8
postal: 0.7142857142857143
dismal: 0.7142857142857143
dismissal: 0.7058823529411765
display: 0.6666666666666666
dial: 0.6666666666666666
indispensable: 0.6666666666666666
disposition: 0.631578947368421
proposal: 0.625

<function similar_levenshtein at 0x000001908B157F70>
按相似度排序的前10个结果：
disposal: 1.0
dispose: 0.75
dismissal: 0.6666666666666667
proposal: 0.625
display: 0.625
dismal: 0.625
disappear: 0.5555555555555556
Episcopal: 0.5555555555555556
disparate: 0.5555555555555556
disposition: 0.5454545454545454
```

# 使用方法（windows）

安装python  
在下载下来的find_similar.py所在目录，输入powershell打开一个窗口
![image](https://github.com/freemedom/find-similarly-spelled-words/assets/57294686/9588abce-bc5d-4c42-b9eb-144adc76225d)
![image](https://github.com/freemedom/find-similarly-spelled-words/assets/57294686/2c7f8e86-1793-4cfd-a466-32acd3caa788)

输入python，测试python是否安装正确  
然后，在窗口里输入pip install -i https://pypi.tuna.tsinghua.edu.cn/simple textdistance
等待安装完成textdistance  
然后，输入python .\find_similar.py
即可运行






