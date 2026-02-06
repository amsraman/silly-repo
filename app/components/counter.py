import reflex as rx
from app.states.counter_state import CounterState


def counter_card() -> rx.Component:
    """A visually stunning red-themed counter card component."""
    return rx.el.div(
        rx.el.div(
            class_name="absolute -top-24 -left-24 w-64 h-64 bg-red-200 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-pulse"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 -right-24 w-64 h-64 bg-rose-200 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-pulse"
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("flame", class_name="h-8 w-8 text-red-600 mb-4"),
                rx.el.h1(
                    "Redline Counter",
                    class_name="text-2xl font-black text-red-900 tracking-tight",
                ),
                rx.el.p(
                    "The power of reactive state in crimson",
                    class_name="text-red-700/60 text-sm mb-8 font-medium",
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
                            "text-8xl font-black transition-all duration-300 transform text-rose-800 scale-90",
                        ),
                    ),
                ),
                class_name="flex justify-center items-center py-12",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("minus", class_name="h-6 w-6"),
                    on_click=CounterState.decrement,
                    class_name="""
                        flex items-center justify-center
                        w-16 h-16 rounded-2xl
                        bg-rose-50 border-2 border-rose-100
                        text-rose-700 shadow-sm
                        hover:border-rose-400 hover:text-rose-900 hover:bg-rose-100
                        active:scale-95 transition-all duration-200
                    """,
                ),
                rx.el.button(
                    rx.icon("rotate-ccw", class_name="h-5 w-5"),
                    on_click=CounterState.reset_counter,
                    class_name="""
                        flex items-center justify-center
                        px-8 py-4 rounded-2xl
                        bg-red-600 text-white font-bold
                        hover:bg-red-700 shadow-lg shadow-red-200
                        active:scale-95 transition-all duration-200
                    """,
                ),
                rx.el.button(
                    rx.icon("plus", class_name="h-6 w-6"),
                    on_click=CounterState.increment,
                    class_name="""
                        flex items-center justify-center
                        w-16 h-16 rounded-2xl
                        bg-red-50 border-2 border-red-100
                        text-red-700 shadow-sm
                        hover:border-red-400 hover:text-red-900 hover:bg-red-100
                        active:scale-95 transition-all duration-200
                    """,
                ),
                class_name="flex items-center justify-center gap-6",
            ),
            rx.el.div(
                rx.el.div(
                    class_name=rx.cond(
                        CounterState.count == 0,
                        "w-2.5 h-2.5 rounded-full bg-red-200",
                        rx.cond(
                            CounterState.count > 0,
                            "w-2.5 h-2.5 rounded-full bg-red-500 animate-ping",
                            "w-2.5 h-2.5 rounded-full bg-rose-600 animate-ping",
                        ),
                    )
                ),
                rx.el.span(
                    rx.cond(
                        CounterState.count == 0,
                        "Idle",
                        rx.cond(CounterState.count > 0, "Accelerating", "Decelerating"),
                    ),
                    class_name="text-xs font-black uppercase tracking-[0.2em] text-red-900/40",
                ),
                class_name="flex items-center justify-center gap-3 mt-10",
            ),
            class_name="relative z-10 w-full max-w-md p-10 bg-white/90 backdrop-blur-2xl rounded-[3rem] border-2 border-red-50/50 shadow-[0_32px_64px_-16px_rgba(220,38,38,0.15)]",
        ),
        class_name="relative flex items-center justify-center w-full min-h-screen p-6 bg-red-50",
    )