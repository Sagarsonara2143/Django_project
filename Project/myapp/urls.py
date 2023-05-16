from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('seller-index/',views.seller_index,name='seller-index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('profile/',views.profile,name="profile"),
    path('seller-add-product/',views.seller_add_product,name='seller-add-product'),
    path('seller-view-product/',views.seller_view_product,name='seller-view-product'),
    path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),
    path('seller-edit-product/<int:pk>/',views.seller_edit_product,name='seller-edit-product'),
    path('seller-product-delete/<int:pk>/',views.seller_product_delete, name='seller-product-delete'),
    path('laptops/',views.laptops,name="laptops"),
    path('seller-laptops/',views.seller_laptops,name='seller-laptops'),
    path('cameras/',views.cameras,name='cameras'),
    path('seller-cameras/',views.seller_cameras,name='seller-cameras'),
    path('accessories/',views.accessories,name='accessories'),
    path('seller-accessories/',views.seller_accessories,name='seller-accessories'),
    path('product-details/<int:pk>/',views.product_details,name='product-details'),
    path('add-to-wishlist/<int:pk>/',views.add_to_wishlist,name='add-to-wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('remove-from-wishlist/<int:pk>/',views.remove_from_wishlist,name='remove-from-wishlist'),
    path('add-to-cart/<int:pk>/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.cart,name='cart'),
    path('remove-from-cart/<int:pk>/',views.remove_from_cart,name='remove-from-cart'),
    path('change-cart-qty/',views.change_cart_qty,name='change-cart-qty'),
    path('checkout/',views.checkout,name='checkout'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('success.html/', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'),
    path('myorder/',views.myorder,name='myorder'),
    path('seller-order/',views.seller_order,name='seller-order'),
    path('ajax/validate_email/',views.validate_email,name='validate_email'),
    path('ajax/validate_mobile/',views.validate_mobile,name='validate_mobile'),
    path('ajax/validate_pwd/',views.validate_pwd,name='validate_pwd'),
]




