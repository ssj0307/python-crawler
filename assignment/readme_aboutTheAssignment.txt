What I have done:
1：A crawler that crawls the latest 25 articles about Trump from CNN.com and his latest 25 tweets
I wrote the crawler by two python functions:news_crawler() and twitter_crawler() in the .py file.
2：A simple website that displays the titles of the crawled information
I made it by defining a outputhtml() function in the .py file, showing the lasted news information in the first seach page from CNN.com( the first 3 pages are crawled but only 10 of the results are shown in his webpage) and the latest 10 tweets posted by @realrealDonaldTrump.
3：A convenient way of displaying the information after I click on one of the titles
The corresponding URLs are displayed on the webpage and we can access the information about the news from the URL, however, I have not made it to work when clicking on the title, for I’m not really good at web programming, I’d like to try to finish this function in the future . As for the tweets, it seems only after logging in can people see the full content, that’s a problem to be solved,too.
4：Add a cool feature that you came up with yourself (please explain the feature in your documentation)
My idea is to add a “hot” label to the tweets which have more comments / reposts/ likes (for example:more than 10000). If the viewer is interested in what the popular contents are, then he/she may get to know about such information.

What I am still confused about:
There are several problems I met in the process of doing this assignment,
1.The environment. At first I tried to do this work by mysql and django, but there is something wrong with the connections. Considering the data amount is not very huge, I didn’t do so. And I stored the crawled data in python data structure.
2.I tried to get the news from the first 3 pages in the search page from CNN.com, but it was weird that when I tried to visit:https://edition.cnn.com/search/?size=10&q=%20Donald%20trump&page=3, it still shows “Displaying results 1-10 out of 48020 for Donald trump”. I wonder why it is, maybe I should try to get more pages by imitating clicking the next page. 
I am still a beginner in this field with great passion, it would be so nice if there is any advice and correction, thanks!

Running steps:
Just run crawler.py, it will generate viewpage.html, all the contents are displayed in this webpage.
Everytime run the crawler.py, the latest infromation will be crawled from the original website.

Last run time:
The viewpage.html uploaded was generated at 2019/3.30 0:55 (Beijing time)