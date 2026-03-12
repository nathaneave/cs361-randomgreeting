# CS361 (Group 17) - Big Pool Microservice: Random Greeting

**What does this microservice do?**

This microservice allows the user to get a random greeting. Optionally, the user can provide a name and the greeting provided will include that name. It will return a string with the greeting.

**How do I request data from this microservice?**

To request data from this microservice, you will need to make an `HTTP GET request` to the `/randomgreeting` endpoint. You may optionally pass the `user_name` as a string that represents the `user's name` as a query parameter.

_Example call:_ `GET http://127.0.0.1:8000/randomgreeting`
_Example call:_ `GET http://127.0.0.1:8000/randomgreeting?user_name=Harry`


**How will I receive data from this microservice?**

The microservice will return a `JSON object`. The object will have one name/value pair. The name/value pair will be `greeting` which is a string representing the greeting.

_Example response (no name is provided)_:

Status code: `200`
```yaml
{
"greeting": "Welcome!"
}
```

_Example response (user name is provided)_:

Status code: `200`
```yaml
{
"greeting": "Welcome, Harry!"
}
```
