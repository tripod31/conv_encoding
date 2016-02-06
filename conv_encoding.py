#!/usr/bin/env python3
# coding:utf-8
'''
convert charset,end of line of files.
'''
import argparse
import os.path
import re

from yoshi.util import find_all_files,get_encoding,is_match_patterns_fnmatch,conv_encoding,DecodeException

import gettext

#translation
translation = gettext.translation(
    domain='conv_encoding',
    localedir=os.path.join(os.path.dirname(__file__), 'translations'),
    fallback=True,
    codeset='utf-8'
    )
_=translation.gettext

'''
returns end of line

returns
    'CRLF','LF','NOEOL'(no end of line)
'''
def get_eol(s):
    if re.search('\r\n',s):
        return 'CRLF'
    
    if re.search('\n',s):
        return 'LF'
    
    return 'NOEOL'

'''
determin what to do to the file
'''
def get_todo(info,to_enc,to_eol):
    todo=[]
    if to_eol != 'skip' and info['eol'] != 'NOEOL' and info['eol'] !=to_eol:
        todo.append('eol')
    if to_enc != 'skip' and info['encoding'] != 'ascii' and info['encoding'] != to_enc:
        todo.append('encoding')
    return todo

'''
display two dimension array
Each column length is adjusted to max length of data

arr
    two dimension array,columns x rows
delimiter
    delimiter of column
'''
def print_arr(arr,delimiter=" "):
    if len(arr)==0:
        return
    
    row_len=len(arr[0])
    col_len=[0]*row_len

    #get max length of columns
    for row in arr:
        for idx in range(0,row_len):
            if col_len[idx] < len(row[idx]):
                col_len[idx] = len(row[idx])
    #print
    for row in arr:
        line = ""
        for idx in range(0,row_len):
            if idx>0:
                line += delimiter
            s = row[idx] + ' ' * (col_len[idx] - len(row[idx]))
            line +=s
        print(line)
    
def process(start_dir,pattern,to_encoding,to_eol,preview):
    if not os.path.exists(start_dir):
        print(_("%s: does'nt exists") % start_dir )
        return
    
    files = find_all_files(start_dir)
    count =0
    file_infos=[]
    files_undecoded=[]
    for path in files:
        if not is_match_patterns_fnmatch(path, pattern.split(',')):
            continue
        try:
            encoding,data = get_encoding(path)
        except DecodeException as e:
            files_undecoded.append(path)
            continue
        
        info = {'path':path,'encoding':encoding,'eol':get_eol(data)}
        file_infos.append(info)
    
    if len(files_undecoded)>0:
        print(_("Can't decode these files.They are not precessed:"))
        for path in files_undecoded:
            print(path)
        print("---")
    
    
    print(_("files to skip:"))
    arr=[]
    for info in file_infos:
        if len( get_todo(info, to_encoding, to_eol))==0:
            arr.append([info["encoding"],info['eol'],info["path"]])
    print_arr(arr)
    print("---")
    
    print(_("files to convert:"))
    arr=[]
    for info in file_infos:
        todo = get_todo(info, to_encoding, to_eol)
        if len(todo)>0:
            arr.append([info["encoding"],info['eol'],'change '+"".join(todo),info["path"]])
    print_arr(arr)
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
                    if to_encoding == 'skip':
                        conv_encoding(info["path"], info['encoding'],eol)    #specify original encoding
                    else:
                        conv_encoding(info["path"], to_encoding,eol)
                    count+=1
                except Exception as e:
                    print (info["path"]+':'+str(e))

        print (count,_("files changed"))
    else:
        print (_("***preview mode***"))

if __name__ == '__main__':

    #arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_dir'   ,default="."
                                        ,help=_("directory where files are.default is current directory."))       
    parser.add_argument('--pattern'     ,default="*.txt"
                                        ,help=_("pattern of name of file which are processed.default is '*.txt'"))
    parser.add_argument('--to_encoding' ,default="skip"
                                        ,help=_("specify encoding for example 'utf-8'.or'skip'(leave encoding as is).default is 'skip'"))
    parser.add_argument('--to_eol'      ,default='skip'
                                        ,help=_("specify end of line,'skip'(leave eol as is),'CRLF','LF'.default is 'skip'"))
    parser.add_argument('--preview'     ,action='store_true',default=False
                                        ,help=_("do not change files when specified"))

    args=parser.parse_args()
    process(**vars(args))   #convert namespace object to keyword arguments
