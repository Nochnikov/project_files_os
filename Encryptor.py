from os import getenv
from cryptography.fernet import Fernet
from os import listdir
from dotenv import load_dotenv


load_dotenv()

new_key = getenv('NEW_SPY_KEY')

KEY = Fernet(new_key)

list_of_data = listdir('decrypted_reports')

print('Содержимое папки: ')

for values in list_of_data:
    print(values)
print('=====================================================')
for i in range(len(list_of_data)):
    if 'c' not in list_of_data[i][10:20:]:
        print(f'Начинаю шифрование для {list_of_data[i]} ')
        with open(f'decrypted_reports/{list_of_data[i]}', 'rb') as file:
            data = file.read()
            with open(f'encrypted_reports/{list_of_data[i]}', 'wb') as fl:
                data = KEY.encrypt(data)
                fl.write(data)
    else:
        print(f'Не достоверная информация в {list_of_data[i]}')







