# write a program to check whether an alphabet is vowel or consonent

beg_alphabet = input("Enter an alphabet: ")

chasii = ord(beg_alphabet)
chasii = chasii + 32
alphabet = chr(chasii)
# print(alphabet)

if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
    print(alphabet ," is a vowel.")

else:
    print(alphabet ," is a consonent.")
