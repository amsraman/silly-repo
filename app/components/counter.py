import reflex as rx
from app.states.counter_state import CounterState


def counter_card() -> rx.Component:
    """A visually stunning counter card component with a red theme."""
    return rx.el.div(
        rx.el.div(
            class_name="absolute -top-24 -left-24 w-80 h-80 bg-red-200 rounded-full mix-blend-multiply filter blur-3xl opacity-60 animate-pulse"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 -right-24 w-80 h-80 bg-red-100 rounded-full mix-blend-multiply filter blur-3xl opacity-60 animate-pulse"
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("flame", class_name="h-10 w-10 text-red-600 mb-4"),
                rx.el.h1(
                    "Redline Counter",
                    class_name="text-3xl font-black text-red-950 tracking-tighter",
                ),
                rx.el.p(
                    "Bold energy, simple state.",
                    class_name="text-red-700/60 text-sm font-medium mb-8",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.el.span(
                    CounterState.count,
                    class_name=rx.cond(
                        CounterState.count == 0,
                        "text-8xl font-black transition-all duration-300 transform text-red-900",
                        rx.cond(
                            CounterState.count > 0,
                            "text-8xl font-black transition-all duration-300 transform text-red-600 scale-110",
                            "text-8xl font-black transition-all duration-300 transform text-red-400 scale-90",
                        ),
                    ),
                ),
                class_name="flex justify-center items-center py-12",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("circle_minus", class_name="h-7 w-7"),
                    on_click=CounterState.decrement,
                    class_name="""
                        flex items-center justify-center
                        w-16 h-16 rounded-2xl
                        bg-white border-2 border-red-50
                        text-red-400 shadow-sm
                        hover:border-red-200 hover:text-red-600 hover:bg-red-50
                        active:scale-95 transition-all duration-200
                    """,
                ),
                rx.el.button(
                    rx.icon("refresh-cw", class_name="h-5 w-5"),
                    on_click=CounterState.reset_counter,
                    class_name="""
                        flex items-center justify-center
                        px-8 py-4 rounded-2xl
                        bg-red-600 text-white font-bold
                        hover:bg-red-700 shadow-[0_10px_20px_rgba(220,38,38,0.3)]
                        active:scale-95 transition-all duration-200
                    """,
                ),
                rx.el.button(
                    rx.icon("circle_plus", class_name="h-7 w-7"),
                    on_click=CounterState.increment,
                    class_name="""
                        flex items-center justify-center
                        w-16 h-16 rounded-2xl
                        bg-white border-2 border-red-50
                        text-red-400 shadow-sm
                        hover:border-red-200 hover:text-red-600 hover:bg-red-50
                        active:scale-95 transition-all duration-200
                    """,
                ),
                class_name="flex items-center justify-center gap-6",
            ),
            rx.el.div(
                rx.el.div(
                    class_name=rx.cond(
                        CounterState.count == 0,
                        "w-2 h-2 rounded-full bg-red-200",
                        "w-2 h-2 rounded-full bg-red-500 animate-ping",
                    )
                ),
                rx.el.span(
                    rx.cond(
                        CounterState.count == 0,
                        "Standby",
                        rx.cond(CounterState.count > 0, "Increasing", "Decreasing"),
                    ),
                    class_name="text-xs font-black uppercase tracking-widest text-red-900/40",
                ),
                class_name="flex items-center justify-center gap-2 mt-10",
            ),
            class_name="relative z-10 w-full max-w-md p-10 bg-white/90 backdrop-blur-2xl rounded-[3rem] border border-red-100/50 shadow-[0_32px_64px_rgba(153,27,27,0.08)]",
        ),
        class_name="relative flex items-center justify-center w-full min-h-screen p-6",
    )