import hashlib

#md5 = hashlib.md5("hello").hexdigest()
def main():
	print("<<My First Python Tool>>")
	input_hash = raw_input("Enter the md5 has code: ")
	wordlist = raw_input("Enter the file name: ")
	
	file = open((wordlist), "rt")

	for line in file:
		word_hash = hashlib.md5(line.strip()).hexdigest()

		if input_hash == word_hash:
			print("[+] hash found: {}".format(line.strip()))
			break
		else:
			print("[-] hash failure: {}".format(line.strip()))






if __name__ == '__main__':
	main()
