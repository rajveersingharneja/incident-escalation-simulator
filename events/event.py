from datetime import datetime


class Event:
    def __init__(self, service, level, message, timestamp=None):
        self.service = service
        self.level = level          
        self.message = message

        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.utcnow()

    def __repr__(self):
        return (
            f"<Event service={self.service} "
            f"level={self.level} "
            f"time={self.timestamp}>"
        )
