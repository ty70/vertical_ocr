# vertical-ocr

このプロジェクトは、縦書きの日本語テキストを含む画像から文字を抽出し、横書きのテキストに変換して保存する Python スクリプトです。

## 特徴

* 縦書きテキストの日本語OCR対応
* 出力はテキストファイル形式（.txt）
* コマンドライン引数による柔軟な入力・出力設定

## 使用方法

### 前提条件

* Python 3.7以降
* 以下のライブラリが必要です：

  ```bash
  pip install pytesseract opencv-python
  ```

### Tesseract OCR のインストール

```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-jpn
```

※ `tesseract-ocr-jpn` は日本語認識用の言語データです。

### Tesseract 追加の言語データファイルのインストール

* jpn_vert.trainedataをインストールしていない場合、以下の手順でインストールを行ってください
```bash
cd /usr/share/tesseract-ocr/4.00/tessdata/
sudo wget https://github.com/tesseract-ocr/tessdata/raw/main/jpn_vert.traineddata
```

確認
```bash
tensseract --list-langs
```
```
List of available languages (4):
eng
jpn
jpn_vert ← あればOK
osd
```

### 実行方法

```bash
python ./scripts/vertical_to_horizontal_text.py --input ./input/sample.png --output ./output/sample.txt
```

* `--input`：OCR処理を行う画像ファイル（縦書き）のパス
* `--output`：出力される横書きテキストファイルのパス

## ファイル構成例

```
.
├── input/
│   └── sample.png
├── output/
│   └── sample.txt
├── scripts/
│   └──vertical_to_horizontal_text.py
├── .gitignore
├── LICENSE
├── README_ja.md # このファイル
├── README.md    # English version
└── requirements.txt

```

## ライセンス

このプロジェクトは [MITライセンス](./LICENSE) の下で公開されています。

---

ご質問や機能追加のご要望があれば、ぜひ Issue を登録してください。
