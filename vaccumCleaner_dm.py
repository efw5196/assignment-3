import python_actr
from python_actr.lib import grid
from python_actr.actr import *
from AgentSupport import MotorModule, CleanSensorModule, MyCell
import AgentSupport
import random
import time

class VacuumAgent(python_actr.ACTR):
    goal = python_actr.Buffer()
    body = grid.Body()
    motorInst = MotorModule()
    cleanSensor = CleanSensorModule()
    retrieval = Buffer()
    DM_module = Memory(retrieval)

    def init(self):
        self.goal.set("start_recall_dirt")
        self.home = None

    # Save dirty cell to declarative memory before cleaning it
    def save_dirty_cell_to_dm(self, cleanSensor="dirty:True", body="loc_x:?x loc_y:?y", utility=0.9):
        self.DM_module.add(f"square:dirty location_x:{x} location_y:{y}")
        self.motorInst.clean()

    # Prioritize cleaning dirty squares saved in declarative memory
    def recall_dirty_spots_dm(self, goal="start_recall_dirt", DM_module="busy:False error:False", retrieval="square:dirty location_x:?x location_y:?y"):
        self.motorInst.go_towards(x, y)
        self.goal.set("start_recall_dirt")

    # If no dirty squares are in memory, then default to the swirl pattern
    def forward_rsearch(self, goal="rsearch left ?dist ?num_turns ?curr_dist",
                        motorInst="busy:False", body="ahead_cell.wall:False"):
        self.motorInst.go_forward()
        curr_dist = str(int(curr_dist) - 1)
        self.goal.set("rsearch left ?dist ?num_turns ?curr_dist")

    def left_rsearch(self, goal="rsearch left ?dist ?num_turns 0", motorInst="busy:False"):
        self.motorInst.turn_left(2)
        num_turns = str(int(num_turns) + 1)
        self.goal.set("rsearch left ?dist ?num_turns ?dist")


world = grid.World(MyCell, map=AgentSupport.mymap)
agent = VacuumAgent()
agent.home = ()
world.add(agent, 5, 5, dir=0, color="black")

python_actr.log_everything(agent, AgentSupport.my_log)
window = python_actr.display(world)
world.run()
time.sleep(1)
world.reset_map(MyCell, map=AgentSupport.mymap)
world.add(agent, 5, 5, dir=0, color="black")
world.run()
