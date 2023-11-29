import PySimpleGUI as sg

# Define el path de las imágenes
automaton_model_path = "./assets/AutomatonModel.png"

# Configura el tema de la ventana
sg.theme('DarkBlue')

# Define el layout de la ventana
layout = [
    [sg.Text('Autómata de pila', font=("Times", 32), justification='center', size=(50, 1))],
    [sg.Text('Cadena:', font=("Times", 16)), sg.InputText(font=("Times", 16), size=(50, 1), key='-INPUT-')],
    [sg.Listbox(values=[], enable_events=True, size=(60, 20), key='-LIST-', font=("Times", 10))],
    [sg.Text('Modelo Del Autómata De Pila', font=("Times", 16))],
    [sg.Image(automaton_model_path, key='-IMAGE-')],
    [sg.Text('<Enter> para continuar, <X> para salir', font=("Times", 16), justification='center', size=(50, 1))],
]

# Crea la ventana
window = sg.Window('Autómata de pila', layout, resizable=True)

# Bucle de eventos para procesar "eventos" y obtener los "valores" de las entradas
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':  # Si el usuario cierra la ventana o hace clic en Salir
        break

    # Aquí iría la lógica de tu programa, por ejemplo, si el usuario presiona Enter
    if event == 'Enter':
        # Suponiendo que tienes una función que procesa la entrada
        # result = process_input(values['-INPUT-'])
        # window['-LIST-'].update(result)  # Actualiza la Listbox con el resultado
        pass

window.close()
