from App import App
from MainRunner import MainRunner

mainRunner = MainRunner([0])
generation_data = mainRunner.getGenerationData()


for i in range(len(generation_data)):
    print("Generation: ")
    App(generation_data[i][1], generation_data[i][0])




# Add visualization of best creatures
# Add combination of genes
# Add visualization of different generations

