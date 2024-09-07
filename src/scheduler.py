class Scheduler:
    _max_delay = 0
    _tasks_by_delay = {}

    def add_tasks(self, task):
        """Add task to scheduler tasks_by_delay and calculate max_delay for better performance"""
        self._tasks_by_delay[task.get_delay()] = task
        self._max_delay = max(self._max_delay, task.get_delay())

    def get_tasks(self):
        return self._tasks_by_delay.values()

    def _get_task_by_delay(self, delay):
        """Return task related to specified delay"""
        try:
            return self._tasks_by_delay[delay]
        except KeyError:
            return None

    def _run_task_by_delay(self, delay):
        """Run task related to specified delay"""
        task = self._get_task_by_delay(delay)
        if task is None:
            return None
        return task.run()

    def run(self):
        """Run scheduler"""
        import time
        for elapsed_time in range(self._max_delay + 1):
            print('Start:' if elapsed_time == 0 else f'Elapsed time: {elapsed_time}s')
            self._run_task_by_delay(elapsed_time)
            time.sleep(1)
