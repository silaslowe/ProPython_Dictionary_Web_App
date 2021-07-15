import justpy as jp


@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-2 p-4")
    jp.Input(a=div1, placeholder="input1", classes="form-input")
    jp.Input(a=div1, placeholder="input2", classes="form-input")
    jp.Div(a=div1, text="Result...", classes="text-gray-500")
    jp.Div(a=div1, text="More Div...", classes="text-gray-500")
    jp.Div(a=div1, text="Morer Div ...", classes="text-gray-500")

    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-2")
    jp.Button(a=div2, text="Calculate", classes="border border-blue-500 m-2 py-1 px-4 rounded "
                                               "text-blue-600 hover:bg-red-500 hover:text-white")
    jp.Div(a=div2, text="Div 2 div", classes="text-gray-500")

    return wp


# jp.Route("/", home)

jp.justpy()
