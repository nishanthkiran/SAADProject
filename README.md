# Software Architecure and Design Project

In this project, we extract the CK Metrics related to a java project by using a online tool [CK-Metrics tool](https://github.com/mauricioaniche/ck), and process them using Python.

In order to integrate the tool to run in python, we have created a JAR file for the tool(ck.jar), which we can run from the directory where the jar is located using the follwing command in CMD:

```
java -jar ck.jar
```

![image](https://user-images.githubusercontent.com/47377412/208049196-84a4b549-70fb-4922-8c15-268c8a5b5ce8.png)

After running the Jar file, we can run the python file(Main.py) located in the same directory as the jar file using the follwoing command:
```python
Python Main.py
```

![image](https://user-images.githubusercontent.com/47377412/208049978-64efceba-45b8-40e3-ab34-73b7ba0424f4.png)

After we run the python project, the program asks the user to choose a directory of the code(Java) on which the detection of code smells are to be performed. We can choose the root directory as following:

![image](https://user-images.githubusercontent.com/47377412/208050396-4c99ed7b-10d5-4777-afc5-13507a5c4ec1.png)

In the above image, we have selected the JHotDraw project which is an opensource Java project avaliable on Github.

After the process is completed, a message is displayed on the console, indicating that the code smells are extracted as below:

![image](https://user-images.githubusercontent.com/47377412/208050865-00f78672-b584-4999-b018-212e10ba6c54.png)

You can find the results csv, for God class and Long Methods for the selected project in the results folder. They are in the below format:
 
 1. for God Class, results are in format -> GC-{Project_Name or Base_folder_Name}
 2. for Long Method, results are in format -> LM-{Project_Name or Base_folder_Name}

![image](https://user-images.githubusercontent.com/47377412/208051386-2e75f002-de79-4482-b55a-9d3fd92b3cdf.png)

Above Image, shows the results for Jhotdraw project shown in the example.



 
