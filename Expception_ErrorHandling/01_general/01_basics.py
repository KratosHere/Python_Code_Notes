try:
    numerator = int(input("Enter Numerator:"))
    denominator = int(input("Enter denominator:"))
    result = numerator / denominator

except ZeroDivisionError: # SO if this exception occurs , we handle it:

    print("CANNOT DIVIDE BY ZERO YOU DUMBASS NIGGGAA!!")


except ValueError: # This is a different type of exception , when we try to do mathematical operation with strings instead of numbers kinda like that

    print("BSDK Number se divide kerna STring se kyu ker rha hai")

except Exception: # Just in case you missed some type of exception!

    print("Invalid INPUT!!")

else:
    print(result)

finally:

    print("This will always execute!")