#CIS129_YourName_Lab5.py
# Step 1: Declare variables
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = "y"

# Step 2: Loop to run program again
while keep_going.lower() == "y":
    total_bottles = 0  # reset total_bottles for new week
    counter = 1  # reset counter for new week

    # Step 3: getBottles code
    NBR_OF_DAYS = 7
    total_bottles = 0
    today_bottles = 0
    counter = 0

    while counter < NBR_OF_DAYS:
        today_bottles = int(input(f"Enter number of bottles returned for day #{counter + 1}: "))
        total_bottles += today_bottles
        counter += 1

    # Step 5: calcPayout code
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

    # Step 4: Print total bottles and total payout
    print(f"The total number of bottles collected for the week is: {total_bottles}")
    print(f"The total payout for the week is: ${total_payout:.2f}")

    keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")
