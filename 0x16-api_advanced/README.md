# 0x16. API advanced

## Function Prototypes
| File           | Prototype                               |
| -------------- | --------------------------------------- |
| `0-subs.py`    | `def number_of_subscribers(subreddit)`  |
| `1-top_ten.py` | `def top_ten(subreddit)`                |
| `2-recurse.py` | `def recurse(subreddit, hot_list=[])`   |
| `100-count.py` | `def count_words(subreddit, word_list)` |

## Tasks:

* **0. How many subs?**
  * [0-subs.py](./0-subs.py): queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
  * Returns `0` if an invalid subreddit is given

* **1. Top Ten**
  * [1-top_ten.py](./1-top_ten.py): queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
  * Prints `None` if an invalid subreddit is given

* **2. Recurse it!**
  * [2-recurse.py](./2-recurse.py): queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
  * Returns `None` if no results are found on the given subreddit

* **3. Count it!**
  * [100-count.py](./100-count.py): queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not)
  * Keywords are case-insensitive and delimited by spaces
  * Results are printed in descending order by count
  * Words with identical counts are sorted alphabetically
  * Words with no matches are skipped and not printed
  * Results are based on the number of times a keyword appears, not titles it appears in.
  `java java java` counts as 3 separate occurrecnces of `java`
