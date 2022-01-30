from django.shortcuts import render
import sys
# Create your views here.

#index

def index(request):
	return render(request,"index.html")

def runcode(request):
	if request.method=="POST":
		codeareadata=request.POST["codearea"]	
		context={}
		
		try:
			#save original std oput reference
			orginal_stdout=sys.stdout
			sys.stdout=open("file.txt",'w') #change the std output to file we created
			#execute code

			exec(codeareadata) #example => print('hello')
			sys.stdout.close()

			sys.stdout=orginal_stdout #reset the std opt to it's original value
			#finally read output from file and save in output varibale

			output=open("file.txt",'r').read()
		except Exception as e:
			sys.stdout=orginal_stdout
			output=e
			#finaly return and render index page & send codedata to output to show on page
	return render(request,'index.html',{"code":codeareadata,"output":output})