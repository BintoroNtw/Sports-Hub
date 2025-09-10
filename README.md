https://bintoro-nata-sportshub.pbp.cs.ui.ac.id/

http://ristek.link/BaganRequestClientBintoro

-Membuat sebuah proyek Django baru
Langkah untuk membuat proyek django baru adalah kita masuk ke dalam virtual environment.Ketika sudah muncul (env) pada terminal/command prmpt kita lakukan instalasi djanggo. Berdasarkan contoh di tutorial arahannya adalah membuat file requirements.txt yang didalamnya terdapat djanggo. Akan tetapi kita juga bisa instalasi dengan langsung menjalankan perintah "pip install django".Perbedaan dengan contoh yang di tutorial hanyalah didalam file requirement.txt tidak hanya djanggo dilakukan instalasi, sedangkan contoh yang saya berikan hanya django yang di instalasi.Setelah django di instalasi kita jalankan perintah "django-admin startproject {namaproyek}"

-Membuat aplikasi dengan nama main pada proyek tersebut
Langkah pertama kamu adalah pastikan kamu ada di direktori terluar,seharusnya ada sebuah file bernama manage.py. Kemudian buka terminal/command prompt dan jalankan perintah "python manage.py startapp main"

-Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Untuk melakukan routing pada skala proyek untuk menjalankan aplikasi main. Kita buka direktori proyeknya (spots-hub) kemudian buka file urls.py bukan yang berada di direktori main. Lalu kita tambahkan import fungsi include dar django.urls dengan menambahkan "from django.urls import path, include" dan tambahkan rute URL dengan cara menambahkan di urlpatterns = path('',include('main.urls)). Gunanya adalah path akan diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main.Terakhir kamu jalankan perintah python manage.py runserver.

-Membuat model pada aplikasi dengan nama Product(name CharField,price IntegerField,description TextField,dll)
Kita buka file models.py pada direktori aplikasi dengan nama Product dan isi dengan atribut-atribut yang diminta. 

-Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Kita buka file views.py yang berada di aplikasi Main kemudian tambahkan from django.shortcuts import render. Gunanya adalah mengimpor fungsi render dari modul django.shortcuts. Kemudian fungsi render akan digunakan untuk render tampilan HTML dengan data yang telah diberikan.Lalu tambahkan fungsi show_main dibawah impor. Di akhir jangan lupa tulis return render(request,"main.html",context). Request berfungsi sebagai Objek permintaan HTTP yang dikirim oleh pengguna,main.html adalah nama file template yang digunakan untuk me render tampilanna,dan context adalah dictionary yang akan diteruskan ke interface.

-Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

buatlah file urls.py di dalam aplikasi main. Kemudian isi urls.py dengan template yang diberikan. Terdiri dari
from django.urls import path                = melakukan impor pada fungsi path dari django.urls
from main.views import show_main            = impor fungsi show_main dari main.views

app_name = 'main'                           = membeirkan namespace unik pada url aplikasi

urlpatterns = [
    path('', show_main, name='show_main'),  = list berisi objek URLPattern yang dihasilkan oleh fungsi path()
]

-Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
gunakan terminal/command prompt dan jalankan perintah git add ., git commit -m {pesan}, git push origin master, dan git push pws master.

-Peran settings.py dalam proyek Django
settings.py adalah konfigurasi pusat proyek Django.Semua pengaturan penting proyek ada di sini,seperti
Database yang digunakan (DATABASES),Aplikasi yang terdaftar (INSTALLED_APPS)template,dll
Pengaturan keamanan dan lokal (timezone, bahasa, secret key)
Secara singkat mungkin settings.py memberitahu Django bagaimana proyek harus berjalan dan komponen apa saja yang aktif.

-Cara kerja migrasi database di Django
Migrasi di Django adalah proses menyinkronkan perubahan model (di models.py) dengan database.
Buat atau ubah model di models.py.
    Jalankan python manage.py makemigrations implikasi Django membuat file migrasi yang berisi perubahan database.
    Jalankan python manage.py migrate → Django menerapkan perubahan tersebut ke database fisik.

-Mengapa Django dijadikan permulaan pembelajaran framework
Menurut saya kenapa Django dijadikan permulaan pembelajaran framework adalah cepat menghasilkan aplikasi jadi sambil belajar ada hasil/proyek nyatanya.Lalu banyak tutorialnya di internet jadi saya bisa cari solusi apabila ada kendala.

feedback untuk asdos PBP
Tidak ada,semoga kakak-kakak terus semangat dan rela membantu kami mahasiswa berusaha di matkul PBP ini. Terimakasih kakak-kakak.
