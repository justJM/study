#%% collections.Counter
import collections
c= collections.Counter(['egg','ham','ham','soy'])
print(c['egg'])
print(c['ham'])
print(c)

#%% collections.deque
import collections
d = collections.deque('abcdef')
print(d)
d.remove('c')
print(d)
d.append('h')
print(d)
d.appendleft('X')
print(d)

#%% collections.deque.pop()
d = collections.deque('abcdef')
print(d.pop())
print(d)
print(d.popleft())
print(d)

#%% collections.deque.rotate()
d = collections.deque('abcdef')
print(d)
d.rotate(2)
print(d)
d.rotate(-2)
print(d)

#%% collections.OrderedDict
from collections import OrderedDict
d = {'abd':3,'a':4, 'b':1,'cd':2}
#%% 
OrderedDict(sorted(d.items(),key=lambda t : t[0]))
#%% 
OrderedDict(sorted(d.items(),key=lambda t : t[1]))
#%% 
OrderedDict(sorted(d.items(),key=lambda t : len(t[0])))

#%% heapq
from heapq import *
qdata=[5,7,1,3]
heapify(qdata)
qdata
#%%
heappush(qdata,10)
qdata
#%%
heappop(qdata)
qdata

#%%
from heapq import *
h = []
heappush(h,(5,'write code'))
heappush(h,(7,'release product'))
heappush(h,(1,'write sepc'))
heappush(h,(3,'create test'))

# print(heappop(h))
# print(heappushpop(h,(11,'pust pop')))
# print(h)
# print(heappushpop(h,(0,'heap')))
# print(heapreplace(h,(0,'heap')))
print(h)
print(nlargest(3,h))
print()
print(nsmallest(3,h))

#%% bisect
from bisect import bisect

lst=[10,20,30,40,50]
print(bisect(lst,10))
print(bisect(lst,20))
print(bisect(lst,11))

#%%
from bisect import bisect
grades='FEDCBA'
breakpoints = [30,44,66,75,85]

def grade(total):
    return grades[bisect(breakpoints,total)]

grade_map = map(grade,[33,99,77,44,12,88])
grade_map
list(grade_map)

#%%
import bisect
import random
random.seed(3)
l=[]
for i in range(10):
    r = random.randint(1,50)
    pos = bisect.bisect_left(l,r)
    bisect.insort_left(l,r)
    print('%2d %2d' % (r, pos),l)
#%%
import bisect
import random
random.seed(3)
l=[]
for i in range(10):
    r = random.randint(1,50)
    pos = bisect.bisect(l,r)
    bisect.insort(l,r)
    print('%2d %2d' % (r, pos),l)