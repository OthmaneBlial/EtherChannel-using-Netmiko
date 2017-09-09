from netmiko import ConnectHandler
import data

def config_interface_trunk(interface):
	return ['default int '+ interface, 'int '+ interface, 'switchport trunk encap dot1q', 'switchport mode trunk']


def config_etherchannel(interface, channel_id, channel_mode):
	return ['interface '+ interface, 'sh', 'channel-group '+ channel_id + ' mode '+ channel_mode, 'no sh']



def configure_trunking(SWITCHES):
	idx = 0
	for SWITCH in SWITCHES:
		idx += 1
		print("Applying trunking configuration to SWITCH "+ str(idx))
		net_connect = ConnectHandler(**SWITCH)
		if (idx > 2):
			config_commands = config_interface_trunk('range e0/0-2') + config_interface_trunk('range e1/0-2')
		else:
			config_commands = config_interface_trunk('range e0/0-2')
		net_connect.send_config_set(config_commands)
		time.sleep(2)
	print("Trunking configuration has been applied!")

def configure_etherchannel(SWITCHES):
	idx = 0
	for SWITCH in SWITCHES:
		idx += 1
		print("Applying etherchannel configuration to SWITCH "+ str(idx))
		net_connect = ConnectHandler(**SWITCH)
		if (idx > 2):
			config_commands = config_etherchannel('range e0/0-2', '10', 'active') + config_etherchannel('range e1/0-2', '11', 'active')
		else:
			config_commands = config_etherchannel('range e0/0-2', '10', 'active')
		net_connect.send_config_set(config_commands)
		time.sleep(2)
	print("Etherchannel configuration has been applied!")


SWITCHES = [data.SW1, data.SW2, data.SW3, data.SW4]

configure_trunking(SWITCHES)

configure_etherchannel(SWITCHES)