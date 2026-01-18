import time

from events.source import EventSource
from system.delivery import DeliverySystem
from state.incidents import IncidentState
from decisions.escalation import EscalationLogic


def run():
    services = [
        EventSource("checkout"),
        EventSource("payments"),
        EventSource("auth")
    ]

    delivery = DeliverySystem()
    state = IncidentState()
    logic = EscalationLogic()

    while True:
        for src in services:
            event = src.emit()
            delivered = delivery.deliver(event)

            for e in delivered:
                state.record(e)

                recent = state.recent(e.service)
                last = state.last_decision(e.service)

                decision = logic.decide(e.service, recent, last)
                state.set_decision(e.service, decision)

                print(
                    f"{e.service.upper():10} | "
                    f"{e.level:8} | "
                    f"{decision}"
                )

        time.sleep(1)


if __name__ == "__main__":
    run()
