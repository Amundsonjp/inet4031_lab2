#!/usr/bin/env python3

myFile = open("fileprocessor.input", "r")
fileInfo = myFile.read()
fileLineList = fileInfo.split("\n")
listOfLists = []
i = 0
for line in fileLineList:
   line1 = line.split(":")
   listOfLists[i] = line1
   i = i + 1
print("Printing out User Data:")
for line in listOfLists:
   print(line)
   user = line[0]
   if user[0] == "#":
      print(line[0] + " is skipped because it starts with a hashtag (is commented out)")
   else:
      print("The user " + line[0] + " has a password of " + line[1] + " and has a userid " + line[2] + " and a groupid " + line[3])

print("End of User Data")
