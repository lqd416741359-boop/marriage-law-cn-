# GitHub 上传设置

上传仓库文件时，请上传 `marriage-law-cn` 文件夹内的全部内容，包括 `.gitignore`；不要把外面的 ZIP 上传进仓库。

## 新建仓库

- **Repository name：** `marriage-law-cn`
- **Description：** `中国内地婚姻家庭法律研究与案件准备 Skill：梳理财产债务、子女、安全风险、证据与行动路径。`
- **Visibility：** `Public`
- **Add a README file：** 不勾选
- **Add .gitignore：** 选择 `None`
- **Choose a license：** 选择 `None`

本文件夹已经包含 README、忽略文件和 MIT License，不需要 GitHub 再次生成。

## 上传文件

1. 创建仓库后选择 **Add file → Upload files**。
2. 打开本地 `marriage-law-cn` 文件夹并全选其中全部内容，不要上传外层文件夹。
3. 确认上传列表包含 `agents`、`assets`、`calculators`、`references`、`templates`、`workflows`、`SKILL.md`、`README.md`、`LICENSE`、`.gitignore` 和本文件。
4. Commit message 填写：`Initial release of MarriageLaw CN`
5. 点击 **Commit changes**。

## About 简介与 Topics

在仓库首页右侧 **About** 区域点击齿轮：

- **Description：** `中国内地婚姻家庭法律研究与案件准备 Skill：梳理财产债务、子女、安全风险、证据与行动路径。`
- **Website：** 留空

加入以下 Topics：

```text
codex-skill
ai-skill
marriage-law
family-law
legal-research
china
prc
legal-ai
```

## Social Preview 封面

README 顶部会自动显示 `assets/cover.png`。如需分享仓库链接时显示专用封面：

1. 打开仓库 **Settings → General**。
2. 找到 **Social preview**。
3. 上传 `assets/social-preview.png` 并保存。

## 推荐版本

- 首个 Release 标签：`v1.0.1`
- Release 标题：`MarriageLaw CN v1.0.1`
- Release 简介：`首个公开版本：支持中国内地婚姻登记、离婚、彩礼同居、财产房产、夫妻债务、子女抚养、家暴保护、证据与程序分析。`

第一次上传时不必立即创建 Release，可以在仓库文件确认无误后再创建。

## 上传后检查

- README 顶部封面正常显示且中文无乱码
- `SKILL.md` 位于仓库根目录
- `agents/openai.yaml` 存在
- 两张封面均能打开
- GitHub 识别为 MIT License
- 仓库中没有 ZIP、临时文件或重复嵌套的 `marriage-law-cn/marriage-law-cn` 目录
