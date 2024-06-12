# Arkana Training Odoo V17

## Overview
Repository ini berisikan Guide atau Tutorial Odoo V17 yang ditujukan untuk kebutuhan Training dan juga sebagai Media Pembelajaran untuk Pengenalan Odoo untuk sisi Developer

## Table of Contents
1. [Struktur Folder Odoo](#struktur-folder)
2. [ORM Odoo](#orm-odoo)
3. [Env Odoo](#env-odoo)
4. [Widget Odoo](#widget-odoo)

### Struktur Folder

1. **Controllers**
    - Folder ini berisikan File dengan perintah-perintah yang digunakan untuk melakukan pengolahan informasi secara Front-End yang berkomunikasi dengan Back-End melalui Route yang disertai Parameter dan Ketentuan yang dibutuhkan pada proses pengolahan informasi

2. **Data**
    - Folder ini berisikan File yang memuat Data yang terbentuk pada sebuah Model / Table secara otomatis ketika Module diinstall

3. **Demo**
    - Folder ini berisikan File yang membuat Data Demo / Dummy ketika Mode Demo diaktifkan

4. **Models**
    - Folder ini berisikan File dengan Object - Object dengan Properti yang digenerate menjadi sebuah Table dan Column pada Database disertai dengan fungsi-fungsi dapat yang digunakan untuk kebutuhan pengelolaan data / informasi

5. **Report**
    - Folder ini berisikan File yang digunakan untuk membantu dalam pembuatan Report di Odoo

6. **Security**
    - Folder ini berisikan File yang digunakan untuk membuat Role / Groups serta Hak Akses dan Record Rules terhadap sebuah Model atau Data yang dapat diakses oleh User dengan Role atau Group tertentu

7. **Static**
    - Folder ini berisikan File yang digunakan sebagai Assets, dapat berupa Image, CSS / SCSS File, File JS, File XML Template, Library External yang hendak digunakan, dan juga keperluan sejenisnya

8. **View**
    - Folder ini berisikan File yang digunakan sebagai Visualisasi Data pada Odoo berdasarkan Column dan Table yang terbentuk melalui File yang ada di Folder Models, baik dalam bentuk List View, Form View, Kanban View, Gantt View, Pivot View, Graph View, Calendar View, Search View, dan Lainnya

9. **Wizard** 
    - Folder ini berisikan File yang dibutuhkan untuk keperluan memunculkan Pop-Out Window yang dapat digunakan untuk pengolahan informasi secara lengkap ataupun ringkasan serta dapat digunakan untuk Verifikasi Data guna keperluan Action berikutnya

10. **Init**
    - File ini berguna sebagai inisialisasi dalam menjadikan Folder biasa menjadi module Python. File ini juga berfungsi sebagai constructor sebagaimana pada file python, Odoo akan membaca file ini pertama kali saat diinstal. Pada file ini kita harus mengimport semua folder yang mengandung file python dan mengimport file python yang sejajar dengan file __init__ ini jika ada

11. **Manifest**
    - File ini berguna untuk menjadikan folder biasa menjadi modul Odoo. File ini berisikan dictionary python yang memiliki beberapa key dan mengandung informasi yang diperlukan ketika hendak menginstall suatu Module

### ORM Odoo | [Source](https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html)
1. **Model**
    - Model (Object) adalah sebuah struktur dalam database yang fungsinya untuk menentukan cara sebuah data dikelola. Sederhananya Model adalah Table di Database.
    - Terdapat 3 Model di Odoo, diantara : 
        1. **Models** : Model yang umum dipakai pada Odoo. Setiap class yang menginherite model ini, maka akan membuat sebuah tabel di database yang akan menyimpan data secara permanen.
        2. **TransientModel** : Model ini akan membuat table yang datanya disimpan dalam waktu tertentu dan akan dihapus secara periodik. Biasanya digunakan untuk wizard, report, dll.
        3. **AbstractModel** : Model yang menjadi Super Class dari model-model yang lain seperti Model dan TransientModel. Model ini tidak membuat table apalagi data, jadi model ini nanti akan di inherit oleh model lainnya.

2. **Attribute Class**
    - Ada beberapa Attribute Class untuk Model pada Odoo, diantaranya :
        1. **_auto** : Attribute ini berfungsi untuk membuat Model membentuk sebuah Table di Database apabila bernilai True
        2. **_log_access** : Attribute ini akan membentuk 4 Field Access Log secara otomatis apabila bernilai True
        3. **_table** : Attribute ini berfungsi untuk menentukan Nama Table dari Model yang akan digenerate. Jika tidak didefinisikan akan mengambil dari _name
        4. **_name** : Attribute ini berfungsi untuk memberikan Nama pada sebuah Model, jika _table tidak didefinisikan, maka nama Table pada Database akan mengacu pada Attribute ini
        5. **_description** : Attribute ini berfungsi untuk memberikan keterangan pada sebuah Model
        6. **_inherit** : Attribute ini berfungsi untuk menginherit model Parent. Dengan menggunakan keyword ini, maka kita bisa menambahkan/merubah apapun yang kita inginkan ke model parent seperti field, method, attribute, dll.
        7. **_inherits** : Attribute ini berfungsi untuk membuat delegasi (record) ke model parent. Jika inherit (pewarisan) kita mengcustom tabel/model parent, maka inherits (delegasi) yang kita lakukan adalah membuat sebuah field relasi yang mewakili table parent. Maka semua field table parent akan bisa kita akses pada tabel kita, dan ketika kita membuat record pada table kita, maka Odoo akan otomatis membuat record yang sama pada tabel parent. 
        8. **_rec_name** : Attribute ini berfungsi untuk memberikan label pada sebuah record, defaultnya menggunakan field name. Jika kita tidak membuat field name, maka kita harus menggunakan attribute ini dan mengisinya dengan field penggantinya
        9. **_order** : Attribute ini berfungsi untuk mengurutkan record data.
        10. **_sql_constraints** : Attribute ini berfungsi untuk menggunakan constraint yang ada di SQL.
        11. **_check_company_auto** : Attribute ini berfungsi untuk melakukan checking Company ketika terjadi pembuatan / perubahan Data agar tetap konsisten / sesuai pada Relasi Field

3. **Fields**
    - Ada beberapa Fields yang dapat dibuat di Odoo, diantaranya :
        1. **Boolean**
        2. **Char**
        3. **Float**
        4. **Integer**
        5. **Binary**
        6. **Html**
        7. **Image**
        8. **Monetary**
        9. **Selection**
        10. **Text**
        11. **Date**
        12. **Datetime**
        13. **Many2one**
        14. **One2many**
        15. **Many2many**

4. **Method Decorators**
    - Ada beberapa Method Decorators yang ada di Odoo, diantaranya :
        1. **@api.ondelete** : Method ini berfungsi untuk melakukan checking ketika Data / Record hendak dihapus yang apabila terkena rules / kondisi akan memunculkan Error
        2. **@api.constrains** : Method berfungsi untuk membuat constraints (pengecekan batasan/aturan) value sebuah field ketika ada aksi create / update
        3. **@api.onchange** : Method ini akan melakukan action ketika user melakukan perubahan value sebuah field pada form view
        4. **@api.depends** : Method ini akan melakukan action ketika terjadi perubahan value dari field yang memiliki attribute compute yang mengacu pada Field Depedensinya
        5. **@api.depends_context** : Method ini akan melakukan action ketika terjadi perubahan value dari field yang memiliki attribute compute yang mengacu pada Context Depedensinya

5. **ORM Methods**
    - Create / Update
        1. **create()** : Method ini berfungsi untuk melakukan Create Data berdasarkan values yang diberikan
        2. **copy()** : Method ini berfungsi untuk menduplicate sebuah record
        3. **default_get()** : Method ini berfungsi untuk memberikan informasi Default Value dari Field dalam Field List
        4. **name_create()** : Method ini berfungsi untuk melakukan Create Name berdasarkan Parameter Name yang diberikan
        5. **write()** : Method ini berfungsi untuk merubah value field dari record

    - Search / Read
        1. **browse()** : Method ini berfungsi untuk membuat sebuah recordset dari ID Record yang diberikan
        2. **search()** : Method ini berfungsi untuk mencari Data berdasarkan Domain yang ditentukan dan Returnnya berupa Recordset
        3. **search_count()** : Method ini berfungsi untuk mencari Data berdasarkan Domain dan Returnnya berupa Jumlah Record dari Hasil Pencarian
        4. **search_fetch()** : Method ini berfungsi untuk mencari Data berdasarkan Domain dan Returnnya berupa Data dengan Field - Field yang ditentukan
        5. **search_read()** : Method ini gabungan antara search() dan read() yang berfungsi untuk mencari record berdasarkan domainnya dan membaca value field dari record yang di dapat
        7. **read()** : Method ini berfungsi untuk membaca value field dari record
        8. **read_group()** : Method ini berfungsi untuk mencari Data berdasarkan Domain dan Returnnya berupa List of Records yang sudah digrouping sesuai Request

    - Unlink
        1. **unlink()** : Method ini berfungsi untuk menghapus Record / Data

    - Recordset Operations 
        1. **ids** : Method ini digunakan untuk me-return list of ids dari Record
        2. **exist()** : Method ini digunakan untuk check Record itu exist atau tidak
        3. **ensure_one()** : Method ini digunakan untuk memastikan bahwa Record / Self adalah single Record
        4. **filtered()** : Method ini digunakan untuk filter Record berdasarkan ketentuan Filter
        5. **filtered_domain()** : Method ini digunakan untuk filter Record berdasarkan ketentuan Domain
        6. **mapped()** : Method ini digunakan untuk mapoing Record berdasarkan Request Field yang diminta
        7. **sorted()** : Method ini digunakan untuk mengurutkan Record berdasarkan Request Field yang diminta
        8. **grouped()** : Method ini digunakan untuk grouping Record berdasarkan Request Field yang diminta

### Env Odoo
1. **user** : Mendapatkan informasi user yang aktif
2. **cr** : Berfungsi untuk melakukan proses query
3. **context** : Berfungsi untuk mendapatkan parameter
4. **ref** : Mendapatkan record data yang didefiniskan pada file xml (view, groups, reports, dll) dengan memberikan xml_id nya
5. **company** : Mendapatkan informasi company yang aktif
6. **companies** : Mendapatkan informasi companies yang dimiliki oleh User
7. **lang** : Mendapatkan informasi code bahasa
8. **is_superuser** : Untuk mengcek apakah Env dalam Superuser Mode
9. **is_admin** : Untuk mengecek apakah user yang aktif memiliki Akses "Access Rights”
10. **is_system** : Untuk mengecek apakah user yang aktif memiliki Akses "Settings"
11. **with_context** : Untuk menambahkan atau memperbarui Context yang dibawa
12. **with_user** : Untuk memperbarui informasi User yang melakukan sebuah aksi
13. **with_company** : Untuk memperbarui informasi Company dalam sebuah aksi
14. **sudo()** : Untuk menjadi aksi yang dilakukan bersumber dari Superuser

### Widget Odoo
1. **many2one_avatar_user**
2. **many2many_tags**
3. **boolean_toggle**
4. **statinfo**
5. **radio**
6. **handle**
7. **badge**
8. **remaining_days**
9. **statusbar**
10. **text**
11. **email**
12. **monetary**
13. **html**
14. **phone**
15. **many2many_binary**
16. **CopyClipboardChar**
17. **many2many_tags_email**
18. **float_time**
19. **url**
20. **image**
21. **selection**
22. **color_picker**
23. **percentage**
24. **progressbar**
25. **integer**
26. **video_preview**
27. **char**
28. **signature**
29. **priority**
30. **pdf_viewer**
31. **date**
32. **many2many_checkboxes**
33. **section_and_note_one2many**
34. **color**
35. **daterange**
36. **ace**
37. **label_selection**
38. **domain**
39. **many2one_avatar_employee**
40. **hr_org_chart**
41. **hr_presence_status**
42. **boolean_favorite**
43. **binary**
44. **timesheet_uom**
45. **embed_viewer**
46. **mass_mailing_html**
47. **mrp_timer**
48. **analytic_distribution**
49. **many2many_tags_email**
50. **res_partner_many2one**