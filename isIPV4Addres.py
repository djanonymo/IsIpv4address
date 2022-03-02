'''An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of digits, full stops and lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 30.

[output] boolean

true if inputString satisfies the IPv4 address naming rules, false otherwise.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
'''
def solution(inputString):
    puntos=0
    pp=0
    pun=0
    num= ["","","",""]
    for i in inputString:
        if i=='.':
            puntos+=1
            pp+=1
            if puntos>3:
                return False
            continue
        num[pp]+=i

    if puntos==3:
        '''if (int(num[0])>=0 and int(num[0])<=255 and int(num[1])>=0 and int(num[1])<=255 and int(num[2])>=0 and int(num[2])<=255 and int(num[3])>=0 and int(num[3])<=255):
            return True
        else: '''
        for i in range(0,4):
            if not(num[i].isnumeric()):
                print(num[i]+" its no numeric ")
                return False
            elif num[i]== "" or len(num[i])>1 and num[i][0] =='0':
                print(" There is no number "+ str(i))
                return False
            elif int(num[i])<0 or int(num[i])>255 :
                print(num[i]+" is not in range [0, 255].")
                return False
        return True
    else:
        return False
    
entrada="0.254.255.00"
print(solution(entrada))
    
