#!/bin/bash

# write a bunch of files to server
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-12T14:36:00.451765", "uid": "1", "name": "John Doe", "md5checksum": "E8C83E232B64CE94FDD0E4539AD0D44F"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-13T14:36:00.451765", "uid": "2", "name": "Mike Kantzer", "md5checksum": "D0E571C33CD39366E186260649BCBB14"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-08-31T14:36:00.451765", "uid": "4", "name": "Jane Franko", "md5checksum": "B150909CE797CD36C3B15322A4C3776F"}'


# execute gets