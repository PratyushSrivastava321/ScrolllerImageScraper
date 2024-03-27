
# Scrolller Image Scraper

This project allows you to scrape any scrolller subreddit page where you just have to enter the link of the subreddit and wait for 5 mins to scrape the images of the page


## Installation
Open your suitable directory

And yeah please make sure you have python [installed](https://www.python.org/downloads/)

```terminal
  git clone https://github.com/PratyushSrivastava321/ScrolllerImageScraper.git
```

```terminal
  cd ScrolllerImageScraper
```

Create the Virtual Environment
and activate it
```terminal
python -m venv venv
```

```terminal
venv\Scripts\activate
```

Now install the required modules with this command
```terminal
pip install -r requirements.txt
``` 
## If modules are not properly installed

If the installation is unsuccessful see the terminal history and recognize which module caused the error 

If you scroll up you will see the most recent module which failed to install 

So simply goto requirements.txt and remove the version of that module 

For example if it is written 
```cffi==1.16.0``` simply change it to ```cffi```

Now if god is good on you all the modules will be installed 

---

## Run the program
simply run the ```main.py``` file and enter the link

you will see a special message if you dont enter the valid link

## Procedure
Hold up, wait for 5 mins

After you entered the valid link there is a headless incognito chrome browser scraping the data for you 

---

#### If you want to see what is happening

Open the ```scraping_links.py``` file and change the 9th line from

```browser = p.chromium.launch()``` 

to 
 
```browser = p.chromium.launch(headless=False)```

---

You can see the terminal for progress happening and then images will download after the scraping is done 



# Note from the Author

Look man I am a newbie and this is all new to me 
So, if you find any bugs or bad practice used 

please make sure to [ping](t.me/PratyushSrivastava) me

```May the images be with you !!```



