# battery_notifier



![test](https://github.com/kaito958/battery_notifier/actions/workflows/test.yml/badge.svg)

![License](https://img.shields.io/badge/license-BSD--3--Clause-blue)



A ROS 2 package to notify real-time battery status using Publisher/Subscriber model.



## Node Description



### battery_publisher

Publishes the current battery percentage of the PC.



* **Topic**: `battery_status` (std_msgs/Float32)



### warning_listener

Subscribes to the battery status and logs warnings. It also publishes an alert signal when the battery is low.


* **Subscribes**: `battery_status` (std_msgs/Float32)

* **Publishes**: `battery_alert` (std_msgs/Bool)

    * True: Battery level <= 20%

    * False: Battery level > 20%


## Requirement

* ROS 2 Humble Hawksbill

* Python 3.10

* `psutil` library



## Usage


Run the nodes using the launch file:


```bash
ros2 launch battery_notifier battery_check.launch.py
```
## Test

Run the test script:


```bash
colcon test --packages-select battery_notifier
```
## License

This package is licensed under the BSD-3-Clause License.


# battery_notifier (Japanese)

ROS 2を用いたバッテリー状態監視パッケージです。Publisher/Subscriberモデルを使用しています。


## ノードの説明

### battery_publisher

PCの実際のバッテリー残量を取得し、トピックとして配信します。


* **Topic**: `battery_status` (std_msgs/Float32)


### warning_listener

バッテリー残量を受信し、ログを出力します。また、残量が少ない場合は警告信号を配信します。



* **Subscribes**: `battery_status` (std_msgs/Float32)


* **Publishes**: `battery_alert` (std_msgs/Bool)


    * True: 残量 20%以下（警告）


    * False: 残量 20%より多い



## 実行方法

Launchファイルを使用して、システム全体（PublisherとSubscriber）を起動します。


```bash
ros2 launch battery_notifier battery_check.launch.py
```
## テスト

以下のコマンドでテストを実行できます。


```bash
colcon test --packages-select battery_notifier
```

## ライセンス

本パッケージは 3条項BSDライセンス の下で公開されています。


© 2025 Kaito Kubota 