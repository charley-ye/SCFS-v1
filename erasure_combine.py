import sys
import argparse




base_path='/home/ori/'
cpy_path='/home/de_test/'



if __name__ == '__main__':
    times= int(sys.argv[1])
    print times
    name= str(sys.argv[2])
    print name
    piece= str(sys.argv[3])
    ft=open(base_path+name+'M'+piece+'.txt','wb')
    for i in range (0,times-1):
        print i
        f=open(cpy_path+'test'+name+'M'+piece+'.txt_obj0_chk'+str(i),"rb")
        ft.write(f.read())
        f.close()
    f=open(cpy_path+'test'+name+'M'+piece+'.txt_obj0_chk'+str(times-1),"rb")
    a=(int(name)*1024*1024*1024/int(name))
    b=a-(a/(12*1024)+1)*1024*8
    q=f.read(b)

    ft.write(q)
   # a= (int(name)*1024*1024)
   # print a
   # print(a/(12*1024)+1)*1024
   # print (a/(12*1024)+1)*1024*12-a
    print (a/(12*1024)+1)*1024*8
    ft.close()
