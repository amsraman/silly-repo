import reflex as rx


class CounterState(rx.State):
    """The state for the counter application."""

    count: int = 0

    @rx.event
    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    @rx.event
    def decrement(self):
        """Decrement the counter by 1."""
        self.count -= 1

    @rx.event
    def reset_counter(self):
        """Reset the counter to 0."""
        self.count = 0

    @rx.var
    def count_color(self) -> str:
        """Dynamically change the text color based on the count value with red accents."""
        if self.count > 0:
            return "text-red-600"
        elif self.count < 0:
            return "text-red-400"
        else:
            return "text-red-900"