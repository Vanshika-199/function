str="The quick Brown Fox"
def count(str):
    lower=0
    upper=0
    for i in str:
        if (i>='a'and i<='z'):
            lower=lower+1                 
        if (i>='A'and i<='Z'):
            upper=upper+1            
    print('Lower case characters: ',lower)
    print('Upper case characters: ',upper)
count(str)

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

