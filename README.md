# ROS2のパッケージ
![test](https://github.com/masaki130/mypkg/actions/workflows/test.yml/badge.svg)

# mypkg
* mypkgという名前のリポジトリに、以下の2つのパッケージを作成した.
  * talker.py
  * listener.py

# 機能
* "talker.py"は、数字をカウントし、トピックを通じて"listener.py"へ送信する.
* "listener.py"は、トピックから"talker.py"のカウント数を受信し、その結果を画面に表示する.

# mypkgの導入
* まず以下のコマンドを入力して、初期状態のパッケージを作成する.
```
$ mkdir -p ros2_ws/src
$ tree ros2_ws/
$ cd ~/ros2_ws/src/
$ ros2 pkg create mypkg --build-type ament_python
$ tree
```

* 次に以下のコマンドを入力すると、pcにmypkgを取り込むことが可能.
```
$ cd ros2_ws/src
$ git clone git@github.com:masaki130/mypkg.git
$ cd mypkg 
```
# 送受信例
* 送信例
  * 1つ目の端末で以下のコマンドを入力する.
```
$ colcon build
$ source ~/.bashrc
$ ros2 run mypkg talker
```

* 受信例
  * 1つ目の端末を開いた状態で、2つ目の端末を開き、以下のコマンドを入力する.
```
$ ros2 run mypkg listener
[INFO] [1670568944.466393100] [listener]: Listen: 53
[INFO] [1670568944.937743900] [listener]: Listen: 54
[INFO] [1670568945.437237900] [listener]: Listen: 55
```

## 必要なソフトウェア
* Python:3.7～3.10

## テスト環境
* Ubntu:22.04

## 権利
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージは，3条項BSDライセンスのもとmasakimitani/emcl由来のコード（© 2022 Masaki Mitani）を利用しています.
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* LICENSEへのリンク
    * [LICENSE](https://github.com/masaki130/ros2_2022/blob/main/LICENSE)
* © 2022 Masaki Mitani
