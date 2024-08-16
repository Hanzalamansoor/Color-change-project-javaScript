#Write a program to fill in a letter template given below with name and date
#letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>

letter = '''
   Dear <|Name|>,
   You are selected!
   <|Date|>
'''
print(letter.replace("<|Name|>","Hanzala mansoor").replace("<|Date|>","25 july 2024")) 
#upper pehlay name wali string aik puri string bani phir uss puri strting say kha k replace kro date say issay chaining khetay hai


