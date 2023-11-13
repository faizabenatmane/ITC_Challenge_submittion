import string
password = input("Enter your password: ")

lentgh_password= len(password)

upper_case=any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case=any([1 if c in string.ascii_lowercase else 0 for c in password])
special=any([1 if c in string.punctuation else 0 for c in password])
digits=any([1 if c in string.digits else 0 for c in password])
caracters=[upper_case,lower_case,special,digits]

score=0

#feedback
feedback=""
with open('/Users/mac/Downloads/common_password-list-10m.txt','r') as f:
    common=f.read().splitlines()
if password in common :
    feedback+="your password exist in the common password list,Avoid using common dictionary words\n"  
if lentgh_password<8:
    feedback +="the Length of your password is too short, Use a longer password\n"    
if sum(caracters)<4:
    feedback += "Your password should contain at least one upper case letter ,one lower case letter ,one special character and one number \n"
#increase score
if(lentgh_password>8):
    score+=1
if(lentgh_password>12):
    score+=1
if(lentgh_password>16):
    score+=1
if(lentgh_password>19):
    score+=1    

if sum(caracters)>1:
    score+=1  
if sum(caracters)>2:
    score+=1  
if sum(caracters)>3:
    score+=1 

if (score<4):
    print("Your Password's Strength is : ",score,"/7\n" "Your Password is Quite Weak!\nRecommendations:",feedback)
else:
    print("Your Password's Strength is : ",score,"/7\n" "Your Password is Strong!\n")


    




    