### 前言
-代码要简洁，前提是思路要清晰；  
-思路要清晰，基本的编程思想要直接！直接！直接！  
-python的程序从想法到落地，要经过以下几个步骤：  
需求分析-功能明确-确定模块-编写代码-测试代码-需求实现  
  
##### 需求分析
本次项目实现的是将.json文件导入本地MongoDB数据库  
目的是在脱离数据库环境操作下依然能够用其他方法恢复数据库  

##### 功能明确  
我们需要读取.json文件，我们需要驱动MongoDB数据库  

##### 确定模块 
结合功能，通过学习、查阅可以确定核心模块：  
-json和pymongo  

##### 编写代码
-具体代码可以跳转到main.py，我们这里只是将一些实现步骤做尽可能的描述：
1. 导入模块
2. 获取当前项目的目录路径
3. 创建一个空的列表，用来存放我们所有即将要读取的json文件
4. 读取当前项目目录下所有的json文件，并利用python列表的添加方法将这些文件增加到第三步创建的空列表中
5. 连接我们的本地数据库，这里我已经事先新建好了一个challenge数据库
6. 将第四步中的列表增加到我们的challenge数据库中
7. 为了测试代码是否起效，使用打印函数查询第六步的challenge数据库

##### 测试代码
首先，我们启动MongoDB数据库，  
由于我是在Windows系统下安装的，所以我采用以下方式来启动，  
当然如果你是Linux系统，可上网自行查阅其他方式来启动数据库  
+ 在..\MongoDB\bin目录下执行mongod -dbpath ..\MongoDB\data\db  
- 在bin目录下另外打开一个cmd  在bin目录下执行mongo命令  
  
在pycharm下启动我们的代码后，可以通过输出控制台或者是进入到我们的MongoDB数据库查看是否插入成功：判断的标志是我们的challenge数据库中的file集合是否有文档？有的话是否跟我们要导入的json文件一致？  
两个条件都满足的情况下即可视为此代码满足功能实现。



---
注：想要看到实现效果需要提前安装好mongodb，本人使用的是window系统，python开发IDE是pycharm
如果环境已经配置好的情况下直接将.json文件拖入到跟main.py相同的目录下后运行mian.py即可实现将
json写入本地mongo数据库
