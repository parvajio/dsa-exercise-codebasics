# 1. Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

# 1. 
# i. 
exp = [2200, 2350, 2600, 2130, 2190]

print(exp[1]- exp[0])

#ii.
print(exp[0] + exp[1] + exp[2])

#iii.
print(2000 in exp)

# iv.
exp.append(1980)
print(exp)


# v.
exp[3] -= 200
print(exp)

# 2. You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']

# i. 
print(len(heros))

# ii.
heros.append("black panther")
print(heros)

# iii.
heros.remove("black panther")
print(heros)

heros.insert(3, "black panther")
print(heros)

# iv.
heros[1:3] = ["doctor strange"]
print(heros) 

# v.
heros.sort()
print(heros)

# 3. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max = int(input("Enter max number: "))
lst = []
for i in range(1,max+1):
    if(i%2 == 0):
        lst.append(i)
print(lst)