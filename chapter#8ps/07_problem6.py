#7. Write a python function to remove a given word from a list ad strip it at the same
# time.



def rem(l, word):
    n = []
    for item in l:
        # Directly append the result of the replace() method
        n.append(item.replace(word, ""))
    return n

l = ["Hanzy", "Umer", "Maham", "an"]
print(rem(l, "an"))
