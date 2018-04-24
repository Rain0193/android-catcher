# 写在前面
本文主要介绍一个基于 **uiautomator2** 封装的一个 **Python** 库 **android-catcher**，该库的功能主要有对 **Android** 设备进行 **UI 自动化测试**和**采集手机性能数据**，适用于如列表滑动、录制视频等各种测试场景下 **CPU、内存、帧率**等信息的捕获，方便后续分析。


# 安装
### 安装 Python
自动化测试的脚本是用 **Python 3** 写的，要运行脚本需要先安装 Python 3 环境  
下载地址：
[Python 3.6.5](https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe)  
### 安装 android-catcher 依赖
打开脚本目录执行以下命令，安装依赖 
```
pip install -r requirements.txt
```


# Usage
### uiautomator2 的使用方式
安装完 uiautomator2 之后，一般只需要执行以下命令对设备进行初始化，在设备上安装 uiautomator2 服务

```
python -m uiautomator2 init
```

出现以下提示则表示安装成功  
![uiautomator初始化成功](https://img-blog.csdn.net/20180424213848579?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NoYXJtaW5nV29uZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
更多的 uiautomator2 的使用方式可参考：https://github.com/openatx/uiautomator2

### 脚本文件说明
这个脚本库根目录下主要的文件有

 - **info.py**：手机性能信息采集的脚本，其中定义了父类 Info，已实现的子类有 **CPUInfo(CPU信息)、MemInfo(内存信息)、FPSInfo(帧率信息)、NetInfo(网络流量信息)**，使用者可以从 Info 派生子类来实现自己的采集需求
 - **task.py**：测试场景的脚本，其中定义了父类 Task，因为没有固定的测试场景，因此使用者需要从 Task 派生子类并重写 `Task#execute` 方法来自定义的测试场景，自定义方式可参考：https://github.com/openatx/uiautomator2
 - **info_task.py**：测试场景和采集信息灵活结合的脚本，使用者不需要用到
 - **utils.py**：工具方法脚本
 - **\_main\_.py**：任务运行的入口脚本，当没有具体的测试场景，只是想采集指定时间段的信息，直接运行该脚本

### 参数说明
- -s：必选参数，指定设备号，可通过 `adb devices` 获取
- -a：必选参数，要测试进程的 applicationId
- -f：可选参数，采样间隔，单位为秒，不建议设置太短，最好是大于 0.1s，默认是 1s
- -d：可选参数，采样持续时间，默认为10s
- -i：可选参数，需要采集的信息，可以设置多个，目前可选的有四个，分别为  `cpu、mem、fps、net`，用 "," 隔开，如 `-i cpu,mem,fps,net`
- -o：可选参数，采集到的信息的输出目录，如 "." 表示当前脚本所在的目录，默认为 "."

### 生成文件说明
采集到的信息根据信息类型分别存放在指定输出目录的 `cpu_stats、mem_stats、fps_stats、net_stats` 四个子目录下，文件名为 `信息类型_设备号_applicationId_版本号_测试场景名_时间戳`，如 `cpu_d3c2edaa_video.like_RecordVideo_1.9.9_1524122928.csv.csv`，实际效果大致如下图
![](https://img-blog.csdn.net/20180424214359452?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NoYXJtaW5nV29uZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)


输出文件为 csv 文件，直接打开和用 Excel 打开的效果分别如下图  
![这里写图片描述](https://img-blog.csdn.net/20180424214415833?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NoYXJtaW5nV29uZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
![这里写图片描述](https://img-blog.csdn.net/20180424214422913?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NoYXJtaW5nV29uZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
另外可以为测试的每个阶段添加一个节点说明 

```
task.period = "idle"
```
生成类似如下的图  
![这里写图片描述](https://img-blog.csdn.net/20180424220059723?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NoYXJtaW5nV29uZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
### 无自定义测试场景的使用方式
适用于没有具体测试场景，在脚本运行之后一段时间内都处于采集状态的情况，持续时间可以通过配置参数指定，过程中使用者可以随意操作手机。通过命令行直接运行 `_main_.py` 脚本文件，并指定相关参数
比方说我要采集 applicationId 为 `video.like` 这个应用 10s 内的 cpu 信息和内存信息，采样间隔为 200ms，输出目录为当前目录，那么可以在脚本所在的目录执行以下命令

```
python _main_.py -s 设备号-a video.like -f 0.2 -d 10 -i mem,cpu -o .
```

脚本运行结束之后可以在根目录下看到如下图所示的文件生成

![这里写图片描述](https://img-blog.csdn.net/20180424214443810?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NoYXJtaW5nV29uZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

注：要带 -d 参数，指定采集的持续时间，否则脚本默认运行 10s，并且无需 -t 参数，默认测试场景名为 `Random`

### 自定义测试场景的使用方式
自定义测试场景不能直接调用 `_main_.py` 脚本，需要创建新的脚本，继承 `task.py#Task` 并重写 `Task#execute` 方法，在 `Task#execute` 中实现自定义测试场景的逻辑，如下图所示：

![这里写图片描述](https://img-blog.csdn.net/20180424214454377?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NoYXJtaW5nV29uZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

这里创建了名为 `start_app.py` 的脚本，运行命令：

```
python start_app.py -s 设备号-a 进程名 -f 0.1 -i cpu,mem -o .
```

就可以启动对应的 APP，并采集 CPU 信息和内存信息，采样间隔为 100ms，输出到当前目录。注意这里没有了 -d 参数，因为采集的持续时间以测试任务的持续时间的持续时间为准，设置的参数一定要按照说明来，否则不能采集到数据
如果想采集自定义的信息，可以继承 `info.py#Info` 并重写 `Info#get_start_info` 和 `Info#get_end_info` 方法，可参考已实现的四种信息采集的写法，最后通过 `Task#add_info` 方法添加。

自定义好测试场景之后，调用 `_main_#main` 方法，传入测试场景实例，测试场景的名称会作为输出文件命名的一部分，这里最好取能准确表达测试场景的名称，如某个 APP 录制视频测试场景的名称为 `RecordVideo`
采集到的信息可通过 Excel 制成图表，以下是完整录制视频这个测试场景的 CPU 占比和内存的变化  
![这里写图片描述](https://img-blog.csdn.net/20180424214747362?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NoYXJtaW5nV29uZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
![这里写图片描述](https://img-blog.csdn.net/20180424214854715?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NoYXJtaW5nV29uZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
通过图表可以直观分析应用不同版本和不同场景下的性能状况

# 写在最后
以上就是该库的一些使用介绍。由于工作经验尚浅，Python 也是现学现用，在写这个库时，可能会有许多考虑不周或不完善的地方，有能力的小伙伴可以直接修改该库，以实现更多自定义功能，另外也希望大家能多用，多发现问题，欢迎 issue，欢迎 star，有新的使用需求和想法也欢迎提出，后续会不断完善，感谢！






























