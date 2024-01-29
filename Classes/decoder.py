def decoder(s):
    def recursive(index):
        final_string = "" #we store the result of each block in a separate variable
        num = 0 #used for storing multiplication part

        #enumarating through the length of our string
        while index < len(s):

            #getting each element and checking if its a digit
            char = s[index]
            if char.isdigit():
                num = num * 10 + int(char)
            #getting the index of starting position
            elif char == '[':
                index, decoded_str = recursive(index + 1)
                final_string += num * decoded_str
                num = 0
            #Getting the index of the ending position
            elif char == ']':
                return index, final_string
            else:
                #Adding in case its just a regular char
                final_string += char
            index += 1
        return final_string
    return recursive(0)


print(decoder("2[aaaaaaaaaaaaaaaa]6[bcd]"))
