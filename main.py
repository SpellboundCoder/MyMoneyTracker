from flet import Page, View, ThemeMode, app
from views import Home, FirstLogin


def main(page: Page):

    page.theme_mode = ThemeMode.DARK
    page.window.width = 500
    page.window.height = 700

    def route_change(route):
        route_page = {
            "/welcome": FirstLogin,
            "/": Home,
        }[page.route](page)
        page.views.clear()
        page.views.append(
            View(
                route=route,
                controls=[route_page]
            )
        )
        page.update()

    page.on_route_change = route_change

    if page.client_storage.contains_key("first_login"):
        page.go("/")
    else:
        page.go("/welcome")


app(target=main)
