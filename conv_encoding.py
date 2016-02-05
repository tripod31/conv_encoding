# coding:utf-8
'''
    ファイルを再帰的に指定文字コードに変換
'''
import argparse
import pprint
import os.path
import re

from yoshi.util import find_all_files,get_encoding,is_match_patterns_fnmatch,conv_encoding

'''
文字列の改行コード種別を返す
戻り値
    'CRLF','LF','NOEOL'(改行なし)
'''
def get_eol(s):
    if re.search('\r\n',s):
        return 'CRLF'
    
    if re.search('\n',s):
        return 'LF'
    
    return 'NOEOL'

'''
ファイルに対する処理を決定
'''
def get_todo(info,to_enc,to_eol):
    todo=[]
    if to_eol != 'skip' and info['eol'] != 'NOEOL' and info['eol'] !=to_eol:
        todo.append('eol')
    if info['encoding'] != 'ascii' and info['encoding'] != to_enc:
        todo.append('encoding')
    return todo

def process(start_dir,pattern,to_encoding,to_eol,preview):
    if not os.path.exists(start_dir):
        print("%s: does'nt exists" % start_dir )
        return
    
    files = find_all_files(start_dir)
    count =0
    file_infos=[]
    for path in files:
        if not is_match_patterns_fnmatch(path, pattern.split()):
            continue
        encoding,data = get_encoding(path)
        info = {'path':path,'encoding':encoding,'eol':get_eol(data)}
        file_infos.append(info)
    
    print("files to skip:")
    for info in file_infos:
        if len( get_todo(info, to_encoding, to_eol))==0:
            print("%s\t%s\t%s" % (info["encoding"],info['eol'],info["path"]))
    print("---")
    
    print("files to convert:")
    for info in file_infos:
        if len(get_todo(info, to_encoding, to_eol))>0:
            print("%s\t%s\t%s" % (info["encoding"],info['eol'],info["path"]))
    print("---")
    
    if preview != True:
        for info in file_infos:
            todo = get_todo(info, to_encoding, to_eol)
            if len(todo)>0:
                eol = None
                if 'eol' in todo:
                    if to_eol == 'CRLF':
                        eol = '\r\n'
                    if to_eol == 'LF':
                        eol = '\n'                   
                try:
                    conv_encoding(info["path"], to_encoding,eol)
                    if 'eol' in todo:
                        print("converted:eol:%s->%s\t%s"%(info["eol"],to_eol,info["path"]))
                    if 'encoding' in todo:
                        print("converted:enc:%s->%s\t%s"%(info["encoding"],to_encoding,info["path"]))
                    count+=1
                except Exception as e:
                    print (info["path"],':',e)

    print (count,"files converted")

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    
    #引数
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_dir'   ,default=".")       
    parser.add_argument('--pattern'     ,default="\.txt$"   ,help="pattern of name of file which are processed")  #必須でない引数
    parser.add_argument('--to_encoding' ,default="cp932")   
    parser.add_argument('--to_eol'      ,default='skip'       
                                        ,help="specify end of line,'skip'=leave eol as is,'CRLF','LF'")
    parser.add_argument('--preview'     ,action='store_true',default=False,help="do not change files when specified")

    args=parser.parse_args()
    process(**vars(args))   #namespaceをキ―ワード引数に変換  
