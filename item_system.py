
a = ['sd', 'sdf', 'sf']

for i in range(len(a)):
    print(a[i])


def answer_response(Statements: list, Options: list):
    global Choices
    if Statements[0] != '':
        for i in range(len(Statements)):
            print(Statements[i])
        if Options[0] != '': 
            if len(Options) == 1:
                input(Options)
            else:
                Choices = input(f"{'|'.join(Options)}: ").lower()
                while Choices not in Options:
                    Choices = input(f"{'|'.join(Options)}: ").lower()
                else:
                    return
        


    
