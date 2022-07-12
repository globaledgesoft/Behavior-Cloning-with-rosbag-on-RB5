import subprocess
import os

def list_topics():
    subprocess.call(["ros2", "topic", "list"])

def record_bag():
    list_topics()

    inp = input("Enter your topic (/TOPIC_NAME or ALL):")

    print("Press CTRL+C to stop the recording...")
    if "ALL" in inp:
        subprocess.call(["ros2", "bag", "record", "-a"])
    else:
        subprocess.call(["ros2", "bag", "record", inp])
def list_bags():
    PATH = "./recorded_bags"
    os.listdir(PATH)


if __name__ == "__main__":
    while True:
        func = [record_bag, list_topics, list_bags]

        print ("Select Option given below:")
        print("1. Record the data")
        print("2. List of topics")
        print("3. List of recorded bag")
        inp = int(input("Enter your choice:"))-1

        func[inp]()

