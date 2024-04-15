# **COMFYUI LLM PARTY——面向comfyui开发的LLM工具节点库** 

## 简介
[comfyui](https://github.com/comfyanonymous/ComfyUI)是一个极为简约的UI界面，主要用于AI绘图等基于SD模型的工作流搭建。本项目希望基于comfyui开发一套完整的用于LLM工作流搭建的节点库。可以让用户更便捷快速地搭建自己的LLM工作流，并且更方便地接入自己的SD工作流中。

## 使用说明
[【ComfyUI×LLM】手把手教你如何搭建积木化智能体（超简单！）](https://www.bilibili.com/video/BV1JZ421v7Tw/?vd_source=f229e378448918b84afab7c430c6a75b)

## 特征
1. 本项目包含如下节点
   -  "LLM": "大语言模型（LLM）"
   -  "load_file": "从comfyui_LLM_party/file加载文件（load_file from comfyui_LLM_party/file）"
   -  "tool_conbine":"工具组合（tool_conbine）"
   -  "tool_conbine_plus":"超大工具组合（tool_conbine_plus）"
   -  "time_tool": "时间工具（time_tool）"
   -  "weather_tool":"天气工具（weather_tool）"
   -  "google_tool":"谷歌搜索工具（google_tool）"
   -  "check_web_tool":"检视网页工具(check_web_tool)"
   -  "file_conbine":"文件组合（file_conbine）"
   -  "file_conbine_plus":"超大文件组合（file_conbine_plus）"
   -  "start_dialog":"开始对话（start_dialog）"
   -  "end_dialog":"结束对话（end_dialog）"
2. 支持openai的API驱动，并支持自定义base_url，可以使用中转API驱动LLM节点
3. 支持多种类型的文件类型导入LLM节点，通过RAG技术让LLM可以针对文件内容作答，目前支持以下文件类型：.docx、.xlsx、.csv、.txt、.py, .js, .java, .c, .cpp, .html, .css, .sql, .r, .swift
4. 通过工具组合节点可以将多个工具传入LLM节点，通过文件组合节点可以将多个文件传入LLM节点
5. 支持谷歌搜索和对单一网页的搜索，让LLM可以联网查询
6. 可以通过start_dialog节点和end_dialog节点，实现两个LLM之间的回环链接，即两个LLM互相为对方的输入和输出！
7. 推荐配合[ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)的show_text节点，作为LLM节点的输出显示

## 下载
[百度云下载](https://pan.baidu.com/s/13ogn1np6bHgxOJhS--QJmg?pwd=jppj) （推荐！包含一个环境配置完毕且包含本项目的comfyui压缩包和一个本项目文件夹，前者下载完后不用再配置环境！）

或使用以下方法之一安装
### 方法一：
1. 导航到 ComfyUI 根文件夹中下的`custom_nodes`子文件夹
2. 使用克隆此存储库。`git clone https://github.com/heshengtao/comfyui_LLM_party.git`

### 方法二：
1. 点击右上角的`CODE`
2. 点击`download zip`
3. 将下载的压缩包解压到ComfyUI 根文件夹中下的`custom_nodes`子文件夹中

## 环境部署
1. 导航到`comfyui_LLM_party`的项目文件夹
2. 在终端输入`pip install -r requirements.txt`将本项目需要的第三方库部署到comfyui的环境中。请注意你是否在comfyui的环境进行安装，并关注终端中的`pip`报错
3. 如果你是用的comfyui启动器，你需要在终端中输入 `启动器配置中的路径\python_embeded\python.exe 启动器配置中的路径\python_embeded\Scripts\pip.exe  install -r requirements.txt`进行安装。`python_embeded`文件夹一般与你的`ComfyUI`文件夹同级。

## 配置
可以使用以下方法之一配置APIKEY
### 方法一：
1. 打开`comfyui_LLM_party`的项目文件夹下的`config.ini`文件
2. 在`config.ini`输入你的`openai_api_key`、`base_url`
3. 如果你要使用谷歌搜索工具，在`config.ini`输入你的`google_api_key`、`cse_id`

### 方法二：
1. 打开comfyui界面
2. 新建大语言模型（LLM）节点，在节点中直接输入你的`openai_api_key`、`base_url`
3. 新建谷歌搜索工具（google_tool）节点，在节点中直接输入你的`google_api_key`、`cse_id`

## 下一步计划：
1. 更多的常用工具节点，比如：代码解释器、文字转语音输出、识别图中文字信息等等
2. 让LLM可以内部调用一个附属于它的LLM，让助手也有自己的助手。
3. 更多可以与comfyui中的大量SD节点进行连接的新节点，让LLM与SD有更多的可能，并提供相关的工作流

## 如果我的工作给您带来了价值，请考虑请我喝一杯咖啡吧！您的支持不仅为项目注入活力，也温暖了创作者的心。☕💖 每一杯都有意义！
<div style="display:flex; justify-content:space-between;">
    <img src="img/zhifubao.jpg" style="width: 48%;" />
    <img src="img/wechat.jpg" style="width: 48%;" />
</div>