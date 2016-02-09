conv_encoding
=====
指定ディレクトリ以下のファイルの文字コード、改行コードを変換するツール

Windows用実行ファイル
-----
+ conv_encoding.exe  
+ conv_encoding_gui.exe(GUI)    

python、必要ライブラリは中に組み込まれています。

開発環境
-----
python3.5

必要ライブラリ
-----
yoshi.util:  
<https://github.com/tripod31/common_python>  
pyqt4(conv_encoding_gui.pyw)

conv_encoding.py
-----
コマンドラインツール

####使用方法

    usage: conv_encoding.py [-h] [--start_dir START_DIR] [--pattern PATTERN]
                            [--to_encoding TO_ENCODING] [--to_eol TO_EOL]
                            [--preview]
    
    optional arguments:
      -h, --help            show this help message and exit
      --start_dir START_DIR ファイルがあるディレクトリ。デフォルトはカレントディレクトリ。
      --pattern PATTERN     処理されるファイルのファイル名のパターン。デフォルトは'*.txt'
      --to_encoding TO_ENCODING
                            変換先のエンコード名。例えば'utf-8'。または'skip'(エンコードを変更しない)。デフォルトは'skip'
      --to_eol TO_EOL       変換先の改行。'skip'(改行を変更しない),'CRLF','LF','CR'。デフォルトは'skip'
      --preview             指定時はファイルを変更しない

conv_encoding_gui.pyw
-----
GUIツール  
<img src="http://www.geocities.jp/tripod31hoge/images/conv_encoding.jpg">
