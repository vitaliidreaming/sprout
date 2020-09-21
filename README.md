### sprout test service

Using Flask and python 3.7.4  

here we have three endpoints:
  - base
  - custom1
  - custom2

data to post should be valid json and follows schema:
```json
{
  "a": <Boolean>,
  "b": <Boolean>,
  "c": <Boolean>,
  "d": <Float>,
  "e": <Integer>,
  "f": <Integer>,
}
```

*host - default localhost is 127.0.0.1:5000*

to work with curl:
```commandline
curl --header "Content-Type: application/json" --request POST --data '{"a": true, "b": true, "c": true, "d": 12.3, "e": 3, "f": 4}' http://127.0.0.1:5000/base
curl --header "Content-Type: application/json" --request POST --data '{"a": true, "b": true, "c": true, "d": 12.3, "e": 3, "f": 4}' http://127.0.0.1:5000/custom1
curl --header "Content-Type: application/json" --request POST --data '{"a": true, "b": true, "c": true, "d": 12.3, "e": 3, "f": 4}' http://127.0.0.1:5000/custom2
```
