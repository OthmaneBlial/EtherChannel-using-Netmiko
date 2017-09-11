# EtherChannel-using-Netmiko
EtherChannel using Netmiko


![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/1.PNG)

First, let's create three files, one for data, the second to configure our topology, and the third is for showing results:
![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/2.PNG)

Then, we start by data.py, and we put all the SSH information Netmiko needs to access each switch:
![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/3.PNG)

Now we go to the configure.py file.
This first config function, will configure a trunk interface:
![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/4.PNG)

Then, we configure an etherchannel:
![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/5.PNG)

After that, we loop throughout the switches and apply the trunk configuration needed:
![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/6.PNG)

We loop again around the switches, in order to configure the etherchannels:
![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/7.PNG)

Now, let's run these two configuration functions:
![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/8.PNG)


![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/9.PNG)

Now, let's go to the show.py, and write down the functions that will check the etherchannel 
state of all the switches:
![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/10.PNG)


We run these functions:

![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/11.PNG)

Here we go, the final results:
![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/12.PNG)


![alt tag](https://github.com/OthmaneBlial/EtherChannel-using-Netmiko/blob/master/Tutorial/13.PNG)


