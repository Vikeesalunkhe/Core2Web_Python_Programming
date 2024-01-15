'''
4. WAP for a function that returns the count of the search element in the list

Input:
listData = [1, 2, 3, 3, 4, 5, 3]
serchEle = 3
Output: 3 found in list 3 time
'''

def Total(List, Ele):
    
    count = 0
    for i in List:
    
        if i == Ele:
            count+=1

    return count

SerEl = 3
listData = [1,2,3,3,4,5,3]
retObj = Total(listData, SerEl)
print(f"{SerEl} found in list {retObj} time ")
