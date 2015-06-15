import string

strippers = '…', '·', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '"', ',', '!', '.', ',', '‘', '’', '`', '~', '/', '+', '=', '|', '\c', '\n', '?', ';', ':', '_', '-', '¿', '»', '«', '¡', '©', '“', '”', 'º', '/', '\c'
spacers = '\n\n\n', '\n\n', '\n', '	', '      ', '     ', '    ', '   ', '  '


superList = str(open('shakespeare.txt', 'r', encoding='latin-1').read())
superList = superList.lower()
for each in strippers:
    superList = superList.replace(each, ' ')
for each in spacers:
    superList = superList.replace(each, ' ')
firstSpot = -1
click = "fuck"

while click == "fuck":
    firstSpot += 1
    try:
        secondSpot = firstSpot + 10
        snippet = superList[firstSpot:secondSpot]
        
        for int in range(1, 26):
            cLine = str()
            for each_chr in snippet:
                numLet = ord(each_chr)
                if numLet == 32:
                    numLet = 96
                #print('numLet1 = ', numLet)
                numLet += int
                if numLet > 122:
                    numLet -= 27
                elif numLet < 96:
                    numLet += 27
                if numLet == 96:
                    numLet = 32
                #print('numShift = ', numLet)
                cLine = cLine+(chr(numLet))
            #print('snippet = ', snippet, '| cLine = ', cLine)
            try:
                print(superList.index(cLine))
                print('winner! | @', int, '|',  snippet, '|', cLine)
            except ValueError:
                continue
    except IndexError:
        click == 'shit'

print('done')
