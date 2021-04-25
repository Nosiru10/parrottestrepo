class CustomExceotion(Exception):
    pass

class ValueTooSmallException(Customexception):
   pass

class VaueTooBigException(customException)
   pass

number_value = 20

while True:
    try:
        input_number = int(inpute("Enter a number:"))
        if input_number< number_value:
            raise ValueTooSmallException
        elif input_number > number_value:
            rsise VaueTooBigException
        break
    except ValueTooSmallException as _:
          print("Value too small")
    except ValueTooBigException as _:
        print("value too big")
    except Exception as _:
        print_.__str__())

print("Hey you get it correctluy")