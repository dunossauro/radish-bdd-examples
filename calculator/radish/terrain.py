from sys import path
from radish import before, after

# relative imports broke E402, C0413
# you can use PYTHONPATH too
path.append('./calculator/calc')
import calculator


@before.each_scenario
def init_calculator(scenario):
    scenario.context.calculator = calculator


@after.each_scenario
def destory_calculator(scenario):
    del scenario.context.calculator
