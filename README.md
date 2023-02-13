# Hi team IOET.

The proposed test was developed with Python and its estándar library, Using Camel Case notation also I did trying to use the pattern chain of responsibility however the algorithm was short the implementation have some limits.

# The Project contains the following folders:

### 1 Constant  - it has 3 files:

###### 1.1	weekdays.py, This file save homologation information of days of the Week and its abbreviations, so that its used like enum method or similar. 

![](https://github.com/jefvasquezg/acme/blob/master/images/1.png)

###### 1.2	default.py, This file save workdays information  (work week and work weekend) and schedules ( morning from ’00:01’ to ’09:00’, noon ’09:01’ to ’18:00’, nights from ’18:01’ to ’00:00’ ), we can send the arguments like start hours, end hours and value amount hours, this file require the timezone class because this declaration declaration will be used to define the working days, their hours and values. 

![](https://github.com/jefvasquezg/acme/blob/master/images/2.png)

###### 1.3	days_info.py, the file has an array, this array build and save information ( days, hours ranges, value amount hours) for all weekdays, this array require import weekdays, defaults and day class of file day.py

![](https://github.com/jefvasquezg/acme/blob/master/images/3.png)

###### The following image shows how this table could be imagined if it really existed and with the aim of helping to understand the exercise, the list_days is built with weekdays, defaults and day 

![](https://github.com/jefvasquezg/acme/blob/master/images/4.png)

### 2	Models – It has 3 files:

###### 2.1	timezone-py, this file contains the timezone class using a special method or constructor, this is used in the defaults.py file to set the parameters of the days. 

![](https://github.com/jefvasquezg/acme/blob/master/images/5.png)

######2.2	day.py, This file contains the day class, using a special method or constructor with all the parameters used to build the list_days array in the days_info.py file. 

![](https://github.com/jefvasquezg/acme/blob/master/images/6.png)

###### 2.3	amount_hour.py, This file contains the AmountHour class, using a special method or constructor with the necessary parameters so that in the main.py file it can be invoked and obtain information related to hours, days and its easy reading, it also returns a concatenation of hours and name of day via the __STR__ method

![](https://github.com/jefvasquezg/acme/blob/master/images/7.png)


### 3 File - folder :

###### Contains the information of the input file that contains the data that will be used to evaluate the exercise, it has some new examples

![](https://github.com/jefvasquezg/acme/blob/master/images/8.png)

### 4 Test - folder :

###### Contains all the tests that were performed on the functions defined in the main.py file, it is necessary to import the functions for the test from the main.py file, as well as the list_days array from the constants file

![](https://github.com/jefvasquezg/acme/blob/master/images/9.png)

###### 4.1 test_validate_valid_line – Tests the validate_amount_payment function with a fake input and an expected response for that input.

######4.2 test_validate_invalide_line – performs a test on the validate_amount_payment function that evaluates if there is an invalid line in the file of a given response to the user.

######4.3 decorator pytest.mark.parametrize – This function was used to evaluate various test inputs.

######4.4 test_validate_valid_multiple_line – was used to test the records that exist in the input file and that might contain a write error that does not match the regular expression defined in the validate_amount_payment method.

###### 4.5 test_get_amount_hour_fail_attribute_error – Used to test that the get_amount_hour method does not receive None values as arguments.

###### 4.6 test_open_file_success – used to test that the specified file opens correctly.

###### 4.7 test_open_file_file_not_exists – used to test whether the file does not exist at the specified path


### 5 Main.py file: 

###### It is required to import the RE module from the standard library, to use regular expressions, also call list_days from constants, timezone from the models folder and AmountHour from the models folder

![](https://github.com/jefvasquezg/acme/blob/master/images/10.png)

###### 5.1 read_data_file This method opens the file, if it cannot read the file it returns false, this return is used to return a message and stop the process if the method is called in the main function.

![](https://github.com/jefvasquezg/acme/blob/master/images/11.png)

###### 5.2 define_amount_hour - This method defines the cost of each hour on each day of the week, it uses list_days, it goes through it hour by hour to know the value of said hours, when you have to compare or know this information in the final calculation

![](https://github.com/jefvasquezg/acme/blob/master/images/12.png)

###### 5.3 is_list_empty -  This method validates that every day has 24 hours in the range from 00:00 to 23:00. If any time is missing, it throws an exception that stops the program and shows the user that x hour is needed in x day, this is because if a person works during these hours they could not be paid, lambda is used to make the information filter faster with fewer lines of code.

![](https://github.com/jefvasquezg/acme/blob/master/images/13.png)

###### 5.4 validate_amount_payment - This method receives the information from the file line by line, uses regular expressions to check that the input format of the data is correct to process, if it is not correct it returns a message indicating the line that has the problem and continues evaluating the other records of the file. file, it also receives the information of the costs per hour of each day of the week so that the hours that must be paid to a person can be compared and accumulated by returning the message requested in the test It determines that the information in the file is valid, invokes the auxiliary methods that determine hours, how much work and total consolidated that must be paid, is the function that has the business logic or in this case the logic of the test.

![](https://github.com/jefvasquezg/acme/blob/master/images/14.png)

###### 5.5 get_worked_days - This method with the information from the file determines the hours that a person worked in the week and avoids that there are no duplicate records using the remove_duplicates_hour method. 

![](https://github.com/jefvasquezg/acme/blob/master/images/15.png)

###### 5.6 remove_duplicates_hour   - This method is in charge of validating the input information, if there is a repeated hour of a day, the method will only take into account the first value found and the next one ignores it, it also calls the validate_exist_hour method. In short, it eliminates duplicate hours for the same input record.

![](https://github.com/jefvasquezg/acme/blob/master/images/16.png)

###### 5.7 validate_exist_hour  - this method evaluates if the hour and day already exist, it does not add it to the list of hours worked, complementing the information from the remove_duplicates_hour method

![](https://github.com/jefvasquezg/acme/blob/master/images/17.png)

###### 5.8 get_amount_hour -  This method determines the value of each hour of each day taking into account the days, taking into account 2 exceptions, that the attributes were not defined correctly, or that the attributes contain something other than hours.

![](https://github.com/jefvasquezg/acme/blob/master/images/18.png)

###### 5.9 Function to start the program - This starts the program and executes the functions described above.

![](https://github.com/jefvasquezg/acme/blob/master/images/19.png)

### 6	- Execution of the program and the unit tests.


###### The program can be executed in the console with the command python main.py or in the execution button of the IDE that is being worked on, in the case of unit tests use the command pytest test/test_main.py
