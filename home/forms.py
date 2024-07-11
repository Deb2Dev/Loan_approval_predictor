from django import forms

class inputs(forms.Form):
    Dependents = forms.IntegerField( 
                     help_text ="Enter the no. of people dependent on your income"
                     ) 
    
    Income = forms.IntegerField( 
                     help_text = "Enter full figure in digits(per annum)"
                     ) 
    
    Loan_Amount = forms.IntegerField( 
                     help_text = "Enter full figure in digits"
                     ) 
    
    Loan_Term = forms.IntegerField( 
                     help_text = "Enter the no. of years"
                     ) 
    
    Cibil_Score = forms.IntegerField( 
                     help_text = "Enter full figure in digits"
                     ) 
    
    Total_Assets = forms.IntegerField( 
                     help_text = "Enter full figure in digits"
                     ) 