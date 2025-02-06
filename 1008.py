import numpy as np
import pandas as pd


ser = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(ser)
print(ser.values)
print(ser.index)
print(ser.shape)

ser1 = pd.Series([2,3,4,5,6], index=['b','c','d','e','f'])
print(ser1)

df = pd.DataFrame([ser,ser, ser1, ser1], index=['a1', 'b1','c1','d1'])
print(df)

print(df.values)
print(df.index)

da = {'a' : 0., 'b' : 1., 'c' : 2.}
print(pd.Series(da))
print(pd.Series(da, index=['b', 'c', 'd', 'a']))

print(np.power(10,pd.DataFrame(np.random.randn(12).reshape(3,4))))

print(ser[0])
print(ser['a'])

print(ser[0:2])
print(ser['a':'c'])


ser2 = pd.Series(np.random.randn(5),  name='seoul')
print(ser2)
ser3 = ser.rename('busan')
print(ser3)

d = {'one': pd.Series([1., 2., 3.],
                       index=['a', 'b', 'c']),
              'two': pd.Series([1., 2., 3., 4.],
                       index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

df1 = pd.DataFrame(d, index=['a','c','d'], columns=['one','two'])
print(df1)
df2 = pd.DataFrame(d, index=['b','d','e'], columns=['three','two'])
print(df2)
df3 = df1 + df2
print(df3)


arr = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
arr[:] = [(1, 2., 'Hello'), (2, 3., 'World')]
print(arr)
print(pd.DataFrame(arr))
print(pd.DataFrame(arr, index=['first', 'second']))
print(pd.DataFrame(arr, columns=['C', 'A', 'B']))

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print(pd.DataFrame(data))

data=pd.DataFrame({('a','b'): {('A','B'): 1, ('A','C'): 2},
                       ('a','a'): {('A','C'): 3, ('A','B'): 4},
                       ('a','c'): {('A','B'): 5, ('A','C'): 6},
                       ('b','a'): {('A','C'): 7, ('A','B'): 8},
                       ('b','b'): {('A','D'): 9, ('A','B'): 10}})

print(data)