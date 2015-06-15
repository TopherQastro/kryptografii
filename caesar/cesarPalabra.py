import string

strippers = '…', '·', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '"', ',', '!', '.', ',', '‘', '’', '`', '~', '/', '+', '=', '|', '\c', '\n', '?', ';', ':', '_', '-', '¿', '»', '«', '¡', '©', '“', '”', 'º', '/', '\c'
spacers = '\n\n\n', '\n\n', '\n', '	', '      ', '     ', '    ', '   ', '  '
vow = 'a', 'e', 'i', 'o', 'u', 'y', 'â', 'ê', 'è', 'ô', 'à', 'è', 'î', 'ã', 'ë', 'ö', 'õ'
accVow = 'á', 'é', 'ó', 'í', 'ú'
allVow = 'y', 'a', 'e', 'i', 'o', 'u', 'ü', 'á', 'é', 'ó', 'í', 'ú', 'â', 'ê', 'è', 'ô', 'ö', 'õ', 'à', 'è', 'î', 'ã', 'ë'
empPat1 = 's', 'n', 'a', 'e', 'i', 'o', 'u', 'y'
cons = 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'ñ'
strippers = '…', '·', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '"', ',', '!', '.', ',', '‘', '’', '`', '~', '/', '+', '=', '|', '\c', '\n', '?', ';', ':', '_', '-', '¿', '»', '«', '¡', '©', '“', '”', 'º', '/', '\c'
spacers = '\n\n\n', '\n\n', '\n', '    ', '      ', '     ', '    ', '   ', '  '
caps =  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ü', 


text = str(open('__txtBiblioteca/es-ES.txt', 'r', encoding='latin-1').read())
 
masterLPop = text.split('\n')
indexList = []
zCt =  0

for each in masterLPop:
    each.lower()
    each.replace('\n', '')
    each.replace(' ', '')
    zCt =  0
    if len(each) == 0:
        indexList.append(each)
    for all in caps:
        try:
            each.index(all)
            indexList.append(each)
            #print('swallowing=', each)
        except ValueError:
            continue
for all in indexList:
    #print('removing=', all)
    zCt += 1
    #print('zCt=', zCt)
    try:
        masterLPop.remove(all)
        #print('snag')
    except ValueError:
        #print('GONEAGE=', each)
        continue

checkLib = []
for all in masterLPop:
    checkLib.append(all)

hitsLib = {}
    
for int in range(1, 26):
    shifter = int
    for each in masterLPop:
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
                
dicFile = csv.writer(open("cWords-hitsLib.csv", "w", encoding='latin-1'))
for key, val in hitsLib.items():
    svWords = str()
    for each in hitsLib[key]:              
        svWords = svWords + each + '^'
    val = svWords
    dicFile.writerow([key, val])    

print('/that business')
