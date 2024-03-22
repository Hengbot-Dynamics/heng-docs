---
sidebar_position: 1
---

# 教程介绍

让我们在不到 5 分钟的时间内发现 **Docusaurus**。

## 入门

首先**创建一个新网站**。

或者**立即尝试 Docusaurus** 和 **[docusaurus.new](https://docusaurus.new)**。

### 你需要什么

- [Node.js](https://nodejs.org/en/download/) 18.0 或更高版本：
  - 安装 Node.js 时，建议您选中所有与依赖项相关的复选框。

## 生成一个新站点

使用**经典模板**生成新的 Docusaurus 站点。

运行命令后，经典模板将自动添加到您的项目中：

```bash
npm init docusaurus@latest my-website classic
```

您可以在命令提示符、Powershell、终端或代码编辑器的任何其他集成终端中键入此命令。

该命令还会安装运行 Docusaurus 所需的所有必需依赖项。

## 启动您的网站

运行开发服务器：

```bash
cd my-website
npm run start
```

`cd` 命令更改您正在使用的目录。为了使用新创建的 Docusaurus 站点，您需要导航那里的终端。

`npm run start` 命令在本地构建您的网站并通过开发服务器提供服务，供您在 http://localhost:3000/ 上查看。

打开“docs/intro.md”（本页）并编辑一些行：网站**自动重新加载**并显示您的更改。