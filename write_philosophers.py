def main():
    write_philosophers = open("philosophers.txt", "w")
    write_philosophers.write("John Locke \n")
    write_philosophers.write("David Hume \n")
    write_philosophers.write("Edmund Burke \n")

    write_philosophers.close()


def add_my_name():
    outfile = open("philosophers.txt", "a")
    outfile.write("James Allen \n")

    outfile.close()


# use outfile instead of wirte_philsophers going forward

main()
add_my_name()
