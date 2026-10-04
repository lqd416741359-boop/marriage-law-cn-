<div align="center">

![MarriageLaw CN 封面](assets/cover.png)

# MarriageLaw CN

**中国内地婚姻家庭法律研究与案件准备 Skill**

![License](https://img.shields.io/badge/license-MIT-c9a45b)
![Scope](https://img.shields.io/badge/scope-中国内地婚姻家庭法-8b2635)
![Language](https://img.shields.io/badge/language-中文-421a22)
![Status](https://img.shields.io/badge/status-v1.0.1-2f855a)

</div>

## 项目简介

MarriageLaw CN 用于协助用户梳理中国内地婚姻家庭法律问题：建立人物关系和时间线，核验现行法律、司法解释和登记规则，分析财产债务、子女、婚姻过错与安全风险，建立证据地图并提出分阶段行动方案。

它不会冒充律师、法官、婚姻登记机关或其他政府部门，也不会承诺离婚、财产分割、抚养安排或赔偿结果。

## 覆盖范围

- 结婚登记、婚姻效力与登记离婚
- 彩礼、同居与共同财产
- 夫妻财产、房产、父母出资和婚内协议
- 夫妻共同债务与个人债务
- 协议离婚与诉讼离婚
- 子女抚养、抚养费与探望
- 婚外赠与、重大过错与离婚损害赔偿
- 家庭暴力与人身安全保护令
- 证据、财产保全、诉讼和执行准备

## 使用示例

```text
请使用 $marriage-law-cn 帮我分析：婚后父母为我们支付首付，房子登记在夫妻双方名下，
目前准备离婚。还贷、父母出资和房屋增值应当核实哪些事实，需要准备什么证据？
```

Skill 会先追问足以改变结论的关键事实，再核验现行规则。涉及登记手续、房产、彩礼、债务、子女、家暴、诉讼时效或司法解释时，应以分析当日的官方来源为准。

## 设计原则

- 先整理事实、人物关系、婚姻状态和时间线
- 同时扫描财产、债务、子女、过错、安全和程序风险
- 区分法律上可能成立与现有证据能否证明
- 不把出轨等同于必然“净身出户”
- 不根据房产登记姓名机械判断最终产权比例
- 家暴、抢夺藏匿子女或转移财产风险优先处理
- 仅加载当前问题需要的参考文件，减少 Token 消耗
- 默认在聊天中回答，仅在用户明确要求时导出文件

## 安装

将整个 `marriage-law-cn` 文件夹复制到 Codex 的 Skills 目录，保持目录结构不变，然后重新加载或重启 Codex。

```text
marriage-law-cn/
├── agents/openai.yaml
├── assets/
│   ├── cover.png
│   └── social-preview.png
├── calculators/property_split.py
├── references/
├── templates/
├── workflows/
├── .gitignore
├── CHANGELOG.md
├── GITHUB_UPLOAD.md
├── LICENSE
├── README.md
└── SKILL.md
```

> 不同版本或安装方式的 Skills 路径可能不同，请以当前 Codex 版本的官方说明为准。

## 计算器说明

`calculators/property_split.py` 只用于用户指定情景下的比例演算，不判断财产性质、法定份额或法院最终分割比例。默认50/50不是法律结论。

## 法律更新基线

V1.0.1 已将2025年2月1日起施行的婚姻家庭编司法解释（二）和2025年5月10日起施行的修订《婚姻登记条例》纳入检索基线，并补强家暴伤情与再次起诉的分析规则。任何高风险或时效敏感问题仍需在回答时重新核验。

## 重要声明

本项目仅用于一般性法律信息研究、事实整理和案件准备，不构成法律意见，不建立律师—客户关系，也不能替代持证律师、法律援助、公安、法院、民政部门或其他有关机构针对具体事实提供的帮助。涉及现实人身危险时，应优先报警、就医并寻求安全支持。

## GitHub 发布

仓库名称、简介、Topics、Social Preview 和逐步上传方法集中写在 [GITHUB_UPLOAD.md](GITHUB_UPLOAD.md)。

## License

本项目采用 [MIT License](LICENSE)。封面图为本仓库配套制作，可随项目在 MIT License 条款下使用。
