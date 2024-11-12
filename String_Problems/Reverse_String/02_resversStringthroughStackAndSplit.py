
# Approches...
# 1.
# Using Split, Reverse and Join
# Python program to reverse words in a string

def reverse_words(str):
    
    # Split the input string by '.' while 
    # ignoring multiple consecutive dots
    words = [word for word in str.split('.') if word]
    
    # Reverse the words
    words.reverse()
    
    # Join the reversed words back into a string
    return '.'.join(words)


if __name__ == "__main__":
    str = "..geeks..for.geeks."
    print("Approche 1-> ",reverse_words(str))

# Approch 2
# Using Stack
# Python program to reverse words in a string

def reverse_words(str):
    stack = []
    word = ""

    # Iterate through the string
    for ch in str:
        
        # If not a dot, build the current word
        if ch != '.':
            word += ch
        
        # If we see a dot, push the word into the stack
        elif word:
            stack.append(word)
            word = ""

    # Last word remaining, push it to stack
    if word:
        stack.append(word)

    # Rebuild the string from the stack
    return ".".join(stack[::-1])

if __name__ == "__main__":
    str = "..geeks..for.geeks."
    print("Approche 2-> ",reverse_words(str))
