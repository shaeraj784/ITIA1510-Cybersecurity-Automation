#Variables
#Establishing variables first as per instruction from ITCS 1140
account = 0
username = 0
password = 0
rotation_interval = 0
password_length = 0
length_score = 0
rotation_count = 0

#Addtl. Variables
#Non-essential variables for various features, usually related to the output
program_version = 'Password Security Checker 1.0.0 Alpha'

#User Prompts
#Querying of the user to obtain relevant info
#Report header should be symmetrical regardless of version number
print('=' + '=' * len(program_version) + '=')
print(' ' + program_version + ' ')
print('=' + '=' * len(program_version) + '=')
account = input('Input the name of the system the account belongs to (E.G. Outlook, Gmail, Proton, etc):')
#Username is collected to log which accounts need remediation
username = input('Input username:')
password = input('Input password:')
rotation_interval = int(input('Input rotation interval per # of months:'))
print(' ')
print(' ')

#Calculations
#Determines the security of a password, no grading scale yet
password_length = len(password)
length_score = password_length * 10
rotation_count = 36 // rotation_interval

#Audit Report
#Displays the end result of the inputs and calculations to the user.
print('=======================================')
print('         Password Audit Report         ')
print('=======================================')
print(' ')
print('Account:            ' + account)
print('Username:           ' + username)
print('Password Length:    ' + str(password_length))
print('Length score:       ' + str(length_score))
print('Rotation Interval:  ' + str(rotation_interval))
print('Rotations (3 yr):   ' + str(rotation_count))
print(' ')
print('---------------------------------------')
print('          Classifications TBA          ')
print('=======================================')
