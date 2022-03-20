 main : main.o src_a.o
	g++ main.o src_a.o -o main

 main.o : main.cpp
	g++ -c main.cpp -o main.o

 src_a.o : src_a.cpp
	g++ -c src_a.cpp -o src_a.o

.PHONY : clean
clean:
	del *.o *.s *.i main.exe -f