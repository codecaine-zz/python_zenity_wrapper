#!/usr/bin/env python3
"""Demo: CRUD Operations Form (Contact Management System)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, FormField, FormsOptions, ListOptions, QuestionOptions, InfoOptions
    import json
    from datetime import datetime
except ImportError as e:
    print(f"Error: Failed to import required modules: {e}", file=sys.stderr)
    sys.exit(1)

# Simple in-memory data store
contacts = [
    {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "phone": "555-0101", "role": "Developer"},
    {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "phone": "555-0102", "role": "Designer"},
    {"id": 3, "name": "Carol White", "email": "carol@example.com", "phone": "555-0103", "role": "Manager"},
]
next_id = 4

try:
    zenity = Zenity()
    
    def show_menu():
        """Display main menu and return user choice"""
        try:
            choice = zenity.list(
                "Select a CRUD operation:",
                ["Select", "Operation", "Description"],
                [
                    [False, "CREATE", "Add a new contact"],
                    [False, "READ", "View all contacts"],
                    [False, "UPDATE", "Modify existing contact"],
                    [False, "DELETE", "Remove a contact"],
                    [False, "SEARCH", "Find contacts"],
                    [False, "EXIT", "Quit the application"],
                ],
                ListOptions(
                    title="CRUD Demo - Contact Management",
                    radiolist=True,
                    width=600,
                    height=400
                )
            )
            return choice
        except:
            return None
    
    def create_contact():
        """Create a new contact"""
        global next_id
        
        result = zenity.forms(
            [
                FormField(type='entry', label='Full Name'),
                FormField(type='entry', label='Email Address'),
                FormField(type='entry', label='Phone Number'),
                FormField(
                    type='combo',
                    label='Role',
                    values=['Developer', 'Designer', 'Manager', 'Analyst', 'Tester', 'DevOps', 'Other']
                ),
                FormField(type='multiline', label='Notes (Optional)')
            ],
            FormsOptions(
                title="CREATE - New Contact",
                text="Enter contact information:",
                separator="|",
                width=550,
                height=600
            )
        )
        
        if result.button == 'ok' and result.values:
            name, email, phone, role, notes = result.values
            
            # Validation
            if not name or not email:
                zenity.error(
                    "Name and Email are required fields!",
                    InfoOptions(title="Validation Error", width=400)
                )
                return False
            
            if email and '@' not in email:
                zenity.warning(
                    "Email format appears to be invalid!",
                    InfoOptions(title="Warning", width=400)
                )
            
            # Create new contact
            new_contact = {
                "id": next_id,
                "name": name,
                "email": email,
                "phone": phone or "N/A",
                "role": role or "Other",
                "notes": notes or "",
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            contacts.append(new_contact)
            next_id += 1
            
            zenity.info(
                f"✓ Contact created successfully!\n\nName: {name}\nEmail: {email}\nID: {new_contact['id']}",
                InfoOptions(title="Success", width=400)
            )
            return True
        
        return False
    
    def read_contacts():
        """Display all contacts"""
        if not contacts:
            zenity.info(
                "No contacts found in the database.",
                InfoOptions(title="READ - View Contacts", width=400)
            )
            return
        
        # Prepare data for display
        contact_data = []
        for contact in contacts:
            contact_data.append([
                False,
                str(contact['id']),
                contact['name'],
                contact['email'],
                contact['phone'],
                contact['role']
            ])
        
        try:
            zenity.list(
                f"Total Contacts: {len(contacts)}",
                ["Select", "ID", "Name", "Email", "Phone", "Role"],
                contact_data,
                ListOptions(
                    title="READ - All Contacts",
                    checklist=True,
                    width=800,
                    height=500
                )
            )
        except:
            # User cancelled the view
            pass
    
    def update_contact():
        """Update an existing contact"""
        if not contacts:
            zenity.info(
                "No contacts available to update.",
                InfoOptions(title="UPDATE", width=400)
            )
            return False
        
        # Select contact to update
        contact_list = []
        for contact in contacts:
            contact_list.append([
                False,
                str(contact['id']),
                contact['name'],
                contact['email']
            ])
        
        try:
            selected = zenity.list(
                "Select a contact to update:",
                ["Select", "ID", "Name", "Email"],
                contact_list,
                ListOptions(
                    title="UPDATE - Select Contact",
                    radiolist=True,
                    width=600,
                    height=400
                )
            )
        except:
            # User cancelled
            return False
        
        if not selected:
            return False
        
        # Find the contact
        contact_id = int(selected.split('|')[0] if '|' in selected else selected)
        contact = next((c for c in contacts if c['id'] == contact_id), None)
        
        if not contact:
            zenity.error(
                "Contact not found!",
                InfoOptions(title="Error", width=400)
            )
            return False
        
        # Show update form with current values
        result = zenity.forms(
            [
                FormField(type='entry', label='Full Name'),
                FormField(type='entry', label='Email Address'),
                FormField(type='entry', label='Phone Number'),
                FormField(
                    type='combo',
                    label='Role',
                    values=['Developer', 'Designer', 'Manager', 'Analyst', 'Tester', 'DevOps', 'Other']
                ),
                FormField(type='multiline', label='Notes')
            ],
            FormsOptions(
                title=f"UPDATE - Edit Contact (ID: {contact['id']})",
                text=f"Current: {contact['name']}\nModify the fields you want to update:",
                separator="|",
                width=550,
                height=600
            )
        )
        
        if result.button == 'ok' and result.values:
            name, email, phone, role, notes = result.values
            
            # Update only provided fields
            if name:
                contact['name'] = name
            if email:
                if '@' not in email:
                    zenity.warning(
                        "Email format appears to be invalid!",
                        InfoOptions(title="Warning", width=400)
                    )
                contact['email'] = email
            if phone:
                contact['phone'] = phone
            if role:
                contact['role'] = role
            if notes:
                contact['notes'] = notes
            
            contact['modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            zenity.info(
                f"✓ Contact updated successfully!\n\nID: {contact['id']}\nName: {contact['name']}\nEmail: {contact['email']}",
                InfoOptions(title="Success", width=400)
            )
            return True
        
        return False
    
    def delete_contact():
        """Delete a contact"""
        if not contacts:
            zenity.info(
                "No contacts available to delete.",
                InfoOptions(title="DELETE", width=400)
            )
            return False
        
        # Select contact to delete
        contact_list = []
        for contact in contacts:
            contact_list.append([
                False,
                str(contact['id']),
                contact['name'],
                contact['email'],
                contact['phone']
            ])
        
        try:
            selected = zenity.list(
                "Select a contact to delete:",
                ["Select", "ID", "Name", "Email", "Phone"],
                contact_list,
                ListOptions(
                    title="DELETE - Select Contact",
                    radiolist=True,
                    width=700,
                    height=400
                )
            )
        except:
            # User cancelled
            return False
        
        if not selected:
            return False
        
        # Find the contact
        contact_id = int(selected.split('|')[0] if '|' in selected else selected)
        contact = next((c for c in contacts if c['id'] == contact_id), None)
        
        if not contact:
            zenity.error(
                "Contact not found!",
                InfoOptions(title="Error", width=400)
            )
            return False
        
        # Confirm deletion
        try:
            confirm_choice = zenity.list(
                f"Are you sure you want to delete this contact?\n\n"
                f"ID: {contact['id']}\n"
                f"Name: {contact['name']}\n"
                f"Email: {contact['email']}\n\n"
                f"This action cannot be undone!",
                ["Choice"],
                [["Yes, Delete"], ["Cancel"]],
                ListOptions(
                    title="Confirm Deletion",
                    height=300,
                    hide_header=True
                )
            )
            confirm = (confirm_choice == "Yes, Delete")
        except:
            confirm = False
        
        if confirm:
            contacts.remove(contact)
            zenity.info(
                f"✓ Contact deleted successfully!\n\nDeleted: {contact['name']}",
                InfoOptions(title="Success", width=400)
            )
            return True
        
        return False
    
    def search_contacts():
        """Search for contacts"""
        from zenity_wrapper import EntryOptions
        
        try:
            search_term = zenity.entry(
                "Enter search term (name, email, or phone):",
                EntryOptions(
                    title="SEARCH - Find Contacts",
                    entry_text=""
                )
            )
        except:
            # User cancelled the search
            return
        
        if not search_term:
            return
        
        # Search in name, email, and phone
        results = []
        search_lower = search_term.lower()
        for contact in contacts:
            if (search_lower in contact['name'].lower() or 
                search_lower in contact['email'].lower() or 
                search_lower in contact['phone'].lower()):
                results.append([
                    False,
                    str(contact['id']),
                    contact['name'],
                    contact['email'],
                    contact['phone'],
                    contact['role']
                ])
        
        if results:
            try:
                zenity.list(
                    f"Found {len(results)} contact(s) matching '{search_term}':",
                    ["Select", "ID", "Name", "Email", "Phone", "Role"],
                    results,
                    ListOptions(
                        title="SEARCH - Results",
                        checklist=True,
                        width=800,
                        height=400
                    )
                )
            except:
                # User cancelled the results view
                pass
        else:
            zenity.info(
                f"No contacts found matching '{search_term}'.",
                InfoOptions(title="SEARCH - No Results", width=400)
            )
    
    # Main application loop
    print("=" * 70)
    print("CRUD DEMO - Contact Management System")
    print("=" * 70)
    print("This demo showcases Create, Read, Update, Delete operations")
    print("using Zenity dialogs.\n")
    
    while True:
        choice = show_menu()
        
        if not choice or choice == "EXIT":
            try:
                exit_choice = zenity.list(
                    "Are you sure you want to exit?",
                    ["Choice"],
                    [["Yes"], ["No"]],
                    ListOptions(
                        title="Confirm Exit",
                        height=200,
                        hide_header=True
                    )
                )
                
                if exit_choice == "Yes":
                    print("\n" + "=" * 70)
                    print("FINAL DATABASE STATE")
                    print("=" * 70)
                    print(f"Total Contacts: {len(contacts)}\n")
                    for contact in contacts:
                        print(f"ID {contact['id']}: {contact['name']} - {contact['email']}")
                    print("=" * 70)
                    print("\n✓ Thank you for using the CRUD Demo!")
                    sys.exit(0)
            except Exception:
                # User cancelled exit confirmation, continue loop
                continue
        
        elif choice == "CREATE":
            create_contact()
        
        elif choice == "READ":
            read_contacts()
        
        elif choice == "UPDATE":
            update_contact()
        
        elif choice == "DELETE":
            delete_contact()
        
        elif choice == "SEARCH":
            search_contacts()

except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except KeyboardInterrupt:
    print("\n\n✗ Application interrupted by user")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
