class StringReverser:
    def reverse_words(self,input_string):
        self.input_string = input_string
        word_slicing = input_string.split()
        reverser = ' '.join(word_slicing[::-1])
        print( reverser)

# Example usage:
obj1 = StringReverser()
input_string = input("enter a string :")
result = obj1.reverse_words(input_string)

