This is the directory where your source code would reside.


# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 


# Output 

The program creates the output file, `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line.

Each line of this file contains these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

For example

If your input data, **`itcont.txt`**, is
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


# Directory structure

The directory structure for your repo should look like this:

    ├── README.md 
    ├── run.sh
    ├── notebook 
    │   └── pharmacy_counting_notebook.ipynb 
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


# Code structure

## 1.`record_drugs` groups the prescription drugs

- group the prescription drugs by drug name

- record them in bag_of_drugs dictionary.


## 2.`count_drugs` extract the drug name, number of prescriber, total cost

- obtain a list ot tuples in (drug_name, num_prescriber, total_cost) format,

- sort the list by drug name in ascending order

- sort the list by total drug cost in descending order.


To run the code, 
`import os`
`import sys`