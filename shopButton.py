from button import Button

class ShopButton(Button):
    def __init__(self, root, upgrade):
        self.first_name = upgrade.name
        self.format_name(upgrade.cost)
        super().__init__(root, self.name)
        self.upgrade = upgrade
        self.upgrade_event = "<<update_time_step>>"
        self.resource_event = "<<update_resouce_display>>"

    def clicked(self):
        new_cost = self.upgrade.purchase()
        if self.upgrade.is_maxed():
            self.destroy()
        else:
            self.format_name(new_cost)
            self.button.config(text=self.name)
            self.root.event_generate(self.upgrade_event)
            self.root.event_generate(self.resource_event)

    def format_name(self, cost):
        self.name = f"{self.first_name}: {cost}"