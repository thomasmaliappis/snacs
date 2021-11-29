CC=g++
ST=--std=c++11
LOP=-o

MAIN=*
TAG=motif

all : clean code1

code1 :
	$(CC) -I ../boost_1_77_0 -g -O0 $(ST) $(LOP) $(TAG) $(MAIN).cpp $(MAIN).h

clean :
	rm -f $(TAG)
