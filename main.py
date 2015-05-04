import PE

fileName='helloworld.exe'
print(fileName+' in first')

PE.pefile(fileName)
print('hello after PE.pefile(fileName)')