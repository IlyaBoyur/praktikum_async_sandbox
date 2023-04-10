class SystemCall:
    def handle(self, sched: "Scheduler", task: "Task"):
        raise NotImplementedError()


class NewTask(SystemCall):
    def __init__(self, target: "Generator"):
        self.target = target

    def handle(self, scheduler: "Scheduler", task: "Task"):
        tid = scheduler.add_task(self.target)
        task.sendval = tid
        scheduler.schedule(task)
