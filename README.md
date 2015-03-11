# news!
a little webcrawler for webnews and flask gunicorn and nginx integration

## description
little a tag extractor and dynamic web page creator for specific sites that declared under crawler.py in the dictionaries. 

setup.py is for installation proccess. it installs gunicorn nginx also installs flask into virtualenv. by the way it updates your ubuntu. and adds crawler as a service named as newscrawler. yes it's for ubuntu.

##### Note: if you want to run your crawler on startup add to /etc/rc.local before exit 0 line:
>sudo service newscrawler start
