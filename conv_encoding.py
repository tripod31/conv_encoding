#!/usr/bin/env python3
# coding:utf-8
'''
convert charset,end of line of files.
'''
import argparse
import os.path
import re
import io

from yoshi.util import find_all_files,get_encoding,is_match_patterns_fnmatch,conv_encoding,DecodeException,get_eol,print_arr

import gettext
#translation
translation = gettext.translation(
    domain='conv_encoding',
    localedir=os.path.join(os.path.dirname(__file__), 'translations'),
    fallback=True,
    codeset='utf-8'
    )
_=translation.gettext

tbl_eol = {'CRLF':'\r\n','CR':'\r','LF':'\n','NOEOL':''}
inv_eol = {v: k for k, v in tbl_eol.items()}

'''
determin what to do to the file
returns
    array that contains 'eol','encoding'
'''
def get_todo(info,to_enc,to_eol_type):
    todo=[]
    if to_eol_type != 'skip' and info['eol_type'] != 'NOEOL' and info['eol_type'] !=to_eol_type:
        todo.append('eol')
    if to_enc != 'skip' and info['encoding'] != 'ascii' and info['encoding'] != to_enc:
        todo.append('encoding')
    return todo

'''
returns if string can be encoded to the encoding,ot not
buf_err
    stringIO().returns error string
'''
def is_encode_ok(s,to_enc,buf_err):
    try:
        s.encode(to_enc)
        ret = True
    except UnicodeEncodeError as e:
        msg = "'"+s[e.start:e.end]+"'"
        eol = get_eol(s)
        #when string is multiline,get number of line that contains error chars        
        if eol != '':
            lno=len(re.findall(eol,s[0:e.start]))+1
            msg += " at line " + str(lno)
        
        buf_err.write(msg)
        ret = False
    return ret

def process(start_dir,pattern,to_enc,to_eol_type,preview):
    if not os.path.exists(start_dir):
        print(_("%s: does'nt exists") % start_dir )
        return
    
    files = find_all_files(start_dir)
    count =0
    files_processed=[]  #files to be processed
    files_skipped=[]    #files to be skipped
    files_dec_ng=[]     #files that can't be decoded
    files_enc_ng =[]    #files that can't be encoded
    #gather information of files.current encoding,end of line
    for path in files:
        if not is_match_patterns_fnmatch(path, pattern.split(',')):
            continue
        try:
            encoding,data = get_encoding(path)
        except DecodeException as e:
            files_dec_ng.append(path)
            continue
        
        info = {'path':path,'encoding':encoding,'eol_type':inv_eol[get_eol(data)]}
        todo = get_todo(info, to_enc, to_eol_type)
        if len(todo)==0:
            files_skipped.append(info)
            continue
        
        if 'encoding' in todo:
            #test encoding
            buf_err = io.StringIO()
            if  not is_encode_ok(data, to_enc,buf_err):
                info['err_str']=buf_err.getvalue()
                files_enc_ng.append(info)
                continue

        files_processed.append(info)
    
    #print files that can't be decoded
    if len(files_dec_ng)>0:
        print(_("Can't decode these files.They are not processed:"))
        for path in files_dec_ng:
            print(path)
        print("---")
    
    #print files that can't be encoded
    if len(files_enc_ng)>0:
        print(_("Can't encode these files.They are not processed:"))
        arr=[]
        for info in files_enc_ng:
            arr.append( [info['encoding'],info['eol_type'],info['path'],info['err_str']])
        print_arr(arr, "[%s,%s] %s:%s")
        print("---")
    
    #print files to be skipped
    if len(files_skipped)>0:
        print(_("files to skip:"))
        arr=[]
        for info in files_skipped:
            arr.append([info['encoding'],info['eol_type'],info['path']])
        print_arr(arr,"[%s,%s] %s")
        print("---")
    
    #print files to be converted
    if len(files_processed)>0:
        print(_("files to convert:"))
        arr=[]
        for info in files_processed:
            todo = get_todo(info, to_enc, to_eol_type)
            
            if 'encoding' in todo:
                msg_to_enc = to_enc
            else:
                msg_to_enc = info['encoding']
            if 'eol' in todo:
                msg_to_eol_type = to_eol_type
            else:
                msg_to_eol_type = info['eol_type']

            arr.append([info["encoding"],info['eol_type'],msg_to_enc,msg_to_eol_type,info["path"]])
        print_arr(arr,"[%s,%s]->[%s,%s] %s")
        print("---")
    else:
        print(_("nothing to do."))
        return
    
    #return here if preview mode
    if preview:
        print (_("***preview mode***"))
        return
    
    #convert
    for info in files_processed:
        todo = get_todo(info, to_enc, to_eol_type)
        if len(todo)>0:
            eol = None
            if 'eol' in todo:
                eol = tbl_eol[to_eol_type]

            if to_enc == 'skip':
                conv_encoding(info["path"], info['encoding'],eol)    #specify original encoding,change only end of line
            else:
                conv_encoding(info["path"], to_enc,eol)
            count+=1

    print (count,_("files changed"))        

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
                                        ,help=_("specify end of line,'skip'(leave eol as is),'CRLF','LF','CR'.default is 'skip'"))
    parser.add_argument('--preview'     ,action='store_true',default=False
                                        ,help=_("do not change files when specified"))

    args=parser.parse_args()
    process(args.start_dir,args.pattern,args.to_encoding,args.to_eol,args.preview)
