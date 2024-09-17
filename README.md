# Python-Webscraper
 
Build a discord bot that compares the price of games between multiple online retailers. 

retailers to include:

- CD Keys
- Humble Bundle
- GOG
- Steam


Us API's where we can?. 


Steam
GOG Galaxy? - Maybe. 
humblebundle  https://pypi.org/project/humblebundle/


We don't need any user data, the API would be useful if the user wanted to login, however we are only wanting to pull the name down, therefore we could scrap the details needed, along with the URLS to the page. 




steam - 

We can search by updating the term parameter in the steam website URL

https://store.steampowered.com/search/?sort_by=_ASC&term=<Enter Game Name Here>&supportedlang=english

We can query the above, so we don't need to pass the exact name of the game.


CD KEYS -

search URL:
https://www.cdkeys.com/pc#q=<Enter Game Name Here>

We can query the above, so we don't need to pass the exact name of the game. 


humble bundle.

search URL:
https://www.humblebundle.com/store/search?sort=bestselling&search=<Enter Game Name Here>&page=1 

Humble bundles search feature isn't as powerful as steam or DC keys, and appears to go off the games exact title and there isn't any additional tags on them. 


GOG

search URL:
https://www.gog.com/en/games?query=<Enter Game Name Here>&order=desc:score