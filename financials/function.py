from django.shortcuts import render
from django.http import HttpResponse
from leases.models import Rental
from leases.serializer import RentalsSerializer
from weasyprint import HTML, CSS
from django.template.loader import render_to_string
from django.db.models import Q
import os

def Make_Damage_Warranty_Form(request, rental_id, product, mount, total, observations):
    serializer_class = RentalsSerializer

    rental = rental_id

    rental = Rental.objects.get(pk = rental_id)
    serializer = serializer_class(rental)
    rental = serializer.data

    customer = rental.get("customer")
    contacts = customer.get("contacts")
    customers = customer.get("contacts")
    for customer in customers:
        name = customer.get("name")
        nit = customer.get("ci_nit")

    selected_products_data = rental.get("selected_products")
    selected_products=[]
    for selected_product_data in selected_products_data:
        if selected_product_data["id"] == product:
            selected_product = {
                'id': selected_product_data["id"],
                'start_time': selected_product_data["start_time"],
                'product':selected_product_data["product"]
            }
            selected_products.append(selected_product)

    ruta_archivo_html = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ejecución_de_garantía.html')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="formulariodesolicitudreserva.pdf"'
    if os.path.exists(ruta_archivo_html):

        with open(ruta_archivo_html, 'r', encoding='utf-8') as archivo_html:
                html_content = archivo_html.read()

    html_string = render_to_string('ejecución_de_garantía.html', {
        'name': name,
        'nit': nit,
        'selected_products':selected_products,
        'warranty': rental.get("initial_total"),
        'contacts': contacts,
        'rental': rental_id,
        'mount': mount,
        'observations': observations,
        'product':product,
        'total':total
        })

    HTML(string=html_string).write_pdf(response, stylesheets=[CSS(
        string='@page { margin-left: 2cm; margin-right: 1cm; margin-top: 2cm; margin-bottom: 1.5cm; }'
        )])
    return response