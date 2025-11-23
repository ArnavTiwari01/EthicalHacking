import hashlib

wordlist = open("wordlist.txt").read().splitlines()
hash_input = input("Hash to crack: ")

for word in wordlist:
    result = hashlib.md5(word.encode()).hexdigest()
    if result == hash_input:
        print("Password found:", word)
        break
