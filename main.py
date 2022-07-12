def main():
    # taking input from the user
    word = input("Enter the word: ").lower()
    char_count = {}
    max_count = 0
    max_char = ''
    
    for char in word:
        if char_count.get(char) and char_count.get(char) >= 1:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1    
            
    for key, value in char_count.items():
        if char_count[key] > max_count:
            max_count = char_count[key]
            max_char = key
            
    return max_char
    
        
output = main()

print(output)