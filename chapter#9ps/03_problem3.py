#Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

def generateTables(n):
      table = ""
      for i in range(1,11) : # this is n x (1,11)
        table += f"{n} X {i} = {n*i}\n" # to concatinate each line of this multiplication inside the table string 
      with open(f"tables/table_{n}.txt", "w") as f :
          f.write(table)


for i in range (2,21) : # We wanted the table of 2 and  (21 ,2) x (1,11)
    generateTables(i)
