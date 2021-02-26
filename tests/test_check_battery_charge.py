!pip install pytest ipython_pytest
import ipython_pytest
%load_ext ipython_pytest

%%pytest

def check_battery_charge():
  tesla = Tesla('S', 'Red')
  tesla.charge_battery()
  assert tesla.battery_charge == 100
