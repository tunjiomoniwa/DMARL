import xml.etree.ElementTree as ET
mytree = ET.parse('fcd.xml')   # to parse file

print(mytree)   # to get root tag
children = list(mytree)  # to get children element

arr = []                                 # 2D array
dic = []                                 # list of dict
for e in list(mytree):                             # get its children
    element = []
    
    
    arr.append(element)        
    dic.append(elementdict)

print(arr)                ## print 2D array
