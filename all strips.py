#this is lstrip function
def lstrip(str1):
    index=-1
    for i in str1:
        if i ==" ":
            index += 1
            continue
        else: 
            index += 1
            break
    return str1[index:] 


#this is rstrip function
def rstrip(str2):

    str3 = str2[::-1]
    index=0
    for i in str3:
        if i ==" ":
            index+=1
            continue
        else: 
            break
    str4 = str3[index:]         
    return str4[::-1]

#this is strip function
def strip(str5):
    n=rstrip(str5)
    a=lstrip(n)
    return a