def decor_invoice(func):
    def wrap(num):
        print("*****")
        func(num)
        print("*****")
        print("End of page")
    return wrap


@decor_invoice
def invoice(num):
    print("Invoice no: ", num)


invoice(int(input("enter the invoice number: ")))
