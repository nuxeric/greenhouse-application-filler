# greenhouse-application-filler
A web scrapper that fills in your contact information, uploads files (resume, transcript, cover letter), and checks out the appropriate boxes for greenhouse.io job postings 

### Prerequisites
Set up your python virtual env, and pip install the modules from rquirements.txt.

### Usage: 
Run the python script, passing in the url as a string like so:

```python greenhouseFiller.py "greenhouse_job_application_for_big_tech_company.com/whatever"```


### Acknowledgments:
Tested and works as of (12/08/2019) using an example link of : "https://boards.greenhouse.io/databricks/jobs/4374189002?gh_src=62a881d62&s=LinkedIn&source=LinkedIn"

This project will be unmaintained as this was a quick project to try to gain a deeper understanding of scraping and driving the web. There are many specific details of the greenhouse.io job application board which is reflected in my code and will need to be updated as soon as greenhouse changes their application "template". 
