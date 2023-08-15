#Написать функцию на Python, которой передаются в качестве параметров команда и текст. 
#Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
#и False в противном случае. Передаваться должна только одна строка,
#разбиение вывода использовать не нужно.

import subprocess

def Command():
    command = input ('Введите команду и текст через пробел ')
    
    
    if __name__ == '__main__':
        result = subprocess.run(command, shell = True, stdout=subprocess.PIPE, encoding='utf-8')
        result_out = result.stdout

        if result.returncode ==0 and isinstance(result_out, str):
            return True
        else:
            return False
    

print(Command())