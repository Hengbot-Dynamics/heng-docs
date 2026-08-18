# Hengbot 公开文档站源码 / Public docs site source

This repository holds the **source tree** of the public Hengbot documentation site, built with Docusaurus 3. Building it locally publishes nothing.

本仓库是 Hengbot 公开文档站的**源码树**，基于 Docusaurus 3 构建。在本地构建不会发布任何内容。

## Repository layout / 仓库结构

| Path | Contents / 内容 |
| --- | --- |
| `docs/` | English source pages — the authoritative copy / 英文源页面，权威副本 |
| `i18n/zh-Hans/docusaurus-plugin-content-docs/current/` | Simplified-Chinese mirror / 简体中文镜像 |
| `blog/`, `src/` | Blog support files (authors/i18n options) and custom pages; no scaffold posts are published / 博客支持文件（作者、i18n 选项）与自定义页面；当前无已发布的脚手架文章 |
| `static/` | Assets served as-is / 原样提供的静态资源 |
| `docusaurus.config.ts`, `sidebars.ts` | Site and sidebar configuration / 站点与侧边栏配置 |

English and Simplified Chinese are mirrored **one file to one file at the same relative path**: `docs/X.md` pairs with `i18n/zh-Hans/docusaurus-plugin-content-docs/current/X.md`. Change both sides in the same edit, and keep `sidebar_position` identical on both — the sidebar order is read from front matter, not from this README.

英文源与简中镜像按**相同相对路径一一对应**：`docs/X.md` 对应 `i18n/zh-Hans/docusaurus-plugin-content-docs/current/X.md`。同一次改动必须两侧同时修改，且两侧 `sidebar_position` 保持一致 —— 侧边栏顺序取自 front matter，不取自本文件。

## Local commands / 本地命令

```
npm install                          # install dependencies / 安装依赖
npm run start                        # dev server, English / 本地开发服务器（英文）
npm run start -- --locale zh-Hans    # dev server, Simplified Chinese / 简中开发服务器
npm run build                        # static build into build/ / 静态构建，产物在 build/
npm run serve                        # preview the built output / 本地预览构建产物
npm run typecheck                    # tsc / 类型检查
```

`npm run build` doubles as the link gate, but read its output rather than trusting the exit code: `docusaurus.config.ts` sets `onBrokenLinks: 'throw'`, so a broken **route** fails the build, while `onBrokenMarkdownLinks: 'warn'` means a broken **Markdown** link only prints a warning and still exits 0.

`npm run build` 兼作链接门禁，但**必须读它的输出，不能只信退出码**：`docusaurus.config.ts` 设了 `onBrokenLinks: 'throw'`，路由断链会让构建失败；而 `onBrokenMarkdownLinks: 'warn'` 意味着 Markdown 断链只打印告警、仍然退出 0。

## Building is not deploying / 构建不等于部署

`npm run build` only writes the local `build/` directory, which is git-ignored. It publishes nothing and changes no live site. Whether any particular revision of this tree is currently served publicly is a separate operational fact that this repository does not record — do not infer it from the working tree.

`npm run build` 只写本地 `build/` 目录（已被 `.gitignore` 忽略），不发布任何内容、不改变任何线上站点。本仓库的某个版本当前是否正在对外提供，是本仓库**不记录**的独立运维事实 —— 不要从工作区状态推断。
