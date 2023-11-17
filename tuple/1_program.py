#tuple

#1.immutable
#2.collection of different data type
#3.access dsts gron index no.
#4.denoted by ()
#5.store multiple items in a single variable.
#6.allow dupticat element
#7.A tuple is a collection which is ordered and unchangeable.


tupleData = ()

print(type(tupleData))                                                      #<class 'tuple'>

lang  = ("Cpp","Java","Python",("Go","Rust","Dart"))

print(type(lang))                                                           #<class 'tuple'>
print(lang.count("Python"))                                                 #1
print(lang.index("Python"))                                                 #2

lang[4] = "Ruby"                                                            #TypeError: 'tuple' object does not support item assignment

newTuple = lang.copy()                                                      #AttributeError: 'tuple' object has no attribute 'copy'



"""tuple only support two methods .count and .index"""
