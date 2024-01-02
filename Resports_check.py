from os import listdir

list_data = listdir('decrypted_reports')

for i in range(len(list_data)):
    with open(f'decrypted_reports/{list_data[i]}', 'r', encoding='UTF-8') as file:
        data = file.read()
        print(data)

print('=========================================================================')
for i in range(len(list_data)):
    with open(f'decrypted_reports/{list_data[i]}', 'r', encoding='UTF-8') as file:
        data = file.read()
        data = data.lower().replace('вра', 'дру')
        # print(data)
        with open(f'decrypted_reports/{list_data[i]}', 'w', encoding='UTF-8') as fl:
            fl.write(data)


for i in range(len(list_data)):
    with open(f'decrypted_reports/{list_data[i]}', 'a', encoding='UTF-8') as file:
        file.write('\n'+'Проверено!')




