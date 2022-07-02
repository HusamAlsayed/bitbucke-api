from bitbucket import BitbucketApi
from pprint import pprint
access_token = 'k7FyZTX4ZFsa8UipjmpOcvy4mCy2ziivUZ0U_WKFREYepEV2z1jq2SH41NdxpHvxP89m4182wmYWepDbX48xR1AsagO5xC4btBh6R7lWs4tv5lAVl2uVg8nf'
refresh_token = 'dbqypE6MRuzLpPAp2f'
consumer_key = 'aZFguVcUrZ8XnU7uay'
consumer_value = 'bgUbE8ezsFE5mf4XGVRMWc6SZX7LZZyp'
bitbucket_api = BitbucketApi(access_token=access_token, refresh_token=refresh_token,
                             consumer_key=consumer_key, consumer_value=consumer_value)
bitbucket_api.refresh_access_token()
repositories = bitbucket_api.get_all_repos_from_workspace('matlabers')
pprint(repositories)