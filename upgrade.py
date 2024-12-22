class Upgrade():
    def __init__(self, name, cost, cost_step, max, base_value, base_value_step, resource_type, shop_action):
        self.name = name
        self.cost = cost
        self.resource_type = resource_type
        self.cost_step = cost_step
        self.max = max
        self.current = 0
        self.base_value = base_value
        self.base_value_step = base_value_step
        self.shop_action = shop_action

    def purchase(self):
        return self.shop_action()

    def is_maxed(self):
        return self.current >= self.max
    
    def in_visibility_threshold(self, resource):
        return resource < self.max * self.cost

    def upgrade(self):
        if self.current < self.max:
            self.cost = self.cost_step(self.cost)
            self.base_value = self.base_value_step(self.base_value)
            self.current += 1
            return True
        else:
            return False