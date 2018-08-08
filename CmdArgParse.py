import sys


def process_args(argv):
    args = []
    l_arg = len(argv) - 1

    switches = []
    flags = []

    if l_arg >= 1:

        for i in range(1, l_arg + 1):
            arg = str(sys.argv[i]).strip()
            args.append(arg)

        while len(args) > 0:
            c_arg = args[0]
            if c_arg[0] == "-":
                if len(args) > 1:
                    sw = [c_arg, args[1]]
                    del (args[0])
                    del (args[0])
                else:
                    sw = [c_arg, None]
                    del (args[0])
                switches.append(sw)
            else:
                flags.append(c_arg)
                del (args[0])
    return (switches, flags)


if __name__ == "__main__":
    print(process_args(sys.argv))
