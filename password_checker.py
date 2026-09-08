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

#Week 03 Variables
char = 0
batch_size = 0
count = 0
total_pass = 0
total_fail = 0
critical_count = 0

#Addtl. Variables
#Non-essential variables for various features, usually related to the output
program_version = 'Password Security Checker 1.2.0 Alpha'
half_count = len(program_version) // 2 + 1
audit_title_justify = 0
batch_title_justify = 0
border_size = len(program_version)+2

#Border Styles
def border_equals():
    print(border_size * '=')
def border_underscore():
    print(border_size * '_')
def border_octothorpe():
    print(border_size * '#')
def border_minus():
    print(border_size * '-')
def border_plus():
    print(border_size * '+')

#____________________ Header & User Prompts ____________________

#Progam Version Header
#print('=' + '=' * len(program_version) + '=')
border_plus()
print(' ' + program_version + ' ')
border_plus()
#print('=' + '=' * len(program_version) + '=')

#Program Loops
#Iterates count up to batch_size
#Variables must be initialized outside of loop as to not overwrite themselves with unintended results
batch_size = 3
count = 0
while count < batch_size:
    count = count + 1

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

#_____________________________ Logic _______________________________

#Calculations
#Determines the security of a password
    password_length = len(password)
    length_score = password_length * 10
    rotation_count = 36 // rotation_interval

#_____________________________ Checks ______________________________

#Digit Check
#Checks if the password contains at least one digit
#Logic was simplified from last version for easier to read code and faster processing
    has_digit = False
    for char in password:
        if char in '0123456789':
            has_digit = True    

#Username Check
#Checks if the password is different from the username
    not_username = password != username

#_____________________________ Ratings _____________________________

#Password Length Ratings
#Determines the rating of the password based on NIST SP 800-63B recommendations
    if password_length >= 15:
        length_verdict = 'STRONG — meets NIST SP 800-63B recommendations'
    elif password_length >= 12:
        length_verdict = 'GOOD — acceptable length for most systems'
    elif password_length >= 8:
        length_verdict = 'MODERATE — meets minimum but falls short of NIST recommendations'
    else:
        length_verdict = 'WEAK — does not meet minimum length requirements'

#Rotation Interval Ratings
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
        total_pass = total_pass + 1
    else:
        overall_pass='OVERALL: FAIL — see findings above'
        total_fail = total_fail + 1

#_________________________ Report & Verdict __________________________

#Audit Report Header
#Should automatically justify based on # of reports as long as the # of reports isn't too big
    audit_title_justify = (len('Audit Report ' + str(count) +  ' of ' + str(batch_size) ))//2
    border_equals()
    print((half_count-audit_title_justify)* ' '  + 'Audit Report ' + str(count) +  ' of ' + str(batch_size) + (half_count-audit_title_justify) * ' ')
    border_equals()
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
        critical_count = critical_count + 1
    else:
        print('PASS — password does not match username')

#Audit Report Verdict
    print(' ')
    border_minus()
    print((half_count - 3 )* ' '  + 'Verdict' +  (half_count - 3) * ' ')
    border_equals()
    print((len(program_version) - len(overall_pass)) * ' ' + overall_pass)
    border_equals()
    print(' ')
    print(' ')

#Batch Summary Report
#Variables here are for formatting
batch_title_justify = len('Batch Audit Summary')//2
print(' ')
print(' ')

#batch_summary_justify is subtracted from due to being the expected bigger number
border_octothorpe()
print((half_count - batch_title_justify)* ' ' + 'Batch Audit Summary' + ' ' * (half_count - batch_title_justify))
border_octothorpe()
print('Passwords audited:  ' + str(batch_size))
print('Passed:             ' + str(total_pass))
print('Failed:             ' + str(total_fail))
print('Critical Flags:     ' + str(critical_count))
#print('_' + '_' * len(program_version) + '_')
print('_' + '_' * len('NOTE: Input is still hardcoded -- file reading coming in Week 08.') + '_')
print(' NOTE: Input is still hardcoded -- file reading coming in Week 08.')
#print('#' + '#' * len(program_version) + '#')
print('#' + '#' * len('NOTE: Input is still hardcoded -- file reading coming in Week 08.') + '#')
