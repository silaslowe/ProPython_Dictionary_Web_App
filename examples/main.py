import justpy as jp


@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hello Werld!",
           classes="text-green-700 bg-yellow-500")
    jp.Div(a=wp, text="Hello Werld Mas!", classes="font-serif text-lg")
    return wp



# jp.Route("/", home)

jp.justpy()
