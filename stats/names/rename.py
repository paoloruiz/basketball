# here we take in some commands, and then replace every name that doesn't exactly match our name with a new one

# arguments are [folder] [filename] [start year] [end year]
import sys
import os
import shutil
from copy import deepcopy

names = dict()
nom = open('names.txt', 'r')
for line in nom:
  line = line.replace('\n', '')
  n = line.split('\t')
  m = n[0].split(' ')
  lastNameIndex = len(m) - 1
  if m[lastNameIndex] in names:
    firstNames = names[m[lastNameIndex]]
    if lastNameIndex > 2:
      firstNames.append(n[1] + m[0] + ' ' + m[1])
    else:
      firstNames.append(n[1] + m[0])
    names[m[lastNameIndex]] = deepcopy(firstNames)
  else:
    firstNames = []
    firstNames.append(n[1] + m[0])
    names[m[lastNameIndex]] = deepcopy(firstNames)
year = str(sys.argv[1])
f = open('../lineup/' + year + 'lineups.txt', 'r')
g = open('../lineup/' + year + 'copy.txt', 'w')
for line in f:
  m = line.split('\t')
  namesList = m[1].split('|')
  for na in namesList:
    if na[0:1] is ' ':
      na = na[1:]
    if ' ' in na[len(na)-1:]:
      na = na[:len(na)-1]
    splitName = na.split(' ')
    lastNameIndex = len(splitName)-1
    if len(names[splitName[lastNameIndex]]) == 1:
      line = line.replace(na, names[splitName[lastNameIndex]][0][4:] + ' ' + splitName[lastNameIndex])
    else:
      letter = splitName[0][0:1]
      namesWithLetter = []
      allNames = names[splitName[lastNameIndex]]
      for possibleName in allNames:
        if letter in possibleName[4:5]:
          namesWithLetter.append(possibleName)
      if len(namesWithLetter) == 1:
        line = line.replace(na, namesWithLetter[0][4:] + ' ' + splitName[lastNameIndex])
      else: 
        teamNames = []
        for q in namesWithLetter:
          if 'TOT' in q or m[2] in q:
            teamNames.append(q)
        if len(teamNames) == 1:
          line = line.replace(na, teamNames[0][4:] + ' ' + splitName[lastNameIndex])
        else:
          print 'The year is ' + str(year)
          print 'The line is'
          print line
          print 'The name we are looking for is ' + na
          print namesWithLetter
          print 'Input the index of the list which is correct'
          index = int(raw_input())
          line = line.replace(na, namesWithLetter[index][4:] + ' ' + splitName[lastNameIndex])
  g.write(line)
f.close()
g.close()
shutil.copyfile('../lineup/' + year + 'copy.txt', '../lineup/' + year + 'lineups.txt')
os.remove('../lineup/' + year + 'copy.txt')

