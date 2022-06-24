from bitbucket import BitbucketApi
from pprint import pprint
access_token = '--'
refresh_token = '--'
consumer_key = '--'
consumer_value = '--'
bitbucket_api = BitbucketApi(access_token=access_token, refresh_token=refresh_token,
                             consumer_key=consumer_key, consumer_value=consumer_value)
bitbucket_api.refresh_access_token()
repositories = bitbucket_api.get_all_repos_from_workspace('matlabers')
pprint(repositories)