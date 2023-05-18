#Create an instance of TV called tv1
#Create an instance of TV called tv2
from pyfiglet import Figlet
from tv import TV

def print_tv_info(tv_name, channel, volume_level):
    f = Figlet(font='slant')
    print(f.renderText(tv_name))
    print(f"\033[96m{tv_name}'s channel is {channel} and volume level is {volume_level}\n \033[95m")

tv1 = TV()
tv2 = TV()
#Turn on tv1
tv1.turnOn()
#Set tv1's channel to 30
tv1.setChannel(30)
#Set tv1's volume level to 3
tv1.setVolume(3)


#Turn on tv2
tv2.turnOn()
#Set tv2's channel to 3
tv2.setChannel(3)
#Set tv2's volume level to 2
tv2.setVolume(2)

#Print tv1's information
print_tv_info("Tv1", tv1.getChannel(), tv1.getVolume())
#Print tv2's information
print_tv_info("Tv2", tv2.getChannel(), tv2.getVolume())