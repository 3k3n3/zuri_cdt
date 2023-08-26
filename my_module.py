"""My module."""


class MyModule:
    """This module helps in calculating the best way to avoid hitting impenetrable rocks under the earth."""
    
    def _init__(self, speed_of_machine):
        self.speed_of_machine = speed_of_machine

    def calculate_distance(self, location_a, location_b):
        # This simulated function returns the distance between the 2 locations.
        return distance

    def expected_time(self, distance):
        """Calculates the expected time to get from point a to point b."""
        time = distance / self.speed_of_machine
        return time

    def obstruction(self, location_a, location_b, time_duration):
        """Check if there is an inpenetrabe obstruction."""
        distance = self.calculate_distance(location_a, location_b)
        expected_time = self.expected_time(distance)

        if time_duration > expected_time + 60:
            return True
        else:
            return False
