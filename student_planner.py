# ------------------------------------------------------
# Copyright (c) 2026 Antonis Koukoumelas. All rights reserved.
# Αυτό το project δημιουργήθηκε από Antonis Koukoumelas.
# ------------------------------------------------------

# student_planner.py

courses = {}

try:
    with open("planner.txt", "r") as f:
        for line in f:
            course, tasks = line.strip().split(":")
            courses[course] = tasks.split(",") if tasks else []
except FileNotFoundError:
    pass

def save_data():
    with open("planner.txt", "w") as f:
        for course, tasks in courses.items():
            f.write(f"{course}:{','.join(tasks)}\n")

def add_course():
    course = input("Όνομα μαθήματος: ")
    if course in courses:
        print("Μάθημα ήδη υπάρχει!")
    else:
        courses[course] = []
        print(f"{course} προστέθηκε!")
    save_data()

def add_task():
    course = input("Σε ποιο μάθημα; ")
    if course in courses:
        task = input("Περιγραφή εργασίας: ")
        courses[course].append(task)
        print("Εργασία προστέθηκε!")
    else:
        print("Μάθημα δεν υπάρχει!")
    save_data()

def view_courses():
    if not courses:
        print("Δεν υπάρχουν μαθήματα.")
    else:
        for course, tasks in courses.items():
            print(f"\n{course}:")
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")

while True:
    print("\n--- Student Planner ---")
    print("1. Προσθήκη μαθήματος")
    print("2. Προσθήκη εργασίας")
    print("3. Προβολή μαθημάτων")
    print("4. Έξοδος")
    
    choice = input("Επιλογή: ")
    if choice == "1":
        add_course()
    elif choice == "2":
        add_task()
    elif choice == "3":
        view_courses()
    elif choice == "4":
        save_data()
        print("Κλείσιμο προγράμματος. Τα δεδομένα σώθηκαν.")
        break
    else:
        print("Λανθασμένη επιλογή. Δοκίμασε ξανά.")
