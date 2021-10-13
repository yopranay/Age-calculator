def game():
    print('Answer the questions to know how long have you lived in this life...')
    name = input('Name:')
    print('What is your age?',(name),'?')
    age = int(input('Age:'))
    days = age*365
    minutes = age*525948
    seconds = age*31556926
    print (name,"has been alive for",days,'days',minutes,'minutes',seconds,'seconds')
    print('Thanks for using my simple program.')
def main():
    game()
    play_again()
def play_again():
  #while is a format of loop which will make the code running until the given value is false
    while True:
        retry = input("Would you like to play again?(yes or no) : ")
        if retry == "yes":
            main()
        if retry == "no":
          #just crashes the code
            exit()
        else:
            print("I'm sorry I could not recognize what you entered")
main()
