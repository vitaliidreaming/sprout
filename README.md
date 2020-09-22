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

to try it with curl:
```commandline
curl --header "Content-Type: application/json" --request POST --data '{"a": true, "b": true, "c": true, "d": 12.3, "e": 3, "f": 4}' http://127.0.0.1:5000/base
curl --header "Content-Type: application/json" --request POST --data '{"a": true, "b": true, "c": true, "d": 12.3, "e": 3, "f": 4}' http://127.0.0.1:5000/custom1
curl --header "Content-Type: application/json" --request POST --data '{"a": true, "b": true, "c": true, "d": 12.3, "e": 3, "f": 4}' http://127.0.0.1:5000/custom2
```

## Decisions  
This project:  
  - made it on Flask for it's routing model.
  - json because it is flexible and widespread approach for communication
  - object oriented paradigm as it good fit to reuse of base case logic
  

Additionally using two libraries: valideer and pytest.
  - Pytest. best library for testing
  - Valideer. to validate incoming json and avoid to implement a lot of validation logic by myself
  
In tests I'm not testing math formula, but only variants.
In math formulas there are no division by zero, so they are safe.  THe way I've typed them in, I've double check.
I've checked them with different numbers
in range from -10 to 100, but left it in tests would be an overkill.

That's all
Thanks.

