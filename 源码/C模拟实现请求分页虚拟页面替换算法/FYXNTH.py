#-*-coding:utf8;-*-
#@:替换
#$:直接加入空闲区
#&:页框空闲
#%:页框不空闲
from __future__ import print_function
import random
def fifo(pageNum,pageFrameNum,size):
    m=[];
    for i in range(pageFrameNum):
        m.insert(i,0);
    for i in range(pageNum):
        k=0;
        while (1):
        #for k in range():
            for j in range(pageFrameNum):
                if m[j]==k:
                    m[j]=k+1;
                    for h in range(pageFrameNum):
                        if m[h]==0:
                            print ("& ",end='');
                        else:
                            if k==0:
                                if h!=j:
                                    print ("% ",end='');
                                else:
                                    print ("$ ",end='');
                            else:
                                if h!=j:
                                    print ("% ",end='');
                                else:
                                    print ("@ ",end='');
                    print ("",end='\n');
                    k=-1;
                    break;
            if k<0:
                break;
            k+=1;

def lru(pageNum,pageFrameNum,size):
    m = [];
    for i in range(pageFrameNum):
        m.insert(i, 0);
    for i in range(pageNum):
        j=0;
        for j in range(pageFrameNum):
            if m[j]==0:
                m[j]=1;
                for k in range(pageFrameNum):
                    if m[k]==0:
                        print ("& ",end='');
                    else:
                        if k!=j:
                            print ("% ",end='');
                        else:
                            print ("$ ",end='');
                print ("",end='\n');
                break;
        j+=1;
        if j>(pageFrameNum-1):
            max=0;
            tmp=0;
            for d in range(pageFrameNum):
                if m[d]>max:
                    max=m[d];
                    tmp=d;
            m[tmp]=1;
            for f in range(pageFrameNum):
                if f!=tmp:
                    print ("% ",end='');
                else:
                    print ("@ ",end='');
            print ("",end='\n');
        while(1):
            tmp=random.randint(0, pageFrameNum-1);
            if m[tmp]>0:
                for t in range(pageFrameNum):
                    if m[t]>0:
                        m[t]+=1;
                m[tmp]=1;
            break;

def clock(pageNum,pageFrameNum,size):
    m=[];
    for i in range(pageFrameNum):
        m.insert(i,-1);
    for i in range(pageNum):
        j=0;
        for j in range(pageFrameNum):
            if m[j]==-1:
                m[j]=1;
                for k in range(pageFrameNum):
                    if m[k]==-1:
                        print ("& ",end='');
                    else:
                        if k!=j:
                            print ("% ",end='');
                        else:
                            print ("$ ",end='');
                print ("",end='\n');
                break;
        j+=1;
        if j>(pageFrameNum-1):
            flag=0;
            tmp=0;
            for d in range(pageFrameNum):
                if m[d]==0:
                    m[d]=1;
                    tmp=d;
                    flag=1;
                    break;
                else :
                    m[d]=0;

            if flag==0:
                for d in range(pageFrameNum):
                    if m[d]==0:
                        m[d]=1;
                        break;
            for f in range(pageFrameNum):
                if f!=tmp:
                    print ("% ",end='');
                else :
                    print ("@ ",end='');
            print ("",end='\n');
        while(1):
            tmp=random.randint(0, pageFrameNum-1);
            if m[tmp]==0:
                m[tmp]=1;
            break;

pageNum=int(input("请输入程序长度:"));
pageFrameNum=int(input("请输入页框个数:"));
size=int(input("请输入页面大小:"));
fifo(pageNum,pageFrameNum,size);
print ("------------------------------------------------");
#lru(pageNum,pageFrameNum,size);
print ("------------------------------------------------");
#clock(pageNum,pageFrameNum,size);