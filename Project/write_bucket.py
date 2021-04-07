from google.cloud import storage
import pickle

def getBucket():
		
	storage_client = storage.Client.from_service_account_json("csci5408-a2-ddb1652742c9.json")
	bucket = storage_client.get_bucket("remote-site")
	return bucket

def processDataAndWriteFileToBucket(bucket, data, fileObj, fileName):

	pickle.dump(data, fileObj)
	fileObj.close()

	blob = bucket.blob(fileName)
	blob.upload_from_filename(fileName)

def writeFileToBucket(bucket, fileName):
		
	blob = bucket.blob(fileName)
	blob.upload_from_filename(fileName)

	print("File uploaded successfully!")

data = [4, 5,'Student', 'ID', 'Product Name', 'Price', 'PCode', '123', 'Piyush', 'ABC', 23546, '234', 'Nirmal', 'ACB', 54556, '345', 'Falgun', 'ACA', 74656, '476', 'Test', 'dfb', 23546]
fileName = "sales.pkl"
fileObj = open(fileName, 'wb')

bucket = getBucket()

processDataAndWriteFileToBucket(bucket, data, fileObj, fileName)