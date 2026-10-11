import time


def play_timer():
    while True:
        time_text = input("Enter time to count down (h:m:s): ")
        parts = time_text.split(":")

        if len(parts) != 3:
            print("Invalid format. Use hours:minutes:seconds.")
            continue

        try:
            hours, minutes, seconds = [int(part) for part in parts]
        except ValueError:
            print("Please enter numbers only.")
            continue

        if hours < 0 or not 0 <= minutes < 60 or not 0 <= seconds < 60:
            print("Invalid time. Check your hours, minutes, and seconds.")
            continue

        break

    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds >= 0:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        if total_seconds == 0:
            break

        time.sleep(1)
        total_seconds -= 1

    print("Time is up!")


play_timer()