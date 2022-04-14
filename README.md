# javaFloatingPointCalculator

This program allows a user to input a number and if it is a java decimal floating point number, the program will return the number. The numbers are checked character by character. 

note*: theres been some test cases where python returns trailing zeroes and a single one. 

eg: .123e4 returns 1230.0000000000002 

debugging showed the program will take 1 to be 1 x 10^-1 = 0.1, 2 x 10^-2 = 0.02, and 3 x 10^-3 = .003 to be transformed

however adding 0.1 and 0.02 it becomes 0.120000000000001 

I am unsure of the cause of this but with this many trailing zeroes, the answer is still correct
