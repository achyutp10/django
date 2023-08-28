# str[start:stop:step]

trial = 'reversal'
newTrial = trial[::-1]
print(newTrial)

def strRev(str):
    if len(str) == 0:
        return str
    else:
        return strRev(str[1:])+ str[0]
str = 'Hello'
reverse = strRev(str)
print('Reverse of string is : ', reverse )