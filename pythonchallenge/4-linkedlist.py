import urllib2

url = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#number = '12345'
#number = '8022'
number = '63579'

data = urllib2.urlopen(url+number).read()

#while (data[0:3]=='and'):
#while (data[-8:-6]=='is'):

while data.find('nothing') != -1:
  str = 'the next nothing is'
  count = data.find(str) + len(str) + 1
#  print count
  data = urllib2.urlopen(url+data[count:]).read()
  print data
#print data
