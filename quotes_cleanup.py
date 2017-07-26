import random

quotes = open("lotr_quotes.txt").readlines()
#
# for x in range(10):
#     print (quotes[x])
#     break
c_quotes = []

for quote in quotes:
    c_quotes.append(quote.strip())

d_quotes = []

# for x in range(10):
for c in c_quotes:
    if len(c) > 5:
        d_quotes.append(c)


print (d_quotes)
# for d in d_quotes:
#     if len(d) > 5:
#         print (d)
#
# print (len(d_quotes))

#
# for x in range (len(d_quotes)):
#     print (d_quotes[x])


# print (d_quotes[random.randint(0,len(d_quotes)-1)])
