eid=[101,102,103,104]
p(101 in eids) #ture
p(108 in eids) #false
p(108 not eids) #ture
enames=("raji","rahul","mahi","jevvi")
p('raji'in enames)#ture
p('mahhi'in enames)#false
sizes={'s','m','xl'}
p('xxl'not in sizes)#ture
ename="raji"
p('a' in ename)#ture
b=bytes([10,20,30,40])

ba=bytearray([10,20,30,40])
p(10 in ba)
numbers=range(100)