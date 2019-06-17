
# 用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push，需要UT。
class TwoQueues(object):
    def __init__(self):
        self._queue1 = []
        self._queue2 = []
 
    def push(self,i):
        if len(self._queue1) == 0:
            self._queue1.append(i)
        elif len(self._queue2) == 0:
            self._queue2.append(i)
        if len(self._queue2) == 1 and len(self._queue1) >= 1:
            while self._queue1:
                self._queue2.append(self._queue1.pop(0))
        elif len(self._queue1) == 1 and len(self._queue2) > 1:
            while self._queue2:
                self._queue1.append(self._queue2.pop(0))
 
    def pop(self):
        if self._queue1:
            return self._queue1.pop(0)
        elif self._queue2:
            return self._queue2.pop(0)
        else:
            return None
    def getStack(self):
        print("queue1",self._queue1)
        print("queue2", self._queue2)

sta = TwoQueues()
sta.push(1)
sta.getStack()
sta.push(2)
sta.getStack()
sta.push(3)
sta.getStack()
sta.push(4)
sta.getStack()
print(sta.pop())
sta.getStack()
print(sta.pop())
sta.getStack()
print(sta.pop())
sta.getStack()