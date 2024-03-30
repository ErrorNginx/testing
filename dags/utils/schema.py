table1_schema = {
    "fields": [
        {"name": "id", "type": "NUMERIC", "mode": "REQUIRED"},
        {"name": "name", "type": "STRING", "mode": "REQUIRED"},
        {"name": "alamat", "type": "STRING", "mode": "REQUIRED"},
    ]
}

table1_schema_raw_credit_card = {
    "fields": [
        {"name": "ID", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "CODE_GENDER", "type": "STRING", "mode": "NULLABLE"},
        {"name": "FLAG_OWN_CAR", "type": "BOOLEAN", "mode": "NULLABLE"},
        {"name": "FLAG_OWN_REALTY", "type": "BOOLEAN", "mode": "NULLABLE"},
        {"name": "CNT_CHILDREN", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "AMT_INCOME_TOTAL", "type": "FLOAT", "mode": "NULLABLE"},
        {"name": "NAME_INCOME_TYPE", "type": "STRING", "mode": "NULLABLE"},
        {"name": "NAME_EDUCATION_TYPE", "type": "STRING", "mode": "NULLABLE"},
        {"name": "NAME_FAMILY_STATUS", "type": "STRING", "mode": "NULLABLE"},
        {"name": "NAME_HOUSING_TYPE", "type": "STRING", "mode": "NULLABLE"},
        {"name": "YEARS_BIRTH", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "YEARS_EMPLOYED", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "FLAG_MOBIL", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "FLAG_WORK_PHONE", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "FLAG_PHONE", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "FLAG_EMAIL", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "OCCUPATION_TYPE", "type": "STRING", "mode": "NULLABLE"},
        {"name": "CNT_FAM_MEMBERS", "type": "NUMERIC", "mode": "NULLABLE"}
    ]
}


schema_aplikasi_transaksi = {
    "fields": [
        {"name": "id", "type": "INTEGER", "mode": "REQUIRED"},
        {"name": "tanggal", "type": "DATE", "mode": "REQUIRED"},
        {"name": "item", "type": "STRING", "mode": "REQUIRED"},
        {"name": "jumlah", "type": "INTEGER", "mode": "REQUIRED"},
        {"name": "harga", "type": "FLOAT", "mode": "REQUIRED"},
        {"name": "total", "type": "FLOAT", "mode": "REQUIRED"}
    ]
}

schema_aplikasi_consumer = {
    "fields": [
        {"name": "id", "type": "INTEGER", "mode": "REQUIRED"},
        {"name": "nama", "type": "STRING", "mode": "REQUIRED"},
        {"name": "alamat", "type": "STRING", "mode": "REQUIRED"},
        {"name": "email", "type": "STRING", "mode": "REQUIRED"},
        {"name": "nomor_telepon", "type": "STRING", "mode": "REQUIRED"}
    ]
}

schema_aplikasi_product = {
    "fields": [
        {"name": "id", "type": "INTEGER", "mode": "REQUIRED"},
        {"name": "nama", "type": "STRING", "mode": "REQUIRED"},
        {"name": "deskripsi", "type": "STRING", "mode": "NULLABLE"},
        {"name": "harga", "type": "FLOAT", "mode": "REQUIRED"},
        {"name": "stok", "type": "INTEGER", "mode": "REQUIRED"}
    ]
}


