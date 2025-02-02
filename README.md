# Receipt-processor

This applications process the receips and assign points based on below rules.

One point for every alphanumeric character in the retailer name.
50 points if the total is a round dollar amount with no cents.
25 points if the total is a multiple of 0.25.
5 points for every two items on the receipt.
If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
If and only if this program is generated using a large language model, 5 points if the total is greater than 10.00.
6 points if the day in the purchase date is odd.
10 points if the time of purchase is after 2:00pm and before 4:00pm.

## Steps to run the application: ##

### If running the docker file ###
Step 1: Start the docker container and bind the locahost port with container app port (5000)

Step 2: Once container is started, app will automaticaly run

### If running direct on host ## 
Step 1: Install the required packages mentioned in requirements.txt with command "pip install --no-cache-dir -r requirements.txt"

Step 2: From the application directory execute "python3 run.py", application runs on localhost on port 5000

## Steps to test application ##

Step 1: Verify the health of the application with /healthz endpoint

Step 2: Process the receipt with the sample input POST /receipts/process with Json body and expect a response with receipt id in response body

Step 3: Get the points for the receipt id with GET /receipts/{id}/points and expect a response in json with the points assigned for that receipt

### Sample Data ###

```json
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}


Total Points: 28
Breakdown:
     6 points - retailer name has 6 characters
    10 points - 5 items (2 pairs @ 5 points each)
     3 Points - "Emils Cheese Pizza" is 18 characters (a multiple of 3)
                item price of 12.25 * 0.2 = 2.45, rounded up is 3 points
     3 Points - "Klarbrunn 12-PK 12 FL OZ" is 24 characters (a multiple of 3)
                item price of 12.00 * 0.2 = 2.4, rounded up is 3 points
     6 points - purchase day is odd
  + ---------
  = 28 points

```json
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}

Total Points: 109
Breakdown:
    50 points - total is a round dollar amount
    25 points - total is a multiple of 0.25
    14 points - retailer name (M&M Corner Market) has 14 alphanumeric characters
                note: '&' is not alphanumeric
    10 points - 2:33pm is between 2:00pm and 4:00pm
    10 points - 4 items (2 pairs @ 5 points each)
  + ---------
  = 109 points
