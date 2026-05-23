import argparse
from .commands import *

commands=[
    {
        "name":"add",
        "help":"Add a capsule",
        "func":add_capsule,
        "arguments":[
            {
                "name":["text"],
                "help":"Capsule text",
            },
            {
                "name":["--after","-a"],
                "help": "Date after which capsule can be opened in YYYY-MM-DD format"
            },
            {
                "name":["--name","-n"],
                "help":"Name of the capsule",
            }
        ]
    },
    {
        "name":"list",
        "help":"List capsules",
        "func":list_capsule,
    },
    {
        "name":"remove",
        "help":"Remove a capsule",
        "func":remove_capsule,
        "arguments":[
            {
                "name":["id"],
                "help":"Capsule ID"
            }
        ]
    },
    {
        "name":"open",
        "help":"Open a capsule",
        "func":open_capsule,
        "arguments":[
            {
                "name":["id"],
                "help":"Capsule ID"
            }
        ]
    }
]

def main():

    parser= argparse.ArgumentParser(
        description="A simple CLI time capsule",
    )

    subparsers= parser.add_subparsers(dest="command")
    
    for command in commands:

        cmd_parser= subparsers.add_parser(
            command["name"],
            help=command["help"]
        )

        cmd_parser.set_defaults(func=command["func"])

        if "arguments" in command:
            for arg in command["arguments"]:
                cmd_parser.add_argument(
                    *arg["name"], #unpacking
                    help=arg["help"],
                )

    args= parser.parse_args()

    if args.command == None:
        parser.print_help()
    else:
        args.func(args)