class Task:
    def __init__(self, name, delay, func, args):
        self._name = name
        self._delay = delay
        self._func = func
        self._args = args

    def get_delay(self):
        """Return delay of task"""
        return self._delay

    def run(self):
        """Run Task"""
        result = self._func(*self._args)
        print(f'the result of task {self._name} is {result}.')
        return result
