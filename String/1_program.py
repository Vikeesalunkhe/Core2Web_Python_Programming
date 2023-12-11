#string

str1 = "Core2Web"

print(str1[3])                       #e
print(str1[2:6])                     #re2w
print(str1[2:5:-1])                  #
print(str1[-3::-1])                  #W2eroC

#Methods

#1.capitalise()    : convert only first letter capital
str1 = "Core2Web Technology"
print(str1.capitalize())              #Core2Web Technology

#2.casefold()      : convert all small letter
print(str1.casefold())                #core2web technology

#3.center()       :  
str2 = "Hello"
print(str2.center(12, "#"))           ####Hello####

#4.count()        : count total no. of given element or element
print(str1.count("o"))               #3

#5.endswith()   
print(str1.endswith("logy"))         #True

#6.expandtabs()
str3 = "core2web\tincubator"
print(str3)                          #core2web	incubator   
print(str3.expandtabs())             #core2web	incubator


