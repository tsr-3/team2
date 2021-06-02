# --- RaspberryPi main script --- #

import datetime
import dateutil.praser

# -- main function -- #
def main():
    # read save file
    while True:
        idm = cardreader()
        result = comp(idm, students, lect_time)
        # comp(idm:str, students:[str], lect_time:{start:datetime,end:datetime,late:datetime})
        # monitor
        # datawrite()

# -- onexec -- #
if __name__ == '__main__':
    main()
