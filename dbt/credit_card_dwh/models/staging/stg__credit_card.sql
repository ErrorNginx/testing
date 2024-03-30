{{
    config(
        materialized='incremental',
        partition_by={
        "field": "created_at",
        "data_type": "date"
        }
    )
}}


SELECT     
    DISTINCT ID,
    CODE_GENDER,
    FLAG_OWN_CAR,
    FLAG_OWN_REALTY,
    CNT_CHILDREN,
    AMT_INCOME_TOTAL,
    NAME_INCOME_TYPE,
    NAME_EDUCATION_TYPE,
    NAME_FAMILY_STATUS,
    NAME_HOUSING_TYPE,
    FLAG_MOBIL,
    FLAG_WORK_PHONE,
    FLAG_PHONE,
    FLAG_EMAIL,
    OCCUPATION_TYPE,
    CNT_FAM_MEMBERS,
    YEARS_BIRTH,
    YEARS_EMPLOYED,
    current_date() as created_at
FROM {{ source('test_location','raw_credit_card') }}