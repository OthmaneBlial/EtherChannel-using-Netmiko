from netmiko import ConnectHandler
import data


def message(msg):
	print('\n\n'+80*'#')
	print('\n\n' + 20*'#' +'  '+ msg + '  '+ 20*'#' + '\n\n')
	print(80*'#'+'\n\n')



def show_etherchannel_summary(SWITCHES):
	idx = 0
	for SWITCH in SWITCHES:
		idx += 1
		print(20*'*'+' Showing Etherchannel summary for SWITCH '+ str(idx) + ' ' + 20*'*')
		net_connect = ConnectHandler(**SWITCH)
		output = net_connect.send_command('sho etherchannel summary  | begin Group')
		print(output)

def show_int_trunk(SWITCHES):
	idx = 0
	for SWITCH in SWITCHES:
		idx += 1
		print(20*'*'+' Showing trunking interfaces for SWITCH '+ str(idx) + ' ' + 20*'*')
		net_connect = ConnectHandler(**SWITCH)
		output = net_connect.send_command('show int trunk')
		print(output)


SWITCHES = [data.SW1, data.SW2, data.SW3, data.SW4]

message('Showing Etherchannel summary')
show_etherchannel_summary(SWITCHES)
message('Showing trunking interfaces')
show_int_trunk(SWITCHES)