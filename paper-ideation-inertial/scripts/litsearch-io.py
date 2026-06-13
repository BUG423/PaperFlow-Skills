#!/usr/bin/env python3
"""litsearch-io.py — IO 领域专用文献检索

基于通用版 litsearch.py，针对惯性定位领域做适配:
- 不使用 CCF-A venue 过滤 (IO 论文跨 cs.RO/cs.CV/cs.LG)
- 默认查询增加 IO 领域关键词
- 输出格式与通用版兼容

用法:
    python3 litsearch-io.py --query "inertial odometry knowledge distillation" --years 2 --limit 20 --json
    python3 litsearch-io.py --query "IMU domain generalization unseen device" --years 3 --limit 15

此脚本也可直接调用通用版:
    python3 ../paper-ideation/scripts/litsearch.py --query "..." --years 2 --limit 20 --json
"""

import sys
import os

# 直接调用通用版 litsearch.py
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Try cloned repo path first, then relative paths
GENERIC_SCRIPT = os.path.join(SCRIPT_DIR, "..", "..", "..", "PaperFlow-Skills", "paper-ideation", "scripts", "litsearch.py")
if not os.path.exists(GENERIC_SCRIPT):
    GENERIC_SCRIPT = os.path.join(SCRIPT_DIR, "..", "..", "paper-ideation", "scripts", "litsearch.py")

if __name__ == "__main__":
    # 转发所有参数到通用版
    # IO 领域不使用 --field (不需要 CCF-A venue 过滤)
    args = sys.argv[1:] if len(sys.argv) > 1 else []

    # 如果没有 --source 参数，默认 all (3源并发)
    if "--source" not in args:
        args.extend(["--source", "all"])

    cmd = [sys.executable, GENERIC_SCRIPT] + args
    os.execv(sys.executable, cmd)
