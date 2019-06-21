**Note**

UCloud 已经上线新版     
[Python2 OpenAPI SDK](https://github.com/ucloud/ucloud-sdk-python2)    
[Python3 OpenAPI SDK](https://github.com/ucloud/ucloud-sdk-python3)    

- 本仓库废弃
- 原来的 SDK 可以继续使用，但不会继续更新。
- 新版的会推送到 python 官方仓库中，可以直接用包管理器（pip、pipenv）安装。

相对旧版 Python SDK，新版本增加了如下特性：

1. 注册到 Python 官方仓库，支持包管理器（pip、pipenv）安装，可以使用国内包管理器镜像加速
2. 自动对幂等请求重试，增强对不稳定网络的适应性
3. 可选的类型检查，增强开发者对使用 SDK 开发大规模应用的信心 
4. 可选的泛化请求方式，支持对 SDK 未支持的 API 发起自定义请求
5. 丰富的工具函数，如轮询实例状态等
6. 统一的 API Schema 定义，保持与 API 同步更新

- 新版地址：https://github.com/ucloud/ucloud-sdk-python3
- 新版文档：https://ucloud.github.io/ucloud-sdk-python3
- 新版安装方式：pip install ucloud-sdk-python3
