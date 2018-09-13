"""
    Takes a file created by the tw_parse.py script
    and allows user to go line by line through the tweets
    annotating for clause type, speech act, location of emoji
"""


def try_input(input_text, acceptable_entries, tries=4):
    while True:
        attempt = input(input_text)
        if attempt in acceptable_entries:
            return attempt
        else:
            tries -= 1
            if tries <= 0:
                raise IOError('... too many unacceptable inputs')
            print(attempt, ' is not an okay tag')
            print('please enter an acceptable value from ', str(acceptable_entries))
            print(tries, 'tries left\n')


if __name__ == '__main__':
    
    with open('EMOTIONLESS_FACE_text.txt', 'annotations', encoding='utf-8') as text_input_file:
        text_input_file = text_input_file.readlines()
    
    index = 0
    
    clause_types = ['d', 'in', 'im', 'u']
    speech_acts = ['a', 'di', 'c', 'e', 'de', 'u']
    locations = ['i', 'ni', 'm', 'nf', 'fi']
    with open('EMOTIONLESS_FACE_annotations.txt', 'w', encoding='utf-8') as output_file:

        for line in text_input_file:
            # print tweet
            if index == 0:
                print(line)
                index += 1
            # skip user
            elif index == 1:
                index += 1
            # allow for input
            elif index == 2:
                """allow the user to annotate
                if user hits enter too early or wrong info
                let them try again without exiting on the error"""
                # declarative, interrogative, imperative, unknown
                clause_type = try_input("Clause-type: (d/in/im/u) ", clause_types)
                # assertive, directive, commissive, expressive, declaration, and unknown
                speech_act = try_input("Speech act: (a/di/c/e/de/u) ", speech_acts)
                # w.annotations.t. the anchor: initial, near initial, medial, near final, final
                location = try_input("Location: (i/ni/m/nf/fi) ", locations)
                # direction = input("Direction: (i/e/u) ")
                a = [clause_type, speech_act, location]
                output_file.write(str(a)+'\n')
                index = 0
                print()


