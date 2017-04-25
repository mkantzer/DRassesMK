#!/bin/bash
# write a bunch of files to server
echo "this script assumes that you have not run any other tests against this instance"
echo "these should return Successfully inserted with post_id"
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-12T14:36:00.451765", "uid": "1", "name": "John Doe", "md5checksum": "E8C83E232B64CE94FDD0E4539AD0D44F"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-12T14:40:00.451765", "uid": "1", "name": "John Doe", "md5checksum": "92D5B45A67FFAEB8358FF155DC6CDAF6"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-12T23:59:00.451765", "uid": "1", "name": "John Doe", "md5checksum": "F439EBE7B0A31FB985996E69F1818AD6"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-13T14:36:00.451765", "uid": "1", "name": "John Doe", "md5checksum": "EFBA495B9ECB5F8607434A933E53BFB9"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-14T14:36:00.451765", "uid": "1", "name": "John Doe", "md5checksum": "8F5C5BD7393BEF16BBD2A89ED7913F21"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-12T14:36:00.451765", "uid": "2", "name": "Mike Kan", "md5checksum": "43248CBC009EA7A9B4F36D040BDB9515"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-12T14:40:00.451765", "uid": "2", "name": "Mike Kan", "md5checksum": "9D2DBB1555A7365428299C58277C628C"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-13T14:36:00.451765", "uid": "2", "name": "Mike Kan", "md5checksum": "EFA6EFAACB0EA1B88537AC1A6CF5D07E"}'
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-13T14:36:00.451765", "name": "Mike Kan", "uid": "2", "md5checksum": "EFA6EFAACB0EA1B88537AC1A6CF5D07E"}'
#curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d ', "md5checksum": ""}'
echo "the next command should return a mismatch between UID and Name"
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-13T14:36:00.451765", "uid": "1", "name": "Mike Kan", "md5checksum": "E29F6B4704D68603BC3FA3B3DB0D87A1"}'
echo "the next should return with a checksum error"
curl 192.168.33.10:8080/post -X POST -H "Content-Type: application/json" -d '{"date": "2015-05-13T14:36:00.451765", "uid": "2", "name": "Mike Kan", "md5checksum": "EFA6EFAACB0EA1B88537AC1A6C58647E"}'
# execute Gets
echo "this should respond with 3"
curl '192.168.33.10:8080/get?uid=1&date=2015-05-12T14:36:00.451765'
echo "this should respond with 1"
curl '192.168.33.10:8080/get?uid=1&date=2015-05-13T14:36:00.451765'
echo "this should respond with 2"
curl '192.168.33.10:8080/get?uid=2&date=2015-05-13T14:36:00.451765'
echo "this should respond with 0"
curl '192.168.33.10:8080/get?uid=3&date=2015-05-13T14:36:00.451765'
echo "this should respond with 0"
curl '192.168.33.10:8080/get?uid=2&date=2018-05-13T14:36:00.451765'