class Frequency_analysis:
    
    import matplotlib.pyplot as plt
    
    data = ""

    def __init__(self, data_file):
        
        self.data_file= data_file

    def load_data(self):
        
        data = open(self.data_file, "r")

        return data.read()

    def count_upper_characters(self):
   
        # define empty dictionaries for letter and count key value pairs
        upper = {}

        print(self.data)

        for character in range(65, 91):
            
            upper.update({chr(character):self.load_data().count(chr(character))})
    
        return upper
    
    def count_lower_characters(self):
 
        # define empty dictionaries for letter and count key value pairs
      
        lower = {}
        for character in range(65, 91):

            lower.update({chr(character).lower():self.load_data().count(chr(character).lower())})

        return lower 

    def sum_upper_lower_characters(self):
  
    # define empty dictionaries for letter and count key value pairs
        combined = {} 
        lower_dict = self.count_lower_characters()
        upper_dict = self.count_upper_characters()
        
        #for character in range(65, 91):
     
            #combined.update({chr(character).lower(): self.count_upper_characters().count(chr(character)) + self.count_lower_characters.count(chr(character).lower())})

            #return lower_dict
        print(lower_dict["A"])




    def calcuate_percentages(self):

        percentages = {}
        for key, value in self.sum_upper_lower_characters().items():

            percentages.update({key: round((value/total_count)*100, 4)})

    def plot_analysis(percentages):
 
        x_axis = []
        y_axis = []

        for character, percentage in percentages.items():
            x_axis.append(character)
            y_axis.append(percentage)

        plt.bar(x_axis, y_axis)
        plt.show()

my_object = Frequency_analysis("test_data.txt")


#print(my_object.count_upper_characters())
#print(my_object.count_lower_characters())
print(type(my_object.sum_upper_lower_characters()))
