import subprocess
import os

def info_bag():
    try:
        dirs = os.listdir("./")
        for name in dirs:
            if ".py" in name:
                continue
            print(name)
    except:
        print("No Rosbag record file found! ")
        return

    inp = input("Enter your bagname for info:")
    subprocess.call(["ros2", "bag", "info", inp])

def play_bag():
    try:
        dirs = os.listdir("./")
        for name in dirs:
            if ".py" in name:
                continue
            print(name)
    except:
        print("No Rosbag record file found! ")
        return

    inp = input("Enter your bagname for playback:")

    print("Press CTRL+C to stop the playing...")
    subprocess.call(["ros2", "bag", "play", inp])

def list_bags():
    try:
        dirs = os.listdir("./")
        for name in dirs:
            if ".py" in name:
                continue
            print(name)
    except:
        print("No Rosbag record file found! ")


if __name__ == "__main__":
    while True:
        func = [play_bag, info_bag, list_bags]

        print ("Select Option given below:")
        print("1. Playback the data")
        print("2. Get info of bag")
        print("3. List all bags")
        inp = int(input("Enter your choice:"))-1

        func[inp]()

