import string

strippers = '…', '·', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '"', ',', '!', '.', ',', '‘', '’', '`', '~', '/', '+', '=', '|', '\c', '\n', '?', ';', ':', '_', '-', '¿', '»', '«', '¡', '©', '“', '”', 'º', '/', '\c'
spacers = '\n\n\n', '\n\n', '\n', '	', '      ', '     ', '    ', '   ', '  '


superList = str(open('englishAllList.txt', 'r', encoding='latin-1').read())
superList = superList.lower()
for each in strippers:
    superList = superList.replace(each, ' ')
for each in spacers:
    superList = superList.replace(each, ' ')
superLib = superList.split(' ')
for all in range(0, 10):
    print(superLib[all])

checkLib = []
for all in superLib:
    checkLib.append(all)

hitsLib = {}
    
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
                #print('@=', shifter, " | ", pWord, ' & ', all, '\n')
                try:
                    hitsLib[pWord].append(cWord+'@'+str(int))
                except KeyError:
                    hitsLib[pWord] = cWord+'@'+str(int) 
                    continue
                
dicFile = csv.writer(open("cWords-hitsLib", "w", encoding='latin-1'))
for key, val in hitsLib.items():
    svWords = str()
    for each in hitsLib[key]:              
        svWords = svWords + each + '^'
    val = svWords
    dicFile.writerow([key, val])    

print('/that business')
