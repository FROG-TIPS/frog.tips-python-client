from frogtips import api, constants, frogsay
import sys
import getopt


def main():
    """Process arguments and display output accordingly."""

    # main() /should/ take sys.argv as its argument. However, since main()
    # is an entry point for this application (see setup.py), we instead have to
    # assign sys.argv to argv /after/ we're inside main().
    argv = sys.argv

    # Short and long options for getopt. For the appropriate syntax to use
    # here, see https://pymotw.com/3/getopt/
    shortopts = "afhrn:s:t:vw"
    longopts = ["about",
                "frogsay",
                "help",
                "random",
                "name=",
                "submit=",
                "tip=",
                "version",
                "warranty"]

    try:
        options, arguments = getopt.getopt(argv[1:], shortopts, longopts)
    except getopt.GetoptError:
        print(constants.HELP)
        sys.exit(2)

    # Display help message if user failed to supply options
    if options == []:
        print(constants.HELP)
        sys.exit()

    # If --about, --help, or --version is anywhere in the options list, print
    # the appropriate message and exit.
    for option, argument in options:
        if option in ("-a", "--about"):
            print(constants.LONG_DESCRIPTION)
            sys.exit()

        if option in ("-h", "--help"):
            print(constants.HELP)
            sys.exit()

        if option in ("-v", "--version"):
            print(constants.APPLICATION_NAME + " " + constants.VERSION)
            sys.exit()

        if option in ("-w", "--warranty"):
            print(constants.WARRANTY)
            sys.exit()

    # Now check for --frogsay and --name (which can be used in combination with
    # the remaining options).
    frogsay_selected = False

    for option, argument in options:
        if option in ("-f","--frogsay"):
            frogsay_selected = True

        if option in ("-n","--name"):
            username = argument
            api.Credentials(username)

    # Finally, check for the remaining options, all of which are mutually
    # exclusive.
    for option, argument in options:
        if option in ("-r","--random"):
            tips = api.Tips()
            tip = tips.get_next_tip()
            if frogsay_selected:
                frogsay.say(tip.get_formatted_tip(), tip.get_id())
            else:
                url = "https://" + constants.FROG_TIPS_DOMAIN + \
                      "/#" + str(tip.get_id())
                print(tip.get_formatted_tip() + " " + url)
            sys.exit()

        if option in ("-t","--tip"):
            tip = api.Tip(int(argument))
            if frogsay_selected:
                frogsay.say(tip.get_formatted_tip(), tip.get_id())
            else:
                url = "https://" + constants.FROG_TIPS_DOMAIN + \
                      "/#" + str(tip.get_id())
                print(tip.get_formatted_tip() + " " + url)
            sys.exit()

        if option in ("-s","--submit"):
            new_tip_text = argument
            new_tip = api.Tip()
            new_tip.submit_tip(new_tip_text)
            if new_tip.get_id() > 0:
                print("Successfully added your FROG tip:\n")
                if frogsay_selected:
                    frogsay.say(new_tip.get_formatted_tip(), new_tip.get_id())
                else:
                    url = "https://" + constants.FROG_TIPS_DOMAIN + \
                          "/#" + str(new_tip.get_id())
                    print(new_tip.get_formatted_tip() + " " + url)
                print("\n" + "It may take a while for our moderation team " +
                      " to look at and approve your FROG tip.")
            else:
                print("Something went wrong adding your FROG tip.")
            sys.exit()


if __name__ == "__main__":
    main()
