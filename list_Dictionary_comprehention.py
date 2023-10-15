num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num_list = []
for num in num_list:
    if num % 2 == 0:
        even_num_list.append(num)
print (even_num_list)

even_num_list = [even_num for even_num in num_list if even_num % 2 == 0]
print (even_num_list)

even_num_list = [
  num
  for num in num_list
  if num % 2 == 0
]

print(even_num_list)

matrix_1d = []
matrix_2d = [[1, 2, 3],
            [4, 5, 6]]

for row in matrix_2d:
    for num in row:
        matrix_1d.append(num)
print(matrix_1d)

matrix_2d = [[1, 2, 3],
            [4, 5, 6]]

matrix_1d = [num for row in matrix_2d for num in row]


vowels = 'aeiou'
sentence = 'I am awesome!'
filtered_letters = []

for letter in sentence:
    if letter not in vowels:
        filtered_letters.append(letter)

print(''.join(filtered_letters))


vowels = 'aeiou'

sentence = 'I am awesome'

filtered_sentence = ''.join([letter for letter in sentence if letter not in vowels])

print(filtered_sentence)

fruit_ranking = [1, 2, 3]
fruit_name = ['Mango', 'Pineapple', 'Watermelon']
fruit_rank_dict = {}

for i in range(len(fruit_ranking)):
    fruit_rank_dict[fruit_ranking[i]] = fruit_name[i]

print(fruit_rank_dict)

fruit_ranking = [1, 2, 3]

fruit = ['Mango', 'Pineapple', 'Watermelon']

fruit_ranking_dict = { fruit_ranking[i] : fruit[i] for i in range(len(fruit_ranking)) }

print(fruit_ranking_dict)