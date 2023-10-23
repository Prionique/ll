from flet import *
from views.index import IndexPage
from flet_route import path, Routing

def main(page: Page):

    routes = [
        path("/", view = IndexPage().view, clear = True)
    ]
    Routing(page= page, app_routes = routes)
    page.go(page.route)

app(main, view = WEB_BROWSER)