#eventus is a program that take the 3 core factors of an event and compiles them unto the 3 core outputs
#the inputs are:
#1. suppliers
#2. members
#3. steps

#the outputs are:
#1. the compiled timeline
#2. the resopnsibilities
#3. the supplier actions

#each of the inputs is supplied as a file
#the outputs are generated as files

#the prgram is run from the command line with a -s flag for supplieers file, a -m flag for members file, and a -e flag for steps file
#the program will then generate the 3 outputs
#the program will also have a -v flag for verbose mode, which will print out the steps as they are being processed
#the program will also have a -h flag for help, which will print out the help file

#use argparse to parse the command line arguments
import argparse
import yaml
import suppliers
import members
import steps


#define the command line arguments
parser = argparse.ArgumentParser(description='Compile an event from suppliers, members, and steps.')
parser.add_argument('-s', '--suppliers', help='the file containing the suppliers', required=True)
parser.add_argument('-m', '--members', help='the file containing the members', required=True)
parser.add_argument('-e', '--steps', help='the file containing the steps', required=True)
parser.add_argument('-v', '--verbose', help='verbose mode', action='store_true', required=False, default=False)
parser.add_argument('-o', '--output', help='the prefix for the output files', required=False, default='eventus')
args = parser.parse_args()

#open the files
suppliers_file = open(args.suppliers, 'r')
members_file = open(args.members, 'r')
steps_file = open(args.steps, 'r')

#each file is a yaml file
#the yaml file is parsed into a dictionary
suppliers_yaml = yaml.load(suppliers_file)
members_yaml = yaml.load(members_file)
steps_yaml = yaml.load(steps_file)

#step through the suppliers, creating the supplier objects, store these in a list called suppliers
suppliers = []
for supplier in suppliers_yaml:
    #create a list of GASs for the supplier
    supplier_gas = []
    for gas in supplier['GASs']:
        supplier_gas.append(suppliers.GAS(gas['name'], gas['description'], gas['overhead_price'], gas['unit_price']))
    #create a list of contacts for the supplier
    supplier_contacts = []
    for contact in supplier['contacts']:
        supplier_contacts.append(suppliers.contact(contact['name'], contact['email'], contact['phone'], contact['address']))
    #create the supplier object
    suppliers.append(suppliers.supplier(supplier['name'], supplier['description'], supplier_contacts, supplier_gas))

#step through the members, creating the member objects, store these in a list called members
members = []
for member in members_yaml:
    #create a list of tags for the member
    member_tags = []
    for tag in member['tags']:
        member_tags.append(tag)
    #if the member is a group, get a list of names from the 'names file' csv file
    if member['group'] == True:
        member_names = []
        names_file = open(member['names_file'], 'r')
        for name in names_file:
            member_names.append(name.strip())
        names_file.close()
        members.append(members.group(member['name'], member['involvement'], member_tags, member_names))
    else:
        members.append(members.indiv(member['name'], member['involvement'], member_tags))

#step through the steps, creating the step objects, store these in a list called steps
steps = []
for step in steps_yaml:
    #create a list of tags for the step
    step_tags = []
    for tag in step['tags']:
        step_tags.append(tag)
    #create a list of suppliers for the step
    step_suppliers = []
    for supplier in step['suppliers']:
        step_suppliers.append(supplier)
    #create a list of members for the step
    step_members = []
    for member in step['members']:
        step_members.append(member)
    #create the step object
    steps.append(steps.step(step['name'], step['description'], step['start'], step['end'], step['duration'], step_tags, step_suppliers, step_members))

#close the files
suppliers_file.close()
members_file.close()
steps_file.close()

#now that all objects have been created, references to other objects can be made

#the program is now ready to run
#the following are the rulse of eventus
#1. the program will start with the first step, the first step must have a start time
#2. 


