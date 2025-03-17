def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Hata: Sıfıra bölme yapılamaz!"
    return a / b

def add(a, b):
    return a + b
def sub(a, b):
    return a - b


print("Hesap Makinesi")
print("1 - Çarpma")
print("2 - Bölme")
print("3 - Toplama")
print("4 - Çıkarma")

try:
    choice = int(input("Yapmak istediğiniz işlemi seçin (1/4): "))

    if choice not in [1, 4]:
        print("Hata: Geçersiz işlem seçimi!")
    else:
        num1 = float(input("Birinci sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))

        if choice == 1:
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
        elif choice==2:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
            
        elif choice==3:
            print(f"{num1} / {num2} = {add(num1, num2)}")            

        else:
            print(f"{num1} / {num2} = {sub(num1, num2)}")

except ValueError:
    print("Hata: Lütfen geçerli bir sayı girin!")
