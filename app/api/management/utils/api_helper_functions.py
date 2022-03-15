import hashlib

from core.models import MetadataLedger, SupplementalLedger


def add_metadata_ledger(data, experience_id):
    """Calls the metadata serializer with data sent over
     and older instance of the data """

    # create hash values of metadata and supplemental data
    metadata_hash = hashlib.sha512(str(data['metadata']).encode(
        'utf-8')).hexdigest()

    # assign hash values to hash key in data
    data['metadata_hash'] = metadata_hash

    # Obtaining key value for comparison of records in metadata ledger
    if experience_id:
        key_hash_value = experience_id
    else:
        key_hash_value = data.get('metadata_key_hash', None)

    record_in_table = None
    if key_hash_value is not None:
        # Comparing metadata_key value in metadata ledger
        # to find older instances
        record_in_table = MetadataLedger.objects.filter(
            metadata_key_hash=key_hash_value, record_status='Active') \
            .first()
        if record_in_table:
            data['metadata_key'] = record_in_table.metadata_key

    return data, record_in_table


def add_supplemental_ledger(data, experience_id):
    """Calls the supplemental serializer with data sent over
         and older instance of the data """

    # create hash values of metadata and supplemental data
    supplemental_hash = hashlib.sha512(str(data['metadata'])
                                       .encode('utf-8')).hexdigest()

    # assign hash values to hash key in data
    data['metadata_hash'] = supplemental_hash

    # Obtaining key value for comparison of records in metadata ledger
    if experience_id:
        key_hash_value = experience_id
    else:
        key_hash_value = data.get('metadata_key_hash', None)

    record_in_table = None
    if key_hash_value is not None:
        # Comparing key value in metadata ledger
        # to find older instances
        record_in_table = SupplementalLedger.objects.filter(
            metadata_key_hash=key_hash_value, record_status='Active') \
            .first()
        if record_in_table:
            data['metadata_key'] = record_in_table.metadata_key

    return data, record_in_table
