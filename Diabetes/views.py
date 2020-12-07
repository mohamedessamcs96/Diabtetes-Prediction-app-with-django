
from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def predict(request):
    return render(request,'predict.html')


def result(request):
    import sklearn
    from sklearn.externals import joblib
    clf=joblib.load('E:\Miller Open University\Courses\Django on Miller\django\diabetes\Diabetes\Diabetes\diabetes')

    v1=float(request.GET(['n1']))
    v2=float(request.GET(['n2']))
    v3=float(request.GET(['n3']))
    v4=float(request.GET(['n4']))
    v5=float(request.GET(['n5']))
    v6=float(request.GET(['n6']))
    v7=float(request.GET(['n7']))
    v8=float(request.GET(['n8']))

    pred=clf.predict([[v1,v2,v3,v4,v5,v6,v7,v8]])

    result2 =""
    if pred==1:
        result2="Positive"
    else:
        result2 ="Negative"


    return render(request,'predict.html',{"result2":result})
