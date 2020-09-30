import matplotlib.pyplot as graph

subject = ["Probability", "Calculas", "Discrete Mathematics", "Adv Engineering Mathematics", 
"Linear Algebra", "Cryptography"]

weightage = [250,900,850,1200,290,345]

seperator = [0.05,0,0,0,0.05,0.05]

graph.title("Mathematics Topic Weightage")
graph.pie(weightage,labels=subject,autopct="%0.1f%%", explode=seperator)
graph.show()