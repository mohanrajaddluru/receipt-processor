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
Step 1: Start the docker container and bind the ports locahost port with container app port (5000)

Step 2: Once container is started app will automaticaly start

### If running direct on host ## 
Step 1: Install the required packages mentioned in requirements.txt with command "pip install --no-cache-dir -r requirements.txt"

Step 2: From the application directory run "python3 run.py" , application runs on localhost on port 5000

## Steps to test application ##

Step 3: Verify the health of the application with /healthz endpoint

Step 4: Process the receipt with the sample input POST /receipts/process with Json body and expect a response with receipt id in response body

Step 5 : Get the points for the receipt id with GET /receipts/{id}/points and expect a response in json with the points assigned for that receipt