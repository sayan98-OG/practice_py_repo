def word_wrap(words :list, length):
    l = words
    mlength = length
    newlst = []
    w=''

    for i in l:

        if len(w)==0:
            w=i
        elif len(i)+len(w)+1<=mlength:
            w=w+'-'+i
        else :
            newlst.append(w)
            w=i
    if len(w)>0:
        newlst.append(w) 
    return newlst

words1 = [ "The", "day", "began", "as", "still", "as", "the", "night", "abruptly", "lighted", "with", "brilliant", "flame" ]

print(word_wrap(words1, 20))