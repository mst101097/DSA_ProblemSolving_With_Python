'''
Monkey patching - In this proccess we can modify the code in run time 
like below example

'''

class test:
    def get_info(self, *args):
        print("Test data")
obj =test()
obj.get_info('2','4')
