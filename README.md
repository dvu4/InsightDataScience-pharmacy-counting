# Table of contents
* [General info](#general-info)
* [Input Dataset](#input-dataset)
* [Output](#output)
* [Repo Directory Structure](#repo-directory-structure)
# [Code structure](#code-structure)
* [Setup](#setup)


# General info

The goal of the project is to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order.


# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 


# Output 

The program creates the output file, `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line.

Each line of this file contains these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

For example

The input data, **`itcont.txt`**, is
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

then the output file, **`top_cost_drug.txt`**, would contain the following lines
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

These files are provided in the `insight_testsuite/tests/test_1/input` and `insight_testsuite/tests/test_1/output` folders, respectively.


# Repo Directory Structure

The directory structure for the repo is organized :

    ├── README.md 
    ├── run.sh
    ├── pharmacy_counting_notebook.ipynb 
    │   
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
            ├── your-own-test_1
                ├── input
                │   └── itcont.txt
                |── output
                    └── top_cost_drug.txt


# Setup

To install python:

`pip install python`  

To check if input file exists:

`import os`
`import sys`


# Code structure

### 1. The function `record_drugs` groups the prescription drugs

- group the prescription drugs by drug name

- record them in bag_of_drugs dictionary.


```
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
```


### 2. The function `count_drugs` extracts the drug name, number of prescriber, total cost

- obtain a list ot tuples in (drug_name, num_prescriber, total_cost) format,

- sort the list by drug name in ascending order

- sort the list by total drug cost in descending order.

```
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
```

# Execution

`bash run.sh`

The `run.sh` script contains 

- `python ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt` 

if you are able to use `Python3`.
- `python3 ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt` 

