#!/usr/bin/env python
# coding: utf-8

import os
from azure.storage.blob import BlobServiceClient
from azure.identity import InteractiveBrowserCredential
import CONFIG

class DownloadADLS:
    '''
    Download a file or directory on an Azure Storage Account to a path on the local filesystem
    '''
    def __init__(self, tenant_id, storage_account_name, container_name):
        '''
        Get authentication token by interactively autenticating with the default web browser
        '''
        credential = InteractiveBrowserCredential(tenant_id=tenant_id)
        service_client = BlobServiceClient(account_url="{}://{}.blob.core.windows.net".format(
            "https", storage_account_name), credential=credential)
        self.client = service_client.get_container_client(container_name)

    def download(self, source, dest):
        '''
        Download a file or directory to a path on the local filesystem
        '''
        
        if not dest:
            raise Exception('A destination must be provided')

        blobs = self.ls_files(source, recursive=True)
        if blobs:
            # if source is a directory, dest must also be a directory
            if not source == '' and not source.endswith('/'):
                source += '/'
            if not dest.endswith('/'):
                dest += '/'

            # append the directory name from source to the destination
            dest += os.path.basename(os.path.normpath(source)) + '/'

            blobs = [source + blob for blob in blobs]
            for blob in blobs:
                blob_dest = dest + os.path.relpath(blob, source)
                self.download_file(blob, blob_dest)
        else:
            self.download_file(source, dest)

    def download_file(self, source, dest):
        '''
        Download a single file to a path on the local filesystem
        '''
        
        # dest is a directory if ending with '/' or '.', otherwise it's a file
        if dest.endswith('.'):
            dest += '/'
        blob_dest = dest + os.path.basename(source) if dest.endswith('/') else dest

        print(f'Downloading {source} to {blob_dest}')
        os.makedirs(os.path.dirname(blob_dest), exist_ok=True)
        bc = self.client.get_blob_client(blob=source)
        
        with open(blob_dest, 'wb') as file:
            data = bc.download_blob()
            file.write(data.readall())

    def ls_files(self, path, recursive=False):
        '''
        List files under a path, optionally recursively
        '''
        
        if not path == '' and not path.endswith('/'):
            path += '/'
            
            blob_iter = self.client.list_blobs(name_starts_with=path)
            files = []
            for blob in blob_iter:
                relative_path = os.path.relpath(blob.name, path)
                
                if recursive or not '/' in relative_path:
                    files.append(relative_path)
        return files


if __name__ == '__main__':
    tenant_id = CONFIG.credentials['tenant_id']
    storage_account_name = CONFIG.credentials['storage_account_name']
    container_name = CONFIG.credentials['container_name']

    source = CONFIG.paths['source']
    dest = CONFIG.paths['dest']

    client = DownloadADLS(tenant_id, storage_account_name, container_name)
    client.download(source, dest)