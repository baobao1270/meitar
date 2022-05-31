# Meitar
Meitar 是一个简单的 BiliBili 动态分页器。
如果您有翻阅大量的 BiliBili 动态的需求（半个月或 1000 条以上），由于 BiliBili 的动态加载机制问题，将产生严重的性能问题。
Meitar 通过爬取动态保存到本地 JSON，然后分页渲染为静态 HTML，从而解决此问题。

Meitar 的名字来自于 VC 圈著名爬爬怪 [御坂美团](https://space.bilibili.com/4810592) 的拼音 Meituan 和英文 Tracker。
~~虽然名字和程序的实际功能并没有什么关系~~

## 使用方法
在 Chrome 浏览器中，安装 [Get Cookies](https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid)
插件，在您登录 BiliBili 账号的情况下获取其 Cookies，并保存到程序相同目录。然后，运行如下命令： 
```
pip install -r requirements.txt
python -m venv venv
venv\Scripts\activate
spider.py    # 抓取指定时间范围并保存为 JSON
stat.py      # 描述性统计（？）
generate.py  # 生成静态 HTML 文件
```
爬取到的动态 JSON 文件为 `output.json`。必须先爬取并生成 `output.json`，然后才能生成 HTML。生成的 HTML 在 `dist` 文件夹中。
