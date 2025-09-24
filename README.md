Tugas 3
-Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dipakai agar informasi dapat dikirim ke server ke client secara aman. Tanpa adanya mekanisme pengiriman data yang baik, aplikasi tidak bisa memunculkan informasi yang terbaru, memperbarui isi/konten, ataupun berinteraksi dengan user secara langsung.

-Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya Json lebih baik untuk penggunaan web modern karena lebih ringkas dan mudah dibaca oleh manusia dibandingkan dengan XML.

-Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkannya?
digunakan untuk memvalidasi aakah data yang dikirim memenuhi aturan yang telah ditentukan,seeprti panjang karakter,tipe data, ataupun require fieldnya.

-Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token digunakan untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery).Tanpa csrf_token, penyerang bisa membuat requesst palsu dari browser yang sudah login. Selain itu Csrf_token bisa memastikan bahwa request berasal dari form yang aman dan bukan pihak ketiga.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Dari alur checklist yang diberikan, saat membuat empat views untuk XML, JSON, XML by ID, dan JSON by ID, saya menyadari pentingnya serializers. Serializer ini membantu mengubah data dari model menjadi format XML atau JSON yang bisa dikirim ke client. Setelah itu, saya membuat routing URL dengan mengimpor view yang sudah dibuat dan menambahkan path-nya di urls.py.

Untuk halaman tampilan data, saya membuat tombol “Add” yang menuju halaman form, dan tombol “Detail” di setiap produk agar bisa melihat informasi lengkapnya. Implementasinya melalui template seperti create_product.html untuk form penambahan data, dan show_product.html untuk menampilkan daftar produk beserta tombol detailnya.

Secara keseluruhan, saat mengerjakan checklist ini, saya tidak sekadar menyalin tutorial. Saya mencoba memahami penggunaan dari masing-masing perintah yang diberikan di tutorial 2. 

-Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Feedback saya adalah semoga asdos dapat lebih sabar lagi dalam menghadapi mahasiswa-mahasiswa yang masih kesulitan memahami apa yang perlu dilakukan. Semoga kakak-kakak asdos sehat selalu.

https://drive.google.com/file/d/1VX_PQFUUwOLalLXO2FIsvnPfRB09DBvy/view?usp=sharing
https://drive.google.com/file/d/1fgKv9W7O0UySXCTq2b5eBb2AUI5AF85z/view?usp=sharing

Tugas 4
-Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya?
Berdasarkan yang dijelaskan di kelas oleh bu Iis. Django authetincationForm itu seperti sebuah template yang diberikan oleh django untuk kita memberikan form yang dapat diisi oleh user. Maka kita tidak perlu lagi repot-repot membuatnya secara manual karena kita cukup import saja. Kelebihan dari Authentication Form adalah menyediakan formulir autentikasi login dan logout yang sudah terintegrasi dengan sistem autentikasi milik Django yang aman,seperti validasi,penolakan permintaan yang tidak valid dengan otomatis.
Kemudian kekurangan dari Authentication Form adalah kurang fleksibel karena  formulir ini dirancang untuk penggunaan umum dan mungkin perlu dimodifikasi atau dirubah jika memang terdapat kebutuhan yang sangat spesisfik dan berbeda dari pola standar biasanya.

-Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
secara definisi autentikasi dan otorisasi sudah bebbeda. Autentikasi yaiut proses memverifiksai identitas pengguna sedangkan otorisasi menentukan hak ases penggunanya,seperti memberikan limitasi atas hal-hal yang boleh dilakukan oleh pengguna.Kemudian autentikasi terjadi sebelum otorisasi sedangkan otorisasi dapat dilakukan setelah autentikasi itu berhasil.Untuk contohnya sendiri adalah autentikasi ketika pengguna ingin login dengan username dan password sedangkan otorisasi adalah role "admin" diperbolehkan menghapus data sedangkan pengguna biasa hanya bisa membaca data yang telah diberikan

- Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
kelebihan cookies:
-data tetap ada walaupun browser sudah ditutup
-tidak membebani server secara langsung
-didukung oleh semua browser

kekurangan cookie:
-ukurannya terbatas
-tingkat keamanannya rendah,data bisa dibaca/diubah oleh pengguna lecuali di encrypt
-Tidak cocok menyimpan data sensitif

Kelebihan session:
-lebih aman, maka data sensitif tidak di client hanya ada IDnya
-dapat menyimpan data yang besar

Kekurangan session:
-Membebani server: tiap user punya entry di memori atau database server.
-Skalabilitas: kalau server banyak (cluster), perlu mekanisme berbagi session (session store, Redis, dsb.).

-Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookie tidak aman secara default dalam pengembangan web. Ada beberapa risiko yang mungkin terjadi dan perlu diwaspadai,terutama berhubungan dengan keamanan dan privasi.

Risiko-risiko yang mungkin terjadi adalah:
-Pencurian cookies: jika cookies tidak dienkripsi atau dikirim melalui koneksi yang tidak aman (HTTP), penyerang dapat mencegat dan menccuri cookies tersebut
-CSRF(Cross Site Request Forgery):
erangan CSRF memaksa pengguna akhir untuk melakukan tindakan yang tidak mereka inginkan pada aplikasi web yang sedang mereka otentikasi. Cookies otentikasi sering kali dimanfaatkan dalam serangan ini. Dimana penyerang dapat mengirimkan request palsu yang mungkin terlihat sah karena ada cookie yang valid.

-Mengimplementasi fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
Saya membuat fungsi registrasi,login, dan logout pada views.py. Kemudian melakukan import di urls.py milik folder main .Kemudian melakukan routing url dengan mnaruhnya di dalam path.

-Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
Saya melakukan registrasi 2 akun epngguna dan kemudian memilih untuk membuat produk baru dengan memencet tommbmol "Add product" di local host.

-Menghubungkan model Product dengan User.
saya membuka file models.py pada subdirektori main kemudian melakukan import User dan pada model Products saya menambahkan kode untuk menghubungkan product dengan satu user melalui sebuah relationship.

-Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
saya memodifikasi kode login_user untuk menyimpan cookie baru bernama last_login yang berisi timestamp terakhir kali pengguna melakukan login.Kita dapat mendapatkannya dengan cara menambahkan if form.isvalid() .

