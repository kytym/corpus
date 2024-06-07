# 形態素解析
## 概要
青空文庫より太宰治作、人間失格のデータを入手しデータを整形したのち、ginzaを用いて形態素分析を行いました。

## data_shaping.py
ダウンロードした元ファイルであるningen_shikkaku.txtを形態素分析しやすいデータに加工し、加工したデータをtest.txtとして出力しています。

## corpus.py
test.txtを読み込み、そのデータを形態素ごとに区切り形態素の数と形態素毎の出現頻度をprintします。元のデータのままではサイズが大きくそのまま実行するとエラーが発生するため、test.txtの冒頭の4000文字を抜き出してから形態素に区切りました。
また、出現頻度が2以上の要素をoutput.csvとしてcsvファイルを出力しています。

## インストール
```
git clone https://github.com/kytym/corpus.git
cd corpus
pip install -r requirements.txt
```

## 使い方
data_shaping.py, corpus.pyの順で実行してください。
```
python data_shaping.py
python corpus.py
```

## 使用したライブラリ、バージョン
python 3.12.3

ginza==5.2.0

ja-ginza==5.2.0

pandas==2.2.2
