"""
このスクリプトは、日本語の縦書き文章が含まれる画像ファイルをOCR（光学文字認識）により解析し、
抽出したテキストを横書きとしてテキストファイルに保存します。

使用方法:
  python vertical_to_horizontal_text.py --input path/to/input_image.png --output path/to/output.txt

引数:
  --input : OCR対象の画像ファイルパス（日本語縦書き）
  --output: 結果を保存するテキストファイルパス（横書きテキスト）
"""

import argparse
from PIL import Image
import pytesseract

def main():
    parser = argparse.ArgumentParser(description="縦書き日本語画像から横書きテキストを抽出")
    parser.add_argument("--input", required=True, help="入力画像ファイルのパス")
    parser.add_argument("--output", required=True, help="出力テキストファイルのパス")
    args = parser.parse_args()

    # OCR対象画像の読み込み
    image = Image.open(args.input)

    # OCR処理（日本語指定）
    text = pytesseract.image_to_string(image, lang='jpn_vert')

    # 改行や不要空白を整理（基本的な整形）
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    horizontal_text = '\n'.join(lines) + '\n' if lines else ''

    # 結果を出力
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(horizontal_text)

    print("✅ 縦書きテキストの横書き出力が完了しました。")

if __name__ == "__main__":
    main()


