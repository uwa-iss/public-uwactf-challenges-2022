.DEFAULT_GOAL := all
all: houseofwhat

houseofwhat: houseofwhat.c
	gcc houseofwhat.c -Xlinker -rpath=./lib -Xlinker -I./lib/ld.so -o houseofwhat

clean:
	rm houseofwhat
