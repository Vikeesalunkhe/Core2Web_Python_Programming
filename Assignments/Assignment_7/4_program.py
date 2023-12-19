"""
4. WAP for a function that returns the count of the search element in the list
"""

def Search(my_list,Element):
    count = 0
    for i in my_list:
        if i == Element:
            count+=1

    return count

Search_ele = int(input("Enter the Search element in list : "))
my_list = [1,5,2,3,6,1,2,4,3,1,4,5,6,2,3,4,1,2]

ret = Search(my_list,Search_ele)
print("Total count of Search elemnt {} is : ".format(Search_ele),ret)
