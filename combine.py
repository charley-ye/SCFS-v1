import sys
import argparse




base_path='/home/last_data/'
cpy_path='/home/ori/'



if __name__ == '__main__':
    times= int(sys.argv[1])
    print times
    name= str(sys.argv[2])
    print name
    ft=open(base_path+name+'M.txt','wb')
    for i in range (0,times-1):
        print i
        f=open(cpy_path+name+'M'+str(i)+'.txt',"rb")
        ft.write(f.read())
        f.close()
    f=open(cpy_path+name+'M'+str(times-1)+'.txt',"rb")
    ft.write(f.read())
    ft.close()
