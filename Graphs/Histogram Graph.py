import matplotlib.pyplot as graph

boys_marks = [70,43,56,91,76,64,71,83,41,76,56,64,64]
girls_marks = [91,83,65,92,54,78,82,59,96,99,100,56]
# Using bins to set range between them. You can also use bins = 3 -> creates 3 divisions.
# You can also use bins and set range -> bins=[45,55,65,70,80,85,95,100]
graph.hist ([boys_marks,girls_marks], bins=[40,50,60,70,80,90,100],
rwidth=0.90, color = ['r','b'], label=["Boys","Girls"])
graph.title("Comparison between scores of boys and girls in a test")
graph.legend()
graph.xlabel("Marks")
graph.ylabel("Number of Students")
graph.show()