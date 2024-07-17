from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from api.api import ProductoAPI

urlpatterns = [
    path('', views.index, name="index"),
    path('micuenta/', views.micuenta, name="micuenta"),
    path('mision_vision/', views.mision_vision, name="mision_vision"),
    path('productos/', views.productos, name="productos"),
    path('proximos_productos/', views.proximos_productos, name="proximos_productos"),
    path('registro_cliente/', views.registro_cliente, name="registro_cliente"),
    path('crear/', views.crear, name="crear"),
    path('detalle/<id>/', views.detalle, name="detalle"),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminar/<id>/', views.eliminar, name="eliminar"),
    path('productos_admin/', views.productos_admin, name="productos_admin"),
    path('logout/', views.cerrar, name="cerrar"),
    path('registrar/', views.registrar, name="registrar"),
    path('profile/', views.profile, name="profile"),
    path('cambiar_password/', auth_views.PasswordChangeView.as_view(template_name='registration/cambiar_password_form.html'), name='cambiar_password'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_cambiado_done.html'), name='password_cambiado_done'),
    path('resetear_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_resetear_form.html'), name='resetear_password'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_resetear_done.html'), name='password_resetear_done'),
    path('resetear/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_resetear_confirm.html'), name='password_resetear_confirm'),
    path('resetear_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_resetear_complete.html'), name='password_resetear_complete'),
    path('agregar/<id>/', views.agregar_producto, name="agregar"),
    path('eliminar/<id>/', views.eliminar_producto, name="eliminar"),  # Cambiado a eliminar_producto
    path('restar/<id>/', views.restar_producto, name="restar"),      # Cambiado a restar_producto
    path('limpiar/', views.limpiar_carrito, name="limpiar_carrito"),
    path('generarBoleta/', views.generarBoleta, name="generarBoleta"),
    path('obtener_boleta/', views.obtener_boleta, name='obtener_boleta'),
    path('compras_realizadas/', views.compras_realizadas, name='compras_realizadas'),
    path('api/create_producto', ProductoAPI.as_view(), name='api_CreateProducto'),
]
