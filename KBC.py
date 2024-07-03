import random as rn
import time as tm

# Question list 
Qlist = [
    "Who is the director of S.H.I.E.L.D. at the beginning of the MCU?",
    "In which movie does Spider-Man first appear in the MCU?",
    "What is the name of Thor's hammer?",
    "Which Infinity Stone is hidden on Vormir?",
    "Who is the Winter Soldier?",
    "What is the real name of the superhero known as Black Panther?",
    "In 'Guardians of the Galaxy,' what is the name of Star-Lord's ship?",
    "What is the name of Tony Stark's AI assistant before he creates F.R.I.D.A.Y.?",
    "Who plays the character of Wanda Maximoff in the MCU?",
    "What planet is Thanos from?",
    "Which movie features the first appearance of Black Widow?",
    "What is the real name of the superhero known as Hawkeye?",
    "Which character is known for saying 'I am Groot'?",
    "Who is Peter Quill's father?",
    "Which actor plays Loki in the MCU?",
    "What is the name of Doctor Strange's mentor?",
    "What is the name of Ant-Man's daughter?",
    "Who is the main antagonist in 'Black Panther'?",
    "Which hero is also known as the Sorcerer Supreme?",
    "What is the name of Captain America's shield made from?",
    "Who is the ruler of the Dark Dimension?",
    "Which movie features the Battle of New York?",
    "What is the name of the AI that becomes Vision?",
    "Who is the younger sister of T'Challa?",
    "Which character does Benedict Cumberbatch play?",
    "What is the name of the kingdom Thor is from?",
    "Which movie introduced the character of Scarlet Witch?",
    "Who becomes the new Captain America after Steve Rogers?",
    "What is the name of the prison the Guardians of the Galaxy escape from?",
    "Who is the director of 'Guardians of the Galaxy'?",
    "Who is the voice of Rocket Raccoon?",
    "Which movie features the introduction of Captain Marvel?",
    "Who is the leader of the Dora Milaje?",
    "Which Avenger does Bruce Banner turn into?",
    "Who is the villain in 'Thor: Ragnarok'?",
    "What is the real name of Black Widow?",
    "Who plays the character of Iron Man?",
    "What type of doctor is Stephen Strange?",
    "What is the name of Peter Parker's best friend?",
    "Which Infinity Stone is housed in the Tesseract?",
    "Who is the father of Tony Stark?",
    "Which character wields the Darkhold in 'WandaVision'?",
    "What planet is the home of the Kree?",
    "Who plays the character of Captain America?",
    "What is the name of the Marvel comic legend who has cameo appearances in many MCU movies?",
    "Who is the first character to wield the Infinity Gauntlet in the MCU?",
    "Who is the leader of the Ravagers?",
    "Which character uses a weapon called the 'Yaka Arrow'?",
    "What is the name of the villain in 'Spider-Man: Homecoming'?",
    "Which Avenger has a prosthetic arm?",
    "Who is the AI that helps Peter Parker in his Spider-Man suit?"
]

#Answer list
Alist =[
    "Nick Fury",
    "Captain America: Civil War",
    "Mjölnir",
    "The Soul Stone",
    "Bucky Barnes",
    "T'Challa",
    "The Milano",
    "J.A.R.V.I.S.",
    "Elizabeth Olsen",
    "Titan",
    "Iron Man 2",
    "Clint Barton",
    "Groot",
    "Ego",
    "Tom Hiddleston",
    "The Ancient One",
    "Cassie",
    "Killmonger",
    "Doctor Strange",
    "Vibranium",
    "Dormammu",
    "The Avengers",
    "J.A.R.V.I.S.",
    "Shuri",
    "Doctor Strange",
    "Asgard",
    "Avengers: Age of Ultron",
    "Sam Wilson",
    "The Kyln",
    "James Gunn",
    "Bradley Cooper",
    "Captain Marvel",
    "Okoye",
    "The Hulk",
    "Hela",
    "Natasha Romanoff",
    "Robert Downey Jr.",
    "Neurosurgeon",
    "Ned Leeds",
    "The Space Stone",
    "Howard Stark",
    "Agatha Harkness",
    "Hala",
    "Chris Evans",
    "Stan Lee",
    "Thanos",
    "Yondu",
    "Yondu",
    "Vulture",
    "Winter Soldier",
    "Karen"
]

#Answer's Option list
options = [
    ["Nick Fury", "Phil Coulson", "Maria Hill", "Alexander Pierce"],
    ["Spider-Man: Homecoming", "Avengers: Age of Ultron", "Captain America: Civil War", "Ant-Man"],
    ["Stormbreaker", "Gungnir", "Mjölnir", "Aegis"],
    ["The Mind Stone", "The Reality Stone", "The Time Stone", "The Soul Stone"],
    ["Steve Rogers", "Sam Wilson", "Bucky Barnes", "Clint Barton"],
    ["T'Challa", "N'Jadaka", "M'Baku", "Zuri"],
    ["The Benatar", "The Milano", "The Eclector", "The Dark Aster"],
    ["J.A.R.V.I.S.", "H.O.M.E.R.", "U.L.T.R.O.N.", "F.R.I.D.A.Y."],
    ["Elizabeth Olsen", "Scarlett Johansson", "Brie Larson", "Karen Gillan"],
    ["Asgard", "Xandar", "Titan", "Krypton"],
    ["Iron Man 2", "The Avengers", "Captain America: The Winter Soldier", "Thor"],
    ["Clint Barton", "Phil Coulson", "Brock Rumlow", "Scott Lang"],
    ["Rocket Raccoon", "Groot", "Drax", "Gamora"],
    ["Ego", "Yondu", "Thanos", "Ronan"],
    ["Tom Hiddleston", "Chris Hemsworth", "Benedict Cumberbatch", "Paul Bettany"],
    ["The Ancient One", "Wong", "Mordo", "Kaecilius"],
    ["Cassie", "Hope", "Janet", "Natasha"],
    ["Killmonger", "Klaw", "M'Baku", "W'Kabi"],
    ["Doctor Strange", "The Ancient One", "Wong", "Mordo"],
    ["Vibranium", "Adamantium", "Uru", "Carbonadium"],
    ["Dormammu", "Thanos", "Loki", "Malekith"],
    ["The Avengers", "Avengers: Age of Ultron", "Avengers: Infinity War", "Avengers: Endgame"],
    ["J.A.R.V.I.S.", "F.R.I.D.A.Y.", "E.D.I.T.H.", "H.O.M.E.R."],
    ["Shuri", "Okoye", "Nakia", "Ramonda"],
    ["Doctor Strange", "Iron Man", "Star-Lord", "Thor"],
    ["Asgard", "Midgard", "Nidavellir", "Sakaar"],
    ["Avengers: Age of Ultron", "Captain America: The Winter Soldier", "Avengers: Infinity War", "Captain America: Civil War"],
    ["Sam Wilson", "Bucky Barnes", "Tony Stark", "Thor"],
    ["The Kyln", "The Raft", "The Vault", "The Cube"],
    ["James Gunn", "Jon Favreau", "Joss Whedon", "Taika Waititi"],
    ["Bradley Cooper", "Vin Diesel", "Dave Bautista", "Chris Pratt"],
    ["Avengers: Endgame", "Avengers: Infinity War", "Captain Marvel", "Thor: Ragnarok"],
    ["Okoye", "Shuri", "Nakia", "Ramonda"],
    ["The Hulk", "Iron Man", "Captain America", "Thor"],
    ["Hela", "Loki", "Thanos", "Malekith"],
    ["Natasha Romanoff", "Wanda Maximoff", "Pepper Potts", "Sharon Carter"],
    ["Robert Downey Jr.", "Chris Evans", "Chris Hemsworth", "Mark Ruffalo"],
    ["Neurosurgeon", "Cardiologist", "Oncologist", "Dermatologist"],
    ["Ned Leeds", "Harry Osborn", "Flash Thompson", "MJ"],
    ["The Space Stone", "The Power Stone", "The Mind Stone", "The Reality Stone"],
    ["Howard Stark", "Obadiah Stane", "Nick Fury", "Steve Rogers"],
    ["Agatha Harkness", "Wanda Maximoff", "Vision", "Monica Rambeau"],
    ["Hala", "Xandar", "Sakaar", "Titan"],
    ["Chris Evans", "Robert Downey Jr.", "Chris Hemsworth", "Mark Ruffalo"],
    ["Stan Lee", "Jack Kirby", "Steve Ditko", "Joe Simon"],
    ["Thanos", "Hulk", "Iron Man", "Thor"],
    ["Yondu", "Star-Lord", "Nebula", "Gamora"],
    ["Yondu", "Rocket", "Drax", "Groot"],
    ["Vulture", "Mysterio", "Doctor Octopus", "Green Goblin"],
    ["Winter Soldier", "War Machine", "Hawkeye", "Star-Lord"],
    ["Karen", "J.A.R.V.I.S.", "E.D.I.T.H.", "F.R.I.D.A.Y."]
]

Mlist = [1000,5000,10000,50000,120000,340000,680000,1320000,5000000,10000000]


abcd = ["A","B","C","D"]
randNumberList = []

#Function to show questions and there options
def showQuestion(randNumber):
    print("Q- ",Qlist[randNumber])
    for a in options[randNumber]:
        print(options[randNumber].index(a)+1, a)

def giveAnswer():
    a = int(input("Your Answer \n"))
    match(a):
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return 4
        case _:
            print("INVALID ENTRY!!! Try Again")
            giveAnswer()


winMoney = 0
#Entry point of program     
for a in range(1,11):
    randNumber = rn.randint(0,len(Qlist)-1)
    if(randNumber in randNumberList):
        # print("Number is Available in randNumberlist")
        print(randNumber)
        print("Question is repeated:- " , a)
    else:
        # print("Number is not available in randNumberlist")
        print("Question:-" , a ,"For ₹",Mlist[a-1])

        tm.sleep(3) #3 sec gap for every question

        showQuestion(randNumber) #function to show question from the question list and with corressponded option

        userSelectedOption = giveAnswer() #User answer function

        #match the option with the user selected option wheather it is right or not
        if(options[randNumber][userSelectedOption-1]==Alist[randNumber]):
            print("You won and you are mind blowing")
            winMoney += Mlist[a-1]
            print("*"*50,"Your Money :- ₹",winMoney)
        else:
            print("Hhyheee.... Chiii sasur")
            print("Right Answer is ",Alist[randNumber])
            print("You won:-",winMoney)
            break
       
    
    randNumberList.append(randNumber)
    

