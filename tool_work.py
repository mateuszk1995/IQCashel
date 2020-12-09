import os
from datetime import datetime, date, timedelta


def construct_command():

    # TODO confirm the date formatting amongst other variables with PB
    yesterday_date = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
    timeout_seconds = 10
    user = "root"
    password = "qualcorpDec09"
    ssh_command = "TBC"

    with open('iqcashel_commands.txt', 'r') as commands_table:
        commands = [command.rstrip() for command in commands_table]

    # TODO add arguments to all necessary commands
    commands[5] = "GETLOGS -since {}".format(yesterday_date)
    commands[8] = "SSH -user:{} -pass:{} -command:{}".format(user, password, ssh_command)
    commands[13] = "FRTRIG -check -timeout:{}".format(timeout_seconds)
    commands[14] = "HEALTHCHECK -since {}".format(yesterday_date)

    return commands


def construct_ip_address():

    with open('ip_address_list.txt', 'r') as ip_table:
        lines = [line.rstrip() for line in ip_table]

    return lines


def run_test():

    path = "C:\\Qualitrol\\iQ-Plus\\iQ-PlusServer"
    os.chdir(path)
    today_date = date.today()

    #   iterate each command over every IP address, print results to seperate files
    for line in ip_addresses:
        for appended in appended_commands:
            filename = ("{}_{}_{}_test.txt".format(today_date, line, appended))
            with open(os.path.join("C:\\2020 Files\\PythonUdemyCourse\\IQCashel", filename), "w") as file1:
                file1.write("{} {} {} test\n".format(today_date, line, appended))
                print(os.system("iqcashel {} {}".format(line, appended)), file=file1)


if __name__ == '__main__':
    appended_commands = construct_command()
    ip_addresses = construct_ip_address()
    run_test()
