all_cat_names = []
try:
    number_of_cats = int(input('How many cats do you have? '))
except ValueError:
    print('Please enter a number: ')
    number_of_cats = int(input('How many cats do you have? '))
    
def store_cat_names(name):
    all_cat_names.append(name)

for i in range(number_of_cats):
    cat_name = input('Enter the name of cat number ' + str(len(all_cat_names) + 1) + ': ')
    if cat_name not in all_cat_names:
        store_cat_names(cat_name)
    else:
        print('This name is already in the list! Type another cat name: ')
        cat_name = input('Enter the name of cat you have not listed before: ')
        store_cat_names(cat_name)

print()
print('The cat names are: ')

for i in all_cat_names:
    print(i)