import os
from google.cloud import firestore

service_info = {
    "type": os.environ.get('TYPE'),
    "project_id": os.environ.get('PROJECT_ID'),
    "private_key_id": os.environ.get('PRIVATE_KEY_ID'),
    "private_key": os.environ.get('PRIVATE_KEY'),
    "client_email": os.environ.get('CLIENT_EMAIL'),
    "client_id": os.environ.get('CLIENT_ID'),
    "auth_uri": os.environ.get('AUTH_URI'),
    "token_uri": os.environ.get('TOKEN_URI'),
    "auth_provider_x509_cert_url": os.environ.get('AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url": os.environ.get('CLIENT_X509_CERT_URL'),
    "universe_domain": os.environ.get('UNIVERSE_DOMAIN')
}

firestore_client = firestore.Client.from_service_account_info(service_info)

def get_image_gen():
    collection_ref = firestore_client.collection('images_gen')
    images_gen = []
    
    for doc in collection_ref.stream():
        images_gen.append({'id': doc.id, **doc.to_dict()})
        
    return images_gen

def insert_image_gen(image_gen):
    collection_ref = firestore_client.collection('images_gen')
    collection_ref.add(image_gen)
    