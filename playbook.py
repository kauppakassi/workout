import vlc
import time

def main():
    people = 3
    for idx in range(people):
        print()
        print(f"Get ready for set {idx + 1} / {people}")
        playsound("tauko15s.m4a")
        countdown(15)
        print()
        print(f"Start set {idx + 1} / {people}")
        playsound("treeni.m4a")
        countdown(22.5)
        print()
        print(f"Midway")
        playsound("puoli.m4a")
        countdown(22.5)


    print("Finished")
    playsound("loppuu.m4a")
    countdown(5)


def playsound(filename):
    p = vlc.MediaPlayer(filename)
    p.play()


def countdown(seconds):
    time_start = time.time()
    prev_second = 0
    print(f"{prev_second}/{seconds}")
    while time.time() - time_start < seconds:
        time.sleep(0.2)
        time_ran = time.time() - time_start
        if time_ran > prev_second + 5:
            prev_second += 5
            print(f"{prev_second}/{seconds}")
    if prev_second != seconds:
        print(f"{prev_second + 5}/{seconds}")


main()