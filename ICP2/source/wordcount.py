with open('file.txt') as f:
  lines = f.readlines()
  data = ''.join(lines[0])
  data1 = ''.join(lines[1])
  print('lines =',len(lines))
  print('Words in first line = ',len(data.split()))
  print('Words in second line = ', len(data1.split()))
  char = ''.join(data.split())
  char1 = ''.join(data1.split())

  print('characters in first line= ',len(char))
  print('characters in second line= ', len(char1))