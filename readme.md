conv_encoding
=====
指定ディレクトリ以下のファイルの文字コード、改行コードを変換するツール

development environment
-----
python3.5

required libraries
-----
yoshi.util:  
<https://github.com/tripod31/common_python>  
pyqt4(conv_encoding_gui.pyw)

conv_encoding.py
-----
コマンドラインツール

####usage

    python conv_encoding.py 
        --start_dir [ディレクトリ] 
        --pattern [ファイル名のパターン]  
        --to_encoding [変換先エンコード名]
        --to_eol [変換先改行コード]
        --preview

+ start_dir  
処理するファイルがあるディレクトリ

+ pattern  
処理するファイル名のパターン。ワイルドカードで指定する。','で区切って複数指定可  
省略時は'*.txt'  
例:  
    >--pattern \*.txt,\*.py

+ to_encoding  
変換先文字コード。  
'utf-8','shift_jis'等  
省略時は'skip'(変換しない)  

+ to_eol  
変換先改行コード。   
CRLF,LF
省略時は'skip'(変換しない)  

+ preview  
指定された場合、実際の変換は行わない

conv_encoding_gui.pyw
-----
GUIツール