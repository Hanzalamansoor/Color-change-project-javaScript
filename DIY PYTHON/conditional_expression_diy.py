#create a program in which you ask user to input the age and check if he is able to drive or not 

# age = int(input("Enter your age to check if you are eligible to drive or not : "))

# if(age>=18) :
#     print("Congratulations you are eligible to drive")
# else :
#     print("sorry You are not eligible to drive")



# Check if the year is a leap year or not : 

# year = int(input("Enter a year : "))

# if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) :
#     print("This is a leap year ")
# else :
#     print("The year is not a leap year")






#Concert celcis into farenhite 

# celsius = float(input("Eneter temperature in celsius : "))
# fahrenhite = (celsius * 9/5) + 32
# print(f"The temperature conversion from celsius to fahrenhite is :{fahrenhite}")



#Calculate the Area of a Circle Given its Radius
# import math
# Radius = float(input("Enter the radius of the circle :"))
# Area = math.pi * Radius**2
# print(f"The final area of the circle given the radius is : {Area} ")



# if the student got 40% then he is passed and even if he got 33 in all of the 3 subject but he is failed  otherwise 
# subject1 = int(input("Enter the marks of  the sudent in subject 1 :"))
# subject2 = int(input("Enter the marks of  the sudent in subject 2 :"))
# subject3 = int(input("Enter the marks of  the sudent in subject 3 :"))

# student_percentage = 100*(subject1+subject2+subject3)/300

# if(student_percentage >= 40 and subject1 >= 33 and subject3 >= 33  and subject3 >= 33) :
#     print(f"Congrats you passed you got{student_percentage}")
# else : 
#     print(f"You failed you got{student_percentage} ")




#check if any of these spam comment is in the text

# p1 = "click here"
# p2 = "buy now"
# p3 = "free"


# text = input("Enter the text :")


# if(p1 in text or p2 in text or p3 in text) :
#     print("You have found a spam comment")
# else :
#     print("No spam comment")












#                   MOVIE RATING PROGRAM PYTHON 

#Rate the movies and prompt which movie is greater than other

#List of movies to rate (between 1-10)
movie1 = int(input("rate the movie( 1-10) Titanic :"))
movie2 = int(input("rate the movie( 1-10) God father :"))
movie3 = int(input("rate the movie( 1-10) L.A confidential :"))
movie4 = int(input("rate the movie( 1-10) Parasite :"))


#conditions to check which movie is the greatest
if(movie1 > movie2 and movie1 > movie3 and movie1 > movie4) :
    print("Titanic is the best movie")
elif(movie2 > movie1 and movie2 > movie3 and movie2 > movie4) :
    print("God father is the best movie")
elif(movie3 > movie1 and movie3 > movie2 and movie3 > movie4) :
    print("L.A confidential is the best movie")
elif(movie4 > movie1 and movie4 > movie2 and movie4 > movie3) :
    print("parasite is the best movie")


    #check for multiple ties 
 # For movie1 ties against all other movies   
elif(movie1 == movie2):
    print("There is a tie between Titanic and God father")
elif(movie1 == movie3):
    print("There is a tie between Titanic and L.A confidential")
elif(movie1 == movie4):
    print("There is a tie between Titanic and parasite")
 # For movie2 ties against all other movies 
elif(movie2 == movie1):
    print("There is a tie between God father and Titanic")
elif(movie2 == movie3):
    print("There is a tie between God father and L.A confidential")
elif(movie2 == movie4):
    print("There is a tie between God father and parasite")
 # For movie3 ties against all other movies 
elif(movie3 == movie1):
    print("There is a tie between L.A confidential and Titanic")
elif(movie3 == movie2):
    print("There is a tie between L.A confidential and God father")
elif(movie3 == movie4):
    print("There is a tie between L.A confidential and parasite")
elif(movie4 == movie1):
    print("There is a tie between parasite and Titanic")
elif(movie4 == movie2):
    print("There is a tie between parasite and God father")
elif(movie4 == movie3):
    print("There is a tie between parasite and L.A confidential")










