Hello Public,
I am planning to build a web scraper in python using requests and parsing using BeautifulSoup and this web scraper stores the scraped data into a CSV file on S3 Bucket of AWS.
I am planning to schedule this scraper using Airflow to run weekly at 12:00 Am using CRON job.
The generated CSV file in S3 will be updated weekly with the changes from the website. 
The rows already present in the csv will be updated,and if not present new rows will be inserted which basically is an upsert process.

Tools planning to use : Python ( Requests, BeautifulSoup, Airflow),Docker, VSCode.
