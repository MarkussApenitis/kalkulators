import PySimpleGUI as sg

oranga_poga: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#90EE90")}
balta_poga: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#ADD8E6")}
CEunC_poga: dict = {'size':(10,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#FF0000")}
liela_poga: dict = {'size':(15,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#006400")}
layout: list = [
    [sg.Text('Kalkulators', size=(50,1), justification='center', background_color="#00FFFF", 
        text_color='black', font=('Franklin Gothic Book', 14, 'bold'))],
    [sg.Text('0.0000', size=(18,1), justification='right', background_color='white', text_color='black', 
        font=('Digital-7',48), relief='sunken', key="_DISPLAY_")],
    [sg.Button('C',**CEunC_poga), sg.Button('CE',**CEunC_poga), sg.Button("/",**balta_poga)],
    [sg.Button('7',**oranga_poga), sg.Button('8',**oranga_poga), sg.Button('9',**oranga_poga), sg.Button("*",**balta_poga)],
    [sg.Button('4',**oranga_poga), sg.Button('5',**oranga_poga), sg.Button('6',**oranga_poga), sg.Button("-",**balta_poga)],
    [sg.Button('1',**oranga_poga), sg.Button('2',**oranga_poga), sg.Button('3',**oranga_poga), sg.Button("+",**balta_poga)],    
    [sg.Button('0',**oranga_poga), sg.Button('.',**oranga_poga), sg.Button('=',**liela_poga, bind_return_key=True)]
]
window: object = sg.Window('Kalkulators', layout=layout, background_color="#00008B", size=(580, 660))
var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}
def format_number() -> float:
    return float(''.join(var['front']).replace(',','') + '.' + ''.join(var['back']))
def update_display(display_value: str):
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)
def number_click(event: str):
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())
def clear_click():
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False 
def operator_click(event: str):
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()
def calculate_click():
    global var
    try:
        var['y_val'] = format_number()
    except ValueError:
        var['x_val'] = var['result']
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_click()    
    except:
        update_display("ERROR! DIV/0")
        clear_click()
while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    if event in ['C','CE']:
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    if event in ['+','-','*','/']:
        operator_click(event)
    if event == '=':
        calculate_click()
    if event == '.':
        var['decimal'] = True
