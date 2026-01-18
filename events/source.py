import random
from events.event import Event


class EventSource:
    def __init__(self, service_name):
        self.service_name = service_name
        self.unstable = False

    def emit(self):
        r = random.random()

        if not self.unstable:
            if r < 0.7:
                return None

            if r < 0.85:
                self.unstable = True
                return Event(
                    self.service_name,
                    "WARNING",
                    "Unusual activity"
                )

            return None

        if r < 0.6:
            return Event(
                self.service_name,
                "ERROR",
                "Error spike"
            )

        if r < 0.8:
            return Event(
                self.service_name,
                "WARNING",
                "Degraded performance"
            )

        self.unstable = False
        return Event(
            self.service_name,
            "RECOVERY",
            "Recovered"
        )
