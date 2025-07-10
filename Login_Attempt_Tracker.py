correct_pass="python123"
attempt=0
while attempt<3:
    pwd=input("enter password:")
    if pwd==correct_pass:
        print("correct password,welcome")
        break
    else:
        attempt+=1
        print("wrong password,try again")
    if attempt==3:
        print("access blocked:Too many attempts")