!pip install pytest ipython_pytest
import ipython_pytest
%load_ext ipython_pytest

%%pytest

def check_if_no_autopilot():
  tesla = Tesla('S', 'Red')
  assert tesla.autopilot('signpost') == 'Autopilot is not available'
