# coding:utf-8
import unittest
import subprocess
from yoshi.util import get_encoding

def create_file():
    f=open("test/utf8.txt","w",encoding="utf-8")
    f.write("あああ\nいいい\n")
    f.close()
    f=open("test/cp932.txt","w",encoding="cp932")
    f.write("あああ\nいいい\n")
    f.close()
    f=open("test/ascii.txt","w",encoding="ascii")
    f.write("abc\ndef\n")
    f.close()

def byte2str(bytes):
    return bytes.decode("cp932").replace("\r\n","\n")

def exec_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    stdout_data, stderr_data = p.communicate()
    return p.returncode,byte2str(stdout_data),byte2str(stderr_data)
            
class MyTest(unittest.TestCase):
    def setUp(self):
        create_file()
    def test_1(self):
        cmd = "python conv_encoding.py --start_dir test --preview --to_encoding utf-8 --pattern \.txt$"
        ret,stdout,stderr = exec_command(cmd)
        self.assertEqual(ret,0)
        self.assertEqual(len(stderr), 0)
        print( stdout)
        self.assertEqual(get_encoding("test/cp932.txt"),"cp932")
    def test_2(self):
        cmd = "python conv_encoding.py --start_dir test --to_encoding utf-8 --pattern \.txt$"
        ret,stdout,stderr = exec_command(cmd)
        self.assertEqual(ret,0)
        self.assertEqual(len(stderr), 0)
        print( stdout)
        self.assertEqual(get_encoding("test/cp932.txt"),"utf-8")
    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
