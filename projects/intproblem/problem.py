words = dict()

fname = raw_input('Please enter your file name:')

fopen = open(fname)
fread = fopen.read()
fuppr = fread.upper()
for line in fuppr:
	fsplt = fuppr.strip()
	fword = fsplt.split()

count = dict()

for word in fword:
	count[word] = count.get(word,0) + 1

print count
