# 目的
* ROS2のノード(プログラム)間で通信を行い、受信内容を画面に出力する.

#
![test](https://github.com/masaki130/mypkg/actions/workflows/test.yml/badge.svg)

# 機能
* mypkgという名前のリポジトリに、同名のディレクトリを作成し、以下の2つのソースファイルを作成した.
  * talker.py
  * listener.py
* "talker.py"は数字をカウントし、それを"listener.py"へ送信する.
* "listener.py"は"talker.py"のカウント数を受信し、その結果を画面に出力する.
 
# mypkgの導入
* 以下のコマンドを入力して、pcにmypkgを取り込む.
```
$ mkdir -p ros2_ws/src
$ cd ros2_ws/src
$ git clone git@github.com:masaki130/mypkg.git
$ cd mypkg
```
# ビルド
* 以下のコマンドを入力してmypkgを読み込む.
```
$ cd ros2_ws
$ colcon build
$ source ~/ros2_ws/install/setup.bash
```
# 送受信例
* 送信例
  * 1つ目の端末(ubuntuの画面)で以下のコマンドを入力する.
```
$ cd ros2_ws
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
* Python 3.7～3.10

## テスト環境
* Ubntu 22.04

## 権利
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* LICENSEへのリンク
    * [LICENSE](https://github.com/masaki130/ros2_2022/blob/main/LICENSE)
* Apache-2.0を含むLICENSE
    * [test/test_copyright.py](https://github.com/masaki130/mypkg/blob/lesson10-1/test/test_copyright.py)
    * [test/test_pep257.py](https://github.com/masaki130/mypkg/blob/lesson10-1/test/test_pep257.py)
    * [test/test_flake8.py](https://github.com/masaki130/mypkg/blob/lesson10-1/test/test_flake8.py)
* © 2022 Masaki Mitani
