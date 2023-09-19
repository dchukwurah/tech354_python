# Collections can store multiple pieces of data

# Lists - arrays

shopping_list = ["Salad", "Eggs", "Doughnuts", "Milk", "Samon"]

print(shopping_list)
print(shopping_list[0])
print(shopping_list[-1])

shopping_list[2] = "Granola"
print(shopping_list)

# List methods

#Adding to the list
shopping_list.append("Carrots") # add to the end
shopping_list.append("Water") # add multiple
print(shopping_list)

# #Remove items from list
# shopping_list.remove("Salad")
# shopping_list.pop() # remove from the list and store item
# shopping_list.pop(1) #
# print(shopping_list)

print(shopping_list[0::2]) #print list step over 1 item
print(shopping_list[-1::-1]) #print list backwards


# Tuples - Immutable, they cannot be changed

