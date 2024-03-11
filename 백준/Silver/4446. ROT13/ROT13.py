
vowel = 'a i y e o u'.split(' ')
consonant = 'b k x z n h d c w g p v j q t s r l m f'.split(' ')

while True:
    try:
        rot13 = input()
        result = ''
        for q in rot13:
            
            if not q.isalpha():
                result += q
                continue
            check = 0
            if q.isupper():
                q = q.lower()
                check = 1
            
            if q in vowel:
                result += vowel[(vowel.index(q)+3) %len(vowel)].upper() if check else vowel[(vowel.index(q)+3) %len(vowel)]
            
            else:
                result += consonant[(consonant.index(q)+10) %len(consonant)].upper() if check else consonant[(consonant.index(q)+10) %len(consonant)]
            
        print(result)
    
    except:
        break