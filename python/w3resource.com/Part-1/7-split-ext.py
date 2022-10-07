path = input('Path File :')
if '.' in path:
    list = path.split('.')
    print('Extention Of File is : ' + str(list[-1]))
else:
    print('Not Found')