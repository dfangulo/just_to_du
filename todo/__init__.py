from .controller import TaskManager
from .menu import menu


class ToDo:
    manager = TaskManager()
    menu_opptions = [
        "Mostrar tareas Activas",
        "Mostrar tareas Completadas",
        "Mostrar tareas Canceladas",
        "Administrar Tareas",
    ]
    sub_menu_options = [
        "Agregar Tarea",
        "Completar Tarea",
        "Editar Tarea",
        "Cancelar Tarea",
        "Borrar Tarea",
    ]

    def run(self) -> None:
        while True:
            self.manager.show_active_tasks()
            menu(self.menu_opptions)
            choice = input("Seleccionar una Opcion: ")
            if choice.lower() == "s":
                break
            elif choice == "1":
                self.show_active_tasks()
            elif choice == "2":
                self.show_completed_tasks()
            elif choice == "3":
                self.show_cancel_tasks()
            elif choice == "4":
                self.task_managment()
            else:
                print("\nOpciones validas '1', '2', '3', '4' o 'S' para salir")
                input(f"\t'{choice.capitalize()}' No es una opcion valida.")

    def show_active_tasks(self) -> None:
        self.manager.show_active_tasks()
        self.manager.show_detail_active_tasks()
        input("Enter para continuar")

    def show_completed_tasks(self) -> None:
        self.manager.show_active_tasks()
        self.manager.show_completed_tasks()
        input("Enter para continuar")

    def show_cancel_tasks(self) -> None:
        self.manager.show_active_tasks()
        self.manager.show_cancel_tasks()
        input("Enter para continuar")

    def task_managment(self) -> None:
        while True:
            self.manager.show_active_tasks()
            menu(self.sub_menu_options)
            sub_choice = input("Seleciona una opcion: ")
            if sub_choice.lower() == "s":
                break
            elif sub_choice == "1":
                self.add_task()
            elif sub_choice == "2":
                self.complete_task()
            elif sub_choice == "3":
                self.edit_task()
            elif sub_choice == "4":
                self.cancel_task()
            elif sub_choice == "5":
                self.delete_task()

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
            task_edit = input("Cual tarea quieres cancelar: ")
            if task_edit:
                self.manager.show_task(int(task_edit))
                cancel_task = input("Confirmar cancelacion (S): ")
                if cancel_task.lower() == "s":
                    self.manager.edit_task(int(task_edit), task_cancel=True)
                    self.manager.edit_task(int(task_edit), task_active=False)
            else:
                input("No se completó ninguna tarea.")

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
