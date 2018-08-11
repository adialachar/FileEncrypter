from django.db import models

# Create your models here.




class Blowfish(models.Model):
	


	a = models.IntegerField()




	
def RSAEnc(file_input_name,file_output_name,queue, p , q, e):

	#with open(file_input_name, 'r')	

	f = open(file_input_name, 'r')
	g = open(file_ouput_name, 'r+')
	enclist = []
	for line in f:
		for i in range(length(line)):

			enclist[i] = cal( int(line[i]), int(e), int( int(p) * int(q))
		
		queue.push(enclist)
		enclist.clear()



	for line in queue

		#write to a file 
		g.write(line)


	return g #idk what to return lol



