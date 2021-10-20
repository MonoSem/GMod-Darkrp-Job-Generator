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
    color = input('Enter the color of the job (r,g,b): ')
    model = input('Enter the model of the job: ')
    description = input('Enter the description of the job: ')
    weapons = input('Enter the weapons of the job ("weapon1","weapon2"): ')
    command = input('Enter the command of the job: ')
    max = input('Enter the limit of the job: ')
    salary = input('Enter the salary of the job: ')
    admin = input('Enter if its a admin only job (true/false): ')
    vote = input('Enter if this Job needs to be voted on (true/false): ')
    hasLicense = input('Enter if this Job spawns with a License (true/false): ')
    candemote = input('Enter if this Job can be demoted (true/false): ')
    category = input('Enter the Category of the job: ')

    print("")
    print("")
    print("#----------------------------#")
    print('TEAM_' + teamid.upper() + ' = DarkRP.createJob("' + name  + '"'', {') 
    print('color = Color(' + color + '),')
    print('model = {' + model + '}')
    print('description = [[' + description + ']],')
    print('weapons = {' + weapons + '}')
    print('command = "' + command + '",')
    print('max = ' + max + ',')
    print('salary = ' + salary + ',')
    print('admin = ' + int(admin) + ',')
    print('vote = ' + vote + ',')
    print('hasLicense = ' + hasLicense + ',')
    print('candemote = ' + candemote + ',')
    print('category = "' + category + '",')
    print('})')
    print("")

flag = True
while flag:
    print("New Job Generation Started")
    generator()
