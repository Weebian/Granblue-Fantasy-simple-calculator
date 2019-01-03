#GBF calc is a simple script that will calculate if we can preform a spark

#Imports
import inspect

#Classes
#The class for the gbf calculator
class Gbf_calc:
    __spark = 300

    def __init__(self, crystal_num, ten_draw_tickets, solo_draw_tickets, spark_num):
        self.__crystal_num = crystal_num
        self.__ten_draw_tickets = ten_draw_tickets
        self.__solo_draw_tickets = solo_draw_tickets
        self.__spark_num = spark_num

    #Method to check if we can spark
    def canSpark(self):
        self.__info()
        if(self.__spark_Calc() >= self.__spark):
            print("We can spark")
        else:
            print("We are short by " + str(self.__spark - self.__spark_Calc()) + " sparks")

    #Method to determine the number of draws can be perform from the number of crystals
    def __calc_crystal_draw(self):
        return int(self.__crystal_num/300)

    #Method to determine the number of 10 draws can be perform from the number of crystals
    def __calc_crystal_10_draw(self):
        return int(self.__crystal_num/3000)

    #Method to determine the number of solo draws after 10 draws using crystals
    def __calc_crystal_1_draw(self):
        return int((self.__crystal_num - self.__calc_crystal_10_draw() * 3000)/300)

    #Method to calculate the number of draws we can do
    def __spark_Calc(self):
        return self.__ten_draw_tickets*10+ self.__solo_draw_tickets + self.__spark_num + self.__calc_crystal_draw()

    #Method to print out info about spark
    def __info(self):
        print("\nNumber of time we can perform a crystal 10 draw: " + str(self.__calc_crystal_10_draw()))
        print("Number of time we can perform a crystal solo draw (after crystal 10 draws) : " + str(self.__calc_crystal_1_draw()))
        print("Number of 10 draw tickets: " + str(self.__ten_draw_tickets))
        print("Number of solo draw tickets: " + str(self.__solo_draw_tickets))
        print("Current number of sparks: " + str(self.__spark_num))
        print("Resulting Number of sparks: " + str(self.__spark_Calc()))
        

#Functions
#Main function
def main():
    print("Simple gbf calculator to determne if we can spark or not")
    print("\nInstructions:")
    print("You'll need to create a gbf_calc object, then call canSpark().")
    print("This will print out the information you require to spark.\n")
    print("Format: Gbf_calc(crystal_num, ten_draw_tickets, solo_draw_tickets, spark_num)")

#Check if running current file as the main file
if __name__ == "__main__":
    main()
