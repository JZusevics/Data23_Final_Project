# Data23 Final Project

current version = 0.25 

The Process:
The data from S3 will be extracted. Next it will be viewed, cleaned and transformeed. Finally, the clean data will then be pushed in to a SQL relational database that will store the data.

Role Allocation:
* Janis - Scrum Master/Developer
* Vrinda - Developer/Better Scrum Master
* Conner - Developer/BA	
* Awele - Developer	 
* Will - Developer	
* Anna - Developer	
* Shaban - Tester/Developer
* James - Tester/Developer
* Stephanie - Developer/Designer	


Naming Convention
* All lower-case file names
* python files-
  * _function_ + _origin_ + _file type_
  * separated by '_'
  * all lower-case
  * (e.g. 'extract_academy_csv.py')
* Variables
  * all lowercase
  * descriptive  
  * CONSTANTS ALL CAPITALISED 
* Tables
  * all lower case
  * all of the words will be singular
 



Final Project File Structure:
* app 📁
  * extract 📁
    * _extract_all.py_  
    * _extract_academy_csv.py_
    * _extract_talent_json.py_
    * _extract_talent_txt.py_
    * _extract_talent_csv.py_
  * transform 📁
    * _clean_talent_json.py_ 
  * load 📁
    * _load_functions.py_
    * _schema_functions.py_
    * _schema.txt_
* test 📁
  * _test_extract.py_  
* _init.py_
* _main.py_
* _config_manager.py_



