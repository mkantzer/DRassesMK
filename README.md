# DRassesMK

This codebase was created by Michael Kantzer, for his evaluation with DataRobot. 

## Setup

Requirements on host machine:
* vagrant
* virtualbox (or another hyperviser with vagrant configured correctly)
* internet connection

Usage (on host machine):
* navigate to project home directory
* `vagrant up`
* wait for buildout to finish

If the server stops responding for some reason, this can be fixed by either:

```
vagrant ssh
sudo service webapp restart
```

or

```
vangrant destroy -f
vagrant up
```

## Endpoints
The VM and associated services should now be fully running. You can execute GET and POST requests against it at:


POST:

`192.168.33.10:8080/post`

This endpoint expects uid, date, name, and md5checksum parameters, aranged in a json structure. For example:

`curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"uid": "1", "name": "John Doe", "date": "2015-05-12T14:36:00.451765", "md5checksum": "E8C83E232B64CE94FDD0E4539AD0D44F"}'`


GET:

`192.168.33.10:8080/get`

This expects a date and a uid parameter. For example:

`curl 'http://192.168.33.10:8080/get?uid=1&date=2015-05-12T14:36:00.451765'`

## Known Issues, Changes I would make
* Error handling is very sparse. This would need to be greatly improved for a production system
* There is not form of authentication on the requests
* input type verification is not currently utilized 