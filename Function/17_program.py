#Named Argument

def compinfo(compName,empCount):
    print(compName, ":", empCount)

compinfo("Microsoft",10000)
compinfo("Amazon",20000)
compinfo("Apple",30000)


compinfo(88888,"Google")
compinfo(empCount = 77777, compName = "Tata")



"""
 O/p  Microsoft : 10000
      Amazon : 20000
      Apple : 30000
      88888 : Google
      Tata : 77777
"""
