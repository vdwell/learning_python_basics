
final_text = ''

def process_text(mytext):
    question_words = ['How', 'Where', 'When', 'Who', 'Will', 'Would']
    flag1 = False
    mytext = mytext.title()
    for qword in question_words:
        if mytext.startswith(qword):
            flag1 = True
            mytext = mytext + '?'
    if flag1 == False:
        mytext = mytext + '.'
    return(mytext)

while True:
    user_input = input('Say something: ')
    if user_input == "\end":
        break
    else:
        processed_user_input = process_text(user_input)
        final_text = final_text + ' ' + processed_user_input        
        continue

print(final_text)