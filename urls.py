from django.conf.urls.static import static 
from django.conf import settings
from .import views
from django.urls import path
from .views import report_issue_view



urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-admin/', views.create_admin, name='create_admin'),
    path('book-login/', views.books_login, name='book_login'),
    path('', views.index, name='index'),
    path('add-book/', views.add_book, name='add_book'),
    path('scan/', views.scan_page, name='scan'),
    path("student/<int:student_id>/", views.student_detail, name="student_detail"),
    path("save_student/", views.save_student, name="save_student"),
    path("student-login/", views.student_login, name="student_login"),
    path("delete-login/", views.delete_login, name="delete_login"),
    path('available/', views.available_books, name='available'),
    path("deletes-stud/", views.deletes_stud, name="deletes_stud"),
    path("borrow/", views.borrow, name="borrow"),
    path("scan-book/", views.scan_book, name="scan_book"),
    path("borrow-list/", views.borrow_list, name="borrow_list"),
    path("show/",views.show,name="delete_book" ),
    path("delete/<int:idn>",views.delete,name="delete"),
    path("show1/",views.show1,name="delete_student"),
    path("delete1/<int:idn1>",views.delete1,name="delete1"),
    path("student-logi/", views.student_log, name="student_logi"),
    path("bulk_uploads_student/", views.bulk_upload_students, name="bulk_uploads_student"),
    path("bulk_upload_books/", views.bulk_upload_books, name="bulk_upload_books"),
    path("books/<int:pk>/abstract/", views.book_abstract, name="book_abstract"),
    path('report-issue/', report_issue_view, name='report_issue'),
      path('search-borrow/', views.search_borrow, name='search_borrow'),
]

if settings.DEBUG:
# Serve static and media files during development
     urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)