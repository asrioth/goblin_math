from upgrade import Upgrade
from resourceManager import Resource

class Shop():
    def __init__(self, resource_manager):
        self.progress_bar_time_step = 1
        self.resource_manager = resource_manager
        self.time_upgrade = Upgrade("Eat Faster", 1, lambda cost: cost+1, 3, self.progress_bar_time_step, lambda base_value: base_value*2, Resource.CRUNCHES, self.buy_time_upgrade)
        self.upgrades = [self.time_upgrade]
    
    def buy_time_upgrade(self):
        if self.resource_manager.take_resource(self.time_upgrade.resource_type, self.time_upgrade.cost):
            if self.time_upgrade.upgrade():
                self.progress_bar_time_step = self.time_upgrade.base_value
            else:
                self.resource_manager.return_resource(self.time_upgrade.resource_type, self.time_upgrade.cost)
        return self.time_upgrade.cost
    
    def get_visible_upgrades(self):
        visible_upgrades = []
        for upgrade in self.upgrades:
            if upgrade.in_visibility_threshold(self.resource_manager.get_resource_value(upgrade.resource_type)):
                visible_upgrades.append(upgrade)
        return visible_upgrades
