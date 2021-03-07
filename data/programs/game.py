import time,random

def newHighScore(newhigh):
    with open("data\highscore.txt", "w") as file:
        file.write(str(newhigh))
    return newhigh

def highScore(newScore):
    with open("data\highscore.txt", "r") as file:
        content = file.read()
        if int(content)<int(newScore):
            return newHighScore(newScore)
        else:
            return int(content)


def present():
    with open(r"data\database\present.txt", "r") as file:
        content = file.read().split("\n")
        presentList = [
           content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
           content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
           content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)]
             ]
        element = presentList[random.randint(0,8)]
        return (presentList,element)

def notPresent():
    with open(r"data\database\notpresent.txt","r") as file:
        content = file.read().split("\n")
        notPresentList = [
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
             ]
        obj = present()

        presentList,element = obj[0],obj[1]
        print("\nRemember these names . You have only 10 sec to answer.\n")
        
        for i in range(len(presentList)):
            a=presentList[i]
            print(a+(10-len(a))*" ", end="     ")
            if ((i+1)%3==0):
                print("\n")
                    
        print("\n")
        notPresentList.insert(random.randint(0,8),element)
        time.sleep(10)
        for i in range(10):
            print("\n")
        return (notPresentList,element)
            
score = 0

while True:
    print("\n")
    print("...........Game Starting........\n")
    time.sleep(2)
    print('Lets go...\n')

    time.sleep(2)
    print("Ready for test.\n")

    obj = notPresent()
    notPresentList,element = obj[0],obj[1]

    for i in range(len(notPresentList)):
        a=notPresentList[i]
        print(a+(10-len(a))*" ", end="     ")
        if ((i+1)%3==0):
            print("\n")
    for i in range(5):
        print("\n")
        
    word = input("\n\n Which word is common in both lists:")
        
    if word==element:
        score+=1
    else:
        score-=1

    print("Your score is:",score)

    ch = input("Do you want to continue(y/n):")
    if ch != "y":
        
        print("high score till now is:",highScore(score))
        time.sleep(5)
        break
        
