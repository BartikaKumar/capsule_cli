from datetime import date
import json
from pathlib import Path
import uuid
import subprocess

base=Path.home()/".local"/"share"/"capsule_cli" #.local/share is for storing app data by linux convention

def add_capsule(args):

    base.mkdir(parents=True,exist_ok=True) # create directories if not present

    today=date.today()
    opendate=date.fromisoformat(args.after) if args.after else None
    
    locked=False
    
    if opendate:
        if today >= opendate:
            print("Storing as a normal capsule because open date has to be in the future.")
            opendate = None
        else:
            locked = True

    p=base/"index.json"
    if p.exists():
        data=json.loads(p.read_text())
    else:
        data=[]
    
    capsule_id=str(uuid.uuid4())
    new_data={
        "id":capsule_id,
        "on":str(today),
        "after":args.after if locked else None,
        "locked":locked,
        "name":args.name if args.name else f"Capsule {today.isoformat()}",
    }

    data.append(new_data)
    p.write_text(json.dumps(data,indent=4))

    (base/"notes").mkdir(exist_ok=True) # create notes directory if not present
    n=base/ "notes" / f"{capsule_id}.md"
    n.write_text(f"# {new_data["name"]}\n\n### Written on {str(today)},\n\n{args.text}\n")

    print(f"Capsule added: {new_data["name"]}")
    print(f"ID: {capsule_id}")
    

def list_capsule(args):

    p=base/"index.json"
    if p.exists():
        data=json.loads(p.read_text())
    else:
        data=[]

    if len(data)==0:
        print("You have no capsules")
        return

    print(f"You have {len(data)} capsules:\n")
    print("Capsule Name -> ID -> locked status\n")
    for note in data:
        print(f"{note["name"]} -> {note["id"]} -> {"Locked" if note["locked"] else "Unlocked"}")

def remove_capsule(args):

    capsule_id=args.id

    p=base/"index.json"
    if p.exists():
        data=json.loads(p.read_text())
    else:
        data=[]

    if len(data)==0:
        print("You have no capsules")
        return

    old_len=len(data)
    data=[note for note in data if note["id"]!=capsule_id]

    if(len(data)==old_len):
        print("Invalid ID")
        return

    p.write_text(json.dumps(data, indent=4))

    n=base/ "notes" / f"{capsule_id}.md"
    if n.exists():
        n.unlink()
    
    print("Capsule removed successfully")

def open_capsule(args):
    
    capsule_id=args.id

    p=base/"index.json"
    if p.exists():
        data=json.loads(p.read_text())
    else:
        data=[]

    if len(data)==0:
        print("You have no capsules")
        return

    for note in data:
        if note["id"]==capsule_id:

            today=date.today()
            opendate=date.fromisoformat(note["after"]) if note["after"] else None
            if opendate and today>=opendate:
                note["locked"]=False

            if note["locked"]:
                print(f"This note is locked. It will open on {note["after"]}")
                return

            p.write_text(json.dumps(data, indent=4))

            n=base/ "notes" / f"{capsule_id}.md"
            if not n.exists():
                print("Note is missing")
                return
            subprocess.run(["xdg-open", str(n)])

            return
        
    print("Invalid ID")