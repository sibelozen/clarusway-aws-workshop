def mill2nd(number):
    if number < 1000:
        return f"just {number} millisecond/s"

    elif number < 60000:
        seconds = number // 1000
        return f"{seconds} second/s"

    elif number < 60000*60:
        minute = number // 60000
        second_remain = number % 60000 // 1000
        if second_remain != 0:
            return f"{minute} minute/s {second_remain} second/s" 
        else:
            return f"{minute} minute/s"

    else:
        hours = number // (60000*60)
        minute_remain = (number % (60000*60))
        minute = minute_remain // 60000
        second_remain = minute_remain % 60000 // 1000
        return f"{hours} hour/s {minute} minute/s {second_remain} second/s"

digit = int(input("Please anter a number "))
print(mill2nd(digit))        
