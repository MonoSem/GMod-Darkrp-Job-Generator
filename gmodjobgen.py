author = """
  ______               _             _____                          
 |  ____|             (_)           |  __ \                         
 | |____   _____ _ __  _ _ __   __ _| |__) |__ _ __ ___  ___  _ __  
 |  __\ \ / / _ \ '_ \| | '_ \ / _` |  ___/ _ \ '__/ __|/ _ \| '_ \ 
 | |___\ V /  __/ | | | | | | | (_| | |  |  __/ |  \__ \ (_) | | | |
 |______\_/ \___|_| |_|_|_| |_|\__, |_|   \___|_|  |___/\___/|_| |_|
                                __/ |                               
                               |___/                                """
print("GMod DarkRP Job Generator made by")
print(author)
print("and Luiggi33")
def generator():
    print("Exit with CTRL+C at all time")
    print("")
    teamid = input('Enter the TeamID: ')
    name = input('Enter the name of the job: ')
    color = input('Enter the color of the job: ')
    model = input('Enter the model of the job: ')
    description = input('Enter the description of the job: ')
    weapons = input('Enter the weapons of the job: ')
    command = input('Enter the command of the job: ')
    max = input('Enter the limit of the job: ')
    salary = input('Enter the salary of the job: ')
    admin = input('Enter the admin of the job (true/false): ')
    vote = input('Enter the vote of the job (true/false): ')
    hasLicense = input('Enter the License of the job (true/false): ')
    candemote = input('Enter the candemote of the job (true/false): ')
    category = input('Enter the Category of the job: ')

    print("")
    print("#----------------------------#")
    print('TEAM_' + upper(teamid) + ' = DarkRP.createJob("' + name  + '"'', {') 
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
    print('candemote =' + candemote + ',')
    print('category = "' + + '"')
    print('})')
    print("")

flag = True
while flag:
    generator()
    flag = True
