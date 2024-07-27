import json
import os
class User():
    def __init__(self, userID: str, path: str):
        self.userID = userID
        self.path = path
        self.session = {}

        self.curent_preset = 'Основы'
        self.curent_task = 1
        self.solved_tasks = {'Основы': {}, 'Условный оператор': {}}


        self.readJSON()


    def readJSON(self):
        if not os.path.exists(self.path):
            self.writeJSON()
        else:
            try:
                with open(f'{self.path}', 'r') as f:
                    self.session = json.load(f)
                    self.curent_preset = self.session['curent_preset']
                    self.curent_task = self.session['curent_task']
                    self.solved_tasks = self.session['solved_tasks']
            except Exception as e:
                print(f'Error {e}')
                

    def writeJSON(self):
        with open(f'{self.path}', 'w') as f:
            self.session['curent_preset'] = self.curent_preset
            self.session['curent_task'] = self.curent_task
            self.session['solved_tasks'] = self.solved_tasks
            json.dump(f, self.session)