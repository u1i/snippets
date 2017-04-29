rom azure.storage.blob import BlobService

blob_service = BlobService(account_name="", account_key="")

blob_service.put_block_blob_from_path("container", "remote-name.jpg", "localfile.jpg")
