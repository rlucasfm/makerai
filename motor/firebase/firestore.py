from google.cloud import firestore

firestore_client = firestore.Client.from_service_account_json('mm-dlabs-firebase-adminsdk-vwph1-76019e1b9c.json')

def get_image_gen():
    collection_ref = firestore_client.collection('images_gen')
    images_gen = []
    
    for doc in collection_ref.stream():
        images_gen.append({'id': doc.id, **doc.to_dict()})
        
    return images_gen

def insert_image_gen(image_gen):
    collection_ref = firestore_client.collection('images_gen')
    collection_ref.add(image_gen)
    