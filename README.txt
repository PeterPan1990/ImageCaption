1.本系统运行环境：Ubuntu 14.04, 软件：Matlab2014a， python2.7， Spyder. 
2.系统依赖库：Caffe, RCNN, 具体配置参照Github 相关项目主页

3.本系统GUI使用python自带gui库tkinter搭建，建议使用spyder演示

4.操作流程：1）使用示例图片演示：点击相应图片，点击generate text按钮生成图片描述；点击detect按钮生成图片主要识别物体
	   
	    2）使用本地图片演示：点击Choose file按钮，选择本地图片，其后操作同1）
           
	    3）使用网页图片演示：在浏览器上找到要处理图片，邮件复制图片链接，拷贝到GUI输入框，下载图片，其后操作同1）

5.note:图片翻译单张图片处理时间大概5s,不同机器可能有差异；图片检测单张图片处理时间大概18s，每张图片大约会提取2000窗口图片进行识别，因此比较慢

6.使用流程：按照好所有依赖软件和库后，打开Demo-gui文件夹中的Demo-tkinter.py文件即可执行
7.完整版的源码和相关的模型文件请参照我们项目的Github主页：https://github.com/PeterPan1990/ImageCaption
