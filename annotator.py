"""
    Takes a file created by the tw-parse script
    and allows user to go line by line through the tweets
    annotating for clause type, speech act, location of emoji
"""
f = open('EXPRESSIONLESS_FACE-t.txt','r')
o = open('EXPRESSIONLESS_FACE-r.txt','w')

index = 0

for line in f.readlines():
    #print tweet
    if index == 0:
        print(line)
        index+=1
    #skip user
    elif index == 1:
        index+=1
    #allow for input
    elif index == 2:
        """allow the user to annotate
        if user hits enter too early or wrong info
        let them try again without exiting on the error"""
        try:
            #declarative, interrogative, imperative, unknown
            clause_type = input("Clause-type: (d/in/im/u) ")
            #assertive, directive, commissive, expressive, declaration, and unknown
            speech_act = input("Speech act: (a/di/c/e/de/u) ")
            #w.r.t. the anchor: intitial, near initial, medial, near final, final
            location = input("Location: (i/ni/m/nf/f) ")
            #direction = input("Direction: (i/e/u) ")
            a = [clause_type,speech_act,location]
            o.write(str(a))
            index+=1
        except:
            clause_type = input("Clause-type: (d/in/im/u) ")
            speech_act = input("Speech act: (a/di/c/e/de/u) ")
            location = input("Location: (i/ni/m/nf/f) ")
            #direction = input("Direction: (i/e/s/u) ")
            a = [clause_type,speech_act,location]
            index+=1
    #skip \n
    elif index == 3:
        index +=1
    #start over for next tweet
    elif index == 4:
        index = 0

o.close()
