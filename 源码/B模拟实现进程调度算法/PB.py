class PB:

    def __init__(self,name,priority,arriveTime,needTime,waitTime,useTime,status):
        self.name=name;
        self.priority=priority;
        self.arriveTime=arriveTime;
        self.needTime=needTime;
        self.waitTime=waitTime;
        self.useTime=useTime;
        self.status=status;

    def setName(self, name):
        self.name = name;

    def getNAme(self):
        return self.name;

    def setPriority(self, priority):
        self.priority = priority;

    def getPriority(self):
        return self.priority;

    def setArriveTime(self, arriveTime):
        self.arriveTime = arriveTime;

    def getArriveTime(self):
        return self.arriveTime;

    def setNeedTime(self, needTime):
        self.needTime = needTime;

    def getNeedTime(self):
        return self.needTime;

    def setWaitTime(self, waitTime):
        self.waitTime = waitTime;

    def getWaitTime(self):
        return self.waitTime;

    def setUseTime(self, useTime):
        self.useTime = useTime;

    def getUseTime(self):
        return self.useTime;

    def setStatus(self, status):
        self.status = status;

    def getStatus(self):
        return self.status;

    def toString(self):
        return "name: ",self.name,",priority: " ,self.priority , ",arriveTime: ",self.arriveTime ,",needTime: " , self.needTime ,",useTime: " , self.useTime,",waitTime: ",self.waitTime,",status: ",self.status;
