from django.urls import path
from . import views

urlpatterns = [
    # 크롤링 및 DB에 저장
    path('crawling/', views.card_gorilla_selenium),
    path('csv_to_db/', views.csv_to_db),
    # 카드
    path('', views.card_list),
    path('<int:card_pk>/', views.card_detail),
    path('<int:card_pk>/review/', views.review),
    path('<int:card_pk>/review/<int:review_pk>/', views.review_detail),
    path('<int:card_pk>/favorite/', views.favorite),
    #카드 추천
    path('<str:username>/gen_recommend/', views.gen_recommend),
    path('<str:username>/recommend/', views.recommend),
]
