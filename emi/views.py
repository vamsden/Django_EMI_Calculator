from django.shortcuts import render


def emi_main(request):
	return render(request,"emi.html", {})

def emi_calc(request):
   if request.method=='POST':
          loanAmount= request.POST.get('loanAmount', '')
          amount = int(loanAmount)

          intrate= request.POST.get('intrate', '')
          interest = int(intrate)

          if interest > 1:
		interest = (interest /100.0)
          else:
             return render(request,"error.html",{})

          period= request.POST.get('period', '')
          pay_period = int(period)
	  

          loan_emi = (amount*pow((interest/12)+1,
	        (pay_period))*interest/12)/(pow(interest/12+1,
	        (pay_period)) - 1)
	  emi =int(loan_emi)	

          total_payment = emi * pay_period

	  total_int_pay = total_payment - amount

   else:
       return render(request,"error.html",{})
      
       
	
   return render(request,"emiresult.html",{'loanAmount':loanAmount,'intrate':intrate,'period':period,'emi':emi,'total_payment': total_payment,'total_int_pay': total_int_pay})




