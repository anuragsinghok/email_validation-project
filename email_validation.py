#Email validation using string function

email = input(" Enter you Email :  ") # email condition -> G@g.com -> minimun 7 character we are using 
#-> we put all the condition 
k = 0
j=0
d=0
if len(email)>=7 :
    if email[0].isalpha():# is alpha is used to check alphabet value here it will check first value should be alphet
        if ('@' in email) and (email.count("@") ==1):# it will check email me @ hona chaiye and count 1 hona chaiye @ ek hi baar hona chaiye
            if (email[-4] == '.') ^ (email[-3] =="."): # ^ ex or operator use kiya check krlo isse email point hona chaiye kon se position pe or ka use nhi kra dono me se koi ek true hoga tbhi true hoga 
                for i in email :
                    if  i == i.isspace():#space checking on email
                        k =1 
                    elif i.isalpha():
                        if i==i.upper():# w -- W==W
                            j =1
                    elif i.isdigit():
                        continue
                    elif i =="_" or i =="." or i =="@":
                        continue
                    else:
                        d = 1

                if k ==1 or j==1 or d==1:
                    print(" wrong email 5")
                else:
                    print("right email")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("invalid email 2")


else:
    print("wrong email 1")
