import time
import emoji


def switch_signal(denser_lane, seconds):
    print("Dynamic Signal Switching Phase" + '\033[0m')
    time.sleep(1)
    print('\033[1m' + '\n\033[99m' +
          "OPENING LANE-{}: ".format(str(denser_lane)) + '\033[0m')
    print(
        "----------------------------------------------------------------------------------"
    )
    if denser_lane == 1:
        print(
            "Lane 1                Lane 2                Lane 3                Lane 4"
        )
        time.sleep(1)
        print("  " + emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "                    " +
              emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n  " +
              emoji.emojize(":green_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n")
        print(
            "----------------------------------------------------------------------------------"
        )
        print('\033[1m' + '\n\033[99m' +
              "LANE-{} OPENED !".format(str(denser_lane)) + '\033[0m')
        print("\n Calculating Signal Open-Close Timing...")
        print('\033[0m' + '\n\033[99m' +
              "LANE-{} will CLOSE after {} seconds ".format(
                  str(denser_lane), str(seconds)) + '\033[0m',
              end="")
        while seconds:
            mins, secs = divmod(seconds, 60)
            print('\033[99m' + ".", end="")
            time.sleep(1)
            seconds -= 1
        print(
            "----------------------------------------------------------------------------------"
        )
        print('\033[1m' + '\n\033[99m' +
              "CLOSING LANE-{}: ".format(str(denser_lane)) + '\033[0m')
        print(
            "----------------------------------------------------------------------------------"
        )
        time.sleep(1)
        print()
        print(
            "Lane 1                Lane 2                Lane 3                Lane 4"
        )
        print("  " + emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "                    " +
              emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n")
    elif denser_lane == 2:
        print(
            "Lane 1                Lane 2                Lane 3                Lane 4"
        )
        time.sleep(1)
        print("  " + emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":green_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n")
        print('\033[1m' + '\n\033[99m' +
              "LANE-{} OPENED !".format(str(denser_lane)) + '\033[0m')
        print("\n Calculating Signal Open-Close Timing...")
        print('\033[0m' + '\n\033[99m' +
              "LANE-{} will CLOSE after {} seconds ".format(
                  str(denser_lane), str(seconds)) + '\033[0m',
              end="")
        while seconds:
            mins, secs = divmod(seconds, 60)
            print('\033[99m' + ".", end="")
            time.sleep(1)
            seconds -= 1
        print()
        print('\033[1m' + '\n\033[99m' +
              "CLOSING LANE-{}: ".format(str(denser_lane)) + '\033[0m')
        print(
            "----------------------------------------------------------------------------------"
        )
        time.sleep(1)
        print()
        print(
            "Lane 1                Lane 2                Lane 3                Lane 4"
        )
        print("  " + emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "                    " +
              emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n")
    elif denser_lane == 3:
        print(
            "Lane 1                Lane 2                Lane 3                Lane 4"
        )
        time.sleep(1)
        print("  " + emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":green_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n")
        print('\033[1m' + '\n\033[99m' +
              "LANE-{} OPENED !".format(str(denser_lane)) + '\033[0m')
        print("\n Calculating Signal Open-Close Timing...")
        print('\033[0m' + '\n\033[99m' +
              "LANE-{} will CLOSE after {} seconds ".format(
                  str(denser_lane), str(seconds)) + '\033[0m',
              end="")
        while seconds:
            mins, secs = divmod(seconds, 60)
            print('\033[99m' + ".", end="")
            time.sleep(1)
            seconds -= 1
        print()
        print('\033[1m' + '\n\033[99m' +
              "CLOSING LANE-{}: ".format(str(denser_lane)) + '\033[0m')
        print(
            "----------------------------------------------------------------------------------"
        )
        time.sleep(1)
        print()
        print(
            "Lane 1                Lane 2                Lane 3                Lane 4"
        )
        print("  " + emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "                    " +
              emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n")
    elif denser_lane == 4:
        print(
            "Lane 1                Lane 2                Lane 3                Lane 4"
        )
        time.sleep(1)
        print("  " + emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "                    " +
              emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":green_circle:") + "\n")
        print('\033[1m' + '\n\033[99m' +
              "LANE-{} OPENED !".format(str(denser_lane)) + '\033[0m')
        print("\n Calculating Signal Open-Close Timing...")
        print('\033[0m' + '\n\033[99m' +
              "LANE-{} will CLOSE after {} seconds ".format(
                  str(denser_lane), str(seconds)) + '\033[0m',
              end="")
        while seconds:
            mins, secs = divmod(seconds, 60)
            print('\033[99m' + ".", end="")
            time.sleep(1)
            seconds -= 1
        print()
        print('\033[1m' + '\n\033[99m' +
              "CLOSING LANE-{}: ".format(str(denser_lane)) + '\033[0m')
        print(
            "----------------------------------------------------------------------------------"
        )
        time.sleep(1)
        print()
        print(
            "Lane 1                Lane 2                Lane 3                Lane 4"
        )
        print("  " + emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "                    " +
              emoji.emojize(":red_circle:") + "                   " +
              emoji.emojize(":red_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n  " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "                    " +
              emoji.emojize(":white_circle:") + "                   " +
              emoji.emojize(":white_circle:") + "\n")

    print('\033[0m' + '\n\033[99m' +
          "LANE-{} is now CLOSED ".format(str(denser_lane) + '\033[0m'))


# def avg_signal_oc_time(lane_count):
#     if lane_count > 50:
#         return 20
#     elif lane_count > 35:
#         return 15
#     elif lane_count > 20:
#         return 10
#     elif lane_count <= 20:
#         return 5
