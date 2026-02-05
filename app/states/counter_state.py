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
        """Dynamically change the text color based on the count value."""
        if self.count > 0:
            return "text-emerald-500"
        elif self.count < 0:
            return "text-rose-500"
        else:
            return "text-gray-700"