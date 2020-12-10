f=open('text.txt','r')
f=open('text.txt','r',encoding=('utf8'))
print(f)
print('Name of the file: ',f.name)
print('File contents: ',f.read())
print('File is open in mode:',f.mode)

print('File is closed: ',f.closed)
f.close()
print('And now closed: ',f.closed)

with open('text.txt','w',encoding=('utf8')) as s:
    s.write('I like Java!')

# !!!  
print('File contents: ',s.read())