# LogTweet

Create a tweet based on a log message for today. 


## Usage
The log url can be configured. The log has to have a format like my log, which you can find at [https://log100days.lpld.io/log.md](https://log100days.lpld.io/log.md). 

My log is based on the [original #100DaysOfCode log repo](https://github.com/kallaway/100-days-of-code/blob/master/log.md). 
This is a markdown log. 
Have created a little Flask app that converts my log to an HTML site using the `markdown2` package. But other Markdown converters should work similar. 

Once you have an HTML document with `h2` day headers and `h3` sections for "Today's Progress" and "Link(s)", you can point the tool at that URL and generate a Tweet from it. 

To actually enable the tweeting, you need to create a Twitter developer account and get an API key, API secret, Access Token and Access Token Secret. 
Also, because the tool creates shortened links via the Bit.ly service, you need an account there and an API key.


### Options

If you want to create a tweet for a different day than today, you can do so with the `--offset` command line flag. 
The offset is defined in integer days relative to today. 
So to generate a tweet for yesterday use `-o -1`. 

If you want to suppress the actual tweeting and only see the message in the console, use the `--testmode` command line flag.

## Installation
Download the latest source distribution form GitHub.

You can install the script with `pip install <targz-file>`.

I recommend `pipx` to install python scripts and other tools in isolated virtual environments. This keeps the you platform python clean and you don't have to worry about activating a particular virtual environment to use a tool/script. 

## Configuration

You need a configuration file for the script to work. 
The `config.ini` can either be in the current working directory or in `~/.config/logtweet/`. 

The latter directory should be created during installation and an exmaple config file is added there. 

In that config file you define the URL where your log can be found and the API keys and access tokens that are needed for Twitter and Bit.ly.
