# NOTE: This starter code is intentionally incomplete so all tests fail.
# Students will need to define the parser, subcommands, and handlers.

import argparse

tasks_list = []

def add_task(args):
    tasks_list.append(args.description)
    print(f"✅ Task added: {args.description}")
    for task in tasks_list:
        print(task)

def list_tasks(args):
    print("📋 Listing all tasks...")
    for task in tasks_list:
        print(task)

# TODO: Define the main() function
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add", help="Add new a task")
    add_parser.add_argument("description", help="Description of the task")
    add_parser.set_defaults(func=add_task)

    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.set_defaults(func=list_tasks)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

# Inside main():
# - Create an ArgumentParser with a helpful description
# - Add subparsers for "add" and "list" commands
# - For "add", require a "description" argument and set its handler
# - For "list", just set the handler to list_tasks
# - Parse the arguments and call the appropriate handler (if exists)

