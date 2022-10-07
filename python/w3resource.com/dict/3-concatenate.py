#!/usr/bin/python3

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
main_dict = {}
for d in (dic1,dic2,dic3): main_dict.update(d) # main.dict.update(dict1),main.dict.update(dict2) ..etc
print(main_dict)