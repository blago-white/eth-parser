import time


class PriceLogger:
    time_logs = dict()

    def add_log(self, log_value: float):
        self.time_logs.update({time.time(): log_value})

    def delete_latest_log(self):
        del self.time_logs[list(self.time_logs.keys())[0]]

    def get_log_time(self, log_number: int):
        return list(self.time_logs.keys())[log_number]

    def get_log_value(self, log_number: int):
        return self.time_logs[list(self.time_logs.keys())[log_number]]
