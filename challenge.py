# Write a program to append the times tables to out jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output)
# from the For loops part 2 lecutre in section 6).

# The first column of numbers should be right justified
with open('sample.txt', 'a') as jabber:
    for i in range(2, 13):
        for j in range(2, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=jabber)
        print("-" * 20, file=jabber)