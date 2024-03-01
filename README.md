# Course Scraping and sharing using Telegram bot

This project mainly aims to scrape the given site which shares udemy courses that are free for a short period of time. After scraping, main data about courses are added to `.csv` file for further processing. `scrapy` library in `Python` is used for scraping. Then using  `telebot`library, the necessary data about courses are shared on the target channel.

I built this project for my telegram channel that was focused on technology(@digitoloq). Sharing free udemy courses releated to programming was a good idea for boosting the channel but it was time-consuming to do it manually. So, I built this project to save time. Unfortunately, due to busy schedule I even cannot find time to use this bot. 
## Configuration
1. In `telegramlearning.py` file, add your bot key, and channel ID.
2. You can change the path of the `.csv` file.

## Getting started

1. Firstly, go to the main directory and use `scrapy crawl coursetreat` on `cmd`

2. Then, run the `telegramlearning.py` file. 

3. Go and add the bot on your account. Then after starting you can use `/show {number of couses} ` to share the courses on target channel.


## Contribution
Feel free to contribute by opening issues or submitting pull requests. Any contributions are highly appreciated!


