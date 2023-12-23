# 0x05. Processes and Signals

## Introduction

This project delves into the realm of processes and signals in a Linux environment. It includes a collection of Bash scripts and a C program to illustrate process management, signal handling, and related concepts.

## Learning Objectives
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

General Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Project Structure

- **[0x05-processes_and_signals](0x05-processes_and_signals):** Main directory for the project.

  - **[0-show_your_bash_pid](0x05-processes_and_signals/0-show_your_bash_pid):** Bash script displaying the PID of the Bash process.

    ```bash
    #!/usr/bin/env bash
    # Displays the PID of the Bash process
    ```

  - **[1-list_your_processes](0x05-processes_and_signals/1-list_your_processes):** Bash script listing processes.

    ```bash
    #!/usr/bin/env bash
    # Lists processes
    ```

  - **[2-show_your_bash_pid_made_easy](0x05-processes_and_signals/2-show_your_bash_pid_made_easy):** Bash script displaying PID and process name.

    ```bash
    #!/usr/bin/env bash
    # Displays PID and process name
    ```

  - **[3-list_your_processes_made_easy](0x05-processes_and_signals/3-list_your_processes_made_easy):** Bash script listing processes with a given name.

    ```bash
    #!/usr/bin/env bash
    # Lists processes with a given name
    ```

  - **[4-to_infinity_and_beyond](0x05-processes_and_signals/4-to_infinity_and_beyond):** Bash script displaying a message indefinitely.

    ```bash
    #!/usr/bin/env bash
    # Displays a message indefinitely
    ```

  - **[5-dont_stop_me_now](0x05-processes_and_signals/5-dont_stop_me_now):** Bash script managing an infinite loop.

    ```bash
    #!/usr/bin/env bash
    # Manages an infinite loop
    ```

  - **[6-stop_me_if_you_can](0x05-processes_and_signals/6-stop_me_if_you_can):** Bash script stopping a process without using kill or killall.

    ```bash
    #!/usr/bin/env bash
    # Stops a process without using kill or killall
    ```

  - **[7-highlander](0x05-processes_and_signals/7-highlander):** Bash script displaying messages with signal handling.

    ```bash
    #!/usr/bin/env bash
    # Displays messages with signal handling
    ```

  - **[8-beheaded_process](0x05-processes_and_signals/8-beheaded_process):** Bash script to kill a process.

    ```bash
    #!/usr/bin/env bash
    # Kills a process
    ```

  - **[100-process_and_pid_file](0x05-processes_and_signals/100-process_and_pid_file):** Bash script creating a process and PID file.

    ```bash
    #!/usr/bin/env bash
    # Creates a process and PID file
    ```

  - **[101-manage_my_process](0x05-processes_and_signals/101-manage_my_process):** Bash script managing a process using init script style.

    ```bash
    #!/usr/bin/env bash
    # Manages a process using init script style
    ```

  - **[102-zombie.c](0x05-processes_and_signals/102-zombie.c):** C program creating zombie processes.

    ```c
    // C program creating zombie processes
    // Displays Zombie process created, PID: ZOMBIE_PID
    ```

## Usage
- Each script or program comes with its own set of instructions. Follow the guidelines in the comments and execute the scripts to observe their behavior.

- For the C program, compile using:
      ```c
      gcc 102-zombie.c -o zombie
      ./zombie
      ```

- Remember to check for zombie processes using:
      ```bash
      ps aux | grep -e 'Z+.*<defunct>'
      ```

## License
- This project is licensed under the MIT License