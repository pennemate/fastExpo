#################################################
#                                               #
# Sarah Khoja                                   #
# Crypto- Square and Multiply function          #
# AKA- Fast exponentiation                      #
#                                               #
#################################################


'''
input: exponent as an integer
output: exponent as binary array
'''
def toBin(e):                                     #function to convert exp to binary
    binExp=[]                                       #array to hold final
    while(e>0):
        binExp.append(e%2)                        #mod 2 for the 1/0
        e= e/2                                  #div 2 to decrease the exponent, prevent infinite loop, get next mod
    binExp=binExp[::-1]                             #let's make it backwards- good for SAM
    return binExp

'''
input: (b^e) mod m
output: the result of that calculation
'''
def SAM(b,e,m):                                     #Square and Multiply Function
    result=1                                        #store the original base in result
    e=toBin(e)                                      #convert exp to binExp
    binLen=len(e);
    for i in e:                                     #continue from the first binary digit (whcih is really the last) til the second to last
        if (i==0):
            result=(result*result)% m               #we always Square
        else:
            result=(result*result*b) % m            #we sometimes Multiply
    return result

def main():
    ans= raw_input("Do you wish to use the fast exponentiation calculator? (Y or N)\n")
    while(ans=='y' or ans=='Y'):
        base= int(raw_input("Please enter the base integer:\n"))
        exp=int(raw_input("Please enter the exponent\n"))
        mod=int(raw_input("Please enter the modulus\n"))
        print ("The result is :", SAM(base,exp,mod))
        ans= raw_input("Do you wish to use the fast exponentiation calculator? (Y or N)\n")
    print("Thank you for using the calculator\n")

if __name__== "__main__":
    main()
