POST method :

json format from postman

**post musician json**

{
   "musician" : "Musician",
    "first_name" : "John",
    "last_name":"Doe",
    "email":"doe@mail.com"
}

**post instrument json**
{
   "type" : "StringInstrument",
    "manufacturer":"Wittner",
    "model":"Pro",
    "musician_email":"doe@mail.com"
}
{
    "type" : "electric piano",
    "manufacture":"Fender",
    "model":"Rhodes",
    "musician_email":"doe@mail.com"
}
{
    "type" : "electric piano",
    "manufacture":"Yamaha",
    "model":"S90",
    "musician_email":"doe@mail.com"
}

**post delete json**
{
    "action": "RemoveInstrument",
    "name" : "StringInstrument",
    "manufacture":"Wittner",
    "model":"Pro",
    "musician_email":"doe@mail.com"
}
{
    "action": "RemoveInstrument",
    "name" : "electric piano",
    "manufacture":"Fender",
    "model":"Rhodes",
    "musician_email":"doe@mail.com"
}
{
    "action": "RemoveInstrument",
    "name" : "electric piano",
    "manufacture":"Yamaha",
    "model":"S90",
    "musician_email":"doe@mail.com"
}