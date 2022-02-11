#!/bin/bash
# Compile and run PMCTest in 64 bit mode using C++
# (c) 2012 by Agner Fog. GNU General Public License www.gnu.org/licenses

# Compile A file if modified
if [ PMCTestA.cpp -nt a64.o ] ; then
g++ -o pmc_test2 -O2 -c -m64 -oa64.o PMCTestA.cpp 
fi

# Compile B file and link
g++ -O2 -m64 a64.o PMCTestB.cpp -lpthread -o pmc_test2
if [ $? -ne 0 ] ; then exit ; fi
./pmc_test2

# read -p "Press [Enter]"
