from google.cloud import storage
import pickle
import os

def getBucket():

	storage_client = storage.Client.from_service_account_json("csci5408-a2-ddb1652742c9.json")
	bucket = storage_client.get_bucket("remote-site")
	return bucket

def readFileFromBucket(bucket, fileName):

	blob = bucket.blob(blob_name = fileName).download_as_string()
	with open (fileName, "wb") as f:
		f.write(blob)

	fileobj = open(fileName, 'rb')
	data = pickle.load(fileobj)
	fileobj.close()

	if os.path.exists(fileName):
  		os.remove(fileName)

	return data