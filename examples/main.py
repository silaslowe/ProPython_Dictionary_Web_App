import justpy as jp


@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hello Werld!")
    jp.Div(a=wp, text="Hello Werld Mas!")
    return wp

@jp.SetRoute("/about")
def about():
    wp= jp.WebPage()
    jp.Div(a=wp, text="Yeah!!!")
    jp.Div(a=wp, text="YaaY!!!")
    return wp

# jp.Route("/", home)

jp.justpy()
