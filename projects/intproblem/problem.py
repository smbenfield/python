words = dict()

fname = raw_input('Please enter your file name:')

fopen = open(fname)
fread = fopen.read()
for line in fread:
	fsplt = fread.strip()
	fword = fsplt.split(" ")

count = dict()

for word in fword:
	if word not in count:
		count[word] = 1
	if word in count:
		count[word] = count[word] + 1

print count
