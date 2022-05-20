import matplotlib.pyplot as plt

cipher_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

'''
Unicode (UTF-8) table

Capital Letters A-Z = Range 64 (0x41) - 90 (0x5a)
Lower Case Letters a-z = Range 97 (0x61) - 122 (0x7a)

'''

class Cipher_text:
    def __init__(self, cipher_text):
        self.cipher_text = cipher_text

    def load_cipher_text():
        print("hello")

    def count_upper_characters(self, cipher_text):
   
        # define empty dictionaries for letter and count key value pairs
        upper = {}

        for character in range(65, 91):

            upper.update({chr(character):cipher_text.count(chr(character))})
    
        return upper
    
    def count_lower_characters(self, cipher_text):
 
        # define empty dictionaries for letter and count key value pairs
      
        lower = {}
        for character in range(65, 91):

            lower.update({chr(character).lower():cipher_text.count(chr(character).lower())})

        return lower 

    def sum_upper_lower_characters(self, upper, lower):
  
    # define empty dictionaries for letter and count key value pairs
        combined = {}  
        for character in range(65, 91):

            combined.update({chr(character).lower(): upper.count(chr(character)) + lower.count(chr(character).lower())})

        return combined

    def calcuate_percentages(combined):

        percentages = {}
        for key, value in combined.items():

            percentages.update({key: round((value/total_count)*100, 4)})

    def plot_analysis(percentages):
 
        x_axis = []
        y_axis = []

        for character, percentage in percentages.items():
            x_axis.append(character)
            y_axis.append(percentage)

        plt.bar(x_axis, y_axis)
        plt.show()