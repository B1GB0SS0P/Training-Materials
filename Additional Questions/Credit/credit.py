def credit(n):
    s = str(n)[::-1]
    count = 0
    for i in range(0,len(s)):
        if i % 2 == 1:
            if int(s[i]) * 2 >= 10:
                count += 1 + int(s[i]) * 2 - 10
            else:
                count += int(s[i]) * 2 
        else:
            count += int(s[i])
    if (count % 10 == 0) and (len(s) == 15) and (str(n)[:2] in ['34', '37']):
        return 'AMEX'
    elif (count % 10 == 0) and (len(s) == 16) and (str(n)[:2] in ['51', '52', '53', '54', '55']):
            return 'MASTERCARD'
    elif (count % 10 == 0) and (len(s) == 16 or len(s) == 13) and (str(n)[0] == '4'):
        return 'VISA'
    else:
        return 'INVALID'

print(credit(378282246310005))
print(credit(371449635398431))
print(credit(378734493671000))
print(credit(5555555555554444))
print(credit(5105105105105100))
print(credit(4111111111111111))
print(credit(4012888888881881))
print(credit(4222222222222))
print(credit(6176292929))
    

