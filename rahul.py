def press(value):
    global exp

    if value == "=":
        try:
            result = str(eval(exp))  # ✅ calculate
            dis_var.set(result)      # ✅ show result
            exp = result             # ✅ save result
        except:
            dis_var.set("error")
            exp = ""

    elif value == "c":
        exp = ""
        dis_var.set("0")

    elif value == "backspace":
        exp = exp[:-1]
        dis_var.set(exp if exp else "0")

    elif value == "%":
        try:
            exp = str(eval(exp) / 100)
            dis_var.set(exp)
        except:
            dis_var.set("error")
            exp = ""

    elif value == "+/-":
        try:
            exp = str(eval(exp) * -1)
            dis_var.set(exp)
        except:
            dis_var.set("error")
            exp = ""

    else:
        if exp == "" or exp == "0":
            if value in "+-*/.":
                exp = "0" + value
            else:
                exp = value
        else:
            exp += value
        dis_var.set(exp)    # ✅ inside else block now