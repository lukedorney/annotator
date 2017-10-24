import ast
"""takes a set of -r files from annotatory.py, which contain the annotations,
and compute statistics on the model, prints results to the console"""
#examples
f1 = open('FACE_WITH_TEARS_OF_JOY-r.txt','r')
f2 = open('FACE_WITHOUT_MOUTH-r.txt','r')
f3 = open('SMILING_FACE_WITH_OPEN_MOUTH_AND_COLD_SWEAT-r.txt','r')
f4 = open('SMIRKING_FACE-r.txt','r')
f5 = open('UPSIDE_DOWN_FACE-r.txt','r')
f6 = open('WEARY_FACE-r.txt','r')

index = 0
r = []
#set this to the number files your actually using
while index < 6:
    if index == 0:
        data = ast.literal_eval(f1.readline())
        #print(str(data))
        r.append(data)
        index +=1
    elif index ==1:
        data = ast.literal_eval(f2.readline())
        r.append(data)
        index +=1
    elif index ==2:
        data = ast.literal_eval(f3.readline())
        r.append(data)
        index +=1
    elif index ==3:
        data = ast.literal_eval(f4.readline())
        r.append(data)
        index +=1
    elif index ==4:
        data = ast.literal_eval(f5.readline())
        r.append(data)
        index +=1
    elif index ==5:
        data = ast.literal_eval(f6.readline())
        r.append(data)
        index +=1

#print(str(r))

declarative = 0
interogative = 0
imperative = 0
undefined_clause = 0

assertive = 0
directive = 0
commissive = 0
expressive = 0
declaration = 0
undefined_sa = 0

initial = 0
n_initial = 0
medial = 0
n_final = 0
final = 0

count = 0
for group in r:
    for tweet in group:
        x = 0
        for annotation in tweet:
            if x == 0:
                if annotation == 'd':
                    declarative+=1
                elif annotation == 'in':
                    interogative+=1
                elif annotation == 'im':
                    imperative+=1
                else:
                    undefined_clause+=1
                x+=1 
            elif x==1:
                if annotation == 'a':
                    assertive+=1
                elif annotation =='di':
                    directive+=1
                elif annotation =='c':
                    commissive+=1
                elif annotation =='e':
                    expressive+=1
                elif annotation =='de':
                    declaration +=1
                else:
                    undefined_sa +=1
                x+=1
            elif x==2:
                if annotation =='i':
                    initial+=1
                elif annotation =='ni':
                    n_initial+=1
                elif annotation =='m':
                    medial +=1
                elif annotation =='nf':
                    n_final +=1
                elif annotation =='f':
                    final +=1
                else:
                    continue
                x+=1
            else:
                continue
        count +=1

print(str(count))
print("Clause count: declarative = "+str(declarative)+", interogative = "+str(interogative)+", imperative = " +str(imperative)+", undefined = "+str(undefined_clause))
print('Speech act count: assertive= '+str(assertive)+', directive= '+str(directive)+", commissive= "+str(commissive)+', expressive= '+str(expressive)+', declaration= '+str(declaration)+', undefined= '+str(undefined_sa))
print('Location count: initial= '+str(initial)+', near initial= '+str(n_initial)+', medial= '+str(medial)+', near final= '+str(n_final)+', final= '+str(final))
