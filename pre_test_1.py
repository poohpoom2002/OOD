print(' *** Wind classification ***')
speed = float(input('Enter wind speed (km/h) : '))
if(speed < 0):
    print("!!!Wrong value can't classify.")
elif(speed < 52) :
    print("Wind classification is Breeze.")
elif(speed < 56) :
    print("Wind classification is Depression.")
elif(speed < 102) :
    print("Wind classification is Tropical Storm.")
elif(speed < 209) :
    print("Wind classification is Typhoon.")
else :
    print("Wind classification is Super Typhoon.")