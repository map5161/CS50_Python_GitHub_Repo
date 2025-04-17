def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

###################################
def is_valid(s):
    if two_letters(s):
        if max_min(s):
            if middle_check(s):
                if punctuation(s):
                    return True
    return False

####################################
def max_min(maxmin):
    length = len(maxmin)
    if length >=2 and length <= 6:
        return True
    
####################################
#def two_letters(two):
#    if max_min(two):
#        first = two[0]
#        second = two[1]
#        if first.isalpha():
#            if second.isalpha():
#                return True
#    else:
#        return False    


####################################
def two_letters(two):
    if max_min(two):
        return two[0].isalpha() and two[1].isalpha()  
    
####################################
def middle_check(middle):
     
     if len(middle) >= 3:
        zero_check = middle[2]
        if zero_check == "0":
            return False
     
     if middle.isalpha():
         return True
     else:
        for m in middle:
            l = len(middle)
            if m.isnumeric():
                x = middle.index(m)
                break

        first_slice = middle[0:x]
        second_slice = middle [x:l]

        flag = "valid"

        for s in second_slice:
            if s.isalpha():
                return False
        return True
         

        #for s in second_slice:
        #    if s.isalpha():
        #        flag = "invalid"
        #        break
            
        #if flag is "valid":
        #    return True
        

##################################
#def punctuation(punct):
#    omit_list = [" ", ".", ","]
#    flag = "valid"
#    for p in punct:
#        if p in omit_list:
#            flag = "invalid"
#            break
    
#    if flag == "valid":
#        return True
    
#############################

def punctuation(punct):
    omit_list = [" ", ".", ","]
    for p in punct:
        if p in omit_list:
            return False
    return True


main()