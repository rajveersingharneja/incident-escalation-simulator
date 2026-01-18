from collections import defaultdict
from datetime import datetime, timedelta


class IncidentState:
    def __init__(self):
        self.events = defaultdict(list)
        self.last_action = {}

    def record(self, event):
        self.events[event.service].append(event)

    def recent(self, service, minutes=2):
        cutoff = datetime.utcnow() - timedelta(minutes=minutes)
        return [
            e for e in self.events.get(service, [])
            if e.timestamp >= cutoff
        ]

    def last_decision(self, service):
        return self.last_action.get(service)

    def set_decision(self, service, decision):
        self.last_action[service] = {
            "decision": decision,
            "time": datetime.utcnow()
        }
