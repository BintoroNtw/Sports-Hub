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
Penggunaan cookie tidak aman secara default dalam pengembangan web. Ada beberapa risiko yang mungkin terjadi dan perlu diwaspadai,terutama berhubungan dengan keamanan dan privasi.s

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


Tugas 5
-Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan atau penentuan aturan CSS mana yang akan diterapkan pada suatu elemen HTML, ketika terdapat beberapa selector yang menunjuk ke elemen yang sama, ditentukan oleh konsep Spesifisitas.Spesitifitas dihitung berdasarkan empat tingkatan, dari yang paling tinggi ke paling rendah prioritasnya:
    -Inline Style (1, 0, 0, 0): Properti CSS yang ditulis langsung di dalam tag HTML menggunakan atribut style
    -ID Selector (0, 1, 0, 0): Selector yang menunjuk elemen berdasarkan atribut id
    -Class, Attribute, dan Pseudo-class Selector (0, 0, 1, 0): Selector yang menunjuk berdasarkan atribut class (misalnya, .button)
    -Element dan Pseudo-element Selector (0, 0, 0, 1): Selector yang menunjuk berdasarkan nama tag HTML,misalnya, p, div

-Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive Web Design (RWD) adalah pendekatan dalam pengembangan web yang bertujuan agar tata letak (layout) dan konten sebuah situs web secara otomatis menyesuaikan diri dengan berbagai ukuran layar perangkat,contohnya adalah dekstop,tablet,ponsel. Tujuannya sendiri untuk memberikan pengalaman yang optimal untuk user tanpa memandang device yang digunakan.Contoh aplikasi yang sudah menerapkan Responsive design adalah: Facebook,Twitter web,roblox,youtube,dll

-Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Padding adalah ruang di dalam elemen, antara konten (teks/gambar) dan border-nya. Memberikan "bantalan" di sekitar konten.
Border adalah garis yang mengelilingi padding dan konten. Ini adalah batas visual elemen yang sebenarnya.
Margin adalah ruang di luar elemen, antara border elemen tersebut dengan elemen lain di sekitarnya. Digunakan untuk mengontrol jarak antar elemen.

-Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox maupun Grid Layout adalah modul tata letak CSS modern yang memecahkan masalah kompleks penataan elemen HTML yang dulunya sulit dilakukan hanya dengan float atau posistioning.
    -Flexbox
    Metode tata letak satu dimensi untuk mengatur baris atau kolom elemen dalam wadah (container).
    -grid layout
    Metode tata letak dua dimensi yang memungkinkan penataan elemen dalam baris dan kolom secara simultan.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Saya menambahkan fungsi delete product dan edit product. Kemudian melakukan routing dengan menaruhnya di path pada file urls.py.Lalu saya melakukan kustomisasi warna pada laman login,register,tambah product,edit product,dan detail product dengan mengubahnya menjadi warna biru dan kuning. Halaman produk saya ubah header atasnya mennjadi warna gelap dan memberikan efek hover pada beberapa tombol,seperti home,product, dan logout ketika akan diklik ada warna gelapnya.Saya juga menambahkan nama suer sebagai penjual dan harga pada home page.Saya juga menbamhkan foto emoji sedih apabila product belum ada.

1.Perbedaan antara Synchronous Request dan Asynchronous Request

Synchronous request merupakan jenis permintaan di mana browser harus menunggu hingga server selesai memproses dan mengirimkan respons sebelum melanjutkan aktivitas lain. Pola interaksinya cenderung bersifat “klik → tunggu → reload”, karena setiap kali permintaan dikirim, seluruh halaman akan dimuat ulang. Akibatnya, pengguna tidak dapat melakukan interaksi lain selama proses tersebut berlangsung, dan pengalaman penggunaan terasa lebih lambat.

Sebaliknya, asynchronous request (yang biasanya dilakukan melalui AJAX) memungkinkan browser mengirim dan menerima data di latar belakang tanpa perlu memuat ulang seluruh halaman. Dengan cara ini, pengguna tetap bisa berinteraksi dengan halaman — seperti menggulir, mengetik, atau menekan tombol lain — sambil menunggu respons dari server. Data yang diterima kemudian diolah oleh JavaScript dan ditampilkan secara dinamis di bagian tertentu halaman. Contohnya, ketika menambahkan produk baru di katalog, daftar produk langsung diperbarui tanpa harus melakukan refresh halaman.

2.Cara Kerja AJAX di Django (Alur Request–Response)

Ketika pengguna memicu suatu aksi, seperti menekan tombol “Add Product” atau “Login”, JavaScript akan mengirimkan permintaan ke server Django menggunakan metode fetch() atau XMLHttpRequest(). Permintaan ini dikirim ke endpoint Django tertentu yang telah disiapkan untuk menangani data tersebut.

Selanjutnya, Django menerima request melalui fungsi view (misalnya add_product_ajax atau login_ajax) dan menjalankan logika yang diperlukan — seperti validasi data, operasi CRUD, atau autentikasi pengguna. Setelah selesai diproses, Django mengirimkan kembali response dalam format JSON menggunakan JsonResponse().

JavaScript di sisi klien kemudian menerima data JSON tersebut, memprosesnya, dan memperbarui tampilan halaman secara langsung tanpa perlu reload. Misalnya, produk baru muncul di daftar produk, atau muncul notifikasi seperti “Login berhasil”.

Dengan mekanisme ini, komunikasi antara klien dan server berlangsung cepat, efisien, dan tidak mengganggu aktivitas pengguna di halaman web.

3.Keuntungan Menggunakan AJAX Dibandingkan Render Biasa di Django

Penggunaan AJAX memberikan berbagai keuntungan dibandingkan metode render tradisional yang mengharuskan halaman dimuat ulang setiap kali ada permintaan ke server. Beberapa di antaranya yaitu:

Proses lebih cepat dan efisien.
Hanya data penting yang dikirim dan diterima, bukan keseluruhan halaman HTML, sehingga waktu respons menjadi lebih singkat.

Tampilan halaman tidak perlu reload.
Pengguna tetap berada di halaman yang sama tanpa kehilangan posisi scroll atau data input.

Interaksi terasa real-time.
Misalnya, ketika menambahkan produk, data langsung muncul di layar tanpa perlu menunggu pemuatan ulang.

Pengalaman pengguna lebih baik.
Website terasa lebih interaktif, responsif, dan menyerupai aplikasi modern (SPA-like).

Beban server lebih ringan.
Karena server hanya mengirim data JSON, bukan template HTML penuh, konsumsi bandwidth menjadi lebih kecil.

Dengan kata lain, AJAX meningkatkan efisiensi komunikasi antara klien dan server serta memberikan kesan interaktif yang lebih menyenangkan bagi pengguna.

4.Cara Memastikan Keamanan Saat Menggunakan AJAX untuk Login dan Register di Django

Walaupun AJAX membuat proses login dan register lebih cepat, aspek keamanan tetap harus dijaga dengan baik. Beberapa langkah yang perlu diterapkan antara lain:

Gunakan CSRF Token (Cross-Site Request Forgery Protection).
Django sudah menyediakan sistem CSRF secara otomatis. Setiap permintaan POST dari AJAX wajib menyertakan token CSRF melalui header X-CSRFToken agar tidak rentan terhadap serangan permintaan palsu dari situs lain.

Gunakan HTTPS.
Pastikan seluruh komunikasi antara klien dan server terenkripsi agar data sensitif seperti username dan password tidak mudah disadap.

Validasi data di sisi server.
Semua data yang dikirim melalui AJAX harus tetap diverifikasi dan divalidasi oleh Django, bukan hanya oleh JavaScript di sisi klien yang mudah dimanipulasi.

Batasi informasi yang dikirimkan dalam respons.
Jangan pernah mengirimkan data sensitif dalam bentuk JSON. Jika login gagal, cukup kirimkan pesan umum seperti “Username atau password salah” tanpa memberikan detail tambahan.

Gunakan rate limiting pada endpoint sensitif.
Hal ini mencegah percobaan login berulang yang berpotensi menjadi serangan brute force.

Dengan langkah-langkah tersebut, fitur login dan register berbasis AJAX dapat berjalan cepat sekaligus tetap aman.

5.Pengaruh AJAX terhadap Pengalaman Pengguna (User Experience) di Website

AJAX memiliki dampak besar terhadap pengalaman pengguna (User Experience/UX) karena membuat interaksi di website terasa lebih cepat, mulus, dan responsif. Pengguna tidak lagi harus menunggu halaman dimuat ulang setiap kali melakukan aksi.

Selain itu, AJAX memungkinkan adanya real-time feedback, seperti munculnya pesan “Produk berhasil ditambahkan” sesaat setelah tombol diklik. Hal ini menciptakan kesan bahwa website lebih interaktif dan responsif terhadap tindakan pengguna.

Halaman juga menjadi lebih dinamis karena pengguna bisa menambah, mengedit, atau menghapus data tanpa kehilangan konteks halaman yang sedang dibuka. Dengan begitu, fokus pengguna tidak terganggu, dan navigasi menjadi lebih nyaman.

Secara keseluruhan, penggunaan AJAX meningkatkan kepuasan dan kenyamanan pengguna, menjadikan website terasa seperti aplikasi modern yang cepat, efisien, dan intuitif.

Referensi:
Tutorial 5 PBP
W3Schools – How To Create a Snackbar / Toast
YouTube channel Lun Dev
Website Mendix
GeeksforGeeks – Handling AJAX in Django