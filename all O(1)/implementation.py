class BestDataStructure:
    def __init__(self):
        self.main_map = {}
        #self.all_keys = set()
        self.available_keys = set()
        self.value_for_all = None

    def set(self, key, value):
        self.main_map[key] = value
        self.available_keys.add(key)

    def get(self, key):
        if key in self.main_map:
            if key in self.available_keys:
                return self.main_map[key]
            if self.value_for_all:
                return self.value_for_all
        return "No such key "

    def setAll(self, value):
        self.value_for_all = value
        self.available_keys.clear()