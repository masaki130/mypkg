# ROS2のパッケージ
![test](https://github.com/masaki130/mypkg/actions/workflows/test.yml/badge.svg)

# mypkg
* mypkgという名前のリポジトリに、以下の2つのパッケージを作成した.
  * talker.py
  * listener.py

# 機能
* talker.pyで数字をカウントし、トピックを通じて送信する.
* listener.pyでトピックからメッセージを受信し、結果を画面に表示する.

# mypkgの導入
* 任意のディレクトリで以下のコマンドを入力すると、pcにmypkgを取り込むことが可能.
```
$ git clone git@github.com:masaki130/mypkg.git
$ cd mypkg 
```
# 送受信例
* 送信例
  * 1つ目の端末で以下のコマンドを入力する.
```
$ colcon build
$ ros2 run mypkg talker
```

* 受信例
  * 1つ目の端末を開いた状態で、2つ目の端末を開き、以下のコマンドを入力する.
```
$ ros2 run mypkg listener
```

## 必要なソフトウェア
* Python:3.10

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
