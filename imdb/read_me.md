#### International Business School

## MIB Automation

 

### Home Assignment





## IMDb (International Movie Database) Scraping Automation Process





##### This automation process is able to gather data from the IMDb webpage then based on the gathered information generates and sends forms in email.

The application reads movie pages on IMDb and gathers the cast list for each movie. It reads 150 pages of top movies and  saves all the cast members into the "imdb.csv" file. Then the app uses the gathered data and creates a top list of the most frequent 5 cast members in the gathered movies, and saves it as "cast.csv" file. Then it uploads the result as a spreadsheet on Google Drive.

Based on the top 5 cast members list the automation process generates a voting form based on the top 5 cast members and then sends the generated Google Form to a list of email addresses that is defined in a separate Google Spreadsheet by the user.

The scraping, uploading, form generation and email send is scheduled to run once every week.



#### Instruction before starting the process

##### Dependencies to install before executing:

- Python3, Scrapy, Numpy, Pandas, google-api-python-client, google-auth-httplib2, google-auth-oauthlib, Git Bash
- to install Python3 go to: https://www.python.org/downloads/ 
- if you are on Windows, to install Git Bash go to: https://git-scm.com/downloads 

##### Before starting the app please copy the followings in the Git Bash cli and press enter to install necessary the packages:

```
pip install scrapy numpy pandas 
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

##### To make authentication of google drive do the followings:

- go to "https://developers.google.com/drive/api/v3/quickstart/python" and click enable drive.

- to trough in the resulting dialog box and grant all permissions, click "DOWNLOAD CLIENT CONFIGURATION" and save the file credentials.json to your working directory.

- after start the upload_to_drive.py  in the working directory with Git Bash and grant authorization to the app in the browser:

  ```
  python upload_to_drive.py
  ```

  Then grant access to the app in the opening browser window, after that the "token.json" file is created automatically in your working directory, and you are now ready to start the application.



#### Starting the application

##### To start the app go to the imdb folder and write in the Git Bash cli:

```
./start.sh 
```

and press enter. To run the shell file please make sure that you use Git Bash. The shell executes the scraping "crapy crawl imdb_movies", the cast memebers.py and the upload_to_drive.py files automatically. It deletes  the previously saved imdb.csv file from the folder, as well.

Then please wait until the scraping, processing and uploading is finished, this should take at least 5 minutes, so please be patient.

When the process is finished you should see an "imdb.csv" and "cast.csv " file in your working directory.



#### Google Drive AppScript configuration

If everything went good so far, a spreadsheet file with name "cast" is uploaded to your Google Drive main folder.

The next step is to make a new AppScript project, to do so, please go to https://script.google.com/home and add a new project with the plus sign and give it a name.

Open the "appscript.gs" file in the working folder of your computer and copy the code to the online editor and save it.

In the code change the document id to the document id

[^1]: https://docs.google.com/spreadsheets/d/1wmFx8Wmi2vZJVPDidpfyV9o9U33n8uQKGjqs/edit#gid=0 document id can be found in the URL of the document between d/ and /edit.

 to the one of your file:

```
const PERSONS = Sheets.Spreadsheets.Values.get("document id","A2:A6");
```

Then create in your Google Drive a new spreadsheet document and write the receiver's email addresses in the "A" column one by one. This document id should be added to the app script, as well:

```
const EMAILS = Sheets.Spreadsheets.Values.get("document id", "A1:A");
```

Enable Spreadsheet service in the menu on the Services tab with plus sign, from the dropdown menu and then save it and run the script.



#### Scheduling

The scraping, uploading, form generation and email send is scheduled to run once every week.

##### AppScript scheduling:

To schedule the AppScript go to the https://script.google.com/home  page, choose your app and push the clock icon, then choose the "Triggers" option. Then push the add trigger button and set type of time based trigger to "Week timer", and Select day of week and time of the day.

##### Schtasks scheduling on Windows:

If you are on Windows, open command prompt and copy the followings and press enter.

After the /TR tag add your own path to the start.sh file on your system.

```
SCHTASKS /CREATE /SC WEEKLY /D MON /TN "Imdb scraping" /TR "C:\Users\tamas\Documents\IBS\automation\home_assignment\start.sh" /ST 11:00
```

This command will run the scraping app every Monday at 11 o' clock in the morning.

If you want to change the day, just modify the day of the week in D  to other values. By modifying the ST tag, the execution hour a minute can be changed.




