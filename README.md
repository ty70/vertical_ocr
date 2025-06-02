# vertical-ocr

This project is a Python script that extracts characters from images containing vertically written Japanese text and converts it into horizontal text for saving.

## Features

* OCR support for vertically written Japanese text
* Output in text file format (.txt)
* Flexible input/output configuration via command-line arguments

## Usage

### Prerequisites

* Python 3.7 or higher
* The following libraries are required:

  ```bash
  pip install pytesseract opencv-python
  ```

### Installing Tesseract OCR

```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-jpn
```

Note: `tesseract-ocr-jpn` provides the language data for Japanese recognition.

### Installing Additional Tesseract Language Data

If `jpn_vert.traineddata` is not installed, you can add it as follows:

```bash
cd /usr/share/tesseract-ocr/4.00/tessdata/
sudo wget https://github.com/tesseract-ocr/tessdata/raw/main/jpn_vert.traineddata
```

To confirm installation:

```bash
tesseract --list-langs
```

```
List of available languages (4):
eng
jpn
jpn_vert ← OK if listed
osd
```

### Execution Example

```bash
python ./scripts/vertical_to_horizontal_text.py --input ./input/sample.png --output ./output/sample.txt
```

* `--input`: Path to the image file (vertically written) for OCR processing
* `--output`: Path to the output horizontal text file

## Example File Structure

```
.
├── input/
│   └── sample.png
├── output/
│   └── sample.txt
├── scripts/
│   └── vertical_to_horizontal_text.py
├── .gitignore
├── LICENSE
├── README_ja.md # Japanese version
├── README.md    # this file
└── requirements.txt
```

## License

This project is released under the [MIT License](./LICENSE).

---

If you have any questions or feature requests, please feel free to open an issue.
