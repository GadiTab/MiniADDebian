#!/usr/bin/python
from os import system
import pwd, grp
def m_menu():
    system("clear")
    print "################################################################# \nMade by: Gadi Tabak \n   Linux tiny Active Directory \n#################################################################"
    mmenu=raw_input("1) List of all users\n2) List of all groups\n3) Reset password\n4) Create new user\n5) Create new group\n6) List all mounts\n7) Mount a folder\n8) Add new command to .profile of a certain user\n9) Exit\nYour number: ")
    if mmenu=="1":
        l_users()
    elif mmenu=="2":
        l_groups()
    elif mmenu=="3":
        r_password()
    elif mmenu=="4":
        global c_user_again
        c_user_again = 0
        c_user()
    elif mmenu=="5":
        c_group()
    elif mmenu=="6":
        l_mounts()
    elif mmenu=="7":
        m_folder()
    elif mmenu=="8":
        n_cmd()
    elif mmenu=="9" or mmenu=="exit":
        print "Good Bye"
    else:
        m_menu()


def l_users():
    global l_users_user
    global l_users_again
    l_users_again=0
    l_users_i=0
    l_users_break=0
    system("clear")
    for p in pwd.getpwall():
        if p[2] >= 1000:
            l_users_user=p[0]
            l_users_i=int(l_users_i+1)
            print l_users_i, "-", l_users_user
    l_users_i += 1
    l_users_back=l_users_i
    print l_users_back,"- Main menu"
    l_users_i=0
    l_users_input=raw_input("User: ")
    for p in pwd.getpwall():
        if p[2] >= 1000:
            l_users_user=p[0]
            l_users_i += 1
            if l_users_input==str(l_users_back) or l_users_input.lower()=="back" or l_users_input.lower()=="main menu":
                l_users_break=1
                break
            elif l_users_input==str(l_users_i) or l_users_input==l_users_user:
                l_users_useroptions()
                break
    l_users_back -=1
    if l_users_break==1:
        m_menu()
    elif l_users_i == l_users_back:
        l_users()




def l_users_useroptions():
    global l_users_user
    global l_users_again
    global l_users_input
    system("clear")
    options="1) Show user Groups \n2) Show user id \n3) Show user aliases \n4) Add new alias \n5) Change password \n6) Back \n7) Main menu \n"
    print options, "Action: "
    if l_users_again==0:
        l_users_input=raw_input()
    if l_users_input=="1":
        print "{}'s Groups:".format(l_users_user)
        for g in grp.getgrall():
            for l_users_groups in g[3]:
                if l_users_groups == l_users_user:
                    print g[0]
        l_users_input=raw_input("What would you like to do next? ")
        l_users_again=1
        l_users_useroptions()
    elif l_users_input=="2":
        l_users_id=pwd.getpwnam(l_users_user).pw_uid
        print "{} ID is: {}".format(l_users_user,l_users_id)
        l_users_input = raw_input("What would you like to do next? ")
        l_users_again = 1
        l_users_useroptions()
    elif l_users_input=="3":
        print "{} use the next aliases:".format(l_users_user)
        l_users_aliases='grep /home/{}/.bashrc -e "^alias" | cut -d ":" -f 2-999'.format(l_users_user)
        system(l_users_aliases)
        l_users_input = raw_input("What would you like to do next? ")
        l_users_again = 1
        l_users_useroptions()
    elif l_users_input=="4":
        l_users_alias_alias=raw_input("Alias name: ")
        l_users_alias_cmd=raw_input("Will do the new command?: ")
        l_users_alias_newalias="echo \"alias {}='{}'\" >> /home/{}/.bashrc".format(l_users_alias_alias,l_users_alias_cmd,l_users_user)
        system(l_users_alias_newalias)
        l_users_input = raw_input("What would you like to do next? ")
        l_users_again = 1
        l_users_useroptions()
    elif l_users_input=="5":
        l_users_cpwd_user="passwd {}".format(l_users_user)
        system(l_users_cpwd_user)
        l_users_input = raw_input("What would you like to do next? ")
        l_users_again = 1
        l_users_useroptions()
    elif l_users_input=="6" or l_users_input.lower() == "back":
        l_users()
    elif l_users_input=="7":
        m_menu()
    else:
        l_users_useroptions()


def l_groups():
    global l_groups_group
    global l_groups_again
    l_groups_again = 0
    l_groups_i=0
    l_groups_break=0
    system("clear")
    for g in grp.getgrall():
        if g[2] >= 1000:
            l_groups_group=g[0]
            l_groups_i += 1
            print l_groups_i,"-",l_groups_group
    l_groups_i += 1
    l_groups_back = l_groups_i
    print l_groups_back,"- Main menu"
    l_groups_i = 0
    l_groups_input = raw_input("Group: ")
    for g in grp.getgrall():
        if g[2] >= 1000:
            l_groups_group=g[0]
            l_groups_i += 1
            if l_groups_input == str(l_groups_back) or l_groups_input.lower() == "back" or l_groups_input.lower() == "main menu":
                l_groups_break=1
            elif l_groups_input == str(l_groups_i) or l_groups_input == l_groups_group:
                l_groups_groupoptions()
    l_groups_back -=1
    if l_groups_break == 1:
        m_menu()
    elif l_groups_i == l_groups_back:
        l_groups()


def l_groups_groupoptions():
    global l_groups_group
    global l_groups_again
    global l_groups_input
    system("clear")
    options = "1) Show users in the group \n2) Show group id \n3) Add user to this group \n4) Back \n5) Main menu"
    print options
    if l_groups_again == 0:
        l_groups_input = raw_input("Action: ")
    if l_groups_input == "1":
        print "{}'s group members:".format(l_groups_group)
        for g in grp.getgrall():
            if g[0] == l_groups_group:
                print g[3]
        l_groups_input=raw_input("What would you like to do next? ")
        l_groups_again = 1
        l_groups_groupoptions()
    elif l_groups_input == "2":
        l_groups_id=grp.getgrnam(l_groups_group)
        print "{} ID is {}".format(l_groups_group,l_groups_id[2])
        l_groups_input = raw_input("What would you like to do next? ")
        l_groups_again = 1
        l_groups_groupoptions()
    elif l_groups_input == "3":
        system("clear")
        while True:
            l_groups_input=raw_input(("Which user would you like to add to the group {}? Type \'Back\' to return\nUser: ").format(l_groups_group))
            print ""
            if l_groups_input.lower() == "back":
                l_groups_groupoptions()
                break
            l_groups_adduser="addgroup {} {}".format(l_groups_input,l_groups_group)
            system(l_groups_adduser)
            print ""
    elif l_groups_input == "4":
        l_groups()
    elif l_groups_input == "5":
        m_menu()
    else:
        l_groups_groupoptions()


def r_password():
    system("clear")
    r_password_input=raw_input("Which user would you like to reset his password? Type \'Back\' to return.\nUser: ")
    if r_password_input.lower() == "back":
        m_menu()
    else:
        r_password_cmd = "passwd {}".format(r_password_input)
        system(r_password_cmd)
        r_password_question()


def r_password_question():
    r_password_answer=raw_input("Would you like to reset password to another user? Yes/No: ")
    if r_password_answer.lower() == "yes":
        r_password()
    elif r_password_answer.lower() == "no":
        m_menu()
    else:
        r_password_question()


def c_user():
    global c_user_input
    global c_user_again
    c_user_flag=0
    system("clear")
    options="1) Create user without home directory \n2) Create user without shell \n3) Create user with home directory and shell\n4) Back"
    print options
    if c_user_again == 0:
        c_user_input=raw_input("Action: ")
    if c_user_input == "1" or c_user_input == "2" or c_user_input == "3":
        c_user_user=raw_input("Username: ")
        for p in pwd.getpwall():
            if p[0] == c_user_user:
                c_user_flag = 1
                break
        if c_user_flag == 0:
            c_user_city = raw_input("The new user city: ")
            c_user_street = raw_input("The new user street: ")
            c_user_phone = raw_input("New user's phone: ")
            if c_user_input == "1":
                c_user_cmd="useradd -M -c \"{},{},{}\" {}".format(c_user_city,c_user_street,c_user_phone,c_user_user)
                c_user_password="passwd {}".format(c_user_user)
                system(c_user_cmd)
                system(c_user_password)
            elif c_user_input == "2":
                c_user_cmd = "useradd -m -d /home/{} -s /usr/sbin/nologin -c \"{},{},{}\" {}".format(c_user_user, c_user_city, c_user_street, c_user_phone, c_user_user)
                c_user_password = "passwd {}".format(c_user_user)
                system(c_user_cmd)
                system(c_user_password)
            elif c_user_input == "3":
                c_user_cmd = "useradd -m -d /home/{} -c \"{},{},{}\" {}".format(c_user_user, c_user_city, c_user_street, c_user_phone, c_user_user)
                c_user_password = "passwd {}".format(c_user_user)
                system(c_user_cmd)
                system(c_user_password)
            c_user_input = raw_input("What would you like to do next?\nAction: ")
            c_user_again = 1
            c_user()
        else:
            c_user_existed=raw_input("This user name is already taken. Would you like to try again? Yes/No: ")
            if c_user_existed.lower() == "no":
                m_menu()
            else:
                c_user()
    elif c_user_input.lower() == "back" or c_user_input == "4":
        m_menu()
    else:
        c_user()


def c_group():
    global c_group_flag
    c_group_flag = 0
    system("clear")
    c_group_input=raw_input("What group would you like to create? Type \'Back\' to return. \nAction: ")
    if c_group_input.lower() == "back":
        m_menu()
    else:
        for g in grp.getgrall():
            if g[0] == c_group_input:
                c_group_flag = 1
                break
        if c_group_flag == 0:
            c_group_cmd="addgroup {}".format(c_group_input)
            system(c_group_cmd)
            c_group_question()
        else:
            c_group_existed=raw_input("This group name is already taken. Would you like to try again? Yes/No: ")
            if c_group_existed.lower() == "no":
                m_menu()
            else:
                c_group()

def c_group_question():
    c_group_answer = raw_input("Would you like to create another group? Yes/No: ")
    if c_group_answer.lower() == "yes":
        c_group()
    elif c_group_answer.lower() == "no":
        m_menu()
    else:
        c_group_question()


def l_mounts():
    system("clear")
    l_mounts_input=raw_input("Please type a specific mount you would like to see OR type \"all\" to see all the mounts. Type \"back\" to return. \nAction: ")
    if l_mounts_input.lower() == "a" or l_mounts_input.lower() == "all" or l_mounts_input == "":
        print ""
        system("mount")
        l_mounts_input=raw_input("\nWhat would you like to do next?\n1) Search for a specific mount \n2) Mount a folder \n3) Unmount \n4) Back to main menu \nAction: ")
        if l_mounts_input=="1":
            l_mounts()
        elif l_mounts_input=="2":
            m_folder()
        elif l_mounts_input == "3":
            u_mount()
        elif l_mounts_input=="4" or l_mounts_input.lower() == "back":
            m_menu()
    elif l_mounts_input.lower() == "back":
        m_menu()
    else:
        print ""
        l_mounts_search="mount | grep {}".format(l_mounts_input)
        system(l_mounts_search)
        l_mounts_input = raw_input("\nWhat would you like to do next?\n1) Search for another specific mount \n2) Mount a folder \n3) Unmount \n4) Back to main menu \nAction: ")
        if l_mounts_input == "1":
            l_mounts()
        elif l_mounts_input == "2":
            m_folder()
        elif l_mounts_input == "3":
            u_mount()
        elif l_mounts_input == "4" or l_mounts_input.lower() == "back":
            m_menu()


def u_mount():
    u_mount_input=raw_input("\nWhat mount would you like to unmount? \nUnmount: ")
    u_mount_cmd="umount {}".format(u_mount_input)
    system(u_mount_cmd)
    u_mount_input = raw_input("\nWhat would you like to do next?\n1) Search for a specific mount \n2) Mount a folder \n3) Back to main menu \nAction: ")
    if u_mount_input == "1":
        l_mounts()
    elif u_mount_input == "2":
        m_folder()
    elif u_mount_input == "3" or u_mount_input.lower() == "back":
        m_menu()

def m_folder():
    system("clear")
    m_folder_question=raw_input("Would like you like to mount a device or a folder? \n1) Device \n2) Folder \n3) Back \nMount: ")
    if m_folder_question=="1":
        print ""
        system("ls /dev/sd* | cut -d / -f 3")
        m_folder_device=raw_input("\nWhat device would you like to mount? Type \"back\" to return to main menu\nDevice: ")
        if m_folder_device == "back":
            m_folder()
        else:
            m_folder_folder=raw_input("where do you wish to mount it? Please type the full path.\nPath: ")
            m_folder_mount="mount /dev/{} {}".format(m_folder_device, m_folder_folder)
            system(m_folder_mount)
            m_folder_input=raw_input("Would you like to mount another folder? Yes/No: ")
            if m_folder_input.lower() == "no":
                m_menu()
            else:
                m_folder()
    elif m_folder_question=="2":
        m_folder_mount=raw_input("What folder would you like to mount? Type \"Back\" to return. \nFolder: ")
        if m_folder_mount.lower() == "back":
            m_folder()
        else:
            m_folder_dest=raw_input("Where do you want to mount it? \nDestination: ")
            if m_folder_dest.lower() == "back":
                m_folder()
            else:
                m_folder_cmd="mount --bind {} {}".format(m_folder_mount, m_folder_dest)
                system(m_folder_cmd)
    elif m_folder_question.lower() == "back" or m_folder_question == "3":
        m_menu()
    else:
        m_folder()
    m_folder_next()


def m_folder_next():
    m_folder_question=raw_input("\nWhat would you like to do now? \n1) See mounts list \n2) Mount again \n3) Return to main menu \nAction: ")
    if m_folder_question == "1":
        l_mounts()
    elif m_folder_question == "2":
        m_folder()
    elif m_folder_question == "3":
        m_menu()
    else:
        m_folder_next()

def n_cmd():
    system("clear")
    n_cmd_i = 0
    for p in pwd.getpwall():
        if p[2] >= 1000:
            n_cmd_user=p[0]
            n_cmd_i += 1
            print n_cmd_i, "-", n_cmd_user
    n_cmd_i += 1
    n_cmd_back=n_cmd_i
    print n_cmd_back, "- Return to main menu"
    n_cmd_i=0
    n_cmd_input=raw_input("\nChoose a user you would like to add a command to his profile.\nUser: ")
    for p in pwd.getpwall():
        if p[2] >= 1000:
            n_cmd_user = p[0]
            n_cmd_i += 1
            if n_cmd_input == str(n_cmd_back) or n_cmd_input.lower() == "back":
                m_menu()
            elif n_cmd_input == n_cmd_user or n_cmd_input == str(n_cmd_i):
                n_cmd_add_cmd=raw_input("What command would you like to add? ")
                n_cmd_profile="echo \"{}\" >> /home/{}/.profile".format(n_cmd_add_cmd, n_cmd_user)
                system(n_cmd_profile)
    n_cmd_input=raw_input("What would you like to do now? \n1) Choose a user again \n2) Back to main menu \nAction: ")
    if n_cmd_input == "1":
        n_cmd()
    else:
        m_menu()

m_menu()