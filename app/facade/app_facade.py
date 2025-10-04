class AppFacade:
    def __init__(self, tarea_service):
        self.tarea_service = tarea_service

    def create_tarea(self, tarea_data):
        return self.tarea_service.create_tarea(tarea_data)

    def list_tareas(self, strategy=None):
        return self.tarea_service.list_tareas(strategy)

    def update_tarea(self, tarea_id, tarea_data):
        return self.tarea_service.update_tarea(tarea_id, tarea_data)

    def delete_tarea(self, tarea_id):
        return self.tarea_service.delete_tarea(tarea_id)

