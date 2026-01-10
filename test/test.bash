#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kaito Kubota
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

# 1. リスナーノード（判定機）だけをバックグラウンドで起動
# launchではなくnode単体で動かすのがポイント（偽データを送るため）
ros2 run battery_notifier warning_listener &
NODE_PID=$!

# ノードの立ち上がり待ち
sleep 2

# 2. 偽のバッテリー残量「15.0」をトピックとして送信（入力）
# これが「ブラックボックステスト」の入力になります
timeout 10 ros2 topic pub -r 10 /battery_status std_msgs/msg/Float32 "{data: 15.0}" > /dev/null &
PUB_PID=$!

# 3. 警告トピックが出ているか監視（出力）
# 15%を送ったので、battery_alert は True (data: true) になるはず
echo "Testing: Injecting 15% battery level..."
RESULT=$(timeout 5 ros2 topic echo /battery_alert | grep "data: true" | head -n 1)

# 4. プロセスの後片付け
kill $NODE_PID
kill $PUB_PID

# 5. 結果判定
if [ -n "$RESULT" ]; then
    echo "✅ Test PASSED: Alert signal detected successfully."
    exit 0
else
    echo "❌ Test FAILED: Alert signal NOT detected."
    # 失敗時はログを見たいかもしれないので、念のため状況を表示
    exit 1
fi