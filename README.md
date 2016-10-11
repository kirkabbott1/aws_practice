PostgreSQL setup on Ubuntu

Install Steps

Overview of the steps:

Add the official / latest repository for the PostgreSQL packages to the repository list for apt-get.
Update the repository index for apt-get based on the newly added repository, and then install the postgresql package.
Give postgres user a password
Configure the postgresql server to be able to accept connections from any computer.
Configure the postgresql server to be able to accept logins from any computer.
Setup an inbound port in Amazon's security group to let PostgreSQL clients in.
Restart the postgresql server.
Connect to the remote postgresql instance from your mac using psql.
Connect to the remote postgresql instance from your mac using Postico.
Install PyGreSQL on the server.
Run a test Python script to test the connection working on the server.
Step 1

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
Step 2

Use apt-get to install:

sudo apt-get update
sudo apt-get install postgresql postgresql-contrib libpq-dev python-dev
Step 3

The install has created a new database user named postgres. To be able to connect to it remotely, we need to give it a password. To do that, first go into the psql shell via:

sudo -u postgres psql postgres
Then inside of the psql shell, do

postgres# \password postgres
This will prompt you to type in a password. Choose a long password for security. Write down the password to remember it if you need to. You will need this for later steps.

Step 4

Edit the /etc/postgresql/9.6/main/postgresql.conf file with the nano text editor like:

sudo nano /etc/postgresql/9.6/main/postgresql.conf and add the following line to the bottom:

listen_addresses='*'
Step 5

Edit the /etc/postgresql/9.6/main/pg_hba.conf file with the nano text editor and add the following line to the bottom:

host  all  all 0.0.0.0/0 md5
Step 6

Go to the AWS console: https://console.aws.amazon.com/. Select your server instance. Select the description tab. Click on the link to the right of "Security Groups". This goes to the Security groups page. Click on the "Inbound" tab. Click "Edit". Then click "Add Rule", and then select "PostgreSQL" for the type, and "Anywhere" for the source.

Step 7

Restart the postgresql server.

sudo service postgresql restart

Step 8

Connect via psql from local machine

psql -h SERVER_IP -U postgres -W
Replace SERVER_IP with the actual server IP address.

Or you can also connect via psql from within an ssh session from the remote server:

psql -h localhost -U postgres -W
Step 9

Connect via Postico from local machine

Create a "New Favorite". Put the server IP address in the "Host" field. Put postgres in the "User" field. Put the password you set up for the postgres user in the "Password" field - select save password in Keychain.

Step 10

Install the PyGreSQL Python module on the server:

sudo pip install PyGreSQL
Step 11

First, from Postico - connected to the remote PostgreSQL instance, create a new database called test_db, and create a table within it called student. Run a test Python script to test that the connection is working on the server.

import pg
db = pg.DB(dbname='test_db', user='postgres', passwd='YOUR_DB_USER_PASSWORD', host='localhost')
query = db.query('select * from student')
print query
Replace YOUR_DB_USER_PASSWORD with the password you set up in step 3.

Resources

http://tecadmin.net/install-postgresql-server-on-ubuntu/
https://help.ubuntu.com/community/PostgreSQL
http://askubuntu.com/questions/423165/remotely-access-postgresql-database
http://dba.stackexchange.com/questions/83984/connect-to-postgresql-server-fatal-no-pg-hba-conf-entry-for-host
