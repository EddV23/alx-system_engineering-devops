# Regular Expressions Project

- This project involves creating Ruby scripts using the Oniguruma regular expression library. Each script focuses on different aspects of regular expressions and is designed to match specific patterns.

## Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

- Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```bash
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

## General Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
- All your regex must be built for the Oniguruma library


## Files

1. [0-simply_match_school.rb](./0x06-regular_expressions/0-simply_match_school.rb): Matches the string "School".
2. [1-repetition_token_0.rb](./0x06-regular_expressions/1-repetition_token_0.rb): Uses repetition tokens to match specific patterns.
3. [2-repetition_token_1.rb](./0x06-regular_expressions/2-repetition_token_1.rb): Continues exploring repetition tokens.
4. [3-repetition_token_2.rb](./0x06-regular_expressions/3-repetition_token_2.rb): Further refinement of repetition token usage.
5. [4-repetition_token_3.rb](./0x06-regular_expressions/4-repetition_token_3.rb): Matches patterns without using square brackets.
6. [5-beginning_and_end.rb](./0x06-regular_expressions/5-beginning_and_end.rb): Matches strings that start with 'h', end with 'n', and can have any single character in between.
7. [6-phone_number.rb](./0x06-regular_expressions/6-phone_number.rb): Matches a 10-digit phone number.
8. [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./0x06-regular_expressions/7-OMG_WHY_ARE_YOU_SHOUTING.rb): Matches capital letters in a string.
9. [100-textme.rb](./0x06-regular_expressions/100-textme.rb): Extracts information from text messages log file.

## Instructions

- To run each script, use the following format:

```bash
./0x06-regular_expressions/script_name.rb "input_string"
```

- Replace "script_name.rb" with the desired script and "input_string" with the string you want to test.

## Example
``bash
./0x06-regular_expressions/0-simply_match_school.rb "Best School" | cat -e
# Output: School$
```
