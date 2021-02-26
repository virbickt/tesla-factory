class Tesla:
    def __init__(self, model: str, color: str, efficiency: float = 0.3, autopilot: bool = False):
        self.__model = model
        self.__color = color
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__autopilot = autopilot
        self.__efficiency = efficiency
        
    @property
    def color(self) -> str:
      return self.__color

    @property
    def seats_count(self) -> int:
      return self.__seats_count

    @property
    def model(self) -> str:
      return self.__model

    @property
    def is_locked(self) -> bool:
      return self.__is_locked

    @property
    def battery_charge(self) -> float:
      return self.__battery_charge
    
    @is_locked.setter
    def lock(self) -> bool:
      if self.__is_locked == False:
        self.__is_locked = True
        return f'Beep'
      return f"Car is already locked!"

    @is_locked.setter
    def unlock(self) -> bool:
      if self.__is_locked:
        self.__is_locked = False
        return f'Beep'
      return f"Car is already unlocked!"

    def open_doors(self) -> str:
      if self.__is_locked == False:
        return "Doors opens sideways"
      return "Car is locked!"

    @color.setter
    def color(self, color: str) -> str:
      """Takes string, sets color to input value"""
      self.__color = color

    @seats_count.setter
    def seats_count(self, seats_count: int) -> int:
      if seats_count < 2:
        return f"Seats count cannot be lower than 2!"
      self.__seats_count = seats_count

    def welcome(self) -> str:
      raise NotImplementedError

    def autopilot(self, obstacle: str) -> str:
        """Takes string, returns string if autopilot is set to True; else returns string with info message"""
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {obstacle}".format(self, obstacle)
        return "Autopilot is not available"

    def check_battery_level(self) -> str:
      return f"Battery charge level is " + str(self.__battery_charge) + "%"
        
    def charge_battery(self):
        """Sets battery_charge to 100, runs check_battery_level, returns string with battery level"""
        self.__battery_charge = 100
        self.check_battery_level()

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge = round(self.__battery_charge - battery_discharge_percent, 1)
            self.check_battery_level()
        return f"Battery charge level is too low!"
