#!/usr/bin/env python3

import soma3
import web
import subprocess


#dining = soma3.SomaBlind("F4:21:18:4C:58:1B")
#print(dining.get_position())
#print(dining.get_battery())
#print(dining.set_position(5))
#dining.disconnect()

#dining.connect()
#print(dining.get_position())

urls = (
    '/getbattery/(.*)', 'get_battery',
    '/getposition/(.*)', 'get_position',
    '/moveup/(.*)', 'move_up',
    '/stop/(.*)', 'move_stop',
    '/movedown/(.*)', 'move_down',
    '/setposition/(.*)/(.*)', 'set_position',
	'/alive', 'alive',
)
app = web.application(urls, globals())
class get_battery:
	def GET(self, mac):
		blind = soma3.SomaBlind(mac)
		return blind.get_battery()
class get_position:
	def GET(self, mac):
		blind = soma3.SomaBlind(mac)
		return blind.get_position()
class move_down:
	def GET(self, mac):
		blind = soma3.SomaBlind(mac)
		return blind.close()
class move_up:
	def GET(self, mac):
		blind = soma3.SomaBlind(mac)
		return blind.open()
class set_position:
	def GET(self, mac, position):
		blind = soma3.SomaBlind(mac)
		return blind.set_position(position)
class alive:
    def GET(self):
        return "ALIVE"		
if __name__ == "__main__":
    app.run()
