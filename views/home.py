from flet import *


class Home(Container):
    def __init__(self, home_page: Page):
        super().__init__(expand=True)

        self.page = home_page

        self.earnedNumber = 11
        self.spentNumber = 10

        self.earned = Container(
            content=Column([
                Text("Total Earned:", size=25),
                Row([
                    ProgressBar(value=0.5, bar_height=10, color=colors.GREEN_ACCENT_700, width=350),
                    Row([
                        Text(f"{self.earnedNumber}$", size=20, weight=FontWeight.W_700),
                        IconButton(icon=icons.ADD, icon_color=colors.GREEN_ACCENT_700),
                    ]),

                ], alignment=MainAxisAlignment.SPACE_BETWEEN),
            ])
        )
        self.spent = Container(
            content=Column([
                Text("Total Spent:", size=25),
                Row([
                    ProgressBar(value=0.5, bar_height=10, color=colors.RED_ACCENT_700, width=350),
                    Row([
                        Text(f"{self.spentNumber}$", size=20, weight=FontWeight.W_700),
                        IconButton(icon=icons.ADD, icon_color=colors.RED_ACCENT_700),
                    ]),

                ], alignment=MainAxisAlignment.SPACE_BETWEEN),
            ])
        )

        self.content = Column([

            self.earned,
            self.spent,

        ])
