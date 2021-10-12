import random
def create(qn):
    modified_qn=[]
    ques=list(qn)
    for i in range(len(ques)):
        if ques[i]==' ':
            modified_qn.append(' ')
        else:
            modified_qn.append('*')
    t=' '.join(str(x) for x in modified_qn)
    return t

def is_present(letter,qn):
    c=qn.count(letter)
    if c==0:
        return False
    else:
        return True


def unlock(modified_qn,qn,letter):
    temp=[]
    word=list(qn)
    picked_word=list(modified_qn)
    for i in range(len(word)):
        if word[i]==' ' or word[i]== letter:
            temp.append(word[i])
        elif picked_word[i]!='*' and picked_word[i]!=' ':
            temp.append(picked_word[i])
        else:
            temp.append('*')
    q=''.join(str(x) for x in temp)
    return q



def play():
    # importing the module
    import imdb

    # creating instance of IMDb
    ia = imdb.IMDb()

    # getting top 250 movies
    search = ia.get_top250_movies()
    search2 = ia.get_popular100_movies()
    # print(search)
    movies = ["3 idiots","taare zameen par","fanaa","ajab prem ki gajab kahani","half girlfriend"]
    for i in range(250):
        movies.append(search[i]['title'])
    for i in range(100):
        movies.append(search2[i]['title'])
    #print(movies)
    print("\nRULES :-\n1)For every question 10 marks is allocated\n2)For every iteration of guessing letter or movie name reducess your points by 0.5")
    p1name = input("\n\nPlayer 1, Enter your name: ")
    p2name = input("Player 2, Enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = -1
    game = 1
    while (game):
        turn = turn + 1
        marks = -0.5
        if turn % 2 == 0:
            qn = random.choice(movies)
            #print(qn)
            qn=qn.lower()
            modified_qn = create(qn)
            print("\n\nHey", p1name, "guess the movie name:\n", modified_qn)
            not_said = True
            while (not_said):
                marks=marks+0.5
                if marks==10:
                    print("Sorry your turn is over, too many attempts\nAnswer is - ",qn)
                    game=False
                    not_said=False
                    break
                ch = int(input("Enter 1 to guess the movie and 2 to unlock the letters and 3 to quit and reveal the answer"))
                while ch!=1 and ch!=2 and ch!=3:
                    print("Wrong input,try again")
                    ch = int(input("Enter 1 to guess the movie and 2 to unlock the letters and 3 to quit and reveal the answer"))
                if ch == 1:
                    name = input("Guess the movie")
                    name=name.lower()
                    if name == qn:
                        pp1 = pp1 + (10 - marks)
                        print("Well done, Correct Answer and your score is:", pp1)
                        not_said = False
                    else:
                        print("Nope, Wrong answer")
                if ch == 2:
                    letter = input("Enter the letter")
                    letter=letter.lower()
                    if(is_present(letter,qn)):
                        modified_qn = unlock(modified_qn, qn,letter)
                    else:
                        print("Letter not present")
                    print(modified_qn)
                if ch==3:
                    print("Answer is:- ",qn)
                    break;

            d=input("Enter 0 to exit, any other key to continue\n")
            if d=='0':
                print("Thank You for playing")
                print(p1name," your score is ",pp1)
                print(p2name, " your score is ", pp2)
                game= False
            else:
                continue

        else:
            qn = random.choice(movies)
            #print(qn)
            qn = qn.lower()
            modified_qn = create(qn)
            print("Hey", p2name, "guess the movie name:\n", modified_qn)
            not_said = True
            while (not_said):
                marks = marks + 0.5
                ch = int(input("Enter 1 to guess the movie and 2 to unlock the letters and 3 to quit and reveal the answer"))
                while ch!=1 and ch!=2 and ch!=3:
                    print("Wrong input, Try again")
                    ch = int(input("Enter 1 to guess the movie and 2 to unlock the letters and 3 to quit and reveal the answer"))

                if ch == 1:
                    name = input("Guess the movie")
                    name=name.lower()
                    if name == qn:
                        pp2 = pp2 + (10 - marks)
                        print("Well done, Correct Answer and your score is:", pp2)
                        not_said = False
                    else:
                        print("Nope, Wrong answer, try guessing letters")
                if ch == 2:
                    letter = input("Enter the letter")
                    if (is_present(letter, qn)):
                        modified_qn = unlock(modified_qn, qn, letter)
                    else:
                        print("Letter not present")
                    print(modified_qn)
                if ch==3:
                    print("Answer is :-",qn)
                    break;
            d = (input("Enter 0 to exit, any other key to continue"))
            if d == '0':
                print("Thank You for playing")
                print(p2name, " your score is ", pp2)
                print(p1name, " your score is ", pp1)
                game = False




play()
