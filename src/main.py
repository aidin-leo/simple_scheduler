import time


class Task:
    def __init__(self, name, t, f):
        self.name = name
        self.t = t
        self.f = f

    def run(self):
        print('starting:', self.name)
        self.f()
        print(self.name, 'ended')


class Scheduler:
    def __init__(self, tasks):
        self.tasks = tasks

    def get_task_data(self):
        result = {}
        for task in self.tasks:
            result[task.t] = task
        return result

    def run(self):
        data = self.get_task_data()
        et = 0
        for i in range(max(data)):
            print(et, 's')
            time.sleep(1)
            et += 1

            try:
                task = data[et]
                task.run()
            except KeyError:
                pass


def f1():
    print('f1')


def f2():
    print('f2')


def f3():
    print('f3')


tasks = [
    Task('t1', 10, f1),
    Task('t2', 20, f2),
    Task('t3', 30, f3)
]
scheduler = Scheduler(tasks)
scheduler.run()
