# Iteration variable
i = 0
# File enter
name = raw_input('Enter file:')
# Sort Mode
sort = raw_input("Sort by (A)lpha or (V)alue?")
# File open, not read
handle = open(name,'r')
# File read, one big string
text = handle.read()
text = text.upper()
# File split at spaces, in list now
words = text.split()
# Sorts list
words.sort()

# Slims down list
slimwords = list()
for word in words:
	if not word in slimwords:
		slimwords.append(word)

# Establish dictionary
counts = dict()
# Loop through list, add one if there, create and add if not
for word in words:
	counts[word] = counts.get(word,0) + 1

# Prints values
if sort is 'A':
	for word in slimwords:
 		print word, counts[word]
else:
	tmp = list()
	for word, count in counts.items():
		tmp.append((count, word))
	tmp.sort(reverse = True)
	for item in tmp:
		print item

# Largest so far thing
bigcount = None
bigword = None
# Loop through list, save biggest so far
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

# Print biggest so far
print "Your largest word was:"
print bigword,bigcount
