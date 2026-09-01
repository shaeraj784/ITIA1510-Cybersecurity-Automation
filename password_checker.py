#_________________________ Variables _________________________

#Establishing variables first as per instruction from ITCS 1140
#Week 01 Variables
account = 0
username = 0
password = 0
rotation_interval = 0
password_length = 0
length_score = 0
rotation_count = 0

#Week 02 Variables
length_verdict = 0
has_digit = 0
not_username = 0
rotation_verdict = 0
length_ok = 0
overall_pass = 0


#Addtl. Variables
#Non-essential variables for various features, usually related to the output
program_version = 'Password Security Checker 1.1.0 Alpha'
half_count = len(program_version) // 2 + 1

#____________________ Header & User Prompts ____________________

#Progam Version Header
print('=' + '=' * len(program_version) + '=')
print(' ' + program_version + ' ')
print('=' + '=' * len(program_version) + '=')

#User Prompts
#Querying of the user to obtain relevant info
#Report header should be symmetrical regardless of version number
account = input('Input which system the account belongs to (E.G. Outlook, Gmail, Proton, etc):')
#Username is collected to log which accounts need remediation and to ensure that the password is not the same as the username
username = input('Input username:')
password = input('Input password:')
rotation_interval = int(input('Input rotation interval per # of months:'))
print(' ')
print(' ')

#_____________________________ Logic ____________________________

#Calculations
#Determines the security of a password
password_length = len(password)
length_score = password_length * 10
rotation_count = 36 // rotation_interval

#Password Length Ratings
#Determines the rating of the password based on NIST SP 800-63B recommendations
if password_length >= 15:
    length_verdict = 'STRONG — meets NIST SP 800-63B recommendations'
elif password_length >= 6:
    length_verdict = 'GOOD — acceptable length for most systems'
elif password_length >= 4:
    length_verdict = 'MODERATE — meets minimum but falls short of NIST recommendations'
else:
    length_verdict = 'WEAK — does not meet minimum length requirements'

#_____________________________ Checks _____________________________

#Digit Check
#Checks if the password contains at least one digit
has_digit = '0' in password or '1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password

#Username Check
#Checks if the password is different from the username
not_username = password != username

#Rotation Interval Ratings / Check
#Rates the rotation interval based on NIST SP 800-63B recommendations
if rotation_interval <= 6:
    rotation_verdict = 'EXCELLENT — frequent rotation policy detected'
elif rotation_interval >= 6 and rotation_interval <= 12:
    rotation_verdict = 'ACCEPTABLE — rotation interval within recommended range'
else:
    rotation_verdict = 'WARNING — rotation interval exceeds recommended maximum of 12 months'

#___________________ Overall Verdict Determination __________________

#Determines the overall security of the password based on the previous checks
length_ok = password_length >= 15
overall_pass = length_ok and has_digit and not_username
if overall_pass == True:
    overall_pass='OVERALL: PASS — password meets all checked criteria'
else:
    overall_pass='OVERALL: FAIL — see findings above'

#_________________________ Report & Verdict __________________________

#Audit Report Header
print('=' + '=' * len(program_version) + '=')
print((half_count - 6 )* ' '  + 'Audit Report' +  (half_count - 6) * ' ')
print('=' + '=' * len(program_version) + '=')
print(' ')

#Audit Report Body
#Displays the end result of the inputs and calculations to the user.
print('Account:            ' + account)
print('Username:           ' + username)
print('Password Length:    ' + str(password_length))
print('Length score:       ' + str(length_score))
print('Rotation Interval:  ' + str(rotation_interval))
print('Rotations (3 yr):   ' + str(rotation_count))
print(length_verdict)
print(rotation_verdict)
if not_username == False:
    print('CRITICAL — password must not match username')
else:
    print('PASS — password does not match username')

#Audit Report Verdict
print(' ')
print('-' + '-' * len(program_version) + '-')
print((half_count - 3 )* ' '  + 'Verdict' +  (half_count - 3) * ' ')
print('=' + '=' * len(program_version) + '=')
print(overall_pass)
print('=' + '=' * len(program_version) + '=')
