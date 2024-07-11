from django.shortcuts import render
from .forms import inputs
from joblib import load



model = load('./savedModels/model.joblib')
scaler = load('./savedModels/scaler.joblib')
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = inputs(request.POST)
        if form.is_valid():
            Dependents = request.POST['Dependents']
            Income = request.POST['Income']
            Loan_Amount = request.POST['Loan_Amount']
            Loan_Term = request.POST['Loan_Term']
            Cibil_Score = request.POST['Cibil_Score']
            Total_Assets = request.POST['Total_Assets']
            X = [[Dependents,Income,Loan_Amount,Loan_Term,Cibil_Score,Total_Assets]]
            X = scaler.transform(X)
            
            prediction = model.predict(X)
            pred = prediction[0]
            #print(pred)
            return render(request, 'home/home.HTML',{'title': 'Result', 'form':form, 'pred':pred })
    else:
        form = inputs()
    return render(request, 'home/home.HTML',{'title': 'Home', 'form':form })


def about(request):
    return render(request, 'home/about.HTML',{'title': 'About'})
