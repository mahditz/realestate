from django.shortcuts import render
from .models import sell,rent
from django.views.generic import ListView,DetailView
from django.http import JsonResponse,HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class SellView(ListView):

	template_name = "sell.html"
	queryset = sell.objects.filter(status=True).order_by('-date').values(
		"id","code","area","priceK","priceM","metraj","room_qty","building_age","phase","block","title","image")[0:12]
	context_object_name = 'files'


	def post(self,request,*args,**kwargs):
		if self.request.method == "POST":
			area   = request.POST.get("area")
			area ="اکباتان" if area == "ekbatan" else "بیمه" if area =="bime" else ".*"
			mtype  = request.POST.get("mtype")
			mtype = "آپارتمان" if mtype == "apartment" else "اداری و تجاری" if mtype =="office" else ".*"
			maxp   = request.POST.get("maxp")
			minp   = request.POST.get("minp")
			metmin = request.POST.get("metmin")
			metmax = request.POST.get("metmax")
			cunt   = request.POST.get("c");
			cunt = int(cunt)
			s = sell.objects.filter(
				Q(area__area__iregex=r'{}'.format(area)),
				Q(melktype__iregex=r'{}'.format(mtype)),
				Q(priceK__range=(minp,maxp)),
				Q(metraj__range=(metmin,metmax))).order_by('-date').values("id","area","priceK","priceM","metraj","room_qty","building_age","phase","image","title")[cunt:cunt+12]
			# r = serializers.serialize("json",s)
			d = [x for x in s ]
			return JsonResponse({"data":d},status=200)
		return JsonResponse({"success":False}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class RentView(ListView):

	template_name = "rent.html"
	queryset = rent.objects.filter(status=True).order_by('-date').values("id","code","area","priceE","priceR","metraj","room_qty","building_age","phase","block","title","image")[0:12]
	context_object_name = 'files'


	def post(self,request,*args,**kwargs):
		if self.request.method == "POST":
			area = request.POST.get("area")
			area ="اکباتان" if area == "ekbatan" else "بیمه" if area =="bime" else ".*"
			mtype = request.POST.get("mtype")
			mtype = "آپارتمان" if mtype == "apartment" else "اداری و تجاری" if mtype =="office" else ".*"
			maxv = request.POST.get("maxv")
			minv = request.POST.get("minv")
			metmin = request.POST.get("metmin")
			metmax = request.POST.get("metmax")
			cunt   = request.POST.get("c")
			cunt = int(cunt)
			s = rent.objects.filter(
				Q(area__area__iregex=r'{}'.format(area)),
				Q(melktype__iregex=r'{}'.format(mtype)),
				Q(priceR__range=(minv,maxv)),
				Q(metraj__range=(metmin,metmax))).order_by('-date').values("id","area","priceE","priceR","metraj","room_qty","building_age","phase","image","title")[cunt:cunt+12]
			# r = serializers.serialize("json",s)
			d = [x for x in s ]
			return JsonResponse({"data":d},status=200)
		return JsonResponse({"success":False}, status=400)


# class CreateFileView(CreateView):
# 	template_name = 'createsell.html'
# 	model = sell
# 	success_url = reverse_lazy('sell')
# 	fields = '__all__'
 
 
class DetailSellFiles(DetailView):
	model = sell
	template_name = "detail_sell.html"


class DetailRentFiles(DetailView):
    model  = rent
    template_name = "detail_rent.html"