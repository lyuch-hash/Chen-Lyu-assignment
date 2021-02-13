# Your name: chen lyu
# Your student id:62850933
# Your email:lyuch@umich.edu
# List who you have worked with on this homework:no one


# import the random module for use in this program
import random

# Create the class Magic_8
class Magic_8:

    # create the constructor (__init__) method
    # it takes as input: a list of possible answers
    # it sets this object's answer_list (instance variable) to the passed list of possible answers
    # it sets this object's question_list (instance variable) to the an empty list
    # it sets this object's answer_history_list (instance variable) to an empty list 
    def __init__(self, lst):
        self.answer_list=lst
        self.question_list=list()
        self.answer_history_list=list()

    def __str__(self):
        string=str()
        for i in range(len(self.answer_list)):
            string=string+", "+self.answer_list[i]
        string=string[2:]
        return string

    
    def shake_ball(self):
        a=random.randint(0,len(self.answer_list)-1)
        self.answer_history_list.append(a)
        return self.answer_list[a]
    
    def check_question(self,question):
        if question in self.question_list:
            return 'I already answered that question!'
        else:
            self.question_list.append(question)
            return self.shake_ball()
    
    def print_history(self):
        
        
            if len(self.answer_history_list)!=0:
                for i in range(len(self.answer_history_list)):
                   print("["+str(i+1)+"]"+" "+self.question_list[i]+" - "+self.answer_list[self.answer_history_list[i]])
            else:
              print("None yet")
     
    def generate_n_responses(self,num):
        dic=dict()
        self.answer_history_list.clear()
        for i in range(num):
          self.shake_ball()
        for i in range(num):
          dic[self.answer_history_list[i]]=dic.get(self.answer_history_list[i],0)+1
        count=0
        item=0
        
        for a,b in dic.items():
            if a>count:
                count=a
                item=b
            
           
        print("longest run was length of "+str(b)+"for index "+str(a)) 
         
        
    # create the shake_ball method
    # it randomly picks an index from 0 to the number of items in the answer_list minus one
    # it adds that index to the end of the answer_history_list
    # it returns the answer at the picked index

    # create the check_question method that takes a question
    # it checks if the question is in the question_list and if so returns 
    #         "I already answered that question!”
    # Otherwise it adds the question to the question_list and
    # returns the answer from shake_ball

    # create the print_history method
    # prints "[answer index] question - answer" for each of the indices in the answer_history_list
    # from the first to the last with each on a single line.  If there are not items in the 
    # answer_history_list it prints "None yet"
    # it does not return anything!
            
    # EXTRA POINTS
    # create the generate_n_responses method
    # it takes as input:
    #    a number, n. Ex: 200
    # it generates a random response n times by calling shake_ball
    # then returns the index and length of the longest consecutive run
    # It should reset the answer_history_list to an empty list first. 
    # A run is a repetition of the same number consecutively in a list.
    # Ex: If 10 random answers are  [1,5,6,3,2,4,1,4,4,4] then three 4's is the longest run
    # hence the function should return "longest run was length of 3 for index 4
    

def main():

    # You are welcome to replace the answer_list with your desired answers
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Magic_8(answer_list)

    # get the first question or quit

    # loop while question is not "quit"
   
        # get an answer from check_question

        # print question - answer

        # get the next question or quit 

def test():
    
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Magic 8 Ball:")
    bot2 = Magic_8(answer_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_history()
    print()

    print("Asking the Question: Am I hungry?")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Am I hungry? again")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Should I go for a walk?")
    print(bot2.check_question("Should I go for a walk"))
    print()

    print("Printing the history")
    bot2.print_history()
    print()
    
    
    print("Testing generate_n_responses method with 200 responses")
    print(bot2.generate_n_responses(200))


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() 


