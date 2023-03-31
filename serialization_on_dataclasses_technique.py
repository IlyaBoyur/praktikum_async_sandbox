import json
import pickle
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar


class TaskType(str, Enum):
    TASK_ONE = 'task_one'
    TASK_TWO = 'task_two'


@dataclass
class BaseTask:
    TYPE: ClassVar[TaskType]
    name: str


@dataclass
class TaskOne(BaseTask):
    TYPE: ClassVar[TaskType] = TaskType.TASK_ONE
    param_one: str


@dataclass
class TaskTwo(BaseTask):
    TYPE: ClassVar[TaskType] = TaskType.TASK_TWO
    param_two: str


TYPE_TO_CLASS_MAP = {
    TaskType.TASK_ONE: TaskOne,
    TaskType.TASK_TWO: TaskTwo,
}


def approach_with_pickle():
    tasks = [
        TaskOne(name='test 1', param_one='test 1'),
        TaskTwo(name='test 2', param_two='test 2'),
    ]
    pickled_tasks = pickle.dumps(tasks)

    unpickled_tasks = pickle.loads(pickled_tasks)
    print(unpickled_tasks[0].name)
    print(unpickled_tasks[1].name)


def approach_with_json():
    tasks = [
        TaskOne(name='test 1', param_one='test 1'),
        TaskTwo(name='test 2', param_two='test 2'),
    ]

    json_tasks = json.dumps(
        [
            {'type': task.TYPE, 'task_body': task.__dict__} for task in tasks
        ],
    )

    unjson_tasks = [
        TYPE_TO_CLASS_MAP[task_dict['type']](**task_dict['task_body'])
        for task_dict in json.loads(json_tasks)
    ]
    print(unjson_tasks[0].name)
    print(unjson_tasks[1].name)



if __name__ == '__main__':
    approach_with_pickle()
    approach_with_json()