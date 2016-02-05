conv_encoding
=====
文字コード、改行コードを変換するツール


development enviromment
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

    python conv_encoding.py --start_dir [ディレクトリ] --pattern [ファイル名のパターン、ワイルドカード]  
        --to_encoding [変換先エンコード名]
        --to_eol [変換先改行コード]
        --preview

+ to_eol  
変換先改行コード。   
CRLF,LF,skip(変換しない)
+ preview  
実際の変換は行わない

conv_encoding_gui.pyw
-----
GUIツール