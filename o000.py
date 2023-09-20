a = {'olma': "qizil" " " "sariq", "nok": 'sariq' " " 'kok'}
for i in a.items():
    print(i)
c = input("if you want to change values enter yes else no: ")
if c.lower() == 'yes':
    print(a.keys())
    n = input("choose which keys do you want to change: ")
    if n.lower() == 'olma' or 'nok':
        if n.lower() == "olma":
            print(a.get('olma'))
            a['olma'] = input("")
        elif n.lower() == 'nok':
            print(a.get('nok'))
            a['nok'] = input("")
        else:
            print('wrng ')
print(a)
