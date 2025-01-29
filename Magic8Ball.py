#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["As I see it, yes." , "Ask again later." , "Better not tell you now." , "Cannot predict now." , 
           "Concentrate and ask again." , "Dont count on it." , "It is certain." , "It is decidedly so." , 
           "Most likely." , "My reply is no." , "My sources say no."]

  #Answer question randomly with one of the options from your earlier list.
  question = input("Ask me a question:")
  num = random.random() 
  num = num * 1000
  num = int(num)
  num = num % 11
  print(answers[num])



if __name__ == '__main__':
  main()
