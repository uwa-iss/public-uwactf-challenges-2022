iv = 140512244688361
ciphertext = [7393415227443049, 8077192723678156, 4101310444290190, 8090446768978805, 4118192954888783, 2719978387027670, 3869257800022688, 12514449250651222, 13720115820361887, 14458697086363679, 14458697086363679]

prev = iv
plaintext = []
for i in ciphertext:
	res = i ^ prev
	prev = i
	plaintext.append(res)

for i in range(0, len(plaintext)): plaintext[i]=str(plaintext[i])
plaintext = "".join(plaintext)

i = 0
while i < len(plaintext):
    if plaintext[i] == "1":
        print(chr(int(plaintext[i:i+3])),end="")

        i += 3
    else:
        print(chr(int(plaintext[i:i+2])), end="")
        i += 2
print()