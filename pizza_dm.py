import python_actr
from python_actr.actr import *
from python_actr.actr.hdm import *

class PizzaBuilder_DM(ACTR):
    goal = Buffer()
    retrieval = Buffer()
    DM_module = HDM(retrieval, finst_size=22, finst_time=100.0)
    my_pizza = ["crust"]

    def cook_pizza(self, pizza_ingred):
        return ("_".join(pizza_ingred))

    def init(self):
        # Add memory chunks for pizza steps
        self.DM_module.add("prev:crust next:marinara")
        self.DM_module.add("prev:marinara next:mozzarella")
        self.DM_module.add("prev:mozzarella next:pepperoni")
        self.DM_module.add("prev:pepperoni next:onion")
        self.DM_module.add("prev:crust next:bbq")
        self.DM_module.add("prev:bbq next:cheddar")
        self.DM_module.add("prev:cheddar next:bacon")
        self.DM_module.add("prev:bacon next:onion")
        
        # Set initial goal
        self.goal.set("build_pizza")
        self.wait(0.05)  # Simulate a brief delay

    def build_pizza_step(self, goal="build_pizza", retrieval="prev:?last_ingredient next:?next_ingredient"):
        if next_ingredient not in self.my_pizza:
            print(f"Adding {next_ingredient} to the pizza...")
            self.my_pizza.append(next_ingredient)
            self.DM_module.request(f"prev:{next_ingredient} next:?new_ingredient")
            self.wait(0.05)  # Simulate a brief delay
        else:
            self.goal.set("cook_pizza")

    def end_pizza(self, goal="cook_pizza"):
        print("Cooking the pizza...")
        self.wait(1)  # Simulate the cooking time
        final_pizza = self.cook_pizza(self.my_pizza)
        print(f"Mmmmmm my {final_pizza} pizza is gooooood!")
        self.stop()

    def request_next_ingredient(self, goal="build_pizza"):
        last_ingredient = self.my_pizza[-1]
        self.DM_module.request(f"prev:{last_ingredient} next:?next_ingredient")
        self.wait(0.05)  # Simulate a brief delay

class EmptyEnvironment(python_actr.Model):
    pass

env_name = EmptyEnvironment()
agent_name = PizzaBuilder_DM()
env_name.agent = agent_name
python_actr.log_everything(env_name)
env_name.run()
