# PKUAutoElective 2021 Spring Version

本项目基于 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective)，对 2021 春季学期的选课网站 API 改动进行了调整。并针对验证码系统的改动，将识别系统转为在线平台 [TT识图](http://www.ttshitu.com)，目前识别准确度仍然略微堪忧。

## 安装

请参考 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective) 项目提供的安装指南进行安装，但本项目不依赖于 `pytorch`，因此可以省略其中的以下部分

> 安装 PyTorch，从 PyTorch 官网 中选择合适的条件获得下载命令，然后复制粘贴到命令行中运行即可下载安装。（注：本项目不需要 cuda，当然你可以安装带 gpu 优化的版本）
> 
> ......
> 
> PyTorch 安装时间可能比较长，需耐心等待。
> 如果实在无法安装，可以考虑用其他方式安装 PyTorch，详见附页 PyTorch 安装

## 配置文件

### config.ini

参考 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective) 项目中的 `config.ini` 配置说明

### apikey.json

该文件为 [TT识图](http://www.ttshitu.com) 平台的 API 密钥，在平台注册后，填入用户名与密码即可。

```json
{
    "username": "xiaoming",
    "password": "xiaominghaoshuai" 
}
```