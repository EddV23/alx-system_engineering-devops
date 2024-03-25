# 0x15.API

## Background Context

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build

## Learning Objectives
### General
- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python

## Tasks

* **0. Gather data from an API**
  * [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py): Python script
  that returns information on the to-do list progress of a given employee ID.
  * Usage: `python3 0-gather_data_from_an_API.py <employee ID>`.
  * Output: `Employee <employee name> is done with tasks(<# completed tasks>/<total # tasks>):`

* **1. Export to CSV**
  * [1-export_to_CSV.py](./1-export_to_CSV.py): Python script exports to-do list
  information of a given employee ID to CSV format.
  * Usage: `python3 1-export_to_CSV.py <employee ID>`
  * File name: `<user id>.csv`.
  * Format: `"<user id>","<username>","<task completed status>","<task title>"`.

* **2. Export to JSON**
  * [2-export_to_JSON.py](./2-export_to_JSON.py): Python script that exports
  to-do list information of a given employee ID to JSON format.
  * Usage: `python3 2-export_to_JSON.py <employee ID>`
  * File name: `<user id>.json`
  * Format: `{ "<user id>": [ {"task": "<task title>", "completed": <task completed status>, "username": "<username>"}}, ... ]}`

* **3. Dictionary of list of dictionaries**
  * [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py):
  Python script that exports to-do list information for all employees to JSON format.
  * Usage: `python3 3-dictionary_of_list_of_dictionaries.py`
  * File name: `todo_all_employees.json`
  * Format: `{ "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ], "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ]}`
