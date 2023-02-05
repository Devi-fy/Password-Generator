import secrets
import string
import time

digits = string.digits
abcup = string.ascii_uppercase
abclow = string.ascii_lowercase

LIST = digits + abcup + abclow

password = ''
print('Input how long you want the password')
pwdlength = int(input('Pwd Length : '))
print('WARNING : Might take a minute depending on how long your password is!')

start = time.time()
count = 0
for i in range(pwdlength):
    password += ''.join(secrets.choice(LIST))
    time.sleep(float(.1))
    count = count + 1
    print('On character', count, '.', pwdlength - count, ' characters to go!' )
    if count == pwdlength:
        print('DONE') 
    
end = time.time()

print('Password: ', password)

length = start-end
print('It took', length, 'seconds to genarate your password.')
