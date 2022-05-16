class Color:
    def __init__(self, r_name = "red",
                 g_name = "green", b_name = "blue"):
        self.r_name = r_name
        self.g_name = g_name
        self.b_name = b_name

    def name_print(self, delim = ","):
        print("{r}{delim}{g}{delim}{b}".format(r=self.r_name, g = self.g_name,
                                               b = self.b_name, delim = delim))

color_1 = Color("赤", "緑", "青")
color_2 = Color(g_name="midori")
color_1.name_print("|")
color_2.name_print()
color_1.r_name = "あか"
color_2.r_name = "あお"
color_1.name_print("#")
color_2.name_print("-")
