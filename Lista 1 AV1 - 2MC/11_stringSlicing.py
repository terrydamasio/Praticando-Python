# Slicing create a substring by extracting elements from another string
#       indexing[] or slice()
#       [start:stop:step]


nome = "Terry Damasio"

firstName = nome[0:6]
lastName = nome[6:14]
reversedName = nome[::-1]

print(firstName)
print(lastName)
print(reversedName)

# Slice
# slice(start: count from end negative)
email = "terrydamasio.dev@gmail.com"
slice = slice(16, -4)

emailSliced = email[slice]
print(emailSliced)
