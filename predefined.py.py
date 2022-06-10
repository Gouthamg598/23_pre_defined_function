'''sort'''
# a=[1,5,35,6]
# a.sort()
# print(a)
# print(sorted([12,5,9,2]))
# print(sorted((9,19,6,7)))
# a=['a','V','A','p']
# print(sorted(a))#['A', 'V', 'a', 'p']
# print(ord('A'))#65
# print(chr(68))#D

'''all'''
# print(all([True,1,2,]))#True
# print(all([True,1,2,'']))#False
# print(all([True,1,2,' ']))#True
# print(all([True,1,2,0]))#false
# print(all([True,1,2,None]))#false
# print(all([True,1,2,False]))#false
# print(all([True,1,7964,531,' ']))#True

'''any'''
# print(any([True,False,True,46,5,'']))#True
# print(any([False,False,'']))#False
# print(any([False,False,' ']))#True
# print(any([True,False,46,5,'',None,0]))#True
# print(any([False,46,5,'',None,0]))#True
'''eval()'''
# print('eval=',eval('5+63+6.3-1'))#eval= 73.3
# print('eval=',eval(b'5+63+6.3-1'))#eval= 73.3
# a=eval('7+63.9')
# b=eval('786+656.6')
# print(a,type(a))#70.9 <class 'float'>  
# print(b,type(b))#1442.6 <class 'float'>
# print(a+b)#1513.5
'''bool'''
# print(bool(False)) #False
# print(bool(True))#True
# print(bool(0))#False
# print(bool(1))#True
# print(bool(''))#False
# print(bool(' '))#True
# print(bool(bool))#True
# for i in reversed([10,5,789,63,5]):
    # print(i,end=' ')
    
# for i in reversed((10,5,789,63,5)):
    #  print(i,end=' ')