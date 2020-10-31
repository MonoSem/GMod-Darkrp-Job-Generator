author = """
  ______               _             _____                          
 |  ____|             (_)           |  __ \                         
 | |____   _____ _ __  _ _ __   __ _| |__) |__ _ __ ___  ___  _ __  
 |  __\ \ / / _ \ '_ \| | '_ \ / _` |  ___/ _ \ '__/ __|/ _ \| '_ \ 
 | |___\ V /  __/ | | | | | | | (_| | |  |  __/ |  \__ \ (_) | | | |
 |______\_/ \___|_| |_|_|_| |_|\__, |_|   \___|_|  |___/\___/|_| |_|
                                __/ |                               
                               |___/                                """
print(author)
print("GMod DarkRP Job Generator")
print("")
name = input('Enter name of job: ')
color = input('Enter color of job: ')
model = input('Enter model of job: ')
description = input('Enter description of job: ')
weapons = input('Enter weapons of job: ')
command = input('Enter command of job: ')
max = input('Enter limit of job: ')
salary = input('Enter salary of job: ')
admin = input('Enter admin of job (true/false): ')
vote = input('Enter vote of job (true/false): ')
hasLicense = input('Enter License of job (true/false): ')
candemote = input('Enter candemote of job (true/false): ')

print("")
print("#----------------------------#")
print('= DarkRP.createJob("' + name  + '"'', {') 
print('color = Color(' + color + '),')
print('model = {' + model + '}')
print('description = [[' + description + ']],')
print('weapons = {' + weapons + '}')
print('command = "' + command + '",')
print('max =' + max + ',')
print('salary =' + salary + ',')
print('admin =' + admin + ',')
print('vote =' + vote + ',')
print('hasLicense =' + hasLicense + ',')
print('candemote =' + candemote)
print('})')
print("")
input("Press enter to exit")
