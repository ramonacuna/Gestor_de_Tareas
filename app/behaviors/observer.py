class Event:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, fn):
        self._subscribers.append(fn)

    def notify(self, *args, **kwargs):
        for fn in self._subscribers:
            fn(*args, **kwargs)

tarea_created = Event()

def send_email_notification(tarea):
    print(f"Notificación: Nueva tarea creada -> {tarea.title}")

def send_push_notification(tarea):
    print(f"Push: Se creó una nueva tarea '{tarea.title}'")

tarea_created.subscribe(send_email_notification)