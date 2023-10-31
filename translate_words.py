!pip install googletrans==4.0.0-rc1
from google.colab import drive
drive.mount('/content/drive')
from googletrans import Translator
import os

# Googleドライブ内のテキストファイルへのパスを指定
input_file_path = '/content/drive/MyDrive/fin_Scraping/finland_word_13.txt'

# 出力ディレクトリを指定
output_dir = '/content/drive/MyDrive/fin_Scraping/Translate_JP'

# 出力ディレクトリが存在しない場合、作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 翻訳する関数を定義
def translate_text(input_text):
    translator = Translator()
    translation = translator.translate(input_text, src='ja', dest='fi')
    return f"{translation.origin},{translation.text}"

# テキストファイルを読み込み、翻訳して結果を一時的なリストに保存
translated_lines = []
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    for line in input_file:
        translated_line = translate_text(line)
        translated_lines.append(translated_line)

# すべての翻訳結果を1つのファイルに書き込む
output_file_path = os.path.join(output_dir, 'translated_output.txt')
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in translated_lines:
        output_file.write(line + '\n')

# 結果を出力
print("翻訳が完了しました。結果は以下のファイルに保存されました:")
print(output_file_path)
