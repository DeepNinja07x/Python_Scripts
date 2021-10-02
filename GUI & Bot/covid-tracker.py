from covid import Covid
import matplotlib.pyplot as plt

covid=Covid()  #storing calling function of Covid

name=input("Enter your country name: ")

virusdata=covid.get_status_by_country_name(name)

remove=['id', 'country', 'latitude', 'longitude', 'last_update']
for i in remove:
    virusdata.pop(i)

all_val = virusdata.pop('confirmed')
ids = list(virusdata.keys())
value = [str(i) for i in virusdata.values()]

plt.pie(value,labels=ids, colors = ['r','y', 'g', 'b'], autopct='%1.1f%%')
plt.title("Country: "+ name.upper() + "\nTotal Cases: " + str(all_val))
plt.legend()
plt.show()
