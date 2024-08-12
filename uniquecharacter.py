input_string = "Guvi Geeks Private Limited"
letter = []

for char in input_string:
    if input_string.count(char) == 1: #if input string has unique latter that will be 1
        letter += char      
            
print("String with unique letters: ", letter)