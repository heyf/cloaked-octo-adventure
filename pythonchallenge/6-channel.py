import zipfile

zip = zipfile.ZipFile('channel.zip')

suffix = r".txt"
number = "90052"

data = zip.read(number+suffix)

str = 'nothing is'

while data.find(str) != -1:
  counter = data.find(str) + len(str) + 1
  number = data[counter:]
  data = zip.read(number+suffix)
  info = zip.getinfo(number+suffix)
  print info.comment

zip.close()
