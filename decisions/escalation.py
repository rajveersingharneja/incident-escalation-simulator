from datetime import datetime, timedelta


class EscalationLogic:
    def __init__(self, cooldown_minutes=5):
        self.cooldown = timedelta(minutes=cooldown_minutes)

    def decide(self, service, recent_events, last_action):
        now = datetime.utcnow()

        if last_action:
            if now - last_action["time"] < self.cooldown:
                return "WAIT"

        levels = [e.level for e in recent_events]

        error_count = levels.count("ERROR")
        warning_count = levels.count("WARNING")
        recovery_count = levels.count("RECOVERY")

        if recovery_count >= error_count and error_count > 0:
            return "WAIT"


        if error_count >= 3:
            return "ESCALATE"



        if error_count == 1 and warning_count >= 1:
            return "MONITOR"

        if warning_count >= 2:
            return "MONITOR"

        return "WAIT"
