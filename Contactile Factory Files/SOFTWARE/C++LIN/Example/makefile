exe: example.o
	g++ -std=c++17 -L../Library -lm -o example example.o -lPTSDK -lpthread

example.o:
	g++ -std=c++17 -I../Include -c example.cpp

clean:
	rm example.o
	rm example
