LogTweet
========

Create a tweet based on the log message for today from [https://log100days.lpld.io/log.md](https://log100days.lpld.io/log.md).

# Installation
You can install the script with `pip install <targz-file>`.

# Usage
Just run the script with `logtweet` from the command line. 
It will automatically post a tweet based on the log message for today form [https://log100days.lpld.io/log.md](https://log100days.lpld.io/log.md).

You can also create a tweet for a different day with the `--offset` command line flag. 
The offset is defined in integer days relative to today. 
So to generate a tweet for yesterday use `-o -1`. 