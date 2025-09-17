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