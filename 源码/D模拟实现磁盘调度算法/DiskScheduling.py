#-*-coding:utf8;-*-
import OS
import random

class DiskScheduling:
    cd=int(input("Please input track number:"));
    print "The generated random track number is:";
    osss=[];
    for i in range(cd):
        oos=OS.OS();
        oos.setx(random.randint(0, 200));
        print oos.getx();
        osss.insert(i,oos);

    def FCFS(oss, cd):#FCFS
        sum = 0.0;
        ave = 0.0;
        os1 = [];
        for i in range(cd):
            os1.insert(i,oss[i]);
            #os1[i] = oss[i];
        now = input("Please now track number:");
        print "Disk scheduling order:";
        for i in range(cd):
            print os1[i].getx();
        for i in range(cd):
            os1[i].sety(now - os1[i].getx());
            if os1[i].gety() < 0:
                os1[i].sety(-os1[i].gety());
            sum += os1[i].gety();
            now = os1[i].getx();
        ave = sum / cd;
        print "move track number:";
        print sum;
        print "average move track number:";
        print ave;

    def SSTF(oss,cd):#SSTF
        sum = 0.0;
        ave = 0.0;
        os1 = [];
        for i in range(cd):
            os1.insert(i, oss[i]);
            #os1[i] = oss[i];
        now = input("Please now track number:");
        print "Disk scheduling order:";

        for i in range(cd):
            os1[i].sety(now-os1[i].getx());
            if os1[i].gety()<0:
                os1[i].sety(-os1[i].gety());
        for i in range(cd):
            for j in range(cd-1):
                k=j+1;
                while (k<cd):
                    if os1[j].gety()>os1[k].gety():
                        t=os1[j];
                        os1[j]=os1[k];
                        os1[k]=t;
                    k+=1;
            print os1[i].getx();
            sum+=os1[i].getx();

        ave = sum / cd;
        print "move track number:";
        print sum;
        print "average move track number:";
        print ave;

    def SCAN(oss,cd):#SCAN
        sum=0.0;
        ave=0.0;
        temp=0;
        now=0;
        os1=[];
        for i in range(cd):
            os1.insert(i, oss[i]);
            #os1[i] = oss[i];
        now = input("Please now track number:");
        print "Disk scheduling order:";
        for i in range(cd):
            j=i+1;
            while (j<cd):
                if os1[i].getx()>os1[j].getx():
                    temp=os1[i].getx();
                    os1[i].setx(os1[j].getx());
                    os1[j].setx(temp);
                j+=1;

        flag=1;
        for i in range(cd):
            if os1[i].getx()>now:
                os1[i].sety(os1[i].getx()-now);
                now=os1[i].getx();
                sum+=os1[i].gety();
                flag+=1;
                print os1[i].getx();
        if flag<=9:
            while (cd-flag>=0):
                os1[cd-flag].sety(now-os1[cd-flag].getx());
                now=os1[cd-flag].getx();
                sum+=os1[cd-flag].gety();
                print os1[cd-flag].getx();
                cd-=1;
        ave = sum / cd;
        print "move track number:";
        print sum;
        print "average move track number:";
        print ave;

    def CSCAN(oss,cd):#CSCAN
        sum = 0.0;
        ave = 0.0;
        temp = 0;
        now = 0;
        os1 = [];
        for i in range(cd):
            os1.insert(i, oss[i]);
            #os1[i] = oss[i];
        now = input("Please now track number:");
        print "Disk scheduling order:";

        for i in range(cd):
            j=i+1;
            while(j<cd):
                if os1[i].getx()>os1[j].getx():
                    temp=os1[i].getx();
                    os1[i].setx(os1[j].getx());
                    os1[j].setx(temp);
                j+=1;
        for i in range(cd):
            print os1[i].getx();
        flag=0;
        for i in range(cd):
            if os1[i].getx()>now:
                os1[i].sety(os1[i].getx()-now);
                now=os1[i].getx();
                sum+=os1[i].gety();
                flag+=1;
        os1[0].sety(now-os1[cd-1].getx());
        for i in range(cd-flag):
            os1[i].sety(now-os1[i].getx());
            now=os1[i].getx();
            sum+=os1[i].gety();
        ave = sum / cd;
        print "move track number:";
        print sum;
        print "average move track number:";
        print ave;

    while (1):
        print "1.FCFS";
        print "2.SSTF";
        print "3.SCAN";
        print "4.CSCAN";
        print "5.EXIT";
        fc = input("Please select function:");
        if fc == 1:
            FCFS(osss, cd);
        elif fc == 2:
            SSTF(osss, cd);
        elif fc == 3:
            SCAN(osss, cd);
        elif fc == 4:
            CSCAN(osss, cd);
        elif fc == 5:
            print "The End!";
            break;
        else:
            print "Input Wrong!";