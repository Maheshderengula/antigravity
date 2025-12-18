tell ={'raju':4806,'mode':4333}
tell ['judio'] =3777
tell
{'raju':4806,'mode':4333,'judio':3777}
tell['raju']
4806
tell['tel']
Traceback ( most recent call last ):
File "<stdin>",line 1,in <module>
key error : 'tel'
print(tell.get('tel'))

del tell['mode']
tell['tel'] = 4127
tell
{'raju':4806,'mode':4333,'tel':4127}
list(tell)
['raju','mode','tel']
sorted(tell)
['mode','raju','tel']
'mode' in tell 
Ture
'tel' not in tell
false