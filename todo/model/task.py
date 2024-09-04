from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Task:
    task_name: str
    task_duration: str = None
    task_creation_date: str = None
    task_completion_date: str = None
    task_active: bool = True
    task_complete: bool = False
    task_cancel: bool = False

    def __str__(self) -> str:
        return f"""    Nombre: {self.task_name}
    Fecha Inicio: {self.task_creation_date}
    Activa: {'Si' if self.task_active else 'No'}
    Completada: {'Si' if self.task_complete else 'No'}
    Tiempo: {str(self.set_duration())}"""

    def edit_task(self, task_name: str = None, task_cancel: bool = None, task_active: bool = None) -> None:
        if task_name is not None:
            self.task_name = task_name
        if task_cancel is not None:
            self.task_cancel = task_cancel
        if task_active is not None:
            self.task_active = task_active

    def __post_init__(self) -> None:
        if self.task_creation_date is None:
            self.task_creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def complete_task(self) -> None:
        self.task_completion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.task_complete = True
        self.task_active = False
        self.task_duration = self.set_duration()

    def set_duration(self) -> datetime:
        start = datetime.strptime(self.task_creation_date, "%Y-%m-%d %H:%M:%S")
        if self.task_completion_date:
            # Convertir cadenas de texto a objetos datetime
            end = datetime.strptime(self.task_completion_date, "%Y-%m-%d %H:%M:%S")
        else:
            ended = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            end = datetime.strptime(ended, "%Y-%m-%d %H:%M:%S")
        duration = end - start
        return duration

    def serialize(self) -> dict:
        """
        Serializa el objeto Task en un diccionario.
        """
        return {
            'task_name': self.task_name,
            'task_duration': self.task_duration,
            'task_creation_date': self.task_creation_date,
            'task_completion_date': self.task_completion_date,
            'task_active': self.task_active,
            'task_complete': self.task_complete,
            'task_cancel': self.task_cancel
        }

    @classmethod
    def deserialize(cls, data: dict):
        """
        Deserializa un diccionario en un objeto Task.
        """
        return cls(
            task_name=data['task_name'],
            task_duration=data['task_duration'],
            task_creation_date=data['task_creation_date'],
            task_completion_date=data['task_completion_date'],
            task_active=data['task_active'],
            task_complete=data['task_complete'],
            task_cancel=data['task_cancel']
        )