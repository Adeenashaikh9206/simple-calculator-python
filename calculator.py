from nicegui import ui

class Calculator:
    def __init__(self, display_label):
        self.expression = ""
        self.display = display_label

    def append(self, char):
        self.expression += str(char)
        self.display.set_text(self.expression)

    def clear(self):
        self.expression = ""
        self.display.set_text("0")

    def delete(self):
        self.expression = self.expression[:-1]
        self.display.set_text(self.expression if self.expression else "0")

    def calculate(self):
        try:
            formatted_expr = self.expression.replace('x', '*').replace('÷', '/')
            if '%' in formatted_expr:
                formatted_expr = formatted_expr.replace('%', '/100')
                
            result = str(eval(formatted_expr))
            self.expression = result
            self.display.set_text(result)
        except Exception:
            self.display.set_text("Error")
            self.expression = ""

# Page routing define karne se client/session conflicts bilkul khatam ho jate hain
@ui.page('/')
def index():
    # Custom CSS for premium animations & styling
    ui.add_head_html('''
    <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .calc-container {
            animation: fadeIn 0.8s ease-out;
            box-shadow: 0 20px 25px -5px rgba(59, 130, 246, 0.1), 0 10px 10px -5px rgba(59, 130, 246, 0.04);
            border: 2px solid #eff6ff;
        }
        .calc-btn {
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        .calc-btn:hover {
            transform: translateY(-3px) scale(1.05) !important;
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3) !important;
        }
        .calc-btn:active {
            transform: scale(0.95) !important;
        }
    </style>
    ''')

    # Main Page Container
    with ui.element('div').classes('w-full min-h-screen flex items-center justify-center bg-blue-50 p-4'):
        
        # Calculator Card
        with ui.card().classes('calc-container w-full max-w-sm p-6 rounded-3xl bg-white space-y-4'):
            
            # Title
            ui.label('NEO CALC').classes('text-xs font-bold tracking-widest text-blue-400 text-center w-full')
            
            # Display Screen
            with ui.element('div').classes('w-full bg-blue-50/50 p-6 rounded-2xl text-right overflow-hidden border border-blue-100/50'):
                display = ui.label('0').classes('text-4xl font-light text-blue-900 break-all transition-all duration-300')

            # Initialize Calculator with reference to this specific page's display
            calc = Calculator(display)

            # Buttons Grid Layout
            with ui.grid(columns=4).classes('w-full gap-3'):
                
                # Row 1
                ui.button('C', on_click=calc.clear).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-red-50 text-red-500 hover:bg-red-100 shadow-none')
                ui.button('⌫', on_click=calc.delete).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-blue-50 text-blue-600 hover:bg-blue-100 shadow-none')
                ui.button('%', on_click=lambda: calc.append('%')).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-blue-50 text-blue-600 hover:bg-blue-100 shadow-none')
                ui.button('÷', on_click=lambda: calc.append('÷')).classes('calc-btn rounded-2xl h-14 text-lg font-bold bg-blue-600 text-white hover:bg-blue-700 shadow-none')

                # Row 2
                ui.button('7', on_click=lambda: calc.append(7)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('8', on_click=lambda: calc.append(8)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('9', on_click=lambda: calc.append(9)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('x', on_click=lambda: calc.append('x')).classes('calc-btn rounded-2xl h-14 text-lg font-bold bg-blue-600 text-white hover:bg-blue-700 shadow-none')

                # Row 3
                ui.button('4', on_click=lambda: calc.append(4)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('5', on_click=lambda: calc.append(5)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('6', on_click=lambda: calc.append(6)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('-', on_click=lambda: calc.append('-')).classes('calc-btn rounded-2xl h-14 text-lg font-bold bg-blue-600 text-white hover:bg-blue-700 shadow-none')

                # Row 4
                ui.button('1', on_click=lambda: calc.append(1)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('2', on_click=lambda: calc.append(2)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('3', on_click=lambda: calc.append(3)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('+', on_click=lambda: calc.append('+')).classes('calc-btn rounded-2xl h-14 text-lg font-bold bg-blue-600 text-white hover:bg-blue-700 shadow-none')

                # Row 5
                ui.button('0', on_click=lambda: calc.append(0)).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 col-span-2 shadow-none')
                ui.button('.', on_click=lambda: calc.append('.')).classes('calc-btn rounded-2xl h-14 text-lg font-medium bg-slate-50 text-slate-700 hover:bg-blue-50/50 shadow-none')
                ui.button('=', on_click=calc.calculate).classes('calc-btn rounded-2xl h-14 text-lg font-bold bg-blue-600 text-white hover:bg-blue-700 shadow-none')

# RUN CONFIGURATION (Uvicorn configuration optimized)
ui.run(title="Neo-Blue Animated Calculator", reload=False, port=8080)