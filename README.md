
# Enterprise Course Catalog: OPENLXP-XIS

The Enterprise Course Catalog (ECC) is one of the three Enterprise Digital Learning Modernization (EDLM) lines of an effort supported by ADL. Today, learner records for Department of Defense (DoD) personnel are stored in disparate locations, along with inconsistent data formats, which complicates the transport, management, and governance of the learner records across and within DoD organizations.  

The goal of the ECC is a learning experience discovery service designed to aggregate metadata describing learning experiences from various internal sources as well as external sources.

ECC system architecture comprises multiple independently deployable components.Each component offers its unique data architecture.

### Experience Index Service

XIS is the primary funnel for learning experience metadata collected by the XIA components. In addition, the XIS can receive supplemental learning experience metadata – field name/value overrides and augmentations – from the XMS.  

Learning experience metadata received from XIAs is stored in the Metadata Loading Area and processed asynchronously to enhance overall system performance and scalability. Processed metadata combined with supplemental metadata provided by an Experience Owner or Experience Manager and the "composite record" stored in the Metadata Repository. Metadata Repository records addition/modification events logged to a job queue, and the metadata is then sent to the Experience Search Engine (XSE) for indexing and high-performance location/retrieval. 

A XIS can syndicate its composite records to another XIS. One or more facets/dimensions can filter the recordset to transmit a subset of the overall composite record repository. In addition, the transmitted fieldset can be configured to contain redacted values for specified fields when information is considered too sensitive for syndication. 

# Workflows
ETL pipeline from XIA loads processed metadata ledger and supplemental ledger in a metadata ledger and supplemental ledger of XIS after a validation. Metadata combined with supplemental metadata provided by an Experience Owner or Experience Manager from XMS also gets stored in XIS. All of them from XIA and XMS finally get merged into XIS's composite ledger after a validation.  

Composite metadata is then sent to an XSE for further discovery.

# Prerequisites
`Python >=3.7` : Download and install python from here [Python](https://www.python.org/downloads/).

`Docker` : Download and install Docker from here [Docker](https://www.docker.com/products/docker-desktop).


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_NAME` - MySql database name

`DB_USER` - MySql database user

`DB_PASSWORD` - MySql database password

`DB_ROOT_PASSWORD` - MySql database root password

`DB_HOST` - MySql datebase host

`DJANGO_SUPERUSER_USERNAME` - Django admin user name

`DJANGO_SUPERUSER_PASSWORD` - Django admin user password

`DJANGO_SUPERUSER_EMAIL` -Django admin user email

`BUCKET_NAME` - S3 Bucket name where schema files are stored

`AWS_ACCESS_KEY_ID` - AWS access keys

`AWS_SECRET_ACCESS_KEY` - AWS access password

`AWS_DEFAULT_REGION` - AWS region

`SECRET_KEY_VAL` -Django Secret key to put in Settings.py

`CERT_VOLUME` - Path for the where all the security certificates are stored

`LOG_PATH` - Log path were all the app logs will get stored

`CELERY_BROKER_URL` - Add CELERY_BROKER_URL tell Celery to use Redis as the broker

`CELERY_RESULT_BACKEND` - Add CELERY_RESULT_BACKEND tell Celery to use Redis as the backend


# Installation

1. Clone the Github repository:

    https://github.com/OpenLXP/openlxp-xis.git

2. Open terminal at the root directory of the project.
    
    example: ~/PycharmProjects/openlxp-xis

3. Run command to install all the requirements from requirements.txt 
    
    docker-compose build.

4. Once the installation and build are done, run the below command to start the server.
    
    docker-compose up

5. Once the server is up, go to the admin page:
    
    http://localhost:8080/admin (replace localhost with server IP)


# Configuration

1. On the Admin page, log in with the admin credentials 


2.  `Add xis configuration` : Configure Experience Index Service(XIA):

    `Target schema:`: Schema file name for source to target mapping schema file
    
    `Xse host:`: Host for the Experience Search Engine
    
    `Xse index:`: Index Name for the Experience Search Engine
    
        (Note: Please make sure to upload schema file in the Experience Schema Server (XSS). 
        In this case, upload schema files into the S3 bucket. )

5. `Add sender email configuration`: Configure the sender email address from which conformance alerts are sent.

6. `Add receiver email configuration` : 
Add an email list to send conformance alerts. When the email gets added, an email verification email will get sent out. In addition, conformance alerts will get sent to only verified email IDs.


# Running Of XIS Tasks:

### Running Tasks
Consolidations and loading of Metadata and Supplemental Metadata into Compositing Ledger and loading it into XSE can be run through two ways:

1. Through API Endpoint:
To run tasks run below API:
    
http://localhost:8080/api/xis-workflow
        
    (Note: Change localhost with XIS host)

2. Periodically through celery beat: 
 On the admin page add periodic task and it's schedule. On selected time interval celery task will run.

### API's 
 XIS supports API's endpoints which can get called from other components

    1. http://localhost:8080/api/catalogs/
    
This API fetch the names of all course providers

    2.http://localhost:8080/api/metadata/%3Cstr:course_id%3E/
    
This API fetch or modify the record of the corresponding course id

# Logs
To check the running of celery tasks, check the logs of application and celery container.

# Documentation

# Troubleshooting


## License

 This project uses the [MIT](http://www.apache.org/licenses/LICENSE-2.0) license.
  
