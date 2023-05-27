import hashlib;
import re;

print("For Generation of Hash of a Text Type: 'Hash' or 'H' or 'h'\n")
print("For Verification of a SHA256 Hash Type: 'Verify' or 'V' or 'v'\n")
print("Any other response will be considered as void by the system\n")

operationType = input('Select your operation- \n')

if ((operationType == 'Hash') or (operationType == 'H') or (operationType == 'h')) : 
    hashText = input('Enter the Text whose SHA256 Hash has to be generated- \n')

    hashValue = hashlib.sha256(hashText.encode('UTF-8'))

    print("The Hash Value for " + hashText + " is-  " + hashValue.hexdigest() +'\n')

elif ((operationType == 'Verify') or (operationType == 'V') or (operationType == 'v')) : 
    verifyText = input('Enter the hash to be verified- \n')

    hashRegex = re.search("^[0-9a-f]{64}$", verifyText)

    if hashRegex == None:
        print('The Hash entered is not a valid SHA256 Hash\n')

    else:
        print('The Hash Entered is valid\n')
        
else:
    print("None of the above two operations are selected. Run the code again to use the program")
