.DEFAULT_GOAL := all
all: sesame

sesame: sesame.c
	gcc sesame.c -no-pie -fno-stack-protector -zexecstack -m32 -o sesame

clean:
	rm sesame


