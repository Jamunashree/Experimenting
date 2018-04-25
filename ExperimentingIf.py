x= "Analyse Survey Data with the scripts on ***link***"
y= "Meet us in the lobby at 8.30"
print("Do you analyze survey data for work?")
ans1=input()
if ans1=='yes':
    print("Do you speak any R?")
    ans2=input()
    if ans2=="yes":
        print(x)
    elif ans2=="no":
        print("Do you analyze survey data with SAS,SUDAAN,Stata or SPSS?")
        ans4=input()    
        if ans4=="no":
            ans5=input("Does it bother you that your analyses might all be wrong?")
        elif ans4=="yes":
            ans7=input("Are you concerned that proprietary software makes statistical research difficult to reproduce?")
            if ans7=="no":
                print(ans6)
            elif ans7=="yes":
                print("Learn R by watching 2 minute videos",x)
            else:
                print('')
            if ans5=="no":
                ans6=input("Do you mind the price tag?")
                if ans6=="no":
                    print("First round's on you",y)
                else:
                    print('')
            else:
                print('')        
        else:
            print('')
    else:
        print('')
        
elif ans1=="no":
    print("Why are you here?")
    ans3=input()
    if ans3=="Heard there was beer":
        print(y)
    else:
        print("")
        
else:
    print('')


    
