
import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []

        for key, value in balls.items():
            for i in range(value):
                self.contents.append(key)
        
    def draw(self, number_drawn):
        drawn = []
        
        if number_drawn > len(self.contents):
            drawn = self.contents
            self.contents = []
            return drawn
        
        else:
            for i in range(number_drawn):
                index = random.randrange(len(self.contents))

                drawn.append(self.contents[index])
                self.contents.pop(index)

        return drawn
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0

    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn_list = new_hat.draw(num_balls_drawn)

        count_colour = 0

        for j in expected_balls.keys():
            if drawn_list.count(j) >= expected_balls[j]:
                count_colour += 1

        if count_colour == len(expected_balls):
            count += 1

    
    return count / num_experiments
