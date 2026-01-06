#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kaito Kubota
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

# GitHub Actions等のCI環境ではセットアップ済み前提で動かす
# ローカル環境依存の cd や source は削除または条件分岐

LOGFILE="/tmp/battery.log"

# ノードを10秒間だけ起動して、ログをファイルに保存
timeout 10 ros2 launch battery_notifier battery_check.launch.py > "$LOGFILE"

# ログの中に「Real Battery」が含まれているかチェック
if grep -q 'Real Battery' "$LOGFILE"; then
    echo "Test PASSED"
    exit 0
else
    echo "Test FAILED"
    cat "$LOGFILE"
    exit 1
fi