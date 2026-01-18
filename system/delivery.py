import random
import time


class DeliverySystem:
    def __init__(self):
        pass

    def deliver(self, event):
        """
        Simulates unreliable delivery.
        Returns a list of delivered events.
        """

        delivered = []

        if event is None:
            return delivered

        
        delay = random.uniform(0.1, 1.0)
        time.sleep(delay)

        
        if random.random() < 0.1:
            return delivered

        delivered.append(event)

        
        if random.random() < 0.15:
            delivered.append(event)

        return delivered
