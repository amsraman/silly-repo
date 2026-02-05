import reflex as rx
from app.components.counter import counter_card


def index() -> rx.Component:
    """The main entry point for the counter application."""
    return rx.el.main(
        rx.el.div(
            counter_card(),
            class_name="w-full min-h-screen bg-slate-50 overflow-hidden font-['Inter']",
        )
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index,
    route="/",
    title="Reflex Counter | Clean UI",
    description="A horribly designed counter application built with Reflex.",
)