# Write a program which accepts one charracter and checks whether it is vowel or consonant.
def check_vowel(ch):
    if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    else:
        return False

def main():
    char = input("Enter the one character to check whether it is vowel or not: ")
    is_vowel = check_vowel(char)
    if is_vowel:
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")

if __name__ == "__main__":
    main()