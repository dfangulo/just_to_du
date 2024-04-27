import os
import time
from ..model import Task


class TaskManager:
    tasks_list = []

    def add_task(self) -> None:
        while True:
            task_nane = input("Nombre para la tarea: ")
            if task_nane:
                new_task = Task(task_nane)
                self.tasks_list.append(new_task)
                print(f"{new_task.task_name}, agregada exitosamente")
                time.sleep(1 / 3)
            else:
                time.sleep(1 / 3)
                print("La tarea no fue agregada!.")
                break

    def edit_task(self, index, **kwargs) -> None:
        print(kwargs)
        if 0 <= index < len(self.tasks_list):
            self.tasks_list[index].edit_task(**kwargs)
        else:
            input("Índice de tarea fuera de rango.")

    def show_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks_list):
            print(self.tasks_list[index])
        else:
            input("Índice de tarea fuera de rango.")

    def delete_task(self, index) -> None:
        if 0 <= index < len(self.tasks_list):
            del self.tasks_list[index]
        else:
            input("Índice de tarea fuera de rango.")

    def complete_task(self, index) -> None:
        if 0 <= index < len(self.tasks_list):
            self.tasks_list[index].complete_task()
            input(f"Tarea: '{self.tasks_list[index].task_name}' - Completada!")

    def show_detail_tasks(self) -> None:
        for task in self.tasks_list:
            print(task)

    def show_active_tasks(self) -> None:
        active_tasks: int = 0
        os.system("cls")
        try:
            if self.tasks_list:
                print(
                    "#".center(4),
                    "Nombre de la Tarea".center(60),
                    "Tiempo trascurrido".center(20),
                )
                for index, tarea in enumerate(self.tasks_list):
                    if tarea.task_active and tarea.task_cancel is False:
                        active_tasks += 1
                        print(
                            str(index).center(4),
                            tarea.task_name.ljust(60),
                            str(tarea.set_duration()).center(26),
                        )
                if active_tasks >= 1:
                    return 1

        except Exception as e:
            raise (f"Error en show_tasks_list: {str(e)}")
        return 0

    def show_completed_tasks(self) -> None:
        active_tasks: int = 0
        try:
            if self.tasks_list:
                print(
                    "#".center(4),
                    "Nombre de la Tarea".center(60),
                    "Duración".center(24),
                )
                for index, tarea in enumerate(self.tasks_list):
                    if tarea.task_active is False:
                        active_tasks += 1
                        print(
                            str(index).ljust(4),
                            tarea.task_name.ljust(60),
                            str(tarea.task_duration).ljust(24),
                        )
                if active_tasks >= 1:
                    return 1
            else:
                input("No hay tareas completadas de momento!")
        except Exception as e:
            input(f"Error en show_tasks_list: {str(e)}")
        return 0

    def show_cancel_tasks(self) -> None:
        cancel_tasks: int = 0
        try:
            if self.tasks_list:
                print(
                    "#".center(4),
                    "Nombre de la Tarea".center(60),
                    "Duración".center(24),
                )
                for index, tarea in enumerate(self.tasks_list):
                    if tarea.task_cancel:
                        cancel_tasks += 1
                        print(
                            str(index).ljust(4),
                            tarea.task_name.ljust(60),
                            str(tarea.task_duration).ljust(24),
                        )
                if cancel_tasks >= 1:
                    return 1
            else:
                input("No hay tareas canceladas de momento!")
        except Exception as e:
            input(f"Error en show_cancel_tasks: {str(e)}")
        return 0

    def priority_task(self, index: int) -> None:
        """
        Cambiar una tarea al inicio de la lista
        :borra el elemento y lo copia en 'task'
        :Inserta nuevamenta 'task' en el indice 0
        """
        task = self.tasks_list.pop(index)
        self.tasks_list.insert(0, task)
