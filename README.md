# CrowBuster
raspberry pi4を用いたカラス撃退装置です。

## 使用するハードウェア
本システムで必須となるハードウェアは以下の３つです。
1. **Raspberry Pi4** (4GB,8GBモデル推奨)
2. **Raspberry Pi Camera Module**(USBカメラではシステムの動作を保証できません)
3. Raspberry Piに接続する**スピーカー**

## Raspberry Pi Camera Moduleの設定
1. Raspberry Piのメニューボタンから設定を選択
2. Raspberry Piの設定を選択
![setting_1](https://github.com/merry1147/CrowBuster/blob/main/img/setting1.png)
3. インターフェイスを選択
4. カメラを有効にしてOKボタンを押す
![setting_2](https://github.com/merry1147/CrowBuster/blob/main/img/setting2.png)
5. 再起動を要求されるので再起動する

## セットアップ
Raspberry Pi4における本アプリケーションのセットアップ手順を説明する。

1. Raspberry Pi4にRaspberryPi OSをインストールする  
64bit版OSのインストールを推奨します。

2. LXTerminalを開き、以下のコマンドを実行する
```
sudo apt update
sudo apt upgrade -y
sudo apt install python3-tk python3-pil.imagetk -y
sudo apt install libatlas-base-dev -y
```
3. pip3を最新版にアップデートする
```
sudo pip3 install --upgrade pip
```
4. requirements.txtに書かれているライブラリをインストールする
```
pip3 install -r "requirements.txt"
```
6. アプリケーションを実行する
```
python3 guiapp.py
```
## UI
UIの設定は以下の画像のとおりにできます。
![demo](https://github.com/merry1147/CrowBuster/blob/main/img/UI.png)

## デモ
カラス撃退装置実行デモ

![demo](https://github.com/merry1147/CrowBuster/blob/main/img/demo.gif)
