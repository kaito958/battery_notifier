# battery_notifier

ROS 2 package to notify real-time battery status using Publisher/Subscriber model.
PCの実際のバッテリー残量を取得し、ステータス（正常・充電必要・満充電）を通知するパッケージです。

![Build Status](https://github.com/kaito958/battery_notifier/actions/workflows/test.yml/badge.svg)
![License](https://img.shields.io/badge/license-BSD--3--Clause-blue)

## Description
このパッケージは、Pythonの `psutil` ライブラリを使用してPCのハードウェア情報を読み取り、ROS 2トピックを通じてバッテリー状態を監視します。

- **battery_publisher**: 実際のバッテリー残量(%)と給電状態(AC/Battery)を取得し、`/battery_level` トピックに送信します。
- **warning_listener**: トピックを購読し、残量が20%以下の場合は警告(Warn)、100%の場合は満充電通知(Info)をログ出力します。

## Requirement
- Ubuntu 22.04 LTS
- ROS 2 Humble Hawksbill
- Python 3.10
- `psutil` library

## Usage

### 1. Install Dependencies
このパッケージは外部ライブラリ `psutil` を使用します。
```bash
pip3 install psutil
```
### 2. Clone and Build
ご自身のワークスペース（例: ~/ros2_ws）でビルドしてください。
```


cd ~/ros2_ws/src
# 以下のURLはあなたのリポジトリに合わせてください
git clone https://github.com/kaito958/battery_notifier.git
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```
### 3. Execution
Launchファイルを使用して、PublisherとSubscriberを同時に起動します。
```


ros2 launch battery_notifier battery_check.launch.py
```
### 4. Expected Output
以下のように、実際のバッテリー残量に応じたログが表示されれば成功です。
```


[battery_publisher] [INFO]: Real Battery: 33% (Discharging)
[warning_listener] [INFO]: Status: Normal (33%)
...
[battery_publisher] [INFO]: Real Battery: 19% (Discharging)
[warning_listener] [WARN]: LOW BATTERY: Please charge (19%)
```
### License
このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．

© 2025 Kaito Kubota

Author
Kaito Kubota