# coding:utf-8
import unittest
import subprocess
import os

from yoshi.util import get_encoding
from conv_encoding import process,get_eol_type

def create_file():
    if not os.path.exists('test'):
        os.mkdir('test')
        
    f=open("test/utf8.txt","w",encoding="utf-8",newline='')
    f.write("あああ\nいいい\n")
    f.close()
    f=open("test/cp932.txt","w",encoding="cp932",newline='')
    f.write("あああ\nいいい\n")
    f.close()
    f=open("test/ascii.txt","w",encoding="ascii",newline='')
    f.write("abc\ndef\n")
    f.close()

def byte2str(bytes):
    return bytes.decode("cp932").replace("\r\n","\n")

def exec_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    stdout_data, stderr_data = p.communicate()
    return p.returncode,byte2str(stdout_data),byte2str(stderr_data)

class Test1(unittest.TestCase):
    def setUp(self):
        create_file()
        
    def test_exec_preview(self):
        cmd = "python conv_encoding.py --start_dir test --preview --to_encoding utf-8 --pattern *.txt"
        ret,stdout,stderr = exec_command(cmd)
        self.assertEqual(ret,0)
        self.assertEqual(len(stderr), 0)
        print( stdout)
        self.assertEqual(get_encoding("test/cp932.txt")[0],"shift_jis")
    
    def test_exec(self):
        cmd = "python conv_encoding.py --start_dir test --to_encoding utf-8 --pattern *.txt"
        ret,stdout,stderr = exec_command(cmd)
        self.assertEqual(ret,0)
        self.assertEqual(len(stderr), 0)
        print( stdout)
        self.assertEqual(get_encoding("test/cp932.txt")[0],"utf-8")
        
    def test_exec_call(self):
        process("test","*.txt","utf-8",'CRLF',False)
        enc,data = get_encoding("test/cp932.txt")
        self.assertEqual(enc,"utf-8")
        self.assertEqual(get_eol_type(data),"CRLF")
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test1('test_exec_call'))
    #unittest.main()
    unittest.TextTestRunner(verbosity=2).run(suite)
    