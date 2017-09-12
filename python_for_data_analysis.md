Sources for this book 网上资源:

[github.com/pydata/pydata-book](http://github.com/pydata/pydata-book "sources")

defualt naming conventions 命名规则:

	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt

Introduction引言
===
使用json模块， 转换json格式为python的dict格式

convert json format to dict.

    import json
    line = open(filename).readline()
    outDict = json.loads(line)

使用collections的Counter类统计字典的频次
find the highest frequence of the dict:

    from collections import Counter
    counts = Counter(dict)
    counts.most_common(n)

使用pandas的DataFrame
    
    from pandas import DataFrame
    frame = DataFrame(records)
    frame['tz'].value_counts()

    #fill Na and null
    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'

    tz_counts = clean_tz.value_counts()
    #this command need to enable pylab
    %pylab
    tz_counts[:10].plot(kind='barh', rot=0) 


#Ipython

use ? or ?? to introspection the variable or func:

variable?

use %run command:%run scrip.py

Ipython快捷键:     

![Ipython 快捷键](ipython_keys.PNG)

Magic command:

![Magic command 1](magic_command1.PNG)

![Magic command 2](magic_command2.PNG)

use qt gui:

    ipython qtconsole --pylab=inline

log recording:

    %logstart


