from os import getenv
from cryptography.fernet import Fernet
from os import listdir
import dotenv
import datetime

dotenv.load_dotenv()

SPY_KEY = getenv('SPY_KEY')

KEY = Fernet(SPY_KEY)
direction_list = listdir('spy_reports')
direction_list_dates = []

for i in range(len(direction_list)):
    direction_list_dates.append(direction_list[i][:10:])

for days in range(1, 31):
    to_check_date = datetime.date(year=2023, month=10, day=days).strftime("%d_%m_%Y")

    for i in range(len(direction_list)):
        if to_check_date in direction_list_dates:
            with open(f'spy_reports/{direction_list[i]}', 'rb') as file:
                message = file.read()
            with open(f'decrypted_reports/{direction_list[i]}_decrypted', 'wb') as file:
                file.write(KEY.decrypt(message))
        else:
            print(f"Отчета с датой: {to_check_date} не существует")
            break



