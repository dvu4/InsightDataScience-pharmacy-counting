#!/user/bin/env python3
# -*- coding: utf-8 -*-

" This is the main program for generating a list of all drugs, the total number of UNIQUE individuals \
who prescribed the medication, and the total drug cost, which must be listed in descending order \
based on the total drug cost and if there is a tie, drug name in ascending order."

__author__ = "Duc Vu"
__email__ = "ducvuchicago@gmail.com"
__status__ = "Prototype"
__date__ = "01/28/2019"  # Starting date

import sys  
import os

def main():  

    try:
        infilepath = sys.argv[1]
        outfilepath = sys.argv[2] 
    except IndexError:
        print("You failed to provide arguments!!!")
        sys.exit(1)

    if not os.path.isfile(infilepath):
        print("Input file path {} does not exist. Exiting...".format(infilepath))
        sys.exit(1)

    bag_of_drugs = {}
    drugs_result = []


    # read input file
    with open(infilepath) as fp:
        headerline = fp.readline()
        for line in fp:
            # strip the newline character, then split by comma
            record_drugs(line.strip().split(','), bag_of_drugs)

    count_drugs(bag_of_drugs, drugs_result) 


    # write list to output file
    header = [('drug_name','num_prescriber','total_cost')]
    with open(outfilepath, 'w') as fp:
        fp.write('\n'.join('{},{},{}'.format(x[0], x[1], x[2]) for x in header) + '\n')
        fp.write('\n'.join('{},{},{}'.format(x[0], x[1], x[2]) for x in drugs_result))


def record_drugs(line, bag_of_drugs):  
    """Group the information on prescription drugs by drug name and record them in bag_of_drugs dictionary.       
    Params
    ======
        line (list): containing id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost
        bag_of_drugs (dictionary): dictionary of drugs 
    """
    # get drug_name 
    drug_name = line[3]
    if drug_name != '':
        # group by drug_name
        if drug_name in bag_of_drugs:
            bag_of_drugs[drug_name].append(line) 
        else:
            bag_of_drugs[drug_name] = []
            bag_of_drugs[drug_name].append(line) 
           
        
def count_drugs(bag_of_drugs, drugs_result):
    """Return a list ot tuples in (drug_name, num_prescriber, total_cost) format, sorted by total drug cost and drug name.     
    Params
    ======
        bag_of_drugs (dictionary): dictionary of drugs 
        drugs_result (list of tuples) : list ot tuples (drug_name, num_prescriber, total_cost)
    """   
    for drug_name, values in bag_of_drugs.items():
        # get the list of last_name and fist_name of all prescribers
        list_prescriber = [ tuple([ i[1].lower(), i[2].lower() ]) for i in values ]
        # count the number of unique prescribers who prescribe the drug
        num_prescriber = len(set(list_prescriber))
        # get the total cost of the drug across all prescribers
        total_cost = sum([ int(float(i[-1])) for i in values ])
        # create a list of all drugs, the total number of UNIQUE prescribers, and the total drug cost
        drugs_result.append(tuple([drug_name, num_prescriber, total_cost]))
        
    #sort the drug name in ascending order
    drugs_result.sort(key=lambda x: x[0], reverse=False)
    
    #sort the total drug cost in descending order 
    drugs_result.sort(key=lambda x: x[2], reverse=True)


if __name__ == '__main__':  
   main()