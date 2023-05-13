from App import App
from MainRunner import MainRunner
from Const import GENERATIONS_TO_RUN

mainRunner = MainRunner([GENERATIONS_TO_RUN - 1])
generation_data = mainRunner.getGenerationData()


for i in range(len(generation_data)):
    print("Generation: ")
    App(generation_data[i][1], generation_data[i][0])



# Add combination of genes

