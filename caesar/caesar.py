import string

superList = str(open('lexiLib.txt', 'r', encoding='latin-1').read())
superLib = superList.split(' ')

bLWordStr = str(open('blackWordList.txt', 'r+', encoding='latin-1').read())
bLWords = bLWordStr.split(' ')
for all in bLWords:
    try:
        superList = superLib.remove(all)
    except ValueError:
        continue
print('blackList screened')

checkLib = []
for all in superLib:
    checkLib.append(all)
    
for int in range(1, 26):
    shifter = int
    for each in superLib:
        cWord = str()
        pWord = each
        for each_chr in pWord:
            numLet = ord(each_chr)
            numLet += shifter
##        while (numLet > 122) or (numLet < 97):
##            if numLet > 122:
##                numLet -= 26
##            elif numLet < 97:
##                numLet += 26
            cWord = cWord+(chr(numLet))
##        print('pWord = ', each, '| cWord = ', cWord) 
        for all in checkLib:
            #print(all)
            if (cWord == all):
                print('\n@=', shifter, " | ", pWord, ' & ', all, '\n')       
                
    


