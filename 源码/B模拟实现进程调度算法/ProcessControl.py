#-*-coding:utf8;-*-
import PB

class ProcessControl:
    uTime=1;#时间片
    time=0;#模拟时间
    #按到达时间从小到达模拟进程信息
    pb1 = PB.PB("A", 5, 4, 6, 0, 0, "W");
    pb2 = PB.PB("B", 6, 5, 4, 0, 0, "W");
    pb3 = PB.PB("C", 8, 7, 2, 0, 0, "W");
    listProcessWait = [];
    listProcessRun = [];
    listProcessFinish = [];
    listProcessWait.append(pb1);
    listProcessWait.append(pb2);
    listProcessWait.append(pb3);
    print "process_infomation:";
    for info in listProcessWait:
        print info.toString();

    while (1):

        if len(listProcessWait)>0:
            while (1):

                if len(listProcessWait)<1:

                    break;
                p=listProcessWait[0];
                if p.getArriveTime()<=time:
                    if len(listProcessRun)>0:
                        for i in range(len(listProcessRun)):
                            if p.getPriority()>listProcessRun[i].getPriority():
                                listProcessRun.insert(i,p);
                                listProcessWait.remove(listProcessWait[0]);
                                break;

                            if i>(len(listProcessRun)-2):
                                listProcessRun.append(p);
                                listProcessWait.remove(listProcessWait[0]);
                                break;
                    else:
                        listProcessRun.append(p);
                        listProcessWait.remove(listProcessWait[0]);
                else:
                    break;


        if len(listProcessRun)!=0:
            p=listProcessRun[0];
            listProcessRun.remove(listProcessRun[0]);
            p.setStatus("R");
            print "time";
            print time;
            print "processing:";
            print p.toString();
            p.setWaitTime(-1);
            p.setUseTime(p.getUseTime()+uTime);
            if p.getPriority()>0:
                p.setPriority(p.getPriority()-1);
            else:
                p.setPriority(0);

            print "wait queue:";
            for q in range(len(listProcessRun)):
                print listProcessRun[q].toString();
            print "finish queue:"
            for k in range(len(listProcessFinish)):
                print listProcessFinish[k].toString();

            if p.getUseTime()>=p.getNeedTime():
                p.setStatus("F");
                p.setPriority(-1);
                listProcessFinish.append(p);
            else:
                p.setStatus("W");
                l=0;
                while l<len(listProcessRun):
                    if p.getPriority() > listProcessRun[l].getPriority():
                        listProcessRun.insert(l, p);
                        break;
                    l+=1;
                #for l in range(len(listProcessRun)):
                #    if p.getPriority()>listProcessRun[l].getPriority():
                #        listProcessRun.insert(l,p);
                #        break;
                if l==len(listProcessRun):
                    listProcessRun.append(p);


        for h in range(len(listProcessRun)):
              listProcessRun[h].setWaitTime(listProcessRun[h].getWaitTime()+1);
        time+=1;
        if len(listProcessWait)<1 and len(listProcessRun)<1:
            break;

    print "time";
    print  time;
    print "processing:";
    print "wait queue:";
    for j in range(len(listProcessRun)):
        print listProcessRun[j].toString();
    print "finish queue:"
    for k in range(len(listProcessFinish)):
        print listProcessFinish[k].toString();


