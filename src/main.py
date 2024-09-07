from scheduler import Scheduler
from task import Task


def main():
    scheduler = Scheduler()
    for i in range(1, 4):
        task_name = f'task_{i}'
        task = Task(task_name, i * 2, lambda *args: args, args=(task_name,))
        scheduler.add_tasks(task)
    scheduler.run()


if __name__ == '__main__':
    main()
