import datetime

class Item(object):
    def __init__(self, complete, action):
        self.complete = complete
        self.action = action

    def compile(self,complete, action):
        task = []
        now = datetime.date.today()
        task.append(now)
        task.append(complete)
        task.append(action)
        file = open('todos.txt', 'w')
        file.write(f'[{now},{complete},{action}]')
        file.close()
