from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Listing, Booking,Payment
from .serializers import ListingSerializer, BookingSerializer
import requests
from django.conf import settings
from .tasks import send_payment_confirmation

CHAPA_SECRET_KEY = settings.CHAPA_SECRET_KEY
CHAPA_BASE_URL = settings.CHAPA_BASE_URL

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
@api_view(['GET'])
def welcome(request):
    return Response({'message': 'Welcome to ALX Travel App'})




@api_view(['POST'])
def initiate_payment(request):
    data = request.data
    amount = data.get("amount")
    booking_ref = data.get("booking_reference")
    email = data.get("email")

    headers = {
        "Authorization": f"Bearer {CHAPA_SECRET_KEY}"
    }

    payload = {
        "amount": str(amount),
        "currency": "ETB",  # adjust if needed
        "email": email,
        "tx_ref": booking_ref,
        "callback_url": "http://127.0.0.1:8000/api/payments/verify/"
    }

    response = requests.post(f"{CHAPA_BASE_URL}/transaction/initialize", json=payload, headers=headers)
    resp_json = response.json()

    if resp_json.get("status") == "success":
        transaction_id = resp_json["data"]["tx_ref"]
        Payment.objects.create(
            booking_reference=booking_ref,
            transaction_id=transaction_id,
            amount=amount,
            status="Pending"
        )
        return Response(resp_json["data"])  # contains payment link

    return Response(resp_json, status=400)


@api_view(['GET'])
def verify_payment(request):
    tx_ref = request.query_params.get("tx_ref")

    headers = {"Authorization": f"Bearer {CHAPA_SECRET_KEY}"}
    response = requests.get(f"{CHAPA_BASE_URL}/transaction/verify/{tx_ref}", headers=headers)
    resp_json = response.json()

    try:
        payment = Payment.objects.get(transaction_id=tx_ref)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=404)

    if resp_json.get("status") == "success" and resp_json["data"]["status"] == "success":
        payment.status = "Completed"
        payment.save()
        send_payment_confirmation.delay(payment.email, payment.booking_reference)
        return Response({"message": "Payment successful", "status": payment.status})

    payment.status = "Failed"
    payment.save()
    return Response({"message": "Payment failed", "status": payment.status})

