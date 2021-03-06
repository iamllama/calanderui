from django.db import models


class DqDatafile(models.Model):
    dq_datafile_id = models.AutoField(db_column='DQ_DATAFILE_ID', primary_key=True)  # Field name made lowercase.
    data_file_name = models.CharField(db_column='DATA_FILE_NAME', max_length=150, blank=True,
                                      null=True)  # Field name made lowercase.
    data_file_type = models.CharField(db_column='DATA_FILE_TYPE', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    data_file_contact = models.CharField(db_column='DATA_FILE_CONTACT', max_length=75, blank=True,
                                         null=True)  # Field name made lowercase.
    contact_email = models.CharField(db_column='CONTACT_EMAIL', max_length=150, blank=True,
                                     null=True)  # Field name made lowercase.
    file_source = models.CharField(db_column='FILE_SOURCE', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    cadence = models.CharField(db_column='CADENCE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recurs_on_weekday = models.CharField(db_column='RECURS_ON_WEEKDAY', max_length=50, blank=True,
                                         null=True)  # Field name made lowercase.
    first_or_last = models.CharField(db_column='FIRST_OR_LAST', max_length=10, blank=True,
                                     null=True)  # Field name made lowercase.
    file_format = models.CharField(db_column='FILE_FORMAT', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    file_naming_convention = models.CharField(db_column='FILE_NAMING_CONVENTION', max_length=200, blank=True,
                                              null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', blank=True, null=True)  # Field name made lowercase.
    active_yn = models.CharField(db_column='ACTIVE_YN', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.


class DqFeed(models.Model):
    dq_feed_id = models.IntegerField(db_column='DQ_FEED_ID',primary_key=True)  # Field name made lowercase.
    source_datafile_name = models.CharField(db_column='SOURCE_DATAFILE_NAME', max_length=150, blank=True,
                                            null=True)  # Field name made lowercase.
    source_datafile_type = models.CharField(db_column='SOURCE_DATAFILE_TYPE', max_length=25, blank=True,
                                            null=True)  # Field name made lowercase.
    source_datafile_path = models.CharField(db_column='SOURCE_DATAFILE_PATH', max_length=150, blank=True,
                                            null=True)  # Field name made lowercase.
    source_datafile_display = models.CharField(db_column='SOURCE_DATAFILE_DISPLAY', max_length=150, blank=True,
                                               null=True)  # Field name made lowercase.
    environment = models.CharField(db_column='ENVIRONMENT', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    feed_received_via = models.CharField(db_column='FEED_RECEIVED_VIA', max_length=50, blank=True,
                                         null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    received_date = models.DateTimeField(db_column='RECEIVED_DATE', blank=True, null=True)  # Field name made lowercase.
    review_date = models.DateTimeField(db_column='REVIEW_DATE', blank=True, null=True)  # Field name made lowercase.
    reviewed_by = models.CharField(db_column='REVIEWED_BY', max_length=75, blank=True,
                                   null=True)  # Field name made lowercase.
    total_rows_in_source_file = models.IntegerField(db_column='TOTAL_ROWS_IN_SOURCE_FILE', blank=True,
                                                    null=True)  # Field name made lowercase.
    load_table_name = models.CharField(db_column='LOAD_TABLE_NAME', max_length=150, blank=True,
                                       null=True)  # Field name made lowercase.
    load_date = models.DateTimeField(db_column='LOAD_DATE', blank=True, null=True)  # Field name made lowercase.
    loaded_by = models.CharField(db_column='LOADED_BY', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    rows_loaded = models.IntegerField(db_column='ROWS_LOADED', blank=True, null=True)  # Field name made lowercase.
    rows_failed_to_load = models.IntegerField(db_column='ROWS_FAILED_TO_LOAD', blank=True,
                                              null=True)  # Field name made lowercase.
    dest_golden_table_name = models.CharField(db_column='DEST_GOLDEN_TABLE_NAME', max_length=150, blank=True,
                                              null=True)  # Field name made lowercase.
    dest_golden_table_type = models.CharField(db_column='DEST_GOLDEN_TABLE_TYPE', max_length=25, blank=True,
                                              null=True)  # Field name made lowercase.
    dest_golden_count = models.IntegerField(db_column='DEST_GOLDEN_COUNT', blank=True,
                                            null=True)  # Field name made lowercase.
    dest_quar_table_name = models.CharField(db_column='DEST_QUAR_TABLE_NAME', max_length=150, blank=True,
                                            null=True)  # Field name made lowercase.
    dest_quar_table_type = models.CharField(db_column='DEST_QUAR_TABLE_TYPE', max_length=25, blank=True,
                                            null=True)  # Field name made lowercase.
    dest_quarantine_count = models.IntegerField(db_column='DEST_QUARANTINE_COUNT', blank=True,
                                                null=True)  # Field name made lowercase.
    dq_processing_date = models.DateTimeField(db_column='DQ_PROCESSING_DATE', blank=True,
                                              null=True)  # Field name made lowercase.
    dq_processed_by = models.CharField(db_column='DQ_PROCESSED_BY', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    app_id = models.IntegerField(db_column='APP_ID', blank=True, null=True)  # Field name made lowercase.
    org_id = models.IntegerField(db_column='ORG_ID', blank=True, null=True)  # Field name made lowercase.
    create_dt = models.DateTimeField(db_column='CREATE_DT', blank=True, null=True)  # Field name made lowercase.
    update_dt = models.DateTimeField(db_column='UPDATE_DT', blank=True, null=True)  # Field name made lowercase.

    dq_datafile = models.ForeignKey('DqDatafile', models.DO_NOTHING, db_column='DQ_DATAFILE_ID', blank=True,
                                    null=True)  # Field name made lowercase.
    file_status = models.CharField(db_column='FILE_STATUS', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.


class DqFeedNew(models.Model):
    dq_feed_id = models.IntegerField(db_column='DQ_FEED_ID',primary_key=True)  # Field name made lowercase.
    source_datafile_name = models.CharField(db_column='SOURCE_DATAFILE_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    source_datafile_type = models.CharField(db_column='SOURCE_DATAFILE_TYPE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    source_datafile_display = models.CharField(db_column='SOURCE_DATAFILE_DISPLAY', max_length=150, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    received_date = models.DateTimeField(db_column='RECEIVED_DATE', blank=True, null=True)  # Field name made lowercase.
    total_rows_in_source_file = models.IntegerField(db_column='TOTAL_ROWS_IN_SOURCE_FILE', blank=True, null=True)  # Field name made lowercase.
    load_date = models.DateTimeField(db_column='LOAD_DATE', blank=True, null=True)  # Field name made lowercase.
    loaded_by = models.CharField(db_column='LOADED_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rows_loaded = models.IntegerField(db_column='ROWS_LOADED', blank=True, null=True)  # Field name made lowercase.
    rows_failed_to_load = models.IntegerField(db_column='ROWS_FAILED_TO_LOAD', blank=True, null=True)  # Field name made lowercase.
    create_dt = models.DateTimeField(db_column='CREATE_DT', blank=True, null=True)  # Field name made lowercase.
    update_dt = models.DateTimeField(db_column='UPDATE_DT', blank=True, null=True)  # Field name made lowercase.
    dq_datafile = models.ForeignKey('DqDatafile', models.DO_NOTHING, db_column='DQ_DATAFILE_ID', blank=True, null=True)  # Field name made lowercase.
    file_status = models.CharField(db_column='FILE_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    number_of_files_loaded = models.IntegerField(db_column='NUMBER_OF_FILES_LOADED', blank=True, null=True)  # Field name made lowercase.
    expected_date = models.DateField(db_column='EXPECTED_DATE', blank=True, null=True)  # Field name made lowercase.


