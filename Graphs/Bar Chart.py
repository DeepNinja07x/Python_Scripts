import matplotlib.pyplot as graphs

std_marks = [97,43,69,56,78]
test_no=[1,2,3,4,5]
# Use graphs.barh for horizontal bar graph
graphs.bar(test_no,std_marks,color = 'r',width = 0.4, edgecolor = 'y', linewidth = 2, yerr=1.5,
ecolor = 'g', alpha = 0.7)  # Align = "edge" -> for starting and ending at a value
graphs.xlabel("Test Number")
graphs.ylabel("Student Marks")
graphs.show()