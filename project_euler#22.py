def score(word):
	count = 0
	for j in word:
		if j.isalpha():
			count+=ord(j)-64
	return count


with open("C:\\Users\\Sumanth\\Downloads\\paper.txt", 'r+') as file:
	file_sort = sorted(file.read().split(','))
	print(sum([(file_sort.index(k)+1)*score(k) for k in file_sort]))
file.close()
