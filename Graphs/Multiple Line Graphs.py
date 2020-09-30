import matplotlib.pyplot as graphs

Halflife = [10,20,30,40,50,60,70,80,90,100]
Halflife2 = [10,20,30,40,50,60,70,80,90,100]

Halflife_difficulty = [10,25,34,17,48,56,67,54,87,64]
Halflife2_difficulty = [5,15,27,54,62,65,47,84,68,48]

graphs.xlabel("Game Progress %")
graphs.ylabel("Game Difficulty")
graphs.title("Half Life and Half Life 2 Difficulty Comparison")

graphs.plot(Halflife,Halflife_difficulty,color='r',label = "Half Life")
graphs.plot(Halflife2,Halflife2_difficulty,color='b', label = "Half Life 2")
graphs.legend()
graphs.show()