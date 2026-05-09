# define a dictionary named contact_info
#that includes the following keys and the sample values of your choice:
contact_info = {'name': 'Daisy Dukes', 'address': '123 Main St.', 'city': 'Tampa', 
                'state': 'Flordia', 'zip': 33566}

#Print the address as properly formatted for mailing. Avoid using multiple print
#statements. Experiment with using a multi-line f-string (triple quotes)
print(f'{contact_info['name']}, {contact_info['address']}, {contact_info['city']}, {contact_info['state']}, {contact_info['zip']}')

# Add a new variable for full_name and assign its value as a dictionary containing two
#key:value pairs. The first key:value pair should contain the key “first name” and a first
#name, and the second should contain the key “last name” and a last name.

contact_info = {'address': '123 Main St.', 'city': 'Tampa', 
                'state': 'Flordia', 'zip': 33566}
full_name = {'first_name':'Daisy', 'last_name': 'Dukes'}

full_name.update({'honorific': 'Ms.'})
contact_info.update({'full_name': full_name})