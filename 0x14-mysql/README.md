# 0x14. MySQL

## Requirements
### General
What is the main role of a database
What is a database replica
What is the purpose of a database replica
Why database backups need to be stored in different physical locations
What operation should you regularly perform to make sure that your database backup strategy actually works

## Requirements
### General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

* [4-mysql_configuration_primary](./4-mysql_configuration_primary): The MySQL
`my.conf` configuration file used to set up my first server as a primary database
server on the database `tyrell_corp`.

* [4-mysql_configuration_replica](./4-mysql_configuration_replica): The MySQL
`my.conf` configuration file used to set up my second server as the replica
database server on the database `tyrell_corp`.

* [5-mysql_backup](./5-mysql_backup): Bash script that generates a compressed
`tar.gz` archive from a MySQL dump.
  * Usage: `./5-mysql_backup <MySQL root password>`
  * Generates a dump containing all MySQL databases on the root server.
  * Names the resulting tar archive in the format `day-month-year.tar.gz`.
