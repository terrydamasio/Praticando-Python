# Slicing create a substring by extracting elements from another string
#       indexing[] or slice()
#       [start:stop:step]

nome = "Terry Damasio Santos"
print(nome[0:20:2])

#    start:stop
print(nome[6:])

#     start:step
print(nome[0::2])

# Slice
#slice(start:count from end negative)
email = "terrydamasio.dev@gmail.com"
slice = slice(16, -4)

emailSliced = email[slice]
print(emailSliced)


