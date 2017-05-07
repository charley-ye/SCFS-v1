import sys
import argparse




base_path='/home/test/'
cpy_path='/home/cpy/'



if __name__ == '__main__':
    times= int(sys.argv[1])
    print times
    name= str(sys.argv[2])
    print name
    ft=open(base_path+name+'M.txt','rb')
    for i in range (0,times-1):
        print i
        f=open(cpy_path+name+'M'+str(i)+'.txt',"wb")
        f.write(ft.read(1024*1024*1024))
        f.close()
    f=open(cpy_path+name+'M'+str(times-1)+'.txt',"wb")
    f.write(ft.read((int(name)-(times-1)*1024)*1024*1024))
    f.close()
