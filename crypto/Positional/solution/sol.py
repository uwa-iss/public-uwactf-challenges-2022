def main():
    with open("key.txt", "r") as f:
        key_raw = f.read()
        key_raw = key_raw.replace('\n', '')

    with open("message.txt", "r") as f:
        message_lines = f.readlines()

    key_indexes = []

    for i in range(0, len(key_raw), 2):
        index_str = key_raw[i:i+2]
        if index_str[0] == '0':
            index_str = index_str[1]

        key_indexes.append(int(index_str)-1)
    for i, line in zip(key_indexes, message_lines):
        print(line[i], end='')

    print()

if __name__ == "__main__":
    main()
