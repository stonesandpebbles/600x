from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all possible 
    permutations of lengths 1 to HAND_SIZE.

    If all possible permutations are not in wordList, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    hand_len=0
    for i in hand:
        hand_len+=hand[i]
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score=0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word=None
    # For each word in the wordList
    for word in wordList:
        
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly

      
        #if len(hand)!=0:
       


        if isValidWord(word, hand, wordList):
            #print(word)
            score=getWordScore(word, hand_len)
            #if word=='appels' or word=='spale':
                #print(word+str(score))
            

            if score>max_score:
                max_score=score
                best_word=word[:]
    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    num_letters = calculateHandlen(hand)

    total = 0
   
    while True:
        
                  

        word = compChooseWord(hand, wordList)
        
        if word==None or len(hand)==0:
            break
        print("current hand:")
        displayHand(hand)         
        score=getWordScore(word,calculateHandlen(hand))

        total+=score

        print(word+" earned "+str(score)+" points Total:"+str(total))

        hand=updateHand(hand, word)
       
    print("Total score:"+str(total))
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand=None
    while True:
        
        user_input=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')

        while not (user_input=='r' or user_input=='n' or user_input=='e'):
            print("Invalid command")
            user_input=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
            if user_input=='e':
                break
    
        user_input2=raw_input('Enter u for user play and c for computer play:')
        
        while not (user_input2=='u' or user_input2=='c'):
            print("Invalid command")
            user_input2=raw_input('Enter u for user play and c for computer play:')

        if user_input=='n':

            hand=dealHand(HAND_SIZE)

            last_hand=hand.copy()

                      
        elif user_input=='r':

            if hand==None:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                hand=last_hand.copy()

                
        if user_input2=='u':

            playHand(hand, wordList, HAND_SIZE)

        elif user_input2=='c':
            compPlayHand(hand, wordList)

    

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()

    
    playGame(wordList)

    print "Goodbye!"
