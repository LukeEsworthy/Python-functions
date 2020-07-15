def run(*kids):
    for kid in kids:
        print(f"{kid} is running for dear life.")


def swing(*kids):
    for kid in kids:
        print(f"{kid} almost swung all the way around the swingset.")


def slide(*kids):
    for kid in kids:
        print(f"{kid}\'s hair is sticking straight out from the static electricity after going down the slide.")


def hide_and_seek(*kids):
    for kid in kids:
        print(f"{kid} is playing hide and seek with the others.")


run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")
