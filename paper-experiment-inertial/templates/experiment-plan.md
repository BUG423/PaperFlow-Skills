> stage: experiment | updated: <YYYY-MM-DD>

# 实验记录 — <选定 idea 标题>

## 二次校验结果
- 校验日期: <YYYY-MM-DD>
- 文献再检索: <新增相关 paper 数> / 抢跑风险: <low/medium/high>
- 代码可行性: <score>/5 — <一句话>
- 缺失 baseline: <列表, 如无则写"无">

## 实验环境
- 代码: Begin (路径: <path>)
- 算力: 1×3090
- 环境: uv + PyTorch CUDA 12.1
- 数据集: RoNIN / TLIO / IMUNet / RIDI / OxIOD / RNINv2 (默认全部)

## 选定执行路径
- 路径: A (用户自主) / B (Claude 协助执行)
- 代码路径: <path> (路径 B 必填)
- 数据路径: <path> (路径 B 必填)
- 服务器信息: <如有> (路径 B 选填)

## 新增算法骨架
- 目录: `network/<算法名>/`
- model_factory arch 名: <主模型>, <deploy>, <No_XX>, ...
- 是否需要自定义损失: <是/否>
- 冒烟测试: <通过/未通过>

## 主实验结果
| 数据集 | 方法 | ATE (seen) | ATE (unseen) | RTE | 参数量 |
|--------|------|-----------|-------------|-----|--------|
| RoNIN | 你的方法 | | | | |
| RoNIN | RoNIN-ResNet | | | | |
| RoNIN | TinyIO | | | | |
| TLIO | ... | | | | |

## 消融结果
| 变体 (arch 名) | ATE | Δ vs full model |
|------|-----|----------|
| Full (<算法名>) | | — |
| No XX | | |
| No YY | | |

## H1 验证结果
- 假设: <H1 原文>
- 验证方法: <怎么验证的>
- 结果: <成立/不成立>
- 如果不成立: <pivot 到了哪里, 日期>

## 关键发现
- <写 paper 时最想强调的 1-3 个发现>
- <审稿人可能挑的 1-2 个弱点 + rebuttal 准备>

## 下一步
- paper-writing: 故事线方向
- 补充实验 (如需要): 待跑清单

## 检索元信息
- 二次检索 query: <terms>
- 二次检索日期: <YYYY-MM-DD>
- 新增发现: <N> 篇 | 威胁等级: <none/low/medium/high>
