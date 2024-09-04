from .controller import TaskManager
from .menu import menu


class ToDo:
    manager = TaskManager()

    def run(self) -> None:
        while True:
            self.manager.show_active_tasks()
            key_used = menu(
                [
                    "Mostrar tareas Activas",
                    "Mostrar tareas Completadas",
                    "Mostrar tareas Canceladas",
                    "Administrar Tareas",
                ]
            )
            choice = input("Seleccionar una Opcion: ")
            if choice.lower() == "s":
                break
            elif choice == "f":
                self.show_active_tasks()
            elif choice == "d":
                self.show_completed_tasks()
            elif choice == "b":
                self.show_cancel_tasks()
            elif choice == "g":
                self.task_managment()
            else:
                print(f"\n\t'{choice.capitalize()}' No es una opcion valida.")
                input(f"\nOpciones validas [{', '.join(key_used)} o 's'] para salir")

    def show_active_tasks(self) -> None:
        self.manager.load_tasks_list()
        self.manager.show_active_tasks()
        self.manager.show_detail_active_tasks()
        input("\n\tEnter para continuar")

    def show_completed_tasks(self) -> None:
        self.manager.load_tasks_list()
        self.manager.show_active_tasks()
        self.manager.show_completed_tasks()
        input("\n\tEnter para continuar")

    def show_cancel_tasks(self) -> None:
        self.manager.show_active_tasks()
        self.manager.show_cancel_tasks()
        input("\n\tEnter para continuar")

    def task_managment(self) -> None:
        while True:
            self.manager.show_active_tasks()
            key_used = menu(
                [
                    "Agregar Tarea",
                    "Completar Tarea",
                    "Editar Tarea",
                    "Cancelar Tarea",
                    "Borrar Tarea",
                ]
            )
            sub_choice = input("Seleciona una opcion: ")
            if sub_choice.lower() == "s":
                break
            elif sub_choice == "f":
                self.add_task()
            elif sub_choice == "d":
                self.complete_task()
            elif sub_choice == "b":
                self.edit_task()
            elif sub_choice == "g":
                self.cancel_task()
            elif sub_choice == "e":
                self.delete_task()
            else:
                print(f"\n\t'{sub_choice.capitalize()}' No es una opcion valida.")
                input(f"\nOpciones validas [{', '.join(key_used)} o 's'] para salir")

    def add_task(self) -> None:
        self.manager.add_task()

    def complete_task(self) -> None:
        to_show = self.manager.show_active_tasks()
        if to_show:
            task_complete = input("Cual tarea quieres completar: ")
            if task_complete:
                self.manager.complete_task(int(task_complete))
            else:
                input("No se completó ninguna tarea.")

    def edit_task(self) -> None:
        to_show = self.manager.show_active_tasks()
        if to_show:
            task_edit = input("Cual tarea quieres editar: ")
            if task_edit:
                self.manager.show_task(int(task_edit))
                new_task_name = input("Introduce el nuevo nombre: ")
                self.manager.edit_task(int(task_edit), task_name=new_task_name)
            else:
                input("No se completó ninguna tarea.")

    def cancel_task(self) -> None:
        to_show = self.manager.show_active_tasks()
        if to_show:
            task_edit = input(
                "¿Qué tarea quieres cancelar? Ingresa el número correspondiente: "
            )
            if task_edit:
                self.manager.show_task(int(task_edit))
                cancel_confirmation = input("¿Confirmar cancelación? (Sí/N): ")
                if cancel_confirmation.lower() == "s":
                    self.manager.edit_task(
                        int(task_edit), task_cancel=True, task_active=False
                    )
            else:
                input("No se seleccionó ninguna tarea.")

    def delete_task(self) -> None:
        to_show = self.manager.show_active_tasks()
        if to_show:
            task_delete = input("Cual tarea quieres cancelar: ")
            if task_delete:
                self.manager.show_task(int(task_delete))
                cancel_task = input("Seguro de eliminar la tarea (S): ")
                if cancel_task.lower() == "s":
                    self.manager.delete_task(int(task_delete))
            else:
                input("No se eliminó ninguna tarea.")
