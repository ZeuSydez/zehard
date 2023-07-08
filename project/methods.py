# project/methods.py

def validate(form, mode):
    if mode == "register":
        if  form.get("username") and form.get("email") \
        and form.get("password") and form.get("confirm") \
        and form.get("password") == form.get("confrim"):
            return True
        else:
            return False
    elif mode == "login":
        if form.get("username") and form.get("password"):
            return True
        else:
            return False
    else:
        print("VALİDE FONKSİYONUNUNDA HATA VARRR!!!!!")
        return False