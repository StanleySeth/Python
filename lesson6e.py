#On the try and except block: You crun some codes/statements and if it is successful the try block will get executed other the excepet block will be executed when there is an anticipated error.



try:
    number = 100 / 0
    answer = number / 0
    print("The answer is: ",answer)
except Exception as e:
    print("There is an error: ",e)