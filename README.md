PyYAML==3.12
# lazy python library 

##### Note. This library was written for python3 and scrapy1.6.0. However higher version is supported.

### Installation Instruction
* Create a virtual env
* Install it as you would install python package
```
pip install . 
```


###### Note if you are having installation issue. please check if you have added your public ssh keys to bitbucket. Visit this blog for more details on adding ssh keys to bitbucket
[https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html](https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html)

### Visit documentation here



#### It is recommended to take a look at scrapy documentation also as this library merly hides setup complexity of scrapy and some other settings. You would still need to learn scrapy framework for using spiders

https://docs.scrapy.org/en/latest/



## Build instructions





We use semantic versioning(https://en.wikipedia.org/wiki/Software_versioning)

In order to build the docker container.

0. Increase the tag in `deploy/vortex-py-backend/requirements.txt` to your current tag(this is used to install requirements)
1. Commit your changes.
2. Increase the version(patch, minor , major)

    Normally, its patch
    
    Install bumpversion for easier version management.
    
    In order to increase patch version simply do
    `bumpversion patch`
    
    For example if the current tag is 1.04
    Doing `bumpversion patch` will make the tag 1.05
    
3. push to tags
```git push --tags```

4. Also push to master branch
``` git push origin master```

