class Counter:
    counter = 0

    def update_counter(self):
        self.counter += 1

    def reset_counter(self):
        self.counter = 0

    def get_counter_value(self):
        return self.counter
