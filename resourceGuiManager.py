import tkinter as tk
from stringVar import StringVar
from label import Label
from shopButton import ShopButton

class ResourceGuiManager():
    def __init__(self, window, resource_manager):
        self.resource_manager = resource_manager
        self.resource_label = None
        self.window = window
        self._create_resource_view()
        self.event = "<<update_resouce_display>>"
        self.window.root.bind(self.event, lambda event: self.update_display())
        self.shops = []
        self.shop_frame = tk.Frame(self.window.canvas, bg="green")
        self.shop_frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

    def add_shop(self, shop):
        self.shops.append(shop)
        upgrades = shop.get_visible_upgrades()
        for upgrade in upgrades:
            shop_button = ShopButton(self.shop_frame, upgrade)
            shop_button.pack(20, 20, tk.LEFT)

    def _create_resource_view(self):
        frame = tk.Frame(self.window.canvas, bg="green")
        frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        resource_display = StringVar(self.resource_manager.display)
        self.resource_label = Label(frame, resource_display)
        self.resource_label.pack(20, 20, tk.TOP)

    def update_display(self):
        self.resource_label.update_text(self.resource_manager.display)