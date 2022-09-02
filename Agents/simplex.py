import random

class Environment(object):
    def __init__(self):
        self.locationCondition = {'A': '0', 'B': '0'}
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)

class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print (Environment.locationCondition)
        Score = 0
        vacuumLocation = random.randint(0, 1)
        if vacuumLocation == 0:
            print ("Vacuum is randomly placed at Location A.")
            if Environment.locationCondition['A'] == 1:
                print ("Location A is Dirty.") 
            else: 
                print("Location A is Clean.")

            if Environment.locationCondition['A'] == 1:
                Environment.locationCondition['A'] = 0
                Score += 1
                print ("Location A has been Cleaned.") 
            print ("Moving to Location B...")

            if Environment.locationCondition['B'] == 1:
                print ("Location B is Dirty.") 
            else:
                print("Location B is Clean.")

            if Environment.locationCondition['B'] == 1:
                Environment.locationCondition['B'] = 0;
                Score += 1
                print ("Location B has been Cleaned.")
            print("Environment is Clean.")
                
        elif vacuumLocation == 1:
            print ("Vacuum randomly placed at Location B.")
            if Environment.locationCondition['B'] == 1:
                print ("Location B is Dirty.") 
            else:
                print("Location B is Clean.")

            if Environment.locationCondition['B'] == 1:
                Environment.locationCondition['B'] = 0
                Score += 1
                print ("Location B has been Cleaned.")
            print ("Moving to Location A...")

            if Environment.locationCondition['A'] == 1:
                print ("Location A is Dirty.") 
            else:
                print("Location A is Clean.")

            if Environment.locationCondition['A'] == 1:
                Environment.locationCondition['A'] = 0;
                Score += 1
                print ("Location A has been Cleaned.")
            print("Environment is Clean.")    
            
        print (Environment.locationCondition)
        print ("Performance Measurement: " + str(Score))
        print("\n")

if __name__ == '__main__':
    i = 0
    while i<2:
        theEnvironment = Environment()
        theVacuum = SimpleReflexVacuumAgent(theEnvironment)
        i+=1