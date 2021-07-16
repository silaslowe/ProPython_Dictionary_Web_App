import justpy as jp


@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-2 p-4")
    in_1 = jp.Input(a=div1, placeholder="input1", classes="form-input")
    in_2 = jp.Input(a=div1, placeholder="input2", classes="form-input")
    d_output = jp.Div(a=div1, text="Result...", classes="text-gray-500")
    jp.Div(a=div1, text="More Div...", classes="text-gray-500")
    jp.Div(a=div1, text="Morer Div ...", classes="text-gray-500")

    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-2")
    jp.Button(a=div2, text="Calculate", click=sum_up, in1=in_1, in2=in_2,
              d=d_output,
              classes="border border-blue-500 m-2 py-1 px-4 rounded "
                      "text-blue-600 hover:bg-red-500 hover:text-white")
    jp.Div(a=div2, text="Div 2 div", mouseenter=mouse_enter, mouseleave=mouse_leave, classes="text-gray-500")

    return wp


def sum_up(widget, msg):
    print("Hi")
    total = float(widget.in1.value) + float(widget.in2.value)
    widget.d.text = total


def mouse_enter(widget, msg):
    widget.text = "A mouse entered the house!"


def mouse_leave(widget, msg):
    widget.text = "The mouse leaved"


# jp.Route("/", home)

jp.justpy()
