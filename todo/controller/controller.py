import os
import time
import json
from ..model import Task


class TaskManager:
    tasks_list: list[Task] = []
    task_json_file: str = "todo/json/tasks.json"

    def add_task(self) -> None:
        while True:
            print("Enter para continuar!")
            task_nane = input("\n\tNombre para la tarea: ")
            if task_nane:
                new_task: Task = Task(task_nane)
                self.tasks_list.append(new_task)
                print(f"{new_task.task_name}, agregada exitosamente")
                self.save_tasks_list()
                time.sleep(1 / 3)
            else:
                time.sleep(1 / 3)
                print("La tarea no fue agregada!.")
                break

    def edit_task(self, index, **kwargs) -> None:
        if 0 <= index < len(self.tasks_list):
            self.tasks_list[index].edit_task(**kwargs)
            self.save_tasks_list()
        else:
            input("Índice de tarea fuera de rango.")

    def delete_task(self, index) -> None:
        if 0 <= index < len(self.tasks_list):
            del self.tasks_list[index]
            self.save_tasks_list()
        else:
            input("Índice de tarea fuera de rango.")

    def show_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks_list):
            print(self.tasks_list[index])
        else:
            input("Índice de tarea fuera de rango.")

    def show_detail_active_tasks(self) -> None:
        try:
            print("\n", "¡Tareas Activas!".center(80))
            for task in self.tasks_list:
                if task.task_active:
                    print("+", "-" * 78, "+")
                    print(task)
        except Exception as e:
            input(f"Error en show_detail_active_tasks: {str(e)}")

    def show_active_tasks(self) -> None:
        self.load_tasks_list()
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
            raise (f"Error en show_active_tasks: {str(e)}")
        return 0

    def show_completed_tasks(self) -> None:
        try:
            print("\n", "¡Tareas Completadas!".center(80))
            for task in self.tasks_list:
                if task.task_active is False:
                    print("+", "-" * 78, "+")
                    print(task)
        except Exception as e:
            input(f"Error en show_completed_tasks: {str(e)}")

    def show_cancel_tasks(self) -> None:
        try:
            print("\n", "¡Tareas Canceladas!".center(80))
            for task in self.tasks_list:
                if task.task_cancel:
                    print("+", "-" * 78, "+")
                    print(task)
        except Exception as e:
            input(f"Error en show_cancel_tasks: {str(e)}")

    def priority_task(self, index: int) -> None:
        """
        Cambiar una tarea al inicio de la lista
        :borra el elemento y lo copia en 'task'
        :Inserta nuevamenta 'task' en el indice 0
        """
        task = self.tasks_list.pop(index)
        self.tasks_list.insert(0, task)
        self.save_tasks_list()

    def save_tasks_list(self, filename=task_json_file) -> None:
        try:
            with open(filename, "w") as file:
                json.dump([task.serialize() for task in self.tasks_list], file)
            print("Lista de tareas guardada exitosamente en", filename)
        except Exception as e:
            print("Error al guardar la lista de tareas:", str(e))

    def load_tasks_list(self, filename=task_json_file) -> None:
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks_list = [
                    Task.deserialize(task_data) for task_data in tasks_data
                ]
            print("Lista de tareas cargada exitosamente desde", filename)
        except FileNotFoundError:
            print("El archivo de tareas no existe. Se creará una nueva lista.")
            self.tasks_list = []
        except Exception as e:
            print("Error al cargar la lista de tareas:", str(e))
