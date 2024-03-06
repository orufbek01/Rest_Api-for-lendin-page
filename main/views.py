from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Banner , Services, Testimonial, About, Client, Contact, Portfolio
from .serializers import BannerSerializer , ServicesSerializer, TestimonialSerializer, AboutSerializer, PortfolioSerializer ,ClientSerializer, ContactSerializer

@api_view(['GET'])
def get_banner(request):
    banner = Banner.objects.last()
    ser = BannerSerializer(banner)
    return Response(ser.data)


@api_view(['GET'])
def get_services(request):
    services = Services.objects.all().order_by('-id')[:4]
    ser = ServicesSerializer(services, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_about(request):
    about = About.objects.all()
    ser = AboutSerializer(about, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_testimonial(request):
    testimonial = Testimonial.objects.all().order_by('-id')[:3]
    ser = TestimonialSerializer(testimonial, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_portfolio(request):
    portfolio = Portfolio.objects.all().order_by('-id')[:9]
    ser = PortfolioSerializer(portfolio, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_clients(request):
    clients = Client.objects.all().order_by('-id')[:6]
    ser = ClientSerializer(clients, many=True)
    return Response(ser.data)


@api_view(['POST'])
def create_contact(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    contact = Contact.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        subject=subject,
        message=message,
    )
    return Response(ser.date)


