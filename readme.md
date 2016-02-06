conv_encoding
=====
tool to convert charset,end of line of files that are in specified directory.

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
Command line tool.

####usage

    usage: conv_encoding.py [-h] [--start_dir START_DIR] [--pattern PATTERN]
                            [--to_encoding TO_ENCODING] [--to_eol TO_EOL]
                            [--preview]
    
    optional arguments:
      -h, --help            show this help message and exit
      --start_dir START_DIR
      --pattern PATTERN     pattern of name of file which are processed.default is '*.txt'
      --to_encoding TO_ENCODING
                            specify encoding for example 'utf-8'.or'skip'(leave encoding as is).
                            default is 'skip'
      --to_eol TO_EOL       specify end of line,'skip'(leave eol as is),'CRLF','LF'.
                            default is 'skip'
      --preview             do not change files when specified
  
conv_encoding_gui.pyw
-----
GUI tool.