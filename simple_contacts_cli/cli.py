#!/usr/bin/env python3
import argparse
import json

contacts = {
}

def saveTofile():
    with open("contacts.json", "w") as contactFile:
        json.dump(contacts, contactFile)
        contactFile.close()

def addContact(name, email, phone):
    try:
        if (name.lower) not in contacts.keys(): 
            contacts.update({str((name).lower()) : (email) + ", " + (phone) + "\n"})
        elif (name.lower) in contacts.keys(): 
            overwrite = input(f"contact {(name).lower} already exists, overwrite? \ny/n \n")
            if overwrite == "y": 
                contacts.update({str((name).lower()) : (email) + ", " + (phone) + "\n"})
                print("contact overwritten")
            elif overwrite == "n": 
                print("contact not overwritten")
            else: addContact(name, email, phone)
    except ValueError:
        print("error.")
        addContact(name, email, phone)
    saveTofile()

def loadIn():
    with open("contacts.json", "r") as contactFile:
        try:
            contacts.update(json.load(contactFile))
        except json.decoder.JSONDecodeError:
            pass
            
def main():
    parser = argparse.ArgumentParser(
        prog='contacts',
        usage='%(prog)s [options] name email "phone"',
        description='''very simple command line contact manager'''
        )
            
    subparsers = parser.add_subparsers(dest="command")
    add = subparsers.add_parser("add", help="add a new contact")
    view = subparsers.add_parser("view", help="view all contacts")
    search = subparsers.add_parser("search", help="search for a contact by name")
    delete = subparsers.add_parser("delete", help="delete a contact")
    add.add_argument("name")
    add.add_argument("email")
    add.add_argument("phone")
    search.add_argument("name")
    delete.add_argument("name")
    
    args = parser.parse_args()

    if args.command == "add":
        addContact(args.name, args.email, args.phone)
    elif args.command == "view":
        for y in contacts:
            print(y + ": " + contacts.get(y))
        saveTofile()
    elif args.command == "search":
        if (args.name).lower in contacts:
                 print("\n" + (args.name) + ": " + contacts.get(args.name))
        else: print("\nnot a contact. yet.")
    elif args.command == "delete":
        if (args.name).lower in contacts:
            sureCheck = input("are you sure? \ny/n \n")
            if sureCheck == "y":
                del contacts[args.name]
                saveTofile()
                print("\nno longer a contact.")
            else: print(f"\n{args.name} not deleted")
        else: print("\nalready not a contact.")
    else: parser.print_help()

def start():
    try:
        loadIn()
    except IndexError:
        print("error reading file")
    except FileNotFoundError:
        myFile = open("contacts.json", "w")
    main()
