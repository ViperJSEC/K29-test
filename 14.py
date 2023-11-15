#for n in range(3, 10):
#    if int('121', n + 1) == (int('121', n) + int('13', 16)):
#        print(n)

#for x in range(2, 20):
#    if (int('111', x) + int('13', 5)) == int('515', 6):
#        print(x)

#for x in range(0, 10):
#    if (int('1234' + str(x), 15) + int('5' + str(x) + '678', 15)) % 11 == 0:
#        print(x, (int('1234' + str(x), 15) + int('5' + str(x) + '678', 15)) // 11)

#for x in '0123456789ABCDEFGH':
#    if (int('2671' + x, 18) + int('8513' + x, 18)) % 13 == 0:
#        print(x, (int('2671' + x, 18) + int('8513' + x, 18)) // 13)

#for x in '0123456789ABCDEF':
#    if (int('d49' + x + '1', 16) + int('48a3' + x, 16)) % 14 == 0:
#        print(x, (int('d49' + x + '1', 16) + int('48a3' + x, 16)) // 14)

#for x in range(0, 37):
#    if ((6 * 37 ** 3 + 5 * 37 ** 2 + 4 * 37 ** 1 + x * 37 ** 0) + (5 * 37 ** 3 + x * 37 ** 2 + 4 * 37 ** 1 + 7 * 37 ** 0)) % 79 == 0:
#       print(((6 * 37 ** 3 + 5 * 37 ** 2 + 4 * 37 ** 1 + x * 37 ** 0) + (5 * 37 ** 3 + x * 37 ** 2 + 4 * 37 ** 1 + 7 * 37 ** 0)) // 79)

#for x in '0123456789ABCDEFGHIJ':
#    for y in '0123456789ABCDEFGHIJ':
#        if (int(f'b{y}11cb{x}g17', 20) + int(f'8a{x}17', 20)) % 107 == 0:
#            print(x, y, (int(f'b{y}11cb{x}g17', 20) + int(f'8a{x}17', 20)) // 107)

#for p in range(10, 36):
#    for x in range(0, 35):
#        for y in range(0, 35):
#            if (((1*p**3 + 7*p**2 + x*p**1 + 8*p**0) + (y*p**3 + x*p**2 + y*p**1 + 6*p**0)) == (9*p**3 + y*p**2 + y*p**1 + 0*p**0)):
#                print(x*p**2 + x*p**1 + y*p**0)

#s = 64**13 + 32**6 - 16**2
#print(bin(s)[2:].count('1'))

#s = oct(4096**3125 - 512**625 + 64**125 - 8**25)[2:]
#print(s.count('7'))

#s = bin(512**230 + 256**64 - 32**23)[2:]
#print(s.count('0'))

s = 625**134 * 125**32 + 25**52 - 5
cnt = 0
while s > 0:
    if s % 5 == 4:
        cnt += 1
    s = s // 5
print(cnt)