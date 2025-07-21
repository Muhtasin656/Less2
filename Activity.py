def total(bill_amount,tip_perc):
    total_mount=bill_amount*(1+0.01*tip_perc)
    total_mount=round(total_mount,2)
    print(f"The total amount is {total_mount}")
total(127,12)