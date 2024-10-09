import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'Data'))

from Data.Start import Start


if __name__ == '__main__':
    # company.login('17', 'Сергей')
    # company.add_user('14', 'Светлана', 5)
    start = Start()
