import reflex as rx
from app.states.counter_state import CounterState


def counter_card() -> rx.Component:
    """A visually stunning counter card component."""
    return rx.el.div(
        rx.el.div(
            class_name="absolute -top-24 -left-24 w-64 h-64 bg-indigo-100 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-pulse"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 -right-24 w-64 h-64 bg-purple-100 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-pulse"
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("layers", class_name="h-8 w-8 text-indigo-600 mb-4"),
                rx.el.h1(
                    "Reflex Counter",
                    class_name="text-2xl font-bold text-gray-800 tracking-tight",
                ),
                rx.el.p(
                    "A modern approach to state management",
                    class_name="text-gray-500 text-sm mb-8",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.el.span(
                    CounterState.count,
                    class_name=f"text-8xl font-black transition-all duration-300 transform {CounterState.count_color}",
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
                        bg-white border-2 border-gray-100
                        text-gray-600 shadow-sm
                        hover:border-rose-200 hover:text-rose-500 hover:bg-rose-50
                        active:scale-95 transition-all duration-200
                    """,
                ),
                rx.el.button(
                    rx.icon("rotate-ccw", class_name="h-5 w-5"),
                    on_click=CounterState.reset_counter,
                    class_name="""
                        flex items-center justify-center
                        px-6 py-4 rounded-2xl
                        bg-gray-900 text-white font-semibold
                        hover:bg-gray-800 shadow-lg
                        active:scale-95 transition-all duration-200
                    """,
                ),
                rx.el.button(
                    rx.icon("plus", class_name="h-6 w-6"),
                    on_click=CounterState.increment,
                    class_name="""
                        flex items-center justify-center
                        w-16 h-16 rounded-2xl
                        bg-white border-2 border-gray-100
                        text-gray-600 shadow-sm
                        hover:border-emerald-200 hover:text-emerald-500 hover:bg-emerald-50
                        active:scale-95 transition-all duration-200
                    """,
                ),
                class_name="flex items-center justify-center gap-6",
            ),
            rx.el.div(
                rx.el.div(
                    class_name=rx.cond(
                        CounterState.count == 0,
                        "w-2 h-2 rounded-full bg-gray-300",
                        rx.cond(
                            CounterState.count > 0,
                            "w-2 h-2 rounded-full bg-emerald-400 animate-ping",
                            "w-2 h-2 rounded-full bg-rose-400 animate-ping",
                        ),
                    )
                ),
                rx.el.span(
                    rx.cond(
                        CounterState.count == 0,
                        "Neutral",
                        rx.cond(CounterState.count > 0, "Positive", "Negative"),
                    ),
                    class_name="text-xs font-bold uppercase tracking-widest text-gray-400",
                ),
                class_name="flex items-center justify-center gap-2 mt-10",
            ),
            class_name="relative z-10 w-full max-w-md p-10 bg-white/80 backdrop-blur-xl rounded-[2.5rem] border border-white shadow-[0_20px_50px_rgba(0,0,0,0.05)]",
        ),
        class_name="relative flex items-center justify-center w-full min-h-screen p-6",
    )