# see the blog: 
# http://security.coverity.com/blog/2014/Nov/understanding-python-bytecode.html

import marshal, dis, sys

def openCompiledFile():
    try:
        with open('myfile.pyc', 'rb') as fd:
            # skip the first 12 bytes of the file
            fd.read(4) # python version specific magic number
            fd.read(4) # compilation date
            fd.read(4) # size of source
            
            # get the code object
            code_object = marshal.load(fd)
    except Exception as e:
        print(e)
        sys.exit()
    return code_object

def inspect_code_object(code_object, indent=''):    
    print(code_object.co_consts)
    print(code_object.co_names)

# code_object = openCompiledFile()
# inspect_code_object(code_object)
# 
# # print disassembly
# dis.dis(code_object)

1

def junk():
    f = open('myfile.pyc','rb')
    contents = f.read()
    f.close()
    
    def bytes2str(byte_seq):
        str_seq = ''
        for b in byte_seq:
            str_seq += chr(b)
        return str_seq
    
    contents = bytes2str(contents)
    code_obj = marshal.loads(contents[12:])

junk()