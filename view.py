import flet as ft


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.txtOut = None
        self._btnIn = None
        self.dd_mode = None
        self._txtIn = None
        self.dd = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        # Add your stuff here
        self.dd = ft.Dropdown(label="Select Language",
                              options=[ft.dropdown.Option("Italian"), ft.dropdown.Option("English"),
                                       ft.dropdown.Option("Spanish")])

        self.dd_mode = ft.Dropdown(label="Search Modality",
                                   options=[ft.dropdown.Option("Linear"), ft.dropdown.Option("Dichotomic"),
                                            ft.dropdown.Option("Default")])

        self._txtIn = ft.TextField(label="Inserisci la tua frase")
        self._btnIn = ft.ElevatedButton("Spell Check", on_click=self.__controller.handleSpellCheck)

        self.txtOut = ft.ListView()

        row1 = ft.Row([self.dd])
        row2 = ft.Row([self.dd_mode, self._txtIn, self._btnIn])
        row3 = ft.Row([self.txtOut])

        self.page.add(row1, row2, row3)
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
