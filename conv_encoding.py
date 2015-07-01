# coding:utf-8
'''
    ファイルを再帰的に指定文字コードに変換
'''
import argparse
import pprint
import re
import os.path
import sys
import fnmatch

from yoshi.util import find_all_files,get_encoding,is_match_patterns_fnmatch

def process(start_dir,to_encoding,preview,pattern):
    if not os.path.exists(start_dir):
        print("%s: does'nt exists" % start_dir )
        return
    
    files = find_all_files(start_dir)
    count =0
    file_infos=[]
    for path in files:
        if not is_match_patterns_fnmatch(path, pattern.split()):
            continue
        encoding = get_encoding(path)
        file_infos.append({"path":path,"encoding":encoding})
    
    print("files to skip:")
    for info in file_infos:
        if info["encoding"] == "ascii" or info["encoding"] == to_encoding:
            print("%s\t%s" % (info["encoding"],info["path"]))
    print("---")
    
    print("files to convert:")
    for info in file_infos:
        if info["encoding"] != "ascii" and info["encoding"] != to_encoding:
            print("%s\t%s" % (info["encoding"],info["path"]))
    print("---")
    
    if preview != True:
        for info in file_infos:
            if info["encoding"] != "ascii" and info["encoding"] != to_encoding:            
                try:
                    f = open(info["path"],"rU",encoding=info["encoding"])
                    data = f.read()
                    f.close()
                    f = open(info["path"], 'w',encoding=to_encoding)
                    f.write(data)
                    f.close()
                    print("converted:%s->%s\t%s"%(info["encoding"],to_encoding,info["path"]))
                    count+=1
                except Exception as e:
                    print (info["path"],':',e)
                finally:
                    f.close()

    print (count,"files converted")

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    
    #引数
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_dir',default=".")    #必須でない引数
    parser.add_argument('--to_encoding',default="cp932")    #必須でない引数
    parser.add_argument('--preview',action='store_true',default=False,help="do not change files when specified")
    parser.add_argument('--pattern',default="\.txt$")    #必須でない引数

    args=parser.parse_args()
    process(**vars(args))   #namespaceをキ―ワード引数に変換  
