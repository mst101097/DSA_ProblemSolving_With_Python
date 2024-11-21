# Minimum number of deletions to make a string palindrome
# Given a string of size ‘n’. The task is to remove or delete the minimum number of characters from the string so that the resultant string is a palindrome. 

# Note: The order of characters should be maintained. 

# Examples : 

# Input : aebcbda
# Output : 2
# Remove characters 'e' and 'd'
# Resultant string will be 'abcba'
# which is a palindromic string
# Input : geeksforgeeks
# Output : 8

# A simple solution is to remove all subsequences one by one and check if the remaining string is palindrome or not. The time complexity of this solution is exponential.

# Take two indexes first as ‘i’ and last as a ‘j’
# Compare the character at the index ‘i’ and ‘j’
# If characters are equal, then 
# Recursively call the function by incrementing ‘i’ by ‘1’ and decrementing ‘j’ by ‘1’
# else 
# Recursively call the two functions, the first increment ‘i’ by ‘1’ keeping ‘j’ constant, second decrement ‘j’ by ‘1’ keeping ‘i’ constant.
# Take a minimum of both and return by adding ‘1’   

